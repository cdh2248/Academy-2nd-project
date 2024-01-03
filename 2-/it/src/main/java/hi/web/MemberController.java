package hi.web;

import hi.domain.Member;
import hi.service.MemberService;
import hi.login.LoginForm;
import hi.login.SessionConst;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Slf4j
@Controller
@RequiredArgsConstructor
public class MemberController {

    private final MemberService memberService;

//    @GetMapping("/welcome")
    public String hihi()
    {
        return "/welcome.html";
    }

    @GetMapping("/login")
    public String loginForm(@ModelAttribute("loginForm") LoginForm form){
        log.info("LoginController login get mapping");
        return "login/loginForm";

    }


    @PostMapping("/login")
    public String loginV3(@Valid @ModelAttribute LoginForm form, BindingResult bindingResult, HttpServletRequest request) {
//        int result = 10 / 0; // 강제 예외 발생
        log.info("LoginController] form = " + form);
        if (bindingResult.hasErrors()) {
//            return "login/loginForm";
        }
        log.info("1");
        Member loginMember = memberService.login(form.getLoginId(), form.getPassword());
        log.info("LoginController] loginMember = " + loginMember);

        if (loginMember == null) {
            bindingResult.reject("loginFail", "아이디 또는 비밀번호가 맞지 않습니다.");
            return "login/loginForm";
        }
        log.info("2");
        HttpSession session = request.getSession();
        //세션에 로그인 회원 정보 보관
        session.setAttribute(SessionConst.LOGIN_MEMBER, loginMember);

        return "redirect:/";

    }



    @PostMapping("/logout")
    public String logoutV3(HttpServletRequest request) {

        HttpSession session = request.getSession(false);
        if (session != null) {
            // 가져온 세션을 무효화한다.
            session.invalidate();
        }
        return "redirect:/";
    }

    private void expireCookie(HttpServletResponse response, String cookieName) {
        Cookie cookie = new Cookie(cookieName, null);
        // 서버에서 해당 쿠키의 종료 날짜를 0으로 지정 => 쿠키 종료를 의미함
        cookie.setMaxAge(0);
        response.addCookie(cookie);
    }
}


