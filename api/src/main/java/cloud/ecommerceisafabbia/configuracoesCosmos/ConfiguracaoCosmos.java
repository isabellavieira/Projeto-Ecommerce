package cloud.ecommerceisafabbia.configuracoesCosmos;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

import com.azure.cosmos.CosmosClientBuilder;
import com.azure.cosmos.DirectConnectionConfig;
import com.azure.spring.data.cosmos.config.AbstractCosmosConfiguration;
import com.azure.spring.data.cosmos.config.CosmosConfig;
import com.azure.spring.data.cosmos.repository.config.EnableCosmosRepositories;
import com.azure.spring.data.cosmos.repository.config.EnableReactiveCosmosRepositories;

@Configuration
@EnableConfigurationProperties(PropriedadesCosmos.class)
@EnableCosmosRepositories(basePackages = "cloud.ecommerceisafabbia.repositorioJPA.cosmos")
@EnableReactiveCosmosRepositories
@PropertySource("classpath:application.properties")
public class ConfiguracaoCosmos extends AbstractCosmosConfiguration {

    private static final Logger logger = LoggerFactory.getLogger(ConfiguracaoCosmos.class);  // Loggers SLF4J

    private PropriedadesCosmos propriedades;

    public ConfiguracaoCosmos(PropriedadesCosmos propriedades) {
        super();
        this.propriedades = propriedades;
    }

    @Bean
    public CosmosClientBuilder cosmosClientBuilder() {
        try {
            logger.info("Tentando conectar ao Cosmos DB com o endpoint: {}", propriedades.getUri());
            // Tentativa de construção do cliente Cosmos
            return new CosmosClientBuilder()
                    .endpoint(propriedades.getUri())
                    .key(propriedades.getKey())
                    .directMode(DirectConnectionConfig.getDefaultConfig());

        } catch (Exception e) {
            // Log de erro caso falhe a conexão
            logger.error("Falha na conexão com o Cosmos DB: {}", e.getMessage());
            throw new RuntimeException("Falha ao tentar conectar ao Cosmos DB", e);  // Lançar exceção para interromper a execução
        }
    }

    @Bean
    public CosmosConfig cosmosConfig() {
        return CosmosConfig.builder().build();
    }

    @Override
    protected String getDatabaseName() {
        return this.propriedades.getDatabase();
}
}