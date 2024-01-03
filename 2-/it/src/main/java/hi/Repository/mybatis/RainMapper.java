package hi.Repository.mybatis;

import hi.domain.Rain;
import hi.domain.Rest;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Optional;

@Mapper
public interface RainMapper {

//    void save(Member member);

    List<Rain> findByXY(
            @Param("x") int x,
            @Param("y") int y
    );

}
