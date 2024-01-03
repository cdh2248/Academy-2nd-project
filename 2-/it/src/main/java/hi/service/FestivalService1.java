package hi.service;

import hi.Repository.FestivalRepository;
import hi.domain.Festival;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class FestivalService1 implements FestivalService {

    private final FestivalRepository festivalRepository;
    @Override
    public List<Festival> getAllFestival() {
        return festivalRepository.findAllfestival();
    }

    @Override
    public Festival findFestival(int num) {
        return festivalRepository.findFestival(num);
    }

    @Override
    public List<Festival> searchFestival(String keyword) {
        return festivalRepository.searchFestival(keyword);
    }

    @Override
    public List<Festival> getAftertodayFestival() {
        return festivalRepository.getAftertodayFestival();
    }
}
