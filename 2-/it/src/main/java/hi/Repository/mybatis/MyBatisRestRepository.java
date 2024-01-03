package hi.Repository.mybatis;


import hi.Repository.MemberRepository;
import hi.Repository.RestRepository;
import hi.domain.Member;
import hi.domain.Rest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Slf4j
@Repository
@RequiredArgsConstructor
public class MyBatisRestRepository implements RestRepository {

    private final RestMapper restMapper;

//    @Override
    public Member save(Member member) {
        return null;
    }

    @Override
    public List<Rest> findByroadName(String memberId) {
//        log.info("바티스 실행중] memberId = " + memberId);

        return restMapper.findByroadName(memberId);
    }
}
