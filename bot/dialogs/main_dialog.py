from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
)
from botbuilder.dialogs.prompts import ChoicePrompt, ConfirmPrompt, PromptOptions
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState
from botbuilder.schema import HeroCard, CardAction, CardImage, ActionTypes
from botbuilder.core import CardFactory

from bot.dialogs.consultar_produtos_dialog import ConsultarProdutosDialog


class MainDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__(MainDialog.__name__)

        self.user_profile_accessor = user_state.create_property("MainProfile")

        self.add_dialog(ConsultarProdutosDialog())  # REGISTRA o subdiálogo
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(ConfirmPrompt(ConfirmPrompt.__name__))

        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.prompt_option_step,
                    self.process_option_step  # ESTE método precisa existir 👇
                ],
            )
        )

        self.initial_dialog_id = WaterfallDialog.__name__

    async def prompt_option_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Olá! Bem vindo ao E-Commerce IsaFabBia! Por favor, escolha uma das opções abaixo: "),
                choices=[
                    Choice("Consultar Pedidos"),
                    Choice("Consultar Produtos"),
                    Choice("Extrato de Compras"),
                ],
            ),
        )

    async def process_option_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        option = step_context.result.value

        if option == "Consultar Pedidos":
            await step_context.context.send_activity("Você escolheu Consultar Pedidos.")
        elif option == "Consultar Produtos":
            return await step_context.begin_dialog("ConsultarProdutosDialog")

        elif option == "Extrato de Compras":
            await step_context.context.send_activity("Você escolheu Extrato de Compras.")


        return await step_context.end_dialog()
