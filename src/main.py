# Import external modules/libraries
import requests
# Import built-in modules/libraries
import json
from pprint import pprint
from datetime import datetime, date

# Constants assignment
BASE_URL = "https://api.frankfurter.app" # External API url
TODAY = date.today() # Today's date using date function from datetime
CURRENCY_LIST = { 
    "AUD": "Australian Dollar",
    "BGN": "Bulgarian Lev",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Renminbi Yuan",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "EUR": "Euro",
    "GBP": "British Pound",
    "HKD": "Hong Kong Dollar",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "INR": "Indian Rupee",
    "ISK": "Icelandic Króna",
    "JPY": "Japanese Yen",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NOK": "Norwegian Krone",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "PLN": "Polish Złoty",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "TRY": "Turkish Lira",
    "USD": "United States Dollar",
    "ZAR": "South African Rand"
} # Currency codes

# Feature 1: allow users to access currency codes
def access_currency_list():
    pprint(CURRENCY_LIST)
    
# Feature 2: real time currency converter
def real_time_currency_conversion():
    while True:  # Loop to check whether user is putting in a valid currency code to convert from
        from_currency = str(input("Please enter in the currency code you'd like to convert from: ")).upper()
        if from_currency in CURRENCY_LIST:
            break
        else:
            print("Please input correct currency from below list!")
            pprint(CURRENCY_LIST)

    while True:  # Loop to check whether user is putting in a valid currency code to convert to
        to_currency = str(input("Please enter in the currency code you'd like to convert to: ")).upper()
        if to_currency in CURRENCY_LIST:
            break
        else:
            print("Please input correct currency code from below list!")
            print(CURRENCY_LIST)

    while True:  # Loop to check whether user is putting in numbers
        try:
            amount = float(input("Please enter in the amount of money: "))
            break
        
        except ValueError:  # Error handling to make sure user is putting in numbers
            print("Please input a number!")     

    try:  # Currency converter for TODAY's date
        response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
        if response.status_code == 200:
            print(f"{amount}{from_currency} is {response.json()['rates'][to_currency]}{to_currency} on {TODAY}")
        else:  # Else/error handling when fetch is not successful
            print("Rates fetching from data source is not successful, please try our rates exchange converter later")
    except:  # Catch other errors not handled by else
        print("Rates fetching from data source is not successful, please try our rates exchange converter later")


def get_url(url):  # To return retrieve status code and return relevant information/rates
    try:
        response = requests.get(url)
        status_code = response.status_code
        content = response.text
        return status_code, content
    
    except requests.exceptions.RequestException as e:  # error handling when fetch is not successful, return nill outputs
        return None, None

# Feature 3: historical currency converter
def get_historical_rate():
    while True:  # Loop to check whether user is putting in a valid currency code to convert from
        from_currency = str(input("Please enter in the currency code you'd like to convert from: ")).upper()
        
        if from_currency in CURRENCY_LIST:
            break
        
        else:
            print("Please input correct currency from below list!")
            pprint(CURRENCY_LIST)

    while True:  # Loop to check whether user is putting in a valid currency code to convert to 
        to_currency = str(input("Please enter in the currency code you'd like to convert to: ")).upper()
        
        if to_currency in CURRENCY_LIST:
            break
        
        else:
            print("Please input correct currency code from below list!")
            print(CURRENCY_LIST)
    
    while True:   # Loop to check whether user is putting in historical date in valid format
        try:
            date_str = input("Please enter date in YYYY-MM-DD format: ")
            date_format = "%Y-%m-%d"
            chosen_date_with_time = datetime.strptime(date_str, date_format)
            chosen_date = datetime.date(chosen_date_with_time)
            break
        
        except:
            print("Please input date in YYYY-MM-DD format only!")
    
    # If user puts in a future date get conversionrate for today/realtime
    if chosen_date < TODAY:
        chosen_date = chosen_date
    else:
        print("Please only put historical date, and since you put a future date we will use realtime currency converter")
        chosen_date = TODAY
    
    try:  #Historical currency converter
        status_code, content = get_url(f"{BASE_URL}/{chosen_date}?from={from_currency}&to={to_currency}&amount=100")
        if status_code == 200:
            data = json.loads(content)
            rate = data.get("rates", {}).get(to_currency)
            print(f"100{from_currency} was {rate}{to_currency} on {chosen_date}")  
        else:  # Else/error handling when fetch is not successful
            print("Rates fetching from data source is not successful, please try our rates exchange converter later")
    
    except:  # Catch other errors not handled by else
        print("Rates fetching from data source is not successful, please try our rates exchange converter later")

# User options interface
def main():
    while True:
        try:
            user_option = int(input("Welcome to the currency converter!\n\n1. List of Currency code by Currency names\n2. Real Time Convert Converter\n3. Historical Exchange Rate\n4. Exit the function\n\nPlease select an option: "))
        
            if user_option == 1:  
                access_currency_list()  #Provide list of currency codes for users
                nested_user_option = bool(input("Type anything if you want to proceed to currency conversion, or hit Enter if you want to exit the program: "))  #Ask user if they want to access realtime currency converter
                #  If yess #Call realtime currency converter
                if nested_user_option == True:
                    real_time_currency_conversion() 
                break
    
            elif user_option == 2:  #Call realtime currency converter
                real_time_currency_conversion()
                break
    
            elif user_option == 3:  #Call histlrical currency converter
                get_historical_rate()
                break
        
            elif user_option == 4:  #Exit the app
                break
        
            else:
                print("ERROR: Please input 1,2,3 or 4 only")
    
        except ValueError:
            print("ERROR: Please input 1,2,3 or 4 only")

main()

        

