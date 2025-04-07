package cloud.ecommerceisafabbia.controladores;

import cloud.ecommerceisafabbia.dto.CompraUpdateDTO;
import cloud.ecommerceisafabbia.objetosmodelo.Compra;
import cloud.ecommerceisafabbia.repositorioJPA.CompraRepository;
import cloud.ecommerceisafabbia.servicos.CompraService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/compras")
public class CompraController {

    @Autowired
    private CompraRepository compraRepository;

    @Autowired
    private CompraService compraService;

    @PostMapping
    public ResponseEntity<Compra> criarCompra(@RequestBody Compra compra) {
        compraRepository.save(compra);
        return new ResponseEntity<>(compra, HttpStatus.CREATED);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Compra> obterCompraPorId(@PathVariable Integer id) {
        Optional<Compra> compra = compraRepository.findById(id);
        if(compra.isEmpty()){
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(compra.get(), HttpStatus.OK);
    }

    @GetMapping
    public ResponseEntity<List<Compra>> obterTodasCompras() {
        List<Compra> compras = compraRepository.findAll();
        return new ResponseEntity<>(compras, HttpStatus.OK);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> excluirCompra(@PathVariable Integer id) {
        Optional<Compra> compra = compraRepository.findById(id);
        if(compra.isEmpty()){
            return new ResponseEntity<>("Compra não encontrada", HttpStatus.NOT_FOUND);
        }
        compraRepository.deleteById(id);
        return new ResponseEntity<>("Compra excluída com sucesso", HttpStatus.NO_CONTENT);
    }

    // Endpoint para atualizar uma compra (pedido) pelo ID
    @PutMapping("/{id}")
    public ResponseEntity<Compra> atualizarCompra(@PathVariable Integer id,
                                                  @RequestBody CompraUpdateDTO dto) {
        Optional<Compra> compraAtualizada = compraService.atualizarCompra(id, dto);
        if(compraAtualizada.isEmpty()){
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(compraAtualizada.get(), HttpStatus.OK);
    }
}