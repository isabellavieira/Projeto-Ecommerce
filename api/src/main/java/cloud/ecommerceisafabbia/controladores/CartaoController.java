package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.objetosmodelo.Cartao;
import cloud.ecommerceisafabbia.objetosmodelo.Usuario;
import cloud.ecommerceisafabbia.repositorioJPA.CartaoRepository;
import cloud.ecommerceisafabbia.repositorioJPA.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/usuarios/{id_usuario}/cartoes")
public class CartaoController {

    @Autowired
    private CartaoRepository cartaoRepository;

    @Autowired
    private UsuarioRepository usuarioRepository;

    // Método para adicionar um novo cartão
    @PostMapping
    public ResponseEntity<String> adicionarCartao(@PathVariable("id_usuario") int idUsuario, @RequestBody Cartao cartao) {
        Optional<Usuario> usuarioOptional = usuarioRepository.findById(idUsuario);
        if (usuarioOptional.isEmpty()) {
            return new ResponseEntity<>("Usuário não encontrado", HttpStatus.NOT_FOUND);
        }
        cartaoRepository.save(cartao);
        //usuarioOptional.get().getCartoes().add(cartao);
        usuarioRepository.save(usuarioOptional.get());
        return new ResponseEntity<>("Cartão adicionado com sucesso", HttpStatus.CREATED);
    }

    // Método para buscar o cartão de um usuário
    @GetMapping("/{id_cartao}")
    public ResponseEntity<Cartao> obterCartaoPorId(@PathVariable("id_usuario") int idUsuario, @PathVariable("id_cartao") String idCartao) {
        Optional<Usuario> usuarioOptional = usuarioRepository.findById(idUsuario);
        if (usuarioOptional.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        Optional<Cartao> cartaoOptional = cartaoRepository.findById(Integer.valueOf(idCartao));
        if (cartaoOptional.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(cartaoOptional.get(), HttpStatus.OK);
    }

    // Método para excluir um cartão
    @DeleteMapping("/{id_cartao}")
    public ResponseEntity<String> excluirCartao(@PathVariable("id_usuario") int idUsuario, @PathVariable("id_cartao") String idCartao) {
        Optional<Usuario> usuarioOptional = usuarioRepository.findById(idUsuario);
        if (usuarioOptional.isEmpty()) {
            return new ResponseEntity<>("Usuário não encontrado", HttpStatus.NOT_FOUND);
        }
        Optional<Cartao> cartaoOptional = cartaoRepository.findById(Integer.valueOf(idCartao));
        if (cartaoOptional.isEmpty()) {
            return new ResponseEntity<>("Cartão não encontrado", HttpStatus.NOT_FOUND);
        }
        cartaoRepository.deleteById(Integer.valueOf(idCartao));
        return new ResponseEntity<>("Cartão excluído com sucesso", HttpStatus.NO_CONTENT);
    }
}
