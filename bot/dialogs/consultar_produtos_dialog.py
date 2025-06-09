from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, TextPrompt, ConfirmPrompt, PromptOptions
from botbuilder.core import MessageFactory, CardFactory
from botbuilder.schema import HeroCard, CardImage, CardAction, ActionTypes

from bot.api.product_api import ProductAPI


class ConsultarProdutosDialog(ComponentDialog):
    def __init__(self):
        super(ConsultarProdutosDialog, self).__init__(ConsultarProdutosDialog.__name__)

        self.add_dialog(TextPrompt("TextPrompt"))
        self.add_dialog(ConfirmPrompt("ConfirmPrompt"))

        self.add_dialog(WaterfallDialog(
            "ConsultarProdutosDialog",
            [
                self.perguntar_nome,
                self.buscar_produto,
                self.confirmar_continuar
            ]
        ))

        self.initial_dialog_id = "ConsultarProdutosDialog"

    async def perguntar_nome(self, step_context: WaterfallStepContext):
        return await step_context.prompt(
            "TextPrompt",
            PromptOptions(prompt=MessageFactory.text("🛒 Qual produto você deseja consultar?"))
        )

    async def buscar_produto(self, step_context: WaterfallStepContext):
        step_context.values["nome"] = step_context.result
        nome = step_context.result
        produtos = ProductAPI().buscar_por_nome(nome)

        if not produtos:
            await step_context.context.send_activity("❌ Produto não encontrado.")
        else:
            for produto in produtos[:3]:
                card = CardFactory.hero_card(
                    HeroCard(
                        title=produto["productName"],
                        subtitle=produto["productDescription"],
                        text=f"💲 Preço: R$ {produto['price']}",
                        images=[CardImage(url=produto["imageUrl"][0])],
                        buttons=[CardAction(
                            type=ActionTypes.im_back,
                            title=f"Comprar {produto['productName']}",
                            value=f"Comprar {produto['productName']}"
                        )]
                    )
                )
                await step_context.context.send_activity(MessageFactory.attachment(card))

        return await step_context.prompt(
            "ConfirmPrompt",
            PromptOptions(prompt=MessageFactory.text("🔁 Deseja buscar outro produto? (sim/não)"))
        )

    async def confirmar_continuar(self, step_context: WaterfallStepContext):
        resposta = step_context.result

        if resposta:  # True -> sim
            return await step_context.replace_dialog(self.id)
        else:
            await step_context.context.send_activity("👋 Obrigado! Retornando ao menu principal.")
            return await step_context.end_dialog()
