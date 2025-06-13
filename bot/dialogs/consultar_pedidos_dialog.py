from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, DialogTurnResult
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions
from botbuilder.core import MessageFactory
from bot.api.cosmos_connector import consultar_pedido_por_id
from botbuilder.schema import SuggestedActions, CardAction

class ConsultarPedidosDialog(ComponentDialog):
    def __init__(self, dialog_id: str = "ConsultarPedidosDialog"):
        super(ConsultarPedidosDialog, self).__init__(dialog_id)

        self.add_dialog(TextPrompt("IdPedidoPrompt"))
        self.add_dialog(WaterfallDialog("ConsultarPedidosWaterfallDialog", [
            self.perguntar_id_pedido,
            self.consultar_pedido
        ]))

        self.initial_dialog_id = "ConsultarPedidosWaterfallDialog"

    async def perguntar_id_pedido(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        return await step_context.prompt(
            "IdPedidoPrompt",
            PromptOptions(
                prompt=MessageFactory.text("Por favor, informe o ID do pedido:")
            )
        )

    async def consultar_pedido(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        id_pedido = step_context.result

        # Consulta o pedido no backend
        pedido = consultar_pedido_por_id(id_pedido)

        if pedido:
            detalhes = (
                f"**👤 Usuário**\n"
                f"- Nome: {pedido['nome']}\n"
                f"- CPF: {pedido['cpf']}\n"
                f"- Email: {pedido['email']}\n\n"
                f"**🛍️ Pedido**\n"
                f"- Produto: {pedido['productName']}\n"
                f"- Valor: R$ {pedido['preco']:.2f}\n"
                f"- ID do Pedido: {pedido['id']}\n\n"
                f"**💳 Cartão**\n"
                f"- Número: {pedido['numeroCartao']}\n"
                f"- Validade: {pedido['dtExpiracaoCartao']}\n\n"
                f"**🏠 Endereço**\n"
                f"- Logradouro: {pedido['logradouro']}\n"
                f"- Bairro: {pedido['bairro']}\n"
                f"- Complemento: {pedido['complemento']}\n"
                f"- Cidade: {pedido['cidade']}\n"
                f"- Estado: {pedido['estado']}\n"
                f"- CEP: {pedido['cep']}"
            )
            await step_context.context.send_activity(MessageFactory.text(detalhes))

            # Adiciona o botão "Menu Inicial"
            await step_context.context.send_activity(
                MessageFactory.suggested_actions(
                    actions=[
                        CardAction(title="Menu Inicial", type="imBack", value="Menu Inicial")
                    ],
                    text="Clique no botão abaixo para voltar ao menu inicial:"
                )
            )
        else:
            await step_context.context.send_activity("❌ Pedido não encontrado. Verifique o ID e tente novamente.")

        return await step_context.end_dialog()