package cloud.ecommerceisafabbia.repositorioJPA;

import org.springframework.stereotype.Repository;

import com.azure.spring.data.cosmos.repository.CosmosRepository;

import cloud.ecommerceisafabbia.objetosmodelo.Produto;  // Mudança do pacote e modelo

@Repository
public interface ProdutoRepository extends CosmosRepository<Produto, String> {

}
