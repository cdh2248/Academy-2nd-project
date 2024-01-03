package hi.Repository;


import hi.domain.Member;
import hi.domain.Rest;

import java.util.List;
import java.util.Optional;


public interface RestRepository {

    Member save(Member member);

    List<Rest> findByroadName(String memberId);


}
