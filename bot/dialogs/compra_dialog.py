from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, TextPrompt
from botbuilder.dialogs.prompts import PromptOptions, PromptValidatorContext
from botbuilder.core import MessageFactory, UserState
import re

from bot.services.compra_api_client import enviar_compra
from bot.models.model_produto import ModeloComprarProduto

class ComprarProdutoDialog(ComponentDialog):
    """
    Fluxo de coleta de dados para realizar a compra de um produto,
    com validações e prompts personalizados.
    """
    # Defina o ID de waterfall como uma string literal para evitar NameError
    WATERFALL_ID = "ComprarProdutoDialogFlow"

    def __init__(self, user_state: UserState):
        super().__init__(ComprarProdutoDialog.__name__)
        self.user_state = user_state

        # Prompts com validação
        self.add_dialog(TextPrompt("CartaoPrompt", ComprarProdutoDialog.validar_numero_cartao))
        self.add_dialog(TextPrompt("ExpiracaoPrompt", ComprarProdutoDialog.validar_data_expiracao))
        self.add_dialog(TextPrompt("CvvPrompt", ComprarProdutoDialog.validar_cvv))
        self.add_dialog(TextPrompt("SaldoPrompt", ComprarProdutoDialog.validar_saldo))

        # Sequência de passos
        self.add_dialog(
            WaterfallDialog(
                ComprarProdutoDialog.WATERFALL_ID,
                [
                    self.coletar_numero_cartao,
                    self.coletar_data_expiracao,
                    self.coletar_cvv,
                    self.coletar_saldo,
                    self.processar_compra
                ]
            )
        )

        self.initial_dialog_id = ComprarProdutoDialog.WATERFALL_ID

    async def coletar_numero_cartao(self, step: WaterfallStepContext):
        step.values["productName"] = step.options.get("productName")
        step.values["preco"] = step.options.get("preco", 0.0)
        return await step.prompt(
            "CartaoPrompt",
            PromptOptions(prompt=MessageFactory.text("Digite o número do cartão de crédito:"))
        )

    async def coletar_data_expiracao(self, step: WaterfallStepContext):
        step.values["numeroCartao"] = step.result
        return await step.prompt(
            "ExpiracaoPrompt",
            PromptOptions(prompt=MessageFactory.text("Data de expiração (MM/AA):"))
        )

    async def coletar_cvv(self, step: WaterfallStepContext):
        step.values["expiracao"] = step.result
        return await step.prompt(
            "CvvPrompt",
            PromptOptions(prompt=MessageFactory.text("Digite o CVV do cartão:"))
        )

    async def coletar_saldo(self, step: WaterfallStepContext):
        step.values["cvv"] = step.result
        return await step.prompt(
            "SaldoPrompt",
            PromptOptions(prompt=MessageFactory.text("Informe o saldo disponível para simular a compra:"))
        )

    async def processar_compra(self, step: WaterfallStepContext):
        step.values["saldo"] = float(step.result)

        dados = ModeloComprarProduto(
            product_name=step.values["productName"],
            preco=step.values["preco"],
            numero_cartao=step.values["numeroCartao"],
            data_expiracao=step.values["expiracao"],
            cvv=step.values["cvv"],
            saldo=step.values["saldo"]
        )

        sucesso, mensagem = await enviar_compra(dados.to_payload())
        await step.context.send_activity(mensagem)
        return await step.end_dialog()

    @staticmethod
    async def validar_numero_cartao(prompt_context: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"\d{13,19}", prompt_context.recognized.value))

    @staticmethod
    async def validar_data_expiracao(prompt_context: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"(0[1-9]|1[0-2])/\d{2}$", prompt_context.recognized.value))

    @staticmethod
    async def validar_cvv(prompt_context: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"\d{3,4}", prompt_context.recognized.value))

    @staticmethod
    async def validar_saldo(prompt_context: PromptValidatorContext) -> bool:
        try:
            return float(prompt_context.recognized.value) >= 0
        except:
            return False
