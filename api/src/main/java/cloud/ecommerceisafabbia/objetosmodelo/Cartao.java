package cloud.ecommerceisafabbia.objetosmodelo;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.Data;

import java.time.LocalDate;

@Data
@Entity(name = "cartao")
public class Cartao {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull(message = "O número do cartão é obrigatório")
    @Pattern(regexp = "\\d{16}", message = "O número do cartão deve conter exatamente 16 dígitos")
    @Column(nullable = false, unique = true, length = 16)
    private String numero;

    @NotNull(message = "A data de expiração é obrigatória")
    @Future(message = "A data de expiração deve ser no futuro")
    @Column(nullable = false)
    private LocalDate dtExpiracao;

    @NotNull(message = "O código de segurança (CVV) é obrigatório")
    @Pattern(regexp = "\\d{3}", message = "O CVV deve conter exatamente 3 dígitos")
    @Column(nullable = false, length = 3)
    private String cvv;

    @NotNull(message = "O saldo é obrigatório")
    @DecimalMin(value = "0.0", inclusive = true, message = "O saldo não pode ser negativo")
    @Column(nullable = false)
    private Double saldo;

    @NotNull(message = "O usuário associado ao cartão é obrigatório")
    @ManyToOne
    @JoinColumn(name = "id_usuario", referencedColumnName = "id", nullable = false)
    private Usuario usuario;  // Relacionamento com a entidade Usuario
}