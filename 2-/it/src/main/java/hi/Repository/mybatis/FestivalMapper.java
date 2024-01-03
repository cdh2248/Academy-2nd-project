package hi.Repository.mybatis;

import hi.domain.Festival;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface FestivalMapper {
    List<Festival> findAllFestival();
    List<Festival> searchFestival(String keyword);
    Festival findFestival(int num);
    List<Festival> getAftertodayFestival();
}
