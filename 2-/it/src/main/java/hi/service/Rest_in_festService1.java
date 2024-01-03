package hi.service;

import hi.Repository.Rest_in_festRepository;
import hi.domain.Rest_in_fest;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class Rest_in_festService1 implements Rest_in_festService{
    private final Rest_in_festRepository restInFestRepository;
    @Override
    public List<Rest_in_fest> getAllRest_in_fest() {
        return restInFestRepository.getAllRest_in_fest();
    }
    @Override
    public Rest_in_fest findRestInFest(String go){

        return restInFestRepository.findRestInFest(go);
    }
}
