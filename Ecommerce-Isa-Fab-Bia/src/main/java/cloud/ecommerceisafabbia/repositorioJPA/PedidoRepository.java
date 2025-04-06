package cloud.ecommerceisafabbia.repositorioJPA;

import cloud.ecommerceisafabbia.objetosmodelo.Pedido;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository // Isso garante que o Spring reconheça como um repositório
public interface PedidoRepository extends CrudRepository<Pedido, String> {
}
