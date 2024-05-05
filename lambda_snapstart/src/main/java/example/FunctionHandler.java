package example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class FunctionHandler implements RequestHandler<Map<String, Object>, String> {

    private final Logger logger = LoggerFactory.getLogger(FunctionHandler.class);
    private static boolean isDbConnectionBuilt = false;

    // static initialization
    static {
        System.out.println("static initialization starts");
        createDatabaseConnection();
        System.out.println("static initialization ends");
    }
    
    public FunctionHandler() {
    }

    public String handleRequest(Map<String, Object> input, Context context) {
        System.out.println("handler starts");
        try {
            createDatabaseConnection();
            Thread.sleep(3000); // processing main logic 1
            String name = (String) input.get("name");
            return "Hello, " + name + "!";
        } catch (Exception e) {
            context.getLogger().log("Error parsing input: " + e.getMessage());
            return "Error parsing input";
        } finally {
            System.out.println("handler ends");
        }
    }
    
    private static void createDatabaseConnection() {
        if (!isDbConnectionBuilt) {
            System.out.println("DB connection is being built");
            try {
                Thread.sleep(5000); // getting db connection
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            isDbConnectionBuilt = true;
            System.out.println("DB connection built");
        } else {
            System.out.println("DB connection already built");
        }
    }


}
