from botbuilder.dialogs import WaterfallDialog, WaterfallStepContext, ComponentDialog
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions
from botbuilder.core import MessageFactory
from api.product_api import ProductAPI
from botbuilder.core import UserState

class ConsultarProdutosDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super().__init__("consultarProdutosDialog")

        self.user_profile_accessor = user_state.create_property("ConsultaProdutoProfile")

        self.add_dialog(TextPrompt("TextPrompt"))
        self.add_dialog(
            WaterfallDialog("MainDialog", [
                self.perguntar_nome_produto,
                self.consultar_produto_api
            ])
        )

        self.initial_dialog_id = "MainDialog"

    async def perguntar_nome_produto(self, step_context: WaterfallStepContext):
        return await step_context.prompt(
            "TextPrompt",
            PromptOptions(prompt=MessageFactory.text("Qual produto você quer consultar?"))
        )

    async def consultar_produto_api(self, step_context: WaterfallStepContext):
        nome_produto = step_context.result
        api = ProductAPI()
        resultados = api.search_product(nome_produto)

        if resultados:
            resposta = "Aqui estão os produtos encontrados:\n"
            for p in resultados:
                resposta += f"- {p['productName']} por R${p['price']}\n"
        else:
            resposta = "Nenhum produto encontrado com esse nome."

        await step_context.context.send_activity(MessageFactory.text(resposta))
        return await step_context.end_dialog()
