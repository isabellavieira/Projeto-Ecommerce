package cloud.ecommerceisafabbia.objetosmodelo;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.Data;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@Data
@Entity(name = "usuario")
public class Usuario {

    // Construtor padrão inicializando as listas
    public Usuario() {
        this.cartoes = new ArrayList<>();
        this.enderecos = new ArrayList<>();
    }

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull(message = "O nome é obrigatório")
    @Column(nullable = false, length = 100) // Limitar tamanho do nome
    private String nome;

    @NotNull(message = "O email é obrigatório")
    @Email(message = "Formato de email inválido")
    @Column(nullable = false, unique = true, length = 150) // Email único e com limite de tamanho
    private String email;

    @NotNull(message = "A data de nascimento é obrigatória")
    @Past(message = "A data de nascimento deve estar no passado")
    @Column(nullable = false)
    private LocalDate dtNascimento; // Alterado de LocalDateTime para LocalDate

    @NotNull(message = "O CPF é obrigatório")
    @Pattern(regexp = "\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}", message = "CPF deve estar no formato 000.000.000-00")
    @Column(nullable = false, unique = true, length = 14) // Formato do CPF com tamanho fixo
    private String cpf;

    @NotNull(message = "O telefone é obrigatório")
    @Pattern(regexp = "\\(\\d{2}\\) \\d{4,5}-\\d{4}", message = "Telefone deve estar no formato (99) 99999-9999")
    @Column(nullable = false, length = 15) // Limite de tamanho do telefone
    private String telefone;

    @OneToMany(mappedBy = "usuario", cascade = {CascadeType.PERSIST, CascadeType.MERGE}, orphanRemoval = false, fetch = FetchType.LAZY)
    private List<Cartao> cartoes;

    @OneToMany(mappedBy = "usuario", cascade = {CascadeType.PERSIST, CascadeType.MERGE}, orphanRemoval = false, fetch = FetchType.LAZY)
    private List<Endereco> enderecos;

    public List<Endereco> getEnderecos() {
        return enderecos;
    }

}