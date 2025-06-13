package cloud.ecommerceisafabbia.service;

import cloud.ecommerceisafabbia.objetosmodelo.Usuario;
import cloud.ecommerceisafabbia.objetosmodelo.Cartao;
import cloud.ecommerceisafabbia.objetosmodelo.Endereco;
import cloud.ecommerceisafabbia.objetosmodelo.Produto;
import cloud.ecommerceisafabbia.objetosmodelo.Pedido;

import cloud.ecommerceisafabbia.repositorioJPA.UsuarioRepository;
import cloud.ecommerceisafabbia.repositorioJPA.cosmos.PedidoRepository;
import cloud.ecommerceisafabbia.repositorioJPA.cosmos.ProdutoRepository;
import cloud.ecommerceisafabbia.repositorioJPA.EnderecoRepository;
import cloud.ecommerceisafabbia.repositorioJPA.CartaoRepository;
import cloud.ecommerceisafabbia.request.CompraRequest;
import cloud.ecommerceisafabbia.request.UsuarioRequest;
import cloud.ecommerceisafabbia.request.EnderecoRequest;
import cloud.ecommerceisafabbia.request.CartaoRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.time.LocalDateTime;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.util.UUID;
import java.time.LocalDate;

@Service
public class CompraService {

    @Autowired
    private UsuarioRepository usuarioRepo;
    @Autowired
    private EnderecoRepository enderecoRepo;
    @Autowired
    private CartaoRepository cartaoRepo;
    @Autowired
    private ProdutoRepository produtoRepo;
    @Autowired
    private PedidoRepository pedidoRepository;

    @Transactional
    public String processarCompra(CompraRequest request) {
        // 🧠 Produto (CosmosDB)
        Produto produto = produtoRepo.findByProductName(request.getProductName())
                .orElseThrow(() -> new IllegalArgumentException("Produto inválido ou inexistente!"));

        if (produto.getPrice() != request.getPreco()) {
            throw new IllegalArgumentException("Preço divergente");
        }

        // 🧠 Validação de saldo
        CartaoRequest cartaoDTO = request.getCartao();
        if (cartaoDTO.getSaldo() < produto.getPrice()) {
            throw new IllegalArgumentException("Saldo insuficiente no cartão");
        }

        // 🧠 Cria e salva usuário
        UsuarioRequest usuarioReq = request.getUsuario();
        Usuario usuario = new Usuario();
        usuario.setNome(usuarioReq.getNome());
        usuario.setEmail(usuarioReq.getEmail());
        usuario.setCpf(usuarioReq.getCpf());
        usuario.setTelefone(usuarioReq.getTelefone());
        usuario.setDtNascimento(usuarioReq.getDtNascimento());
        usuarioRepo.save(usuario);

        // 🧠 Cria e salva endereço
        EnderecoRequest enderecoReq = request.getEndereco();
        Endereco endereco = new Endereco();
        endereco.setUsuario(usuario);
        endereco.setLogradouro(enderecoReq.getLogradouro());
        endereco.setComplemento(enderecoReq.getComplemento());
        endereco.setBairro(enderecoReq.getBairro());
        endereco.setCidade(enderecoReq.getCidade());
        endereco.setEstado(enderecoReq.getEstado());
        endereco.setCep(enderecoReq.getCep());
        enderecoRepo.save(endereco);

        // 🧠 Cria e salva cartão
        Cartao cartao = new Cartao();
        cartao.setUsuario(usuario);
        cartao.setNumero(cartaoDTO.getNumero());
        cartao.setDtExpiracao(YearMonth.parse(cartaoDTO.getValidade(), DateTimeFormatter.ofPattern("MM/yy")).atDay(1));
        cartao.setCvv(cartaoDTO.getCvv());
        cartao.setSaldo(cartaoDTO.getSaldo() - produto.getPrice());
        cartaoRepo.save(cartao);

        // 🧠 Salvar pedido no Cosmos DB
        Pedido pedido = new Pedido();
        pedido.setId(UUID.randomUUID().toString()); // Gerando ID único do pedido
        pedido.setProductName(produto.getProductName());
        pedido.setPreco(produto.getPrice());
        pedido.setUsuarioId(usuario.getId());
        pedido.setDataTransacao(LocalDateTime.now());
        pedido.setStatus("Concluída");
        pedidoRepository.save(pedido);

        // Retornar o ID do pedido gerado no Cosmos DB
        return pedido.getId();
    }

    @Transactional
    public String processarCompra(CompraRequest request, String idPedido) {
        // 🧠 Produto (CosmosDB)
        Produto produto = produtoRepo.findByProductName(request.getProductName())
                .orElseThrow(() -> new IllegalArgumentException("Produto inválido ou inexistente!"));

        if (produto.getPrice() != request.getPreco()) {
            throw new IllegalArgumentException("Preço divergente");
        }

        // 🧠 Validação de saldo
        CartaoRequest cartaoDTO = request.getCartao();
        if (cartaoDTO.getSaldo() < produto.getPrice()) {
            throw new IllegalArgumentException("Saldo insuficiente no cartão");
        }

        // 🧠 Cria e salva usuário
        UsuarioRequest usuarioReq = request.getUsuario();
        Usuario usuario = new Usuario();
        usuario.setNome(usuarioReq.getNome());
        usuario.setEmail(usuarioReq.getEmail());
        usuario.setCpf(usuarioReq.getCpf());
        usuario.setTelefone(usuarioReq.getTelefone());
        usuario.setDtNascimento(usuarioReq.getDtNascimento());
        usuarioRepo.save(usuario);

        // 🧠 Cria e salva endereço
        EnderecoRequest enderecoReq = request.getEndereco();
        Endereco endereco = new Endereco();
        endereco.setUsuario(usuario);
        endereco.setLogradouro(enderecoReq.getLogradouro());
        endereco.setComplemento(enderecoReq.getComplemento());
        endereco.setBairro(enderecoReq.getBairro());
        endereco.setCidade(enderecoReq.getCidade());
        endereco.setEstado(enderecoReq.getEstado());
        endereco.setCep(enderecoReq.getCep());
        enderecoRepo.save(endereco);

        // 🧠 Cria e salva cartão
        Cartao cartao = new Cartao();
        cartao.setUsuario(usuario);
        cartao.setNumero(cartaoDTO.getNumero());
        cartao.setDtExpiracao(YearMonth.parse(cartaoDTO.getValidade(), DateTimeFormatter.ofPattern("MM/yy")).atDay(1));
        cartao.setCvv(cartaoDTO.getCvv());
        cartao.setSaldo(cartaoDTO.getSaldo() - produto.getPrice());
        cartaoRepo.save(cartao);

        // 🧠 Salvar pedido no Cosmos DB
        Pedido pedido = new Pedido();
        pedido.setId(idPedido); // Usa o ID fornecido
        pedido.setProductName(produto.getProductName());
        pedido.setPreco(produto.getPrice());
        pedido.setUsuarioId(usuario.getId());
        pedido.setDataTransacao(LocalDateTime.now());
        pedido.setStatus("Concluída");
        pedidoRepository.save(pedido);

        return idPedido; // Retorna o ID do pedido
    }
}
