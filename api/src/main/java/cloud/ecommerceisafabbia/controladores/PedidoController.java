package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.objetosmodelo.Pedido;
import cloud.ecommerceisafabbia.repositorioJPA.PedidoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/pedidos")
public class PedidoController {

    @Autowired
    private PedidoRepository pedidoRepository;

    // Método para buscar todos os pedidos de um usuário
    @GetMapping("/{usuarioId}")
    public ResponseEntity<List<Pedido>> obterPedidosPorUsuario(@PathVariable("usuarioId") String usuarioId) {
        List<Pedido> pedidos = pedidoRepository.findByUsuarioId(usuarioId);
        if (pedidos.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(pedidos, HttpStatus.OK);
    }
}
