package hi.service;

import hi.domain.Festival;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface FestivalService {
    List<Festival> getAllFestival();
    List<Festival> searchFestival(String keyword);

    Festival findFestival(int num);

    List<Festival> getAftertodayFestival();
}



