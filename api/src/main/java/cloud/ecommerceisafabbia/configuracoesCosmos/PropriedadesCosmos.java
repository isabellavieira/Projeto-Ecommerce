package cloud.ecommerceisafabbia.configuracoesCosmos;

import org.springframework.boot.context.properties.ConfigurationProperties;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ConfigurationProperties(prefix = "azure.cosmos")
public class PropriedadesCosmos {

    private String uri;

    private String key;

    private String database;

    public String getUri() { return uri; }
    public String getKey() { return key; }
    public String getDatabase() { return database; }
    
    private boolean queryMetricsEnabled;

    private boolean responseDiagnosticsEnabled;

}
