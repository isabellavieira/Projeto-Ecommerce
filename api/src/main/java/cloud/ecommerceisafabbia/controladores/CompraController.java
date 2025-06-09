package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.request.CompraRequest;
import cloud.ecommerceisafabbia.service.CompraService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import cloud.ecommerceisafabbia.request.Usuario;
import cloud.ecommerceisafabbia.request.Endereco;
import cloud.ecommerceisafabbia.request.Cartao;


@RestController
@RequestMapping("/api/compras")
public class CompraController {

    @Autowired
    private CompraService compraService;

    @PostMapping
    public ResponseEntity<?> realizarCompra(@RequestBody CompraRequest request) {
        try {
            String mensagem = compraService.processarCompra(request);
            return ResponseEntity.ok().body(new ResponseDTO(true, mensagem));
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().body(new ResponseDTO(false, e.getMessage()));
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(new ResponseDTO(false, "Erro interno: " + e.getMessage()));
        }
    }

    static class ResponseDTO {
        private boolean sucesso;
        private String mensagem;

        public ResponseDTO(boolean sucesso, String mensagem) {
            this.sucesso = sucesso;
            this.mensagem = mensagem;
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
    }
}
