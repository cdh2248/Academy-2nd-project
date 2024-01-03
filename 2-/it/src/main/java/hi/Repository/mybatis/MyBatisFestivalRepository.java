package hi.Repository.mybatis;

import hi.Repository.FestivalRepository;
import hi.domain.Festival;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

@Repository
@RequiredArgsConstructor
public class MyBatisFestivalRepository implements FestivalRepository {

    private final FestivalMapper festivalMapper;
    @Override
    public List<Festival> findAllfestival() {
//        System.out.println("----");
//        System.out.println(festivalMapper.findAllFestival());
        return festivalMapper.findAllFestival();
    }

    @Override
    public List<Festival> searchFestival(String keyword) {
        return festivalMapper.searchFestival(keyword);
    }

    @Override
    public Festival findFestival(int num) {
        return festivalMapper.findFestival(num);
    }

    @Override
    public List<Festival> getAftertodayFestival() {
        LocalDateTime now = LocalDateTime.now();
        return festivalMapper.getAftertodayFestival();
    }
}
