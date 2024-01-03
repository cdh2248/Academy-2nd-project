package hi.Repository;


import hi.domain.Member;

import java.util.Optional;


public interface MemberRepository {

    Member save(Member member);

    Optional<Member> findById(String memberId);


}
