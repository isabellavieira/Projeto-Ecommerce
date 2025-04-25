package cloud.ecommerceisafabbia.repositorioJPA;

import cloud.ecommerceisafabbia.objetosmodelo.Endereco;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EnderecoRepository extends JpaRepository<Endereco, Integer> {
    // JpaRepository já fornece implementações padrão para CRUD, como save(), findById(), findAll(), delete(), etc.
}
