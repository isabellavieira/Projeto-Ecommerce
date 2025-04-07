package cloud.ecommerceisafabbia.servicos;

import cloud.ecommerceisafabbia.dto.CompraUpdateDTO;
import cloud.ecommerceisafabbia.objetosmodelo.Compra;
import cloud.ecommerceisafabbia.repositorioJPA.CompraRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class CompraService {

    @Autowired
    private CompraRepository compraRepository;

    public Optional<Compra> atualizarCompra(Integer id, CompraUpdateDTO dto) {
        Optional<Compra> optionalCompra = compraRepository.findById(id);
        if(optionalCompra.isPresent()){
            Compra compraExistente = optionalCompra.get();
            if(dto.getStatus() != null) {
                compraExistente.setStatus(dto.getStatus());
            }
            if(dto.getDetalhesEntrega() != null) {
                compraExistente.setDetalhesEntrega(dto.getDetalhesEntrega());
            }
            // Atualize outros campos se necessário

            compraRepository.save(compraExistente);
            return Optional.of(compraExistente);
        }
        return Optional.empty();
    }
}
