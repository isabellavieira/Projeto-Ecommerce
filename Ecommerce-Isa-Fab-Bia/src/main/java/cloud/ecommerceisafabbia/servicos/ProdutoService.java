package cloud.ecommerceisafabbia.servicos;

import cloud.ecommerceisafabbia.dto.ProdutoUpdateDTO;
import cloud.ecommerceisafabbia.objetosmodelo.Produto;
import cloud.ecommerceisafabbia.repositorioJPA.ProdutoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class ProdutoService {

    @Autowired
    private ProdutoRepository produtoRepository;

    public Optional<Produto> atualizarProduto(Integer id, ProdutoUpdateDTO dto) {
        Optional<Produto> optionalProduto = produtoRepository.findById(id);
        if(optionalProduto.isPresent()){
            Produto produtoExistente = optionalProduto.get();
            if(dto.getNome() != null) {
                produtoExistente.setNome(dto.getNome());
            }
            if(dto.getDescricao() != null) {
                produtoExistente.setDescricao(dto.getDescricao());
            }
            if(dto.getPreco() != null) {
                produtoExistente.setPreco(dto.getPreco());
            }
            // Atualize outros campos se necessário

            produtoRepository.save(produtoExistente);
            return Optional.of(produtoExistente);
        }
        return Optional.empty();
    }
}