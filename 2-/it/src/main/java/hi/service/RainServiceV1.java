package hi.service;

import hi.Repository.RainRepository;
import hi.Repository.RestRepository;
import hi.domain.Member;
import hi.domain.Rain;
import hi.domain.Rest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@Slf4j
@RequiredArgsConstructor
public class RainServiceV1 implements RainService {

    private final RainRepository rainRepository;

//    @Override
//    public Member save(Member member) {
//        return rainRepository.save(member);
//    }


    @Override
    public List<Rain> getFestival(int x , int y) {


//        System.out.println("서비스에서 테스트"+restRepository.findByroadName(memberId));

        return rainRepository.findByXY(x, y);

    }



}
