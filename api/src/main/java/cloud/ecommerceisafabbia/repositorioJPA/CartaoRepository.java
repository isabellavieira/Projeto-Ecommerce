package cloud.ecommerceisafabbia.repositorioJPA;

import cloud.ecommerceisafabbia.objetosmodelo.Cartao;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CartaoRepository extends JpaRepository<Cartao, Integer> {
    // JpaRepository já fornece implementações padrão para CRUD, como save(), findById(), findAll(), delete(), etc.
}
