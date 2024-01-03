package hi.Repository.mybatis;


import hi.Repository.RainRepository;
import hi.Repository.RestRepository;
import hi.domain.Member;
import hi.domain.Rain;
import hi.domain.Rest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Slf4j
@Repository
@RequiredArgsConstructor
public class MyBatisRainRepository implements RainRepository {

    private final RainMapper rainMapper;

//    @Override
    public Member save(Member member) {
        return null;
    }

    @Override
    public List<Rain> findByXY(int x, int y) {

        List<Rain> result =rainMapper.findByXY(x, y);
        System.out.println(result);
//        for (Rain rain:result){
//            System.out.println(rain);
//        }
//        log.info("바티스 실행중] memberId = " + memberId);
//        log.info("바티스 실행중] x,y= " + x + y);
        return result;
    }
}
