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
from bot.api.product_api import ProductAPI  # certifique-se de importar isso
from bot.dialogs.consultar_produtos_dialog import ConsultarProdutosDialog
from bot.dialogs.compra_dialog import CompraDialog  # 👈 ADICIONADO

class MainDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__(MainDialog.__name__)

        self.user_profile_accessor = user_state.create_property("MainProfile")

        self.add_dialog(ConsultarProdutosDialog())  # 🔗 Subdiálogo produtos
        self.add_dialog(CompraDialog("compraDialog"))

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
                prompt=MessageFactory.text("Olá! Bem vindo ao E-Commerce IsaFabBia! Por favor, escolha uma das opções abaixo: "),
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
            return await step_context.begin_dialog("ConsultarProdutosDialog")

        elif option == "Extrato de Compras":
            await step_context.context.send_activity("Você escolheu Extrato de Compras.")
            
        return await step_context.end_dialog()

    async def on_continue_dialog(self, inner_dc):
        print("⚙️ Mensagem recebida:", inner_dc.context.activity.text)

        message = inner_dc.context.activity.text.strip()
        nome_produto = None

        if message.startswith("Comprar "):
            nome_produto = message.replace("Comprar", "").strip()

        # Verificação para garantir que o nome do produto seja válido
            if not nome_produto or len(nome_produto) < 2:
                await inner_dc.context.send_activity("⚠️ Nome do produto inválido. Por favor, informe um nome de produto válido.")
                return await inner_dc.end_dialog()

        # Buscar os produtos no Cosmos DB
            produtos = ProductAPI().buscar_por_nome(nome_produto)

            if produtos:
                produto_encontrado = None
                for produto in produtos:
                    if nome_produto.lower() in produto["productName"].lower():
                        produto_encontrado = produto
                        break

                if produto_encontrado:
                    preco = produto_encontrado.get("price", "0.0")
                    return await inner_dc.begin_dialog("compraDialog", {
                    "productName": produto_encontrado["productName"],
                    "preco": preco
                })
                else:
                    await inner_dc.context.send_activity(f"❌ Produto com nome '{nome_produto}' não encontrado.")
                    return await inner_dc.end_dialog()
            else:
                await inner_dc.context.send_activity("❌ Produto não encontrado.")
                return await inner_dc.end_dialog()
    
        return await super().on_continue_dialog(inner_dc)

