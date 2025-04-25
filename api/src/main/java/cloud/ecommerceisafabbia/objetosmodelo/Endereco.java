package cloud.ecommerceisafabbia.objetosmodelo;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.Data;

@Data
@Entity(name = "endereco")
public class Endereco {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull(message = "O logradouro é obrigatório")
    @Column(nullable = false, length = 255)
    private String logradouro;

    @Column(length = 255)
    private String complemento;

    @NotNull(message = "O bairro é obrigatório")
    @Column(nullable = false, length = 100)
    private String bairro;

    @NotNull(message = "A cidade é obrigatória")
    @Column(nullable = false, length = 100)
    private String cidade;

    @NotNull(message = "O estado é obrigatório")
    @Size(min = 2, max = 50, message = "O estado deve ter entre 2 e 50 caracteres")
    @Column(nullable = false, length = 50)
    private String estado;

    @NotNull(message = "O CEP é obrigatório")
    @Pattern(regexp = "\\d{5}-\\d{3}", message = "CEP deve estar no formato 00000-000")
    @Column(nullable = false, length = 9)
    private String cep;

    @NotNull(message = "O usuário associado é obrigatório")
    @ManyToOne
    @JoinColumn(name = "id_usuario", referencedColumnName = "id", nullable = false)
    private Usuario usuario;
}