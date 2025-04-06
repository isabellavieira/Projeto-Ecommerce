package cloud.ecommerceisafabbia.objetosmodelo;

import java.util.List;

import org.springframework.data.annotation.Id;

import com.azure.spring.data.cosmos.core.mapping.Container;
import com.azure.spring.data.cosmos.core.mapping.PartitionKey;

import lombok.Data;

@Data
@Container(containerName = "pedidos")
public class Pedido {

    @Id
    private String id;

    @PartitionKey
    private String usuarioId;

    private List<String> produtoIds; // Lista de IDs dos produtos no pedido
    private String enderecoId;
    private double totalPrice; // Valor total do pedido
    private String status; // Status do pedido (ex: "Pendente", "Enviado", etc.)

    public Pedido(String usuarioId, List<String> produtoIds, String enderecoId, double totalPrice, String status) {
        this.usuarioId = usuarioId;
        this.produtoIds = produtoIds;
        this.enderecoId = enderecoId;
        this.totalPrice = totalPrice;
        this.status = status;
    }
}
