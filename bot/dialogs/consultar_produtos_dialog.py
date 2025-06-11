from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, DialogTurnResult, DialogTurnStatus, TextPrompt
from botbuilder.dialogs.prompts import PromptOptions
from botbuilder.core import MessageFactory, CardFactory, UserState
from botbuilder.schema import HeroCard, CardAction, CardImage, ActionTypes
from bot.api.product_api import ProductAPI
from bot.dialogs.compra_dialog import ComprarProdutoDialog

class ConsultarProdutosDialog(ComponentDialog):
    """
    Diálogo para pesquisar produtos e iniciar compra.
    """
    def __init__(self, user_state: UserState):
        super().__init__(ConsultarProdutosDialog.__name__)
        self.user_state = user_state

        # Prompt de texto
        self.add_dialog(TextPrompt("NomePrompt"))
        # Sub-diálogo de compra
        self.add_dialog(ComprarProdutoDialog(user_state))
        # Waterfall do fluxo de pesquisa
        self.add_dialog(
            WaterfallDialog(
                "PesquisaFlow",
                [
                    self.perguntar_nome_produto,
                    self.exibir_resultados,
                    self.tratar_selecao
                ]
            )
        )
        self.initial_dialog_id = "PesquisaFlow"

    async def perguntar_nome_produto(self, step: WaterfallStepContext) -> DialogTurnResult:
        return await step.prompt(
            "NomePrompt",
            PromptOptions(prompt=MessageFactory.text("🛒 Qual produto deseja buscar?"))
        )

    async def exibir_resultados(self, step: WaterfallStepContext) -> DialogTurnResult:
        nome = step.result
        produtos = ProductAPI().buscar_produto(nome)

        if not produtos:
            await step.context.send_activity(f"❌ Não encontrei produtos para '{nome}'.")
        else:
            for item in produtos[:5]:
                card = CardFactory.hero_card(
                    HeroCard(
                        title=item.get("productName"),
                        text=f"Preço: R$ {item.get('price', 0.0)}",
                        images=[CardImage(url=url) for url in item.get("imageUrl", [])],
                        buttons=[
                            CardAction(
                                type=ActionTypes.post_back,
                                title="Comprar",
                                value={"action": "buy", "productId": item.get("id")}  
                            )
                        ]
                    )
                )
                await step.context.send_activity(MessageFactory.attachment(card))

        # Mantém o diálogo aguardando a próxima atividade do usuário
        return DialogTurnResult(status=DialogTurnStatus.Waiting, result=step.result)

    async def tratar_selecao(self, step: WaterfallStepContext) -> DialogTurnResult:
        escolha = step.context.activity.value
        if isinstance(escolha, dict) and escolha.get("action") == "buy":
            return await step.begin_dialog(
                ComprarProdutoDialog.__name__,
                {"productId": escolha.get("productId")}    
            )
        await step.context.send_activity("Compra cancelada ou ação inválida.")
        return await step.end_dialog()
