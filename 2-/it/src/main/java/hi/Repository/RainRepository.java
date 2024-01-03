package hi.Repository;


import hi.domain.Member;
import hi.domain.Rain;
import hi.domain.Rest;

import java.util.List;
import java.util.Optional;


public interface RainRepository {

//    Member save(Member member);

    List<Rain> findByXY(int x, int y);


}
