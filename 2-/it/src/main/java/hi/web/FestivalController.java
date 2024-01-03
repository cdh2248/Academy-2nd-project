package hi.web;
import com.fasterxml.jackson.databind.jsonFormatVisitors.JsonArrayFormatVisitor;
import com.fasterxml.jackson.databind.util.JSONPObject;
import com.google.gson.Gson;
import hi.domain.Festival;
import hi.domain.Rain;
import hi.domain.Rest_in_fest;
import hi.service.FestivalService;
import hi.service.RainService;
import hi.service.RainServiceV1;
import hi.service.Rest_in_festService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

@Controller
@RequiredArgsConstructor
public class FestivalController {

    private final FestivalService festivalService;
    private final RainService rainService;
    private final Rest_in_festService restInFestService;

    @GetMapping("festivals")
    public String festivals(Model model){
        List<Festival> festivalList = festivalService.getAllFestival();
        for(Festival r:festivalList){
            System.out.println(r);

        }

        model.addAttribute("festivals", festivalList);
        return "festivals";
    }

    @PostMapping("festivalsAll")
    public String searchAll(@RequestParam("keyword")String keyword, Model model){
        List<Festival> festivalList = festivalService.searchFestival(keyword);
        model.addAttribute("festivals", festivalList);
        return "festivals";
    }
    @PostMapping("festivalsIll")
    public String searchIll(@RequestParam("keyword")String keyword, Model model){
        List<Festival> festivalList = festivalService.getAftertodayFestival();
        model.addAttribute("festivals", festivalList.stream()
                .filter(festival -> festival.getFName().contains(keyword))
                .collect(Collectors.toList()));
        return "festivals";
    }
    @GetMapping("festival/{fNum}")
    public String festival(@PathVariable int fNum, Model model) {
        Festival festival = festivalService.findFestival(fNum);
        List<Rain> rain = rainService.getFestival(52,68);
        Rest_in_fest restInFest= restInFestService.findRestInFest(festival.getGO());
//        List<Rain> rain = rainService.getFestival(festival.getX(), festival.getY());
        String rainJson = new Gson().toJson(rain);
        String str0="\\Img\\"+festival.getGO()+"_0.png";
        String str1="\\Img\\"+festival.getGO()+"_1.png";
        String f1="\\img2\\"+festival.getFName()+"_0.jpg";
        String f2="\\img2\\"+festival.getFName()+"_1.jpg";
        String f3="\\img2\\"+festival.getFName()+"_2.jpg";
        String f4="\\img2\\"+festival.getFName()+"_3.jpg";
        String f5="\\img2\\"+festival.getFName()+"_4.jpg";
        String f6="\\img2\\"+festival.getFName()+"_5.jpg";
        String f7="\\img2\\"+festival.getFName()+"_6.jpg";
        String f8="\\img2\\"+festival.getFName()+"_7.jpg";
        String f9="\\img2\\"+festival.getFName()+"_8.jpg";



        model.addAttribute("str0", str0);
        model.addAttribute("str1", str1);
        model.addAttribute("fest_in", restInFest);

        model.addAttribute("festival", festival);
        model.addAttribute("rainJson", rainJson);

        model.addAttribute("f1", f1);
        model.addAttribute("f2", f2);
        model.addAttribute("f3", f3);
        model.addAttribute("f4", f4);
        model.addAttribute("f5", f5);
        model.addAttribute("f6", f6);
        model.addAttribute("f7", f7);
        model.addAttribute("f8", f8);
        model.addAttribute("f9", f9);

        System.out.println(rainJson);
        return "festival";
    }

//    @GetMapping("/")
    public String main(){
        return "muhanscroll";
    }


    @GetMapping("muhanscroll")
    public String muhanscroll(Model model){
        List<Festival> festivalList = festivalService.getAftertodayFestival();
        sortFestivalListByStartDate(festivalList);
        model.addAttribute("festivals", festivalList);
        return "muhanscroll";
    }

    @GetMapping("stats")
    public String stats(){
        return "stats";
    }



    public static void sortFestivalListByStartDate(List<Festival> festivalList) {
        // Comparator를 사용하여 startDate 필드를 기준으로 정렬합니다.
        Collections.sort(festivalList, new Comparator<Festival>() {
            @Override
            public int compare(Festival festival1, Festival festival2) {
                return festival1.getOpenDate().compareTo(festival2.getOpenDate());
            }
        });
    }
}
