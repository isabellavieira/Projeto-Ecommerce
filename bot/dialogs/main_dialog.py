from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, DialogTurnResult
from botbuilder.dialogs.prompts import ChoicePrompt, PromptOptions
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState

from bot.api.product_api import ProductAPI
from bot.dialogs.consultar_produtos_dialog import ConsultarProdutosDialog
from bot.dialogs.compra_dialog import ComprarProdutoDialog

class MainDialog(ComponentDialog):
    """
    Diálogo principal que mostra opções e intercepta tanto cliques em cards
    quanto texto livre para iniciar a compra.
    """
    MAIN_WATERFALL = "MAIN_WATERFALL"

    def __init__(self, user_state: UserState):
        super().__init__(MainDialog.__name__)

        # Property para armazenar perfil (não usado aqui mas mantido)
        self.profile_accessor = user_state.create_property("UserProfile")

        # Sub-diálogos
        self.add_dialog(ConsultarProdutosDialog(user_state))
        self.add_dialog(ComprarProdutoDialog(user_state))

        # Prompt de escolha
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))

        # Waterfall principal
        self.add_dialog(
            WaterfallDialog(
                MainDialog.MAIN_WATERFALL,
                [
                    self.prompt_for_action,
                    self.handle_action_selection
                ]
            )
        )

        self.initial_dialog_id = MainDialog.MAIN_WATERFALL

    async def prompt_for_action(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        """Exibe o menu de ações."""
        choices = [Choice("Consultar Produtos")]
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Selecione uma opção:"),
                choices=choices
            )
        )

    async def handle_action_selection(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        """Despacha para o diálogo de produtos."""
        choice = step_context.result.value
        if choice == "Consultar Produtos":
            return await step_context.begin_dialog(ConsultarProdutosDialog.__name__)
        return await step_context.end_dialog()

    async def on_continue_dialog(self, inner_dc):
        """
        Intercepta cliques em cards (postBack) e texto livre “Comprar X”.
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
        # 2) Agora protege text de None e trata comandos “comprar ...”
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
