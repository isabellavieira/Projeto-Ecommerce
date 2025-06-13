# bot/dialogs/compra_dialog.py


from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
)
from botbuilder.dialogs.prompts import (
    TextPrompt,
    ChoicePrompt,
    PromptOptions,
    PromptValidatorContext,
)
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState
import re
from bot.services.compra_api_client import enviar_compra
from bot.models.model_produto import ModeloComprarProduto
import uuid


class ComprarProdutoDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super().__init__(ComprarProdutoDialog.__name__)
        self.user_state = user_state

        # Prompts de validação
        self.add_dialog(TextPrompt("CartaoPrompt", ComprarProdutoDialog.validar_numero_cartao))
        self.add_dialog(TextPrompt("ExpiracaoPrompt", ComprarProdutoDialog.validar_data_expiracao))
        self.add_dialog(TextPrompt("CvvPrompt", ComprarProdutoDialog.validar_cvv))
        self.add_dialog(TextPrompt("SaldoPrompt", ComprarProdutoDialog.validar_saldo))

        # Prompts de usuário
        self.add_dialog(TextPrompt("NomePrompt"))
        self.add_dialog(TextPrompt("EmailPrompt", ComprarProdutoDialog.validar_email))
        self.add_dialog(TextPrompt("CpfPrompt", ComprarProdutoDialog.validar_cpf))
        self.add_dialog(TextPrompt("TelefonePrompt"))
        self.add_dialog(TextPrompt("DtNascimentoPrompt", ComprarProdutoDialog.validar_data_nascimento))

        # Prompts de endereço
        self.add_dialog(TextPrompt("LogradouroPrompt"))
        self.add_dialog(TextPrompt("ComplementoPrompt"))
        self.add_dialog(TextPrompt("BairroPrompt"))
        self.add_dialog(TextPrompt("CidadePrompt"))
        self.add_dialog(TextPrompt("EstadoPrompt"))
        self.add_dialog(TextPrompt("CepPrompt", ComprarProdutoDialog.validar_cep))

        # Prompt pós-compra
        self.add_dialog(ChoicePrompt("PosCompraPrompt"))

        # Sequência de passos
        self.add_dialog(
            WaterfallDialog(
                "ComprarFlow",
                [
                    self.coletar_numero_cartao,
                    self.coletar_validade,
                    self.coletar_cvv,
                    self.coletar_saldo,
                    self.coletar_nome,
                    self.coletar_email,
                    self.coletar_cpf,
                    self.coletar_telefone,
                    self.coletar_dt_nascimento,
                    self.coletar_logradouro,
                    self.coletar_complemento,
                    self.coletar_bairro,
                    self.coletar_cidade,
                    self.coletar_estado,
                    self.coletar_cep,
                    self.processar_compra,
                    self.pos_compra_prompt,
                    self.pos_compra_handle,
                ],
            )
        )

        self.initial_dialog_id = "ComprarFlow"


    # 1) Cartão
    async def coletar_numero_cartao(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["productName"] = step.options.get("productName")
        step.values["preco"] = step.options.get("preco", 0.0)
        return await step.prompt("CartaoPrompt", PromptOptions(
            prompt=MessageFactory.text("Digite o número do cartão (13–19 dígitos):")
        ))

    async def coletar_validade(self, step: WaterfallStepContext) -> DialogTurnResult:
        # Salva o número do cartão coletado
        step.values["numero_cartao"] = step.result

        # Solicita a data de validade
        return await step.prompt("ExpiracaoPrompt", PromptOptions(
            prompt=MessageFactory.text("Digite a data de validade do cartão (MM/yy):")
        ))

    async def coletar_cvv(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["validade"] = step.result  # Salva a validade do cartão
        return await step.prompt("CvvPrompt", PromptOptions(
            prompt=MessageFactory.text("Digite o CVV (3 ou 4 dígitos):")
        ))

    async def coletar_saldo(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["cvv"] = step.result  # Salva o CVV
        return await step.prompt("SaldoPrompt", PromptOptions(
            prompt=MessageFactory.text("Digite o saldo disponível no cartão:")
        ))


    # 2) Usuário
    async def coletar_nome(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["saldo"] = float(step.result)
        return await step.prompt("NomePrompt", PromptOptions(
            prompt=MessageFactory.text("Informe seu nome completo:")
        ))

    async def coletar_email(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["nome"] = step.result
        return await step.prompt("EmailPrompt", PromptOptions(
            prompt=MessageFactory.text("Informe seu e-mail:")
        ))

    async def coletar_cpf(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["email"] = step.result
        return await step.prompt("CpfPrompt", PromptOptions(
            prompt=MessageFactory.text("Informe seu CPF (somente números):")
        ))

    async def coletar_telefone(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["cpf"] = step.result
        return await step.prompt("TelefonePrompt", PromptOptions(
            prompt=MessageFactory.text("Informe seu telefone com DDD:")
        ))

    async def coletar_dt_nascimento(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["telefone"] = step.result
        return await step.prompt("DtNascimentoPrompt", PromptOptions(
            prompt=MessageFactory.text("Data de nascimento (YYYY-MM-DD):")
        ))


    # 3) Endereço
    async def coletar_logradouro(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["dt_nascimento"] = step.result
        return await step.prompt("LogradouroPrompt", PromptOptions(
            prompt=MessageFactory.text("Logradouro:")
        ))

    async def coletar_complemento(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["logradouro"] = step.result
        return await step.prompt("ComplementoPrompt", PromptOptions(
            prompt=MessageFactory.text("Complemento (opcional):")
        ))

    async def coletar_bairro(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["complemento"] = step.result
        return await step.prompt("BairroPrompt", PromptOptions(
            prompt=MessageFactory.text("Bairro:")
        ))

    async def coletar_cidade(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["bairro"] = step.result
        return await step.prompt("CidadePrompt", PromptOptions(
            prompt=MessageFactory.text("Cidade:")
        ))

    async def coletar_estado(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["cidade"] = step.result
        return await step.prompt("EstadoPrompt", PromptOptions(
            prompt=MessageFactory.text("Estado (sigla):")
        ))

    async def coletar_cep(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["estado"] = step.result
        return await step.prompt("CepPrompt", PromptOptions(
            prompt=MessageFactory.text("CEP (00000-000):")
        ))

    '''async def coletar_endereco(self, step: WaterfallStepContext) -> DialogTurnResult:
        await step.context.send_activity("O campo 'complemento' é opcional.")
        return await step.next()'''


    # 4) Envia ao backend
    async def processar_compra(self, step: WaterfallStepContext) -> DialogTurnResult:
        step.values["cep"] = step.result
        modelo = ModeloComprarProduto(
            product_name=step.values["productName"],
            preco=step.values["preco"],
            usuario={
                "nome": step.values["nome"],
                "email": step.values["email"],
                "cpf": step.values["cpf"],
                "telefone": step.values["telefone"],
                "dtNascimento": step.values["dt_nascimento"],
            },
            endereco={
                "logradouro": step.values["logradouro"],
                "complemento": step.values["complemento"],
                "bairro": step.values["bairro"],
                "cidade": step.values["cidade"],
                "estado": step.values["estado"],
                "cep": step.values["cep"],
            },
            numero_cartao=step.values["numero_cartao"],
            data_expiracao=step.values["validade"],
            cvv=step.values["cvv"],
            saldo=step.values["saldo"],
        )

        sucesso, mensagem, idPedido = await enviar_compra(modelo.to_payload())
        step.values["idPedido"] = idPedido

        if sucesso:
            await step.context.send_activity(f"✅ {mensagem} ID do Pedido: {idPedido}")
        else:
            await step.context.send_activity(f"❌ {mensagem}")

        return await step.next(None)


    # 5) Prompt pós-compra
    async def pos_compra_prompt(self, step: WaterfallStepContext) -> DialogTurnResult:
        return await step.prompt("PosCompraPrompt", PromptOptions(
            prompt=MessageFactory.text("Deseja ver o extrato de compra ou voltar ao menu inicial?"),
            choices=[Choice("Extrato de Compra"), Choice("Menu Inicial")],
        ))

    async def pos_compra_handle(self, step: WaterfallStepContext) -> DialogTurnResult:
        escolha = step.result.value
        idPedido = step.values["idPedido"]  # Recupera o ID do pedido

        if escolha == "Extrato de Compra":
            # Gera e exibe o extrato com o ID do pedido
            extrato = (
                f"**👤 Usuário**\n"
                f"- Nome: {step.values['nome']}\n"
                f"- CPF: `{step.values['cpf']}`\n"
                f"- E-mail: {step.values['email']}\n\n"
                f"**🛍️ Pedido**\n"
                f"- Produto: *{step.values['productName']}*\n"
                f"- Valor: R$ {step.values['preco']:.2f}\n"
                f"- ID do Pedido: `{idPedido}`\n\n"
                f"**💳 Cartão**\n"
                f"- Validade: {step.values['validade']}\n"
                f"- Últimos 4 dígitos: `{step.values['numero_cartao'][-4:]}`\n\n"
                f"**🏠 Endereço**\n"
                f"- {step.values['logradouro']}\n"
                f"- {step.values['complemento']}\n"
                f"- {step.values['bairro']}\n"
                f"- {step.values['cidade']}\n"
                f"- CEP: {step.values['cep']}"
            )
            await step.context.send_activity(MessageFactory.text(extrato))

        return await step.end_dialog()


    # Validators estáticos

    @staticmethod
    async def validar_numero_cartao(pc: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"\d{13,19}", pc.recognized.value))

    @staticmethod
    async def validar_data_expiracao(pc: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"(0[1-9]|1[0-2])/\d{2}$", pc.recognized.value))

    @staticmethod
    async def validar_cvv(pc: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"\d{3,4}", pc.recognized.value))

    @staticmethod
    async def validar_saldo(pc: PromptValidatorContext) -> bool:
        try:
            return float(pc.recognized.value) >= 0
        except:
            return False

    @staticmethod
    async def validar_email(pc: PromptValidatorContext) -> bool:
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", pc.recognized.value))

    @staticmethod
    async def validar_cpf(pc: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"\d{11}", pc.recognized.value))

    @staticmethod
    async def validar_data_nascimento(pc: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", pc.recognized.value))

    @staticmethod
    async def validar_cep(pc: PromptValidatorContext) -> bool:
        return bool(re.fullmatch(r"\d{5}-\d{3}", pc.recognized.value))
