# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
)
from botbuilder.dialogs.prompts import (
    TextPrompt,
    NumberPrompt,
    ChoicePrompt,
    ConfirmPrompt,
    AttachmentPrompt,
    PromptOptions,
    PromptValidatorContext,
)
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState

from data_models.perfil_do_usuario import PerfilDoUsuario   
from api.product_api import ProductAPI
from botbuilder.schema import (
    ActionTypes,
    HeroCard,
    CardAction,
    CardImage,
)

from botbuilder.core import CardFactory
from dialogs.consultar_produtos_dialog import ConsultarProdutosDialog



class MainDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__(MainDialog.__name__)

        self.user_profile_accessor = user_state.create_property("MainProfile")

        self.add_dialog(ConsultarProdutosDialog(user_state))
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(ConfirmPrompt(ConfirmPrompt.__name__))

        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.prompt_option_step,
                    self.process_option_step
                ],
            )
        )

        self.initial_dialog_id = WaterfallDialog.__name__

    async def prompt_option_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Escolha a opção desejada:"),
                choices=[
                    Choice("Consultar Pedidos"),
                    Choice("Consultar Produtos"),
                    Choice("Extrato de Compras")
                ],
            ),
        )

    async def process_option_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        option = step_context.result.value

        if option == "Consultar Pedidos":
            await step_context.context.send_activity("Você escolheu Consultar Pedidos.")
        elif option == "Consultar Produtos":
            return await step_context.begin_dialog("consultarProdutosDialog")
        elif option == "Extrato de Compras":
            await step_context.context.send_activity("Você escolheu Extrato de Compras.")

        return await step_context.end_dialog()
    

    async def show_card_produtos(self, turn_context, nome_do_produto):
        produto_api = ProductAPI()

        response = produto_api.search_product(nome_do_produto)
        if not response:
            await turn_context.send_activity(
                MessageFactory.text("Nenhum produto encontrado com esse nome.")
            )
            return

        #Montando o card
        card = CardFactory.hero_card(
            HeroCard(
                title=response["productName"],
                text=f"Preço: R$ {response['price']}",
                subtitle=response["productDescription"],
                images=[CardImage(url=produto) for produto in response["imageUrl"]],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title=f"Comprar {response["productName"]}",
                        value=response["id"],
                    )
                ],
            )
        )

        return await turn_context.send_activity(MessageFactory.attachment(card))    

       