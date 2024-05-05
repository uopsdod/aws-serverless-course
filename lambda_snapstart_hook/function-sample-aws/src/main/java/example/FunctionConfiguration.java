package example;

import java.util.function.Function;

import com.amazonaws.services.lambda.runtime.RequestHandler;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class FunctionConfiguration {

	/*
	 * You need this main method (empty) or explicit <start-class>example.FunctionConfiguration</start-class>
	 * in the POM to ensure boot plug-in makes the correct entry
	 */
	public static void main(String[] args) {
	}

	@Bean
	public RequestHandler requestHandler() {
		return new FunctionHandler();
	}


}
