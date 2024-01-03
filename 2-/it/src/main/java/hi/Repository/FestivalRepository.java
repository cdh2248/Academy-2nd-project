package hi.Repository;

import hi.domain.Festival;

import java.util.List;

public interface FestivalRepository {
    List<Festival> findAllfestival();
    List<Festival> searchFestival(String keyword);
    Festival findFestival(int num);
    List<Festival> getAftertodayFestival();
}
