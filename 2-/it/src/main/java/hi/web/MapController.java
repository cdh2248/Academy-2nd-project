package hi.web;

import hi.domain.Member;
import hi.domain.Rest;
import hi.login.LoginForm;
import hi.login.SessionConst;
import hi.service.MemberService;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Slf4j
@Controller
@RequiredArgsConstructor
public class MapController {



//    @GetMapping("/matches")
    public String getAllMatches(Model model){

//        List<Rest> rests = R.getAllMatches();
//        log.info("MatchController] \n \n matches = " + matches);
//        model.addAttribute("matches", matches);

        return "main_1";
    }


}


