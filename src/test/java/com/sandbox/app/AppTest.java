package com.sandbox.app;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class AppTest {

    @Test
    public void testHelloWorld() {
        // Act
        String message = App.getMessage();

        // Assert
        assertEquals("HelloWorld", message);
    }
}
