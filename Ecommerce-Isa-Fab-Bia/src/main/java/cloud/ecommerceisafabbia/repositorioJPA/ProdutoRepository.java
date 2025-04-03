package cloud.ecommerceisafabbia.repositorioJPA;

import cloud.ecommerceisafabbia.objetosmodelo.Produto;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProdutoRepository extends JpaRepository<Produto, String> {
    // JpaRepository já fornece implementações padrão para CRUD, como save(), findById(), findAll(), delete(), etc.
}
