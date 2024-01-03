package hi.domain;


import lombok.Data;

import java.util.Date;

@Data
public class Rain {

    Date baseDate;
    Date fcstDate;
    int nx;
    int ny;
    float precipitation;//강수량
    float  probability;//강수확률
    float temp;//기온


}



