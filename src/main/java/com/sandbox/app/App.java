package com.sandbox.app;

public class App {

    private static final String MESSAGE = "HelloWorld";

	public static void main(String[] args) {
        System.out.println(getMessage());
    }

    public static String getMessage() {
        return MESSAGE;
    }
}