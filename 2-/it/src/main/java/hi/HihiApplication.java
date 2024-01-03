package hi;

import hi.config.MyBatisConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;


@Import(MyBatisConfig.class)
@SpringBootApplication(scanBasePackages = "hi.web")
public class HihiApplication {

	public static void main(String[] args) {
		SpringApplication.run(HihiApplication.class, args);
	}

}











