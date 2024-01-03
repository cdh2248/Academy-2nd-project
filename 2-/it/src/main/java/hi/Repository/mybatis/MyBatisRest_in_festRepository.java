package hi.Repository.mybatis;

import hi.Repository.Rest_in_festRepository;
import hi.domain.Rest_in_fest;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@RequiredArgsConstructor
public class MyBatisRest_in_festRepository implements Rest_in_festRepository {
    private final Rest_in_festMapper restInFestMapper;
    @Override
    public List<Rest_in_fest> getAllRest_in_fest() {
        return restInFestMapper.getAllRest_in_fest();
    }

    @Override
    public Rest_in_fest findRestInFest(String go){
        return restInFestMapper.findRestInFest(go);
    }
}
