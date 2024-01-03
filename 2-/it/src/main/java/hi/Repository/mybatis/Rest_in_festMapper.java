package hi.Repository.mybatis;

import hi.domain.Rest_in_fest;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface Rest_in_festMapper {
    List<Rest_in_fest> getAllRest_in_fest();
    Rest_in_fest findRestInFest(String go);
}
