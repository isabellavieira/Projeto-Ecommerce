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

    public Optional<Usuario> atualizarUsuario(Integer id, UsuarioUpdateDTO dto) {
        Optional<Usuario> optionalUsuario = usuarioRepository.findById(id);
        if(optionalUsuario.isPresent()){
            Usuario usuarioExistente = optionalUsuario.get();
            if(dto.getNome() != null) {
                usuarioExistente.setNome(dto.getNome());
            }
            if(dto.getEmail() != null) {
                usuarioExistente.setEmail(dto.getEmail());
            }
            // Atualize outros campos, se necessário

            usuarioRepository.save(usuarioExistente);
            return Optional.of(usuarioExistente);
        }
        return Optional.empty();
    }
}