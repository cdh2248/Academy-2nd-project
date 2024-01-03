package hi.web;

import hi.domain.Rest;
import hi.domain.Festival;
import hi.service.FestivalService;
import hi.service.RestService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Slf4j
@Controller
@RequiredArgsConstructor
public class RestController {

    private  final RestService restService;


    @GetMapping("/")
    public String mains(){
        return "home";
    }
    @GetMapping("go")
    public String goMain(){
        return "rests";
    }

    @GetMapping("main")
    public String getAllMatches(Model model){

        String id ="진안군";
        List<Rest> rests = restService.getAllRest(id);
        for(Rest r:rests){
            System.out.println(r);
        }

//        System.out.println(rests);

        model.addAttribute("Rest", rests);
        System.out.println(model);

        return "main";
    }





}


