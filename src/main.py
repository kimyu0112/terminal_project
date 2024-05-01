import requests
import json
from pprint import pprint
from datetime import datetime, date

BASE_URL = "https://api.frankfurter.app"
TODAY = date.today()
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
} 

def real_time_currency_conversion():
    while True:
        from_currency = str(input("Please enter in the currency code you'd like to convert from: ")).upper()
        
        if from_currency in CURRENCY_LIST:
            break
        
        else:
            print("Please input correct currency from below list!")
            pprint(CURRENCY_LIST)

    while True:      
        to_currency = str(input("Please enter in the currency code you'd like to convert to: ")).upper()
        
        if to_currency in CURRENCY_LIST:
            break
        
        else:
            print("Please input correct currency code from below list!")
            print(CURRENCY_LIST)

    while True:
        try:
            amount = float(input("Please enter in the amount of money: "))
            break
        
        except ValueError:
            print("Please input a number!")     
    
    response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

    if response.status_code == 200:
        print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency} on {TODAY}")
    else:
        print("Rates fetching from data source is not successful, please try our rates exchange converter later")
        
def get_url(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        content = response.text
        return status_code, content
    except requests.exceptions.RequestException as e:
        print(f"Error making GET request: {e}")
        return None, None

def get_historical_rate():
    while True:
        from_currency = str(input("Please enter in the currency code you'd like to convert from: ")).upper()
        
        if from_currency in CURRENCY_LIST:
            break
        
        else:
            print("Please input correct currency from below list!")
            pprint(CURRENCY_LIST)

    while True:      
        to_currency = str(input("Please enter in the currency code you'd like to convert to: ")).upper()
        
        if to_currency in CURRENCY_LIST:
            break
        
        else:
            print("Please input correct currency code from below list!")
            print(CURRENCY_LIST)
    
    while True:   
        try:
            date_str = input("Please enter date in YYYY-MM-DD format: ")
            date_format = "%Y-%m-%d"
            chosen_date_with_time = datetime.strptime(date_str, date_format)
            chosen_date = datetime.date(chosen_date_with_time)
            break
        except:
            print("Please input date in YYYY-MM-DD format only!")
    
    if chosen_date < TODAY:
        chosen_date = chosen_date
    else:
        print("Please only put historical date, and since you put a future date we will use realtime currency converter")
        chosen_date = TODAY
        
    status_code, content = get_url(f"{BASE_URL}/{chosen_date}?from={from_currency}&to={to_currency}&amount=100")
    
    if status_code == 200:
        data = json.loads(content)
        rate = data.get("rates", {}).get(to_currency)
        print(f"100{from_currency} was {rate}{to_currency} on {chosen_date}")
    else:
        return None

def main():
    while True:
        try:
            user_option = int(input("Welcome to the currency converter!\n\n1. List of Currency code by Currency names\n2. Real Time Convert Converter\n3. Historical Exchange Rate\n4. Exit the function\n\nPlease select an option: "))
        
            if user_option == 1:
                pprint(CURRENCY_LIST)
                nested_user_option = bool(input("Type anything if you want to proceed to currency conversion, or hit Enter if you want to exit the program: "))
                if nested_user_option == True:
                    real_time_currency_conversion()
                break
    
            elif user_option == 2:
                real_time_currency_conversion()
                break
    
            elif user_option == 3:
                get_historical_rate()
                break
        
            elif user_option == 4:
                break
        
            else:
                print("ERROR: Please input 1,2,3 or 4 only")
    
        except ValueError:
            print("ERROR: Please input 1,2,3 or 4 only")

main()
        
        

