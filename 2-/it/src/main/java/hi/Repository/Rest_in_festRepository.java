package hi.Repository;

import hi.domain.Rest_in_fest;

import java.util.List;

public interface Rest_in_festRepository {
    List<Rest_in_fest> getAllRest_in_fest();

    Rest_in_fest findRestInFest(String go);
}
