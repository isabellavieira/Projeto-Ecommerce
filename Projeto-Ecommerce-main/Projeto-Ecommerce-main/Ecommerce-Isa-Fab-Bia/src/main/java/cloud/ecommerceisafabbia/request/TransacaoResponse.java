package cloud.ecommerceisafabbia.request;

import lombok.Data;

import java.time.LocalDateTime;
import java.util.UUID;

@Data
public class TransacaoResponse {
    private String status;               // Status da transação (autorizado, não autorizado)
    private UUID codigoAutorizacao;      // Código único gerado para a autorização
    private LocalDateTime dtTransacao;   // Data e hora da transação
    private String message;              // Mensagem relacionada à transação (erro, sucesso)
}
