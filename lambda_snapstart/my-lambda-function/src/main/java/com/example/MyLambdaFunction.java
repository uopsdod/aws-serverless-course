package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

import java.util.Map;

import org.crac.Resource;
import org.crac.Core;

public class MyLambdaFunction implements RequestHandler<Map<String, Object>, String>, Resource {

    private static boolean isDbConnectionBuilt = false;

    public MyLambdaFunction() {
        Core.getGlobalContext().register(this);
    }

    @Override
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

    @Override
    public void beforeCheckpoint(org.crac.Context<? extends Resource> context) throws Exception {
        System.out.println("Before Checkpoint");
    }

    @Override
    public void afterRestore(org.crac.Context<? extends Resource> context) throws Exception {
        System.out.println("After Restore");
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

    // static initialization
    static {
        System.out.println("static initialization starts");
        createDatabaseConnection();
        System.out.println("static initialization ends");
    }
}
