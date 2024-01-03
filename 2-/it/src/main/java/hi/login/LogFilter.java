package hi.login;

import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import lombok.extern.slf4j.Slf4j;

import java.io.IOException;
import java.util.UUID;

@Slf4j
public class LogFilter implements Filter {

    // 왜 아래 함수를 구현하는가? 왜 throws ServletException을 하는가?
    // Filter 인터페이스를 implements 했기 때문에
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        log.info("log filter init");
    }

    // 고객의 요청이 올 때 마다 해당 메서드가 호출된다.
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        log.info("log filter doFilter");

        HttpServletRequest httpRequest = (HttpServletRequest) request;
        String requestURI = httpRequest.getRequestURI();
// HTTP 요청을 구분하기 위해 요청당 임의의 uuid를 생성해 둔다.
        String uuid = UUID.randomUUID().toString();

        try {
//  log.info("메세지 {[변수1의 치환영역]} {[변수N의 치환영역}",변수1..변수N);
//  logging.level.root=OFF 전체로그 삭제
            log.info("REQUEST [{}][{}]", uuid, requestURI);
            chain.doFilter(request, response);
        } catch (Exception e) {
            throw e;
        } finally {
            log.info("RESPONSE [{}][{}]", uuid, requestURI);
        }

    }

    @Override
    public void destroy() {
        log.info("log filter destroy");
    }
}
