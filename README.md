# File Based Record System

## Project Description

This project is a simple file-based record system built using Python and the Tkinter GUI library. It allows users to store, retrieve, update, and delete student records. The data is stored in individual text files within the `files/` directory, with each file representing a single student's record.

## Features

*   **Graphical User Interface (GUI):** Provides an intuitive interface for interacting with the record system.
*   **Data Entry:** Allows users to input student details such as ID, name, contact number, date of birth, course, address, city, degree, ID proof, and payment mode.
*   **Data Storage:** Stores student records in individual text files within the `files/` directory.
*   **Data Retrieval:** Enables users to select a student record from a list, which populates the corresponding fields in the GUI.
*   **Data Update:** Allows users to modify existing student records and save the changes to the corresponding file.
*   **Data Deletion:** Enables users to delete student records.
*   **File Management:** Automatically lists all available student record files in the GUI.
*   **Login System:** Implements a basic login system for authentication.

## Project Structure


## Modules

*   **login.py:** Implements the login system using Tkinter. It provides a username and password entry, along with login, reset, and exit buttons.
*   **software.py:** Contains the main application logic for the file-based record system. It includes functions for saving, deleting, clearing, and displaying student records.
*   **intro.py:** An empty file.

## How to Run the Application

1.  Make sure you have Python installed.
2.  Install the Tkinter library if you don't have it already.
3.  Run the `login.py` file:

    ```bash
    python login.py
    ```

4.  Log in with the username "admin" and password "admin".
5.  The main application window will appear, allowing you to manage student records.

## Dependencies

*   Tkinter: Used for creating the graphical user interface.
*   ttk (Themed Tkinter): Used for enhanced widgets in Tkinter.
*   messagebox: Used for displaying message boxes for user interaction.
*   os: Used for interacting with the operating system, such as listing files in a directory.

## Notes

*   The project stores data in plain text files, which is not suitable for sensitive information.
*   The login system is very basic and should not be used in a production environment.
*   Error handling and input validation could be improved.