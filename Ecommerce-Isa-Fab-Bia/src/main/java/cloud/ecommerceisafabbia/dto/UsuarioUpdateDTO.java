package cloud.ecommerceisafabbia.dto;

public class UsuarioUpdateDTO {
    private String nome;
    private String email;
    // Adicione outros campos conforme necessário

    // Getters e setters
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
}