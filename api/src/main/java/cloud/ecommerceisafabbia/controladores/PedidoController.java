package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.objetosmodelo.Pedido;
import cloud.ecommerceisafabbia.repositorioJPA.cosmos.PedidoRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/pedidos")
public class PedidoController {

    @Autowired
    private PedidoRepository pedidoRepository;

    // Endpoint para consultar pedido por ID
    @GetMapping("/{id}")
    public ResponseEntity<?> consultarPedidoPorId(@PathVariable String id) {
        Optional<Pedido> pedido = pedidoRepository.findById(id);

        if (pedido.isPresent()) {
            return ResponseEntity.ok(pedido.get());
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Pedido não encontrado.");
        }
    }

    // Endpoint para obter pedidos por usuário
    @GetMapping("/usuario/{id}")
    public ResponseEntity<?> obterPedidosPorUsuario(@PathVariable int id) {
        List<Pedido> pedidos = pedidoRepository.findByUsuarioId(id);

        if (!pedidos.isEmpty()) {
            return ResponseEntity.ok(pedidos);
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Nenhum pedido encontrado para este usuário.");
        }
    }
}
