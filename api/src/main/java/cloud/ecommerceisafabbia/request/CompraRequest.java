package cloud.ecommerceisafabbia.request;

public class CompraRequest {
    private String productName;
    private double preco;
    private UsuarioRequest usuario;
    private EnderecoRequest endereco;
    private CartaoRequest cartao;

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

    public UsuarioRequest getUsuario() {
        return usuario;
    }
    public void setUsuario(UsuarioRequest usuario) {
        this.usuario = usuario;
    }

    public EnderecoRequest getEndereco() {
        return endereco;
    }
    public void setEndereco(EnderecoRequest endereco) {
        this.endereco = endereco;
    }

    public CartaoRequest getCartao() {
        return cartao;
    }
    public void setCartao(CartaoRequest cartao) {
        this.cartao = cartao;
    }
}
