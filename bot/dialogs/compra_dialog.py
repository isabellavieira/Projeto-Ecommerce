from botbuilder.dialogs import (
    ComponentDialog, WaterfallDialog, WaterfallStepContext,
    TextPrompt, PromptOptions
)
from botbuilder.core import MessageFactory
from bot.services.compra_api_client import enviar_compra
from botbuilder.dialogs.prompts import PromptValidatorContext
import re

class CompraDialog(ComponentDialog):
    def __init__(self, dialog_id: str = "compraDialog"):
        super(CompraDialog, self).__init__(dialog_id)

        self.add_dialog(TextPrompt("TextPrompt"))
        self.add_dialog(TextPrompt("EmailPrompt", CompraDialog.validar_email))
        self.add_dialog(TextPrompt("CpfPrompt", CompraDialog.validar_cpf))
        self.add_dialog(TextPrompt("ValorPrompt", CompraDialog.validar_valor))
        self.add_dialog(WaterfallDialog("WaterfallDialog", [
            self.confirmar_compra,
            self.coletar_nome,
            self.coletar_email,
            self.coletar_cpf,
            self.coletar_telefone,
            self.coletar_logradouro,
            self.coletar_complemento,
            self.coletar_bairro,
            self.coletar_cidade,
            self.coletar_estado,
            self.coletar_cep,
            self.coletar_num_cartao,
            self.coletar_validade,
            self.coletar_cvv,
            self.coletar_saldo,
            self.enviar_compra_backend
        ]))

        self.initial_dialog_id = "WaterfallDialog"

    async def confirmar_compra(self, step: WaterfallStepContext):
        step.values["productName"] = step.options["productName"]
        step.values["preco"] = step.options["preco"]
        return await step.prompt("TextPrompt", PromptOptions(
        prompt=MessageFactory.text(f"Deseja confirmar a compra de {step.values['productName']} por R$ {step.values['preco']}? (sim/não) ")
    ))

    async def coletar_nome(self, step: WaterfallStepContext):
        if step.result.lower() != "sim":
            await step.context.send_activity("Compra cancelada.")
            return await step.replace_dialog("MainDialog")  # Redireciona ao menu principal ou ao início
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Informe seu nome completo:")))


    async def coletar_email(self, step: WaterfallStepContext):
        step.values["nome"] = step.result
        return await step.prompt("EmailPrompt", PromptOptions(prompt=MessageFactory.text("Informe seu e-mail:")))

    async def coletar_cpf(self, step: WaterfallStepContext):
        step.values["email"] = step.result
        return await step.prompt("CpfPrompt", PromptOptions(prompt=MessageFactory.text("Informe seu CPF (somente números):")))

    async def coletar_telefone(self, step: WaterfallStepContext):
        step.values["cpf"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Informe seu telefone com DDD:")))

    async def coletar_logradouro(self, step: WaterfallStepContext):
        step.values["telefone"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Logradouro:")))

    async def coletar_complemento(self, step: WaterfallStepContext):
        step.values["logradouro"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Complemento:")))

    async def coletar_bairro(self, step: WaterfallStepContext):
        step.values["complemento"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Bairro:")))

    async def coletar_cidade(self, step: WaterfallStepContext):
        step.values["bairro"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Cidade:")))

    async def coletar_estado(self, step: WaterfallStepContext):
        step.values["cidade"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Estado:")))

    async def coletar_cep(self, step: WaterfallStepContext):
        step.values["estado"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("CEP:")))

    async def coletar_num_cartao(self, step: WaterfallStepContext):
        step.values["cep"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Número do cartão:")))

    async def coletar_validade(self, step: WaterfallStepContext):
        step.values["numero"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("Validade (MM/AA):")))

    async def coletar_cvv(self, step: WaterfallStepContext):
        step.values["validade"] = step.result
        return await step.prompt("TextPrompt", PromptOptions(prompt=MessageFactory.text("CVV:")))

    async def coletar_saldo(self, step: WaterfallStepContext):
        step.values["cvv"] = step.result
        return await step.prompt("ValorPrompt", PromptOptions(prompt=MessageFactory.text("Saldo no cartão (simulado):")))

    async def enviar_compra_backend(self, step: WaterfallStepContext):
        step.values["saldo"] = float(step.result)

        payload = {
            "productName": step.values["productName"],
            "preco": step.values["preco"],
            "usuario": {    
                "nome": step.values["nome"],
                "email": step.values["email"],
                "cpf": step.values["cpf"],
                "telefone": step.values["telefone"]
            },
            "endereco": {
                "logradouro": step.values["logradouro"],
                "complemento": step.values["complemento"],
                "bairro": step.values["bairro"],
                "cidade": step.values["cidade"],
                "estado": step.values["estado"],
                "cep": step.values["cep"]
            },
            "cartao": {
                "numero": step.values["numero"],
                "validade": step.values["validade"],
                "cvv": step.values["cvv"],
                "saldo": step.values["saldo"]
            }
        }

        sucesso, mensagem = await enviar_compra(payload)
        await step.context.send_activity(mensagem)
        return await step.end_dialog()

    @staticmethod
    async def validar_email(prompt_context: PromptValidatorContext) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", prompt_context.recognized.value)

    @staticmethod
    async def validar_cpf(prompt_context: PromptValidatorContext) -> bool:
        return re.fullmatch(r"\d{11}", prompt_context.recognized.value)

    @staticmethod
    async def validar_valor(prompt_context: PromptValidatorContext) -> bool:
        try:
            return float(prompt_context.recognized.value) >= 0
        except ValueError:
            return False
