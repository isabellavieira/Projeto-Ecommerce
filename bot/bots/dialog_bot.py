# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from botbuilder.core import MessageFactory  # Importação necessária
from botbuilder.core import ActivityHandler, ConversationState, TurnContext, UserState
from botbuilder.dialogs import Dialog
from bot.helpers.dialog_helper import DialogHelper
from botbuilder.schema import ChannelAccount, SuggestedActions, CardAction


class DialogBot(ActivityHandler):
    """
    This Bot implementation can run any type of Dialog. The use of type parameterization is to allows multiple
    different bots to be run at different endpoints within the same project. This can be achieved by defining distinct
    Controller types each with dependency on distinct Bot types. The ConversationState is used by the Dialog system. The
    UserState isn't, however, it might have been used in a Dialog implementation, and the requirement is that all
    BotState objects are saved at the end of a turn.
    """

    def __init__(
        self,
        conversation_state: ConversationState,
        user_state: UserState,
        dialog: Dialog,
    ):
        if conversation_state is None:
            raise TypeError(
                "[DialogBot]: Missing parameter. conversation_state is required but None was given"
            )
        if user_state is None:
            raise TypeError(
                "[DialogBot]: Missing parameter. user_state is required but None was given"
            )
        if dialog is None:
            raise Exception("[DialogBot]: Missing parameter. dialog is required")

        self.conversation_state = conversation_state
        self.user_state = user_state
        self.dialog = dialog

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        # Save any state changes that might have ocurred during the turn.
        await self.conversation_state.save_changes(turn_context)
        await self.user_state.save_changes(turn_context)

    async def on_message_activity(self, turn_context: TurnContext):
        await DialogHelper.run_dialog(
            self.dialog,
            turn_context,
            self.conversation_state.create_property("DialogState"),
        )
    async def on_members_added_activity(
        self,
        members_added: [ChannelAccount],
        turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Olá, bem-vindo ao Bot Ecommerce IsaFabBia!")

                # Envia botões interativos
                await turn_context.send_activity(
                    MessageFactory.suggested_actions(
                        actions=[
                            CardAction(title="Consultar Pedidos", type="imBack", value="Consultar Pedidos"),
                            CardAction(title="Consultar Produtos", type="imBack", value="Consultar Produtos")
                        ],
                        text="Escolha uma opção:"
                    )
                )