package cloud.ecommerceisafabbia.request;

import lombok.Data;

import java.time.LocalDateTime;

@Data
public class TransacaoRequest {
    private String numero;       // Número do cartão
    private LocalDateTime dtExpiracao;  // Data de expiração do cartão
    private String cvv;          // Código de segurança do cartão
    private Double valor;        // Valor da transação
}
