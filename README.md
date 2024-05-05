# Currency Converter App – T1A3

## Description

Currency Converter App is a terminal-based application that allows users to convert between different currencies based on current and historical exchange rates. This application is developed using Python programming language.

### Features

- **Realtime currency converter**
  Users can enter the amount, the currencies they want to conver from and convert to. The app will calculate result using real-time exchange rates fetched from external API Frankfurter.

- **Historical currency converter**
  This feature allows users to choose a specific historical date for currency conversion.

- **List of currency codes**
  List of currency codes is provided to assist users who are unsure of the appropriate codes to use.

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

This program requires internet connection to run.

Windows users need to install Windows Subsystem for Linux (WSL) first(https://learn.microsoft.com/en-us/windows/wsl/install).

1. Open a terminal.

2. Clone the GitHub repository.
    ```sh
    git clone https://github.com/kimyu0112/terminal_project.git
    ```

3. Navigate to the `/src` folder.
    ```sh
    cd ./terminal_project
    cd ./src

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

- **Historical currency converter**: 
  same as realtime currency converter, with a few differences:
  1. The app will prompt user to enter a historical date. The entered date will be converted into proper date format using functions from the built-in Python library called datetime.
  2. More error handling will be implemented using if/else statements. If the user mistakenly enters a future date, the app will detect it and return result based on the current date.

- **List of currency codes**: 
  a simple function is set up such that when it is called a list of currency codes is printed. The Pprint built-in python module is used in the app to provide users with clearer structure of the list, making it easier to check currency codes.

## Code Style Guide

This project follows the [PEP 8](https://pep8.org/) style guide for Python code.

## Implementation Plan

I utilized Trello platform to track implementation of my project. 

![Trello Project Tasks](/docs/Trello%20Tasks%20Overview.png)

I have also broken it down into a list below:

#### Feature 1 display currency codes list - deadline 24/04/24
- Complete coding (simple print function)
- Write inline and block comments to explain code
- Test the function to ensure function could work without any issues
- Error handling if there are any
- Check whether there are any typos and whether they follow PEP8 style guide (finalise coding)

![Feature 1 Completed](/docs/Feature%201%20Completed.png)

#### Priority feature 2 realtime currency converter - deadline 01/05/24 
- Complete coding of function
  - researched ways to ensure user input is valid (While True loop)
  - ressearched how to fetch data from external API
- Write inline and block comments to explain code
- Test the function to ensure function could work without any issues
- Error handling for:
  - whether fetching of data from external API is successful
  - other types of error thrown by users not anticipated
- Check whether there are any typos and whether they follow PEP8 style guide (finalise coding)
  
#### Feature 3 historical currency converter - deadline 02/05/24
- Complete coding of function
  - researched ways to ensure user input is valid (done in feature 2)
  - ressearched how to fetch data from external API (done in feature 2)
- Write inline and block comments to explain code
- Test the function to ensure function could work without any issues
  - additional if/else statement to make sure app will not throw an error when user puts in a future date, and will return exchange rate based on current date
- Error handling for:
  - whether fetching of data from external API is successful
  - other types of error thrown by users not anticipated
- Check whether there are any typos and whether they follow PEP8 style guide (finalise coding)

#### User options - deadline 03/05/24
- Complete coding for user options 1, 2, 3 or 4
  - 1, 2, and 3 are features/functions of the app, while 4 allows users to exit the function
- Write inline and block comments to explain code
- Test the function to ensure function could work without any issues
- Error handling using While True loop to ensure user enters valid option
- Check whether there are any typos and whether they follow PEP8 style guide (finalise coding)

#### User manual - deadline 04/05/24
- Bash script to check python installation
- Bash script to create venv environment
- Bash script to run the main app
  - Clone git repository
  - Activate venv environment
- System specific instructions on how to run the app (Windows users have to install WSL)
- Combine them into a user manual

![User Manual](/docs/User%20Manual%20Completed.png)

#### Assignment submission - deadline 05/05/24
- Finish up README.md as per assignment requirement
- Check whether folder organization is as per assignment requirement
- Add proper referencing and acknowledgement
- Push the codes to Git
- Zip the files and submit to Canvas before 23:55

![Submission Task](/docs/Assignment%20Submission%20Due.png)

## REFERENCES

Van Rossum, G., Warsaw, B. and Coghlan, A. (2001) PEP 8 – Style Guide for Python Code. Available at: https://peps.python.org/pep-0008/ (Accessed: 25 April 2024).


Loewen, C., (2024) What is Windows Subsystem for Linux, learn.microsoft.com. Available at: https://learn.microsoft.com/en-us/windows/wsl/about.


Sharma, H 2023, hemangsharma/94692_Data_Science_Practice_Assignment_2, GitHub, viewed 5 May 2024, <https://github.com/hemangsharma/94692_Data_Science_Practice_Assignment_2/tree/main>.


jww 2018, Detect python version in shell script, Stack Overflow, viewed 5 May 2024, <https://stackoverflow.com/questions/6141581/detect-python-version-in-shell-script>.