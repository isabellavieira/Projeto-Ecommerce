from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, TextPrompt, PromptOptions
from botbuilder.core import MessageFactory, CardFactory
from botbuilder.schema import HeroCard, CardImage, CardAction, ActionTypes

from bot.api.product_api import ProductAPI


class ConsultarProdutosDialog(ComponentDialog):
    def __init__(self):
        super(ConsultarProdutosDialog, self).__init__(ConsultarProdutosDialog.__name__)

        self.add_dialog(TextPrompt("TextPrompt"))

        self.add_dialog(WaterfallDialog(
            "ConsultarProdutosDialog",
            [
                self.perguntar_nome,
                self.buscar_produto
            ]
        ))

        self.initial_dialog_id = "ConsultarProdutosDialog"

    async def perguntar_nome(self, step_context: WaterfallStepContext):
        return await step_context.prompt(
            "TextPrompt",
            PromptOptions(prompt=MessageFactory.text("Qual produto você deseja consultar?"))
        )

    async def buscar_produto(self, step_context: WaterfallStepContext):
        nome = step_context.result
        produtos = ProductAPI().buscar_por_nome(nome)

        if not produtos:
            await step_context.context.send_activity("❌ Produto não encontrado.")
            return await step_context.replace_dialog(self.id)  # reinicia o mesmo diálogo
        else:
            for produto in produtos:
                card = CardFactory.hero_card(
                    HeroCard(
                        title=produto["productName"],
                        subtitle=produto["productDescription"],
                        text=f"Preço: R$ {produto['price']}",
                        images=[CardImage(url=produto["imageUrl"][0])],
                        buttons=[
                            CardAction(
                                type=ActionTypes.im_back,
                                title=f"Comprar {produto['productName']}",
                                value=produto["id"]
                            )
                        ]
                    )
                )
                await step_context.context.send_activity(MessageFactory.attachment(card))

        return await step_context.end_dialog()