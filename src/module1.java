// module1.java
// This file should contain a single public class named 'module1' to match the filename.

import java.util.HashSet; // Required for using HashSet
import java.util.Set;    // Required for using Set interface

public class module1 { // Changed public class name to 'module1' to match filename

    public static void main(String[] args) {
        // Instantiate DataManager to call its non-static methods
        DataManager dataManager = new DataManager();

        // Perform operations (adding data)
        dataManager.addData("data1");
        dataManager.addData("data2");
        dataManager.addData("data1"); // This is a duplicate, should be handled
        dataManager.addData("data3");
        dataManager.addData("data2"); // Another duplicate

        // Check data existence and print contents
        System.out.println("Is 'data1' present? " + dataManager.checkDataExists("data1"));
        System.out.println("Is 'data4' present? " + dataManager.checkDataExists("data4"));
        System.out.println("\nContents of the database:");
        dataManager.printDatabaseContents();
    }
}

// DataManager class to handle data operations and redundancy
class DataManager { // This can optionally be 'static class DataManager' if it doesn't need to access module1's members
    // Use generic type <String> for Set and HashSet to prevent raw use warnings
    // Declare as final because it's initialized once in the constructor
    private final Set<String> database;

    public DataManager() {
        this.database = new HashSet<>();
    }

    // Checks if the given data is already present in the database
    public boolean isUnique(String newData) {
        return !database.contains(newData);
    }

    // Validates the data to ensure it's not null or empty
    private boolean validateData(String data) {
        // Simple validation: data must not be null or empty string
        return data != null && !data.trim().isEmpty();
    }

    // Adds data to the database if it's valid and unique
    public boolean addData(String data) {
        if (!validateData(data)) {
            // Data is invalid, return false and don't add
            return false;
        }

        if (isUnique(data)) {
            database.add(data); // Add the data if it's unique
            return true; // Successfully added
        } else {
            // Data is not unique (redundant), so it's not added
            return false;
        }
    }

    // Checks if a specific data item exists in the database
    public boolean checkDataExists(String data) {
        return database.contains(data);
    }

    // Prints all unique data entries currently stored in the database
    public void printDatabaseContents() {
        if (database.isEmpty()) {
            System.out.println("Database is empty.");
        } else {
            for (String item : database) {
                System.out.println("- " + item);
            }
        }
    }
}
