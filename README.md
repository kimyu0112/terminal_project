# Currency Converter App – T1A3

## Description

Currency Converter App is a terminal-based application that allows users to convert between different currencies based on current and historical exchange rates. This application is developed using Python programming language.

### Features

- **Realtime currency converter**: Users can enter the amount, the currencies they want to conver from and convert to. The app will calculate result using real-time exchange rates fetched from external API Frankfurter.

- **Historical currency converter**: This feature allows users to choose a specific historical date for currency conversion.

- **List of currency codes**: List of currency codes is provided to assist users who are unsure of the appropriate codes to use.

Link to the GitHub repository can be found [here](https://github.com/kimyu0112/terminal_project).

### Prerequisites
- Python 3.10.10
- Pip
- Bash shell
- Git

### Python packages (dependencies):
- Pprint
- Requests
- Datetime
- JSON

Installation of the above dependencies, if needed, are included in `run.sh` script.

## How to Run the Program

Windows users need to install Windows Subsystem for Linux (WSL) first(https://learn.microsoft.com/en-us/windows/wsl/install).

1. Open a terminal.

2. Clone the GitHub repository.
    ```sh
    git clone https://github.com/kimyu0112/terminal_project.git
    ```
3. Navigate to the `/src` folder.

4. Turn run.sh script into executable by using the following command:
    ```sh
    chmod +x run.sh
    ```
5. Run the run.sh script.
    ```sh
    ./run.sh
    ```

## Code Logic

- **Realtime currency converter**: 
  1. The function for the realtime currency converter includes a While True loop to ensure that users enter valid currency codes from the CURRENCY_LIST. If the user enters an invalid code, the app will display a list of valid codes and prompt the user to enter a valid code. The loop will continue until the user enters a valid code. This same logic is used for all user inputs in the app.
  2. After user input is validated, the system will fetch the real-time currency rate from an external API. If the fetching process is successful, which will be validated by an "if" function checking if the response code is 200, the system will print out the result of the currency conversion. Error handling is done through an "if/else" statement that checks if the data is fetched successfully, as well as through the use of "try/except" blocks to handle other exceptions.

- **Historical currency converter**: same as realtime currency converter, with a few differences:
  1. The app will prompt user to enter a historical date. The entered date will be converted into proper date format using functions from the built-in Python library called datetime.
  2. More error handling will be implemented using if/else statements. If the user mistakenly enters a future date, the app will detect it and return result based on the current date.

- **List of currency codes**: a simple function is set up such that when it is called a list of currency codes is printed. The Pprint built-in python module is used in the app to provide users with clearer structure of the list, making it easier to check currency codes.

## Code Style Guide

This project follows the [PEP 8](https://pep8.org/) style guide for Python code.

## Implementation Plan
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 

> Your checklists for each feature should have at least 5 items.