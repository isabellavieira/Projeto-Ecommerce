package cloud.ecommerceisafabbia.request;

import java.time.LocalDate;

public class UsuarioRequest {
    private String nome;
    private String email;
    private String cpf;
    private String telefone;
    private LocalDate dtNascimento;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }

    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getTelefone() {
        return telefone;
    }
    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
    public LocalDate getDtNascimento() {
    return dtNascimento;
}
    public void setDtNascimento(LocalDate dtNascimento) {
    this.dtNascimento = dtNascimento;
}
}
