package hi.Repository.mybatis;

import hi.domain.Member;
import org.apache.ibatis.annotations.Mapper;

import java.util.Optional;

// @Mapper: MyBatis에서 인터페이스를 마이바티스 매퍼로 인식
// 인터페이스의 구현 메소드를 호출하면 매퍼 xml의 해당 SQL을 실행하고 결과를 돌려준다.
// 해당 XML의 mapper 태그의 namespace 속성에 Mapper 인터페이스를 지정해야한다.
// (구현체는 자동으로 생성된다.)
// xml의 위치는 src/main/resources 의 하위 폴더로 만든다.
@Mapper
public interface MemberMapper {

    void save(Member member);

    Optional<Member> findById(String id);

}
