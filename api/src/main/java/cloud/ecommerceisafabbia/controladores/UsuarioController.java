package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.objetosmodelo.Usuario;
import cloud.ecommerceisafabbia.repositorioJPA.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/usuarios")
public class UsuarioController {

    @Autowired
    private UsuarioRepository usuarioRepository;

    // Método para criar um novo usuário
    @PostMapping
    public ResponseEntity<Usuario> criarUsuario(@RequestBody Usuario usuario) {
        usuarioRepository.save(usuario);
        return new ResponseEntity<>(usuario, HttpStatus.CREATED);
    }

    // Método para buscar um usuário por ID
    @GetMapping("/{id}")
    public ResponseEntity<Usuario> obterUsuarioPorId(@PathVariable Integer id) {
        Optional<Usuario> usuario = usuarioRepository.findById(id);
        if (usuario.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(usuario.get(), HttpStatus.OK);
    }

    // Método para listar todos os usuários
    @GetMapping
    public ResponseEntity<List<Usuario>> obterTodosUsuarios() {
        List<Usuario> usuarios = usuarioRepository.findAll();
        return new ResponseEntity<>(usuarios, HttpStatus.OK);
    }

    // Método para excluir um usuário por ID
    @DeleteMapping("/{id}")
    public ResponseEntity<String> excluirUsuario(@PathVariable Integer id) {
        Optional<Usuario> usuario = usuarioRepository.findById(id);
        if (usuario.isEmpty()) {
            return new ResponseEntity<>("Usuário não encontrado", HttpStatus.NOT_FOUND);
        }
        usuarioRepository.deleteById(id);
        return new ResponseEntity<>("Usuário excluído com sucesso", HttpStatus.NO_CONTENT);
    }
}
