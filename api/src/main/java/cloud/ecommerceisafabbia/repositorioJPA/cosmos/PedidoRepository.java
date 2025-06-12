package cloud.ecommerceisafabbia.repositorioJPA.cosmos;

import cloud.ecommerceisafabbia.objetosmodelo.Pedido;
import com.azure.spring.data.cosmos.repository.CosmosRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface PedidoRepository extends CosmosRepository<Pedido, String> {
    // Método customizado para buscar pedidos por usuário
    List<Pedido> findByUsuarioId(int usuarioId);
}
