# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from urllib import response
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text
        response = await enviar_compra(payload)  # Função que envia o payload ao backend.

        if response.get("sucesso"):
            await turn_context.send_activity("Compra realizada com sucesso!")
        else:
            await turn_context.send_activity(f"Erro: {response.get('mensagem')}")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Bem-vindo ao Bot Ecommerce IsaFabBia!")
                await turn_context.send_activity("Digite a opção desejada:\n"
                    "1 - Consultar pedidos \n"
                    "2 - Consultar produtos \n"
                    "3 - Extrato de cartão \n")
