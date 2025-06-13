package cloud.ecommerceisafabbia.objetosmodelo;

import org.springframework.data.annotation.Id;
import com.azure.spring.data.cosmos.core.mapping.Container;
import com.azure.spring.data.cosmos.core.mapping.PartitionKey;

import java.time.LocalDateTime;

@Container(containerName = "pedidos")
public class Pedido {

    @Id
    private String id; // ID único do pedido
    private String nome; // Nome do cliente
    private String cpf; // CPF do cliente
    private String email; // Email do cliente
    private String productName; // Nome do produto
    private double preco; // Valor do produto
    private String numeroCartao; // Número do cartão
    private String dtExpiracaoCartao; // Data de expiração do cartão
    private String logradouro; // Logradouro do endereço
    private String bairro; // Bairro do endereço
    private String complemento; // Complemento do endereço
    private String cidade; // Cidade do endereço
    private String estado; // Estado do endereço
    private String cep; // CEP do endereço
    private LocalDateTime dataTransacao; // Data e hora da transação
    private String status; // Status da compra (por exemplo, "Concluída")

    @PartitionKey
    private int usuarioId; // PartitionKey para otimizar as consultas por usuário

    // Getters e setters
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public String getNumeroCartao() {
        return numeroCartao;
    }

    public void setNumeroCartao(String numeroCartao) {
        this.numeroCartao = numeroCartao;
    }

    public String getDtExpiracaoCartao() {
        return dtExpiracaoCartao;
    }

    public void setDtExpiracaoCartao(String dtExpiracaoCartao) {
        this.dtExpiracaoCartao = dtExpiracaoCartao;
    }

    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getComplemento() {
        return complemento;
    }

    public void setComplemento(String complemento) {
        this.complemento = complemento;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }

    public LocalDateTime getDataTransacao() {
        return dataTransacao;
    }

    public void setDataTransacao(LocalDateTime dataTransacao) {
        this.dataTransacao = dataTransacao;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public int getUsuarioId() {
        return usuarioId;
    }

    public void setUsuarioId(int usuarioId) {
        this.usuarioId = usuarioId;
    }
}
