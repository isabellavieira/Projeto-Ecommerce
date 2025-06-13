package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.request.CompraRequest;
import cloud.ecommerceisafabbia.service.CompraService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/compras")
public class CompraController {

    @Autowired
    private CompraService compraService;

    @PostMapping
    public ResponseEntity<?> realizarCompra(@RequestBody CompraRequest request) {
        try {
            String idPedido = compraService.processarCompra(request);
            return ResponseEntity.ok().body(new ResponseDTO(true, "Compra realizada com sucesso!", idPedido));
        } catch (Exception e) {
            return ResponseEntity.internalServerError()
                    .body(new ResponseDTO(false, "Erro interno: " + e.getMessage(), null));
        }
    }

    static class ResponseDTO {
        private boolean sucesso;
        private String mensagem;
        private String idPedido;

        public ResponseDTO(boolean sucesso, String mensagem, String idPedido) {
            this.sucesso = sucesso;
            this.mensagem = mensagem;
            this.idPedido = idPedido;
        }

        public boolean isSucesso() {
            return sucesso;
        }

        public void setSucesso(boolean sucesso) {
            this.sucesso = sucesso;
        }

        public String getMensagem() {
            return mensagem;
        }

        public void setMensagem(String mensagem) {
            this.mensagem = mensagem;
        }

        public String getIdPedido() {
            return idPedido;
        }

        public void setIdPedido(String idPedido) {
            this.idPedido = idPedido;
        }
    }
}
