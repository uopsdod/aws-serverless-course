package example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

import java.util.Map;
import java.util.UUID;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

//0. Import CRaC: Resource/Core
import org.crac.Resource;
import org.crac.Core;

//1. Implement the Resource interface
public class FunctionHandler implements RequestHandler<Map<String, Object>, String>, Resource {

    private final Logger logger = LoggerFactory.getLogger(FunctionHandler.class);
    private static boolean isDbConnectionBuilt = false;
    private static String executionEnvironmentUUID;

    // static initialization
    static {
        System.out.println("static initialization starts");
        createDatabaseConnection();
        System.out.println("static initialization ends");
    }

    public FunctionHandler() {
        // 2. Register the FunctionHandler in the global context
        Core.getGlobalContext().register(this);
    }
    
    public String handleRequest(Map<String, Object> input, Context context) {
        System.out.println("handler starts");
        System.out.println("executionEnvironmentUUID: " + executionEnvironmentUUID);
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

    //3. Implement the before checkpoint hook
    @Override
    public void beforeCheckpoint(org.crac.Context<? extends Resource> context) {
        logger.info("before-checkpoint hook: ");
        logger.info("before-checkpoint hook: Loading extra local files ... ");
        logger.info("before-checkpoint hook: Initializing more classes ... ");
    }

    //4. Implement the after restore hook
    @Override
    public void afterRestore(org.crac.Context<? extends Resource> context) {
        logger.info("after-restore hook:");
        logger.info("after-restore hook: Refreshing Access Key if necessary ... ");
        executionEnvironmentUUID = UUID.randomUUID().toString();
        logger.info("after-restore hook: Generating Unique Key: " + executionEnvironmentUUID);
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
