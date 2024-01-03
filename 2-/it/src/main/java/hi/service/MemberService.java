package hi.service;


import hi.domain.Member;

import java.util.Optional;


public interface MemberService {

    Member save(Member member);

    Optional<Member> findById(String id);

    Member login(String id, String password);

}
