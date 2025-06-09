package cloud.ecommerceisafabbia.service;

import cloud.ecommerceisafabbia.objetosmodelo.*;
import cloud.ecommerceisafabbia.repositorioJPA.*;
import cloud.ecommerceisafabbia.request.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import cloud.ecommerceisafabbia.request.Usuario;
import cloud.ecommerceisafabbia.request.Endereco;
import cloud.ecommerceisafabbia.request.Cartao;

import javax.transaction.Transactional;

@Service
public class CompraService {

    @Autowired private UsuarioRepository usuarioRepo;
    @Autowired private EnderecoRepository enderecoRepo;
    @Autowired private CartaoRepository cartaoRepo;
    @Autowired private ProdutoRepository produtoRepo;

    @Transactional
    public String processarCompra(CompraRequest request) {
        Produto produto = produtoRepo.findByNome(request.getProductName());
        if (produto == null || produto.getPreco() != request.getPreco()) {
            throw new IllegalArgumentException("Produto inválido ou preço divergente");
        }

        CartaoDTO cartaoDTO = request.getCartao();
        if (cartaoDTO.getSaldo() < produto.getPreco()) {
            throw new IllegalArgumentException("Saldo insuficiente no cartão");
        }

        Usuario usuario = new Usuario();
        usuario.setNome(request.getUsuario().getNome());
        usuario.setEmail(request.getUsuario().getEmail());
        usuario.setCpf(request.getUsuario().getCpf());
        usuario.setTelefone(request.getUsuario().getTelefone());
        usuarioRepo.save(usuario);

        Endereco endereco = new Endereco();
        endereco.setUsuario(usuario);
        endereco.setLogradouro(request.getEndereco().getLogradouro());
        endereco.setComplemento(request.getEndereco().getComplemento());
        endereco.setBairro(request.getEndereco().getBairro());
        endereco.setCidade(request.getEndereco().getCidade());
        endereco.setEstado(request.getEndereco().getEstado());
        endereco.setCep(request.getEndereco().getCep());
        enderecoRepo.save(endereco);

        Cartao cartao = new Cartao();
        cartao.setUsuario(usuario);
        cartao.setNumero(cartaoDTO.getNumero());
        cartao.setValidade(cartaoDTO.getValidade());
        cartao.setCvv(cartaoDTO.getCvv());
        cartao.setSaldo(cartaoDTO.getSaldo() - produto.getPreco());
        cartaoRepo.save(cartao);

        return "Compra realizada com sucesso!";
    }
}
