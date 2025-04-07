package cloud.ecommerceisafabbia.dto;

public class CompraUpdateDTO {
    private String status;
    private String detalhesEntrega;
    // Adicione outros campos que possam ser atualizados, como data, forma de pagamento, etc.

    // Getters e setters
    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }
    public String getDetalhesEntrega() {
        return detalhesEntrega;
    }
    public void setDetalhesEntrega(String detalhesEntrega) {
        this.detalhesEntrega = detalhesEntrega;
    }
}