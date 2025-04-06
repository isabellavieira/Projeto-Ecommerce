package cloud.ecommerceisafabbia;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication
@EnableJpaRepositories("cloud.ecommerceisafabbia.repositorioJPA") // Certifique-se de que o pacote está correto
public class EcommerceIsaFabBiaApplication {
    public static void main(String[] args) {
        SpringApplication.run(EcommerceIsaFabBiaApplication.class, args);
    }
}
