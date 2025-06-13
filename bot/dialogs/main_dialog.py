from botbuilder.core import UserState
from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, DialogTurnResult
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions
from botbuilder.core import MessageFactory
from bot.dialogs.consultar_pedidos_dialog import ConsultarPedidosDialog
from bot.dialogs.consultar_produtos_dialog import ConsultarProdutosDialog
from bot.dialogs.compra_dialog import ComprarProdutoDialog

class MainDialog(ComponentDialog):
    """
    Diálogo principal que mostra opções e intercepta tanto cliques em cards
    quanto texto livre para iniciar a compra.
    """
    MAIN_WATERFALL = "MAIN_WATERFALL"

    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__(MainDialog.__name__)

        self.add_dialog(TextPrompt("TextPrompt"))  # Adiciona o diálogo TextPrompt
        self.add_dialog(ConsultarPedidosDialog("ConsultarPedidosDialog"))
        self.add_dialog(ConsultarProdutosDialog("ConsultarProdutosDialog"))
        self.add_dialog(ComprarProdutoDialog("ComprarProdutoDialog"))
        self.add_dialog(WaterfallDialog(self.MAIN_WATERFALL, [
            self.prompt_for_action,
            self.handle_action_selection
        ]))

        self.initial_dialog_id = self.MAIN_WATERFALL

    async def prompt_for_action(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        # Envia botões interativos para o usuário
        return await step_context.prompt(
            "TextPrompt",
            PromptOptions(
                prompt=MessageFactory.suggested_actions(
                    actions=[
                        {"title": "Consultar Pedidos", "type": "imBack", "value": "Consultar Pedidos"},
                        {"title": "Consultar Produtos", "type": "imBack", "value": "Consultar Produtos"}
                    ],
                    text="Escolha uma opção:"
                )
            )
        )

    async def handle_action_selection(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        escolha = step_context.context.activity.text  # Captura o texto enviado pelo botão

        if escolha == "Consultar Pedidos":
            return await step_context.begin_dialog("ConsultarPedidosDialog")
        elif escolha == "Consultar Produtos":
            return await step_context.begin_dialog("ConsultarProdutosDialog")
        elif escolha == "Menu Inicial":
            return await step_context.replace_dialog("MainDialog")  # Reinicia o fluxo
        else:
            await step_context.context.send_activity("Opção inválida. Por favor, tente novamente.")
            return await step_context.replace_dialog("MainDialog")

    async def on_continue_dialog(self, inner_dc):
        """
        Intercepta cliques em cards (postBack) e texto livre "Comprar X".
        Trata postBack antes de tentar usar .text, que pode ser None.
        """
        activity = inner_dc.context.activity

        # 1) Se veio um postBack de botão de compra:
        if isinstance(activity.value, dict) and activity.value.get("action") == "buy":
            dados = activity.value
            return await inner_dc.begin_dialog(
                ComprarProdutoDialog.__name__,
                {
                    "productName": dados.get("productName"),
                    "preco": dados.get("price", 0.0),
                },
            )
        # 2) Agora protege text de None e trata comandos "comprar ..."
        text = activity.text or ""
        if text.lower().startswith("comprar "):
            nome = text[8:].strip()
            produtos = ProductAPI().buscar_por_nome(nome)
            if produtos:
                match = next(
                    (p for p in produtos
                     if nome.lower() in p.get("productName", "").lower()),
                    None,
                )
                if match:
                    return await inner_dc.begin_dialog(
                        ComprarProdutoDialog.__name__,
                        {"productName": match["productName"], "preco": match.get("price", 0.0)},
                    )
            await inner_dc.context.send_activity(f"❌ Não foi possível iniciar compra para '{nome}'")
            return await inner_dc.end_dialog()

        # 3) Caso contrário, segue o fluxo padrão
        return await super().on_continue_dialog(inner_dc)
