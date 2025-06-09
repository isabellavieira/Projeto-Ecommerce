package cloud.ecommerceisafabbia.configuracoesCosmos;

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
@EnableCosmosRepositories(basePackages = "cloud.ecommerceisafabbia.repositorioJPA")
@EnableReactiveCosmosRepositories
@PropertySource("classpath:application.properties")
public class ConfiguracaoCosmos extends AbstractCosmosConfiguration {

    private PropriedadesCosmos propriedades;

    public ConfiguracaoCosmos(PropriedadesCosmos propriedades) {
        super();
        this.propriedades = propriedades;
    }

    @Bean
    public CosmosClientBuilder cosmosClientBuilder() {
        return new CosmosClientBuilder()
                .endpoint(propriedades.getUri())
                .key(propriedades.getKey())
                .directMode(DirectConnectionConfig.getDefaultConfig());
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
