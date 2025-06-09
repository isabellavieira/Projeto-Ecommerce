# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from bot.dialogs.main_dialog import MainDialog



class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Bem-vindo ao Bot Ecommerce IsaFabBia!")
                await turn_context.send_activity("Digite a opção desejada:\\n"\
                    "1 - Consultar pedidos \\n" \
                    "2 - Consultar produtos \\n"\
                    "1 - Extrato de cartão \\n")
