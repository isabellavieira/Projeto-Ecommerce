# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from urllib import response
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

import uuid


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        # Processa a mensagem do usuário
        user_message = turn_context.activity.text
        await turn_context.send_activity(f"You said '{user_message}'")

        # Gerando um ID único para o pedido
        order_id = str(uuid.uuid4())

        # Resposta com o ID de pedido
        response_message = (
            f"Compra realizada com sucesso! Seu ID de pedido é: {order_id}.\n"
        )

        # Enviando a resposta com o ID de pedido para o usuário
        await turn_context.send_activity(response_message)

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
