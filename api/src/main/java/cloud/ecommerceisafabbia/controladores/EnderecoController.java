package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.objetosmodelo.Endereco;
import cloud.ecommerceisafabbia.objetosmodelo.Usuario;
import cloud.ecommerceisafabbia.repositorioJPA.EnderecoRepository;
import cloud.ecommerceisafabbia.repositorioJPA.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/usuarios/{id_usuario}/enderecos")
public class EnderecoController {

    @Autowired
    private EnderecoRepository enderecoRepository;

    @Autowired
    private UsuarioRepository usuarioRepository;

    /**
     * Cria um novo endereço e associa ao usuário, retornando o usuário atualizado.
     */
    @PostMapping
    public ResponseEntity<Usuario> criarEndereco(
            @PathVariable("id_usuario") int idUsuario,
            @RequestBody Endereco endereco
    ) {
        Optional<Usuario> usuarioOpt = usuarioRepository.findById(idUsuario);
        if (usuarioOpt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        Usuario usuario = usuarioOpt.get();
        Endereco salvo = enderecoRepository.save(endereco);
        usuario.getEnderecos().add(salvo);
        usuarioRepository.save(usuario);
        return ResponseEntity.status(HttpStatus.CREATED).body(usuario);
    }

    /**
     * Lista todos os endereços de um usuário.
     */
    @GetMapping
    public ResponseEntity<List<Endereco>> listarEnderecos(
            @PathVariable("id_usuario") int idUsuario
    ) {
        Optional<Usuario> usuarioOpt = usuarioRepository.findById(idUsuario);
        if (usuarioOpt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        List<Endereco> enderecos = usuarioOpt.get().getEnderecos();
        return ResponseEntity.ok(enderecos);
    }

    /**
     * Exclui um endereço de um usuário.
     */
    @DeleteMapping("/{id_endereco}")
    public ResponseEntity<Void> excluirEndereco(
            @PathVariable("id_usuario") int idUsuario,
            @PathVariable("id_endereco") int idEndereco
    ) {
        Optional<Usuario> usuarioOpt = usuarioRepository.findById(idUsuario);
        if (usuarioOpt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        if (!enderecoRepository.existsById(idEndereco)) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        enderecoRepository.deleteById(idEndereco);
        return ResponseEntity.noContent().build();
    }
}
