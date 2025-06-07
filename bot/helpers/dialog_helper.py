from botbuilder.core import StatePropertyAccessor, TurnContext
from botbuilder.dialogs import Dialog, DialogSet, DialogTurnStatus

class DialogoAjudante:
    @staticmethod
    async def run_dialog(
        dialog: Dialog,
        turn_context: TurnContext,
        dialog_state_accessor: StatePropertyAccessor,
    ):
        """
        Run the specified dialog with the current turn context and dialog state accessor.
        """
        dialog_set = DialogSet(dialog_state_accessor)
        dialog_set.add(dialog)

        # Create a dialog context for the current turn
        dialog_context = await dialog_set.create_context(turn_context)

        # Run the dialog and get the result
        result = await dialog_context.continue_dialog()

        if result.status == DialogTurnStatus.Empty:
            # If no active dialog, start the specified dialog
            await dialog_context.begin_dialog(dialog.id)