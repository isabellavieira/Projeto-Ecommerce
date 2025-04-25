package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.objetosmodelo.Produto;
import cloud.ecommerceisafabbia.repositorioJPA.ProdutoRepository;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/produtos")
public class ProdutoController {

    @Autowired
    private ProdutoRepository produtoRepository;

    // Método para criar um novo produto
    @PostMapping
    public ResponseEntity<Produto> criarProduto(@Valid @RequestBody Produto produto) {
        produto.setId(UUID.randomUUID().toString());
        produtoRepository.save(produto);
        return new ResponseEntity<>(produto, HttpStatus.CREATED);
    }

    // Método para buscar um produto por ID
    @GetMapping("/{id}")
    public ResponseEntity<Produto> obterProdutoPorId(@PathVariable String id) {
        Optional<Produto> produto = produtoRepository.findById(id);

        return produto.map(ResponseEntity::ok)
                .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }

    // Método para listar todos os produtos com paginação
    @GetMapping
    public ResponseEntity<Page<Produto>> obterTodosProdutos(Pageable pageable) {
        Page<Produto> produtos = produtoRepository.findAll(pageable);
        return new ResponseEntity<>(produtos, HttpStatus.OK);
    }

    // Método para excluir um produto pelo ID
    @DeleteMapping("/{id}")
    public ResponseEntity<?> excluirProduto(@PathVariable String id) {
        Optional<Produto> produto = produtoRepository.findById(id);

        if (produto.isEmpty()) {
            return new ResponseEntity<>("Produto não encontrado", HttpStatus.NOT_FOUND);
        }

        produtoRepository.delete(produto.get());
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }
}
