package cloud.ecommerceisafabbia.servicos;

import cloud.ecommerceisafabbia.dto.UsuarioUpdateDTO;
import cloud.ecommerceisafabbia.objetosmodelo.Usuario;
import cloud.ecommerceisafabbia.repositorioJPA.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UsuarioService {

    @Autowired
    private UsuarioRepository usuarioRepository;

    public Optional<Usuario> atualizarUsuario(Integer id, UsuarioUpdateDTO usuarioUpdateDTO) {
        Optional<Usuario> optionalUsuario = usuarioRepository.findById(id);
        if (optionalUsuario.isPresent()) {
            Usuario usuarioExistente = optionalUsuario.get();

            // Atualize somente os campos que foram enviados
            if (usuarioUpdateDTO.getNome() != null) {
                usuarioExistente.setNome(usuarioUpdateDTO.getNome());
            }
            if (usuarioUpdateDTO.getEmail() != null) {
                usuarioExistente.setEmail(usuarioUpdateDTO.getEmail());
            }
            // Atualize outros campos conforme necessário

            usuarioRepository.save(usuarioExistente);
            return Optional.of(usuarioExistente);
        }
        return Optional.empty();
    }
}