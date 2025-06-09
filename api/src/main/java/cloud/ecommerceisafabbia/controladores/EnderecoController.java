package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.objetosmodelo.Endereco;
import cloud.ecommerceisafabbia.objetosmodelo.Usuario;
import cloud.ecommerceisafabbia.repositorioJPA.EnderecoRepository;
import cloud.ecommerceisafabbia.repositorioJPA.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/usuarios/{id_usuario}/enderecos")
public class EnderecoController {

    @Autowired
    private EnderecoRepository enderecoRepository;

    @Autowired
    private UsuarioRepository usuarioRepository;

    // Método para adicionar um novo endereço
    @PostMapping
    public ResponseEntity<String> adicionarEndereco(@PathVariable("id_usuario") int idUsuario, @RequestBody Endereco endereco) {
        Optional<Usuario> usuarioOptional = usuarioRepository.findById(idUsuario);
        if (usuarioOptional.isEmpty()) {
            return new ResponseEntity<>("Usuário não encontrado", HttpStatus.NOT_FOUND);
        }
        enderecoRepository.save(endereco);
        usuarioOptional.get().getEnderecos().add(endereco);
        usuarioRepository.save(usuarioOptional.get());
        return new ResponseEntity<>("Endereço adicionado com sucesso", HttpStatus.CREATED);
    }

    // Método para buscar todos os endereços de um usuário
    @GetMapping
    public ResponseEntity<?> obterEnderecos(@PathVariable("id_usuario") int idUsuario) {
        Optional<Usuario> usuarioOptional = usuarioRepository.findById(idUsuario);
        if (usuarioOptional.isEmpty()) {
            return new ResponseEntity<>("Usuário não encontrado", HttpStatus.NOT_FOUND);
        }
      return new ResponseEntity<>(usuarioOptional.get().getEnderecos(), HttpStatus.OK);
    }

    // Método para excluir um endereço de um usuário
    @DeleteMapping("/{id_endereco}")
    public ResponseEntity<String> excluirEndereco(@PathVariable("id_usuario") int idUsuario, @PathVariable("id_endereco") int idEndereco) {
        Optional<Usuario> usuarioOptional = usuarioRepository.findById(idUsuario);
        if (usuarioOptional.isEmpty()) {
            return new ResponseEntity<>("Usuário não encontrado", HttpStatus.NOT_FOUND);
        }
        Optional<Endereco> enderecoOptional = enderecoRepository.findById(idEndereco);
        if (enderecoOptional.isEmpty()) {
            return new ResponseEntity<>("Endereço não encontrado", HttpStatus.NOT_FOUND);
        }
        enderecoRepository.deleteById(idEndereco);
        return new ResponseEntity<>("Endereço excluído com sucesso", HttpStatus.NO_CONTENT);
    }
}
