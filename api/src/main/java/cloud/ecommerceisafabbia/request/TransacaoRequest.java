package cloud.ecommerceisafabbia.request;

import java.time.LocalDateTime;

/**
 * Requisição de transação de cartão de crédito.
 */
public class TransacaoRequest {
    private String numero;            // Número do cartão
    private LocalDateTime dtExpiracao; // Data de expiração do cartão
    private String cvv;               // Código de segurança do cartão
    private Double valor;             // Valor da transação

    public TransacaoRequest() {
    }

    public TransacaoRequest(String numero, LocalDateTime dtExpiracao, String cvv, Double valor) {
        this.numero = numero;
        this.dtExpiracao = dtExpiracao;
        this.cvv = cvv;
        this.valor = valor;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public LocalDateTime getDtExpiracao() {
        return dtExpiracao;
    }

    public void setDtExpiracao(LocalDateTime dtExpiracao) {
        this.dtExpiracao = dtExpiracao;
    }

    public String getCvv() {
        return cvv;
    }

    public void setCvv(String cvv) {
        this.cvv = cvv;
    }

    public Double getValor() {
        return valor;
    }

    public void setValor(Double valor) {
        this.valor = valor;
    }
}
