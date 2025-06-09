
from bot.api.product_api import ProductAPI
from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory

class ConsultarProdutosDialog (ComponentDialog):
    def __init__(self):
        super(ConsultarProdutosDialog, self).__init__(ConsultarProdutosDialog.__name__)

        self.add_dialog(
            WaterfallDialog(
                "ConsultarProdutosDialog",
                [
                    self.product_name_step
                ],
            )
        )
        
        
        self.initial_dialog_id = "ConsultarProdutosDialog"
        
    async def product_name_step(self, step_context: WaterfallStepContext):
        return await step_context.send_activity(
            MessageFactory.text("Você escolheu Consultar Produtos.")
        )
        return await step_context.end_dialog()