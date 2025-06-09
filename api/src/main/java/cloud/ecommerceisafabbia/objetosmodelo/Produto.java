package cloud.ecommerceisafabbia.objetosmodelo;

import java.util.List;

import org.springframework.data.annotation.Id;

import com.azure.spring.data.cosmos.core.mapping.Container;
import com.azure.spring.data.cosmos.core.mapping.PartitionKey;

import lombok.Data;

@Data
@Container(containerName = "products")
public class Produto {

    @Id
    private String id;//teste

    @PartitionKey //por causa da Azure
    private String productCategory;

    private String productName;

    private double price;

   // private List<String> imageUrl;

    private String productDescription;
}
