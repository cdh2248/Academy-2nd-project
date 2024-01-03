package hi.web;

import hi.domain.DAO.FestDAO;
import hi.domain.Festival;
import hi.domain.Rain;
import hi.domain.Rest;
import hi.service.RainService;
import hi.service.RestService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;
import java.util.Optional;

@Slf4j
@Controller
@RequiredArgsConstructor
public class RainController {

//    private  final RainService rainService;




//    @GetMapping("mainRain")
//    public String searchF(@ModelAttribute("festivalSearch")FestDAO festDAO, Model model){
    public String searchF(@RequestParam int x,@RequestParam int y, Model model){

//        List<Rain> playerBy = playerService.findPlayer(player.getPlayerId(), player.getPlayerName(), player.getTeamId());
        Festival festival = new Festival();
//        List<Rain> rains = rainService.getFestival(festival.getX() ,festival.getY());
//        model.addAttribute("Rain", rains);
        System.out.println(model);

        return "mainR";
    }





}


