package hi.service;

import hi.Repository.MemberRepository;
import hi.Repository.RestRepository;
import hi.domain.Member;
import hi.domain.Rest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@Slf4j
@RequiredArgsConstructor
public class RestServiceV1 implements RestService {

    private final RestRepository restRepository;

//    @Override
    public Member save(Member member) {
        return restRepository.save(member);
    }


    @Override
    public List<Rest> getAllRest(String memberId) {

//        System.out.println("서비스에서 테스트"+restRepository.findByroadName(memberId));

        return restRepository.findByroadName(memberId);
    }

//    @Override
    public Member login(String id, String password){

//        log.info("MemberServiceV1] id = " + id+  " "+password+"   아이디 및 비번체크");
////        Optional<Member> member = memberRepository.findById(id);
//        log.info("MemberServiceV1");
//        log.info("MemberServiceV1] member = " + member);
//
//        if(member.get().getMemberPw().equals(password)){
//            return member.get();
//        }

        return null;
    }

}
