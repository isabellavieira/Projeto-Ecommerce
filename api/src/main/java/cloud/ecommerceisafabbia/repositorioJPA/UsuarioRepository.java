package cloud.ecommerceisafabbia.repositorioJPA;

import cloud.ecommerceisafabbia.objetosmodelo.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UsuarioRepository extends JpaRepository<Usuario, Integer> {
    // JpaRepository já fornece implementações padrão para CRUD, como save(), findById(), findAll(), delete(), etc.
}
