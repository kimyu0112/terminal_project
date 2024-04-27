import requests
from pprint import pprint

available_currency_list = {
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

def currency_conversion():
    while True:
        from_currency = str(input("Please enter in the currency code you'd like to convert from: ")).upper()
        if from_currency in available_currency_list:
            break
        else:
            print("Please input correct currency from below list!")
            pprint(available_currency_list)

    while True:      
        to_currency = str(input("Please enter in the currency code you'd like to convert to: ")).upper()
        if to_currency in available_currency_list:
            break
        else:
            print("Please input correct currency code from below list!")
            print(available_currency_list)

    while True:
        try:
            amount = float(input("Please enter in the amount of money: "))
            break 
        except ValueError:
            print("Please input a number!")     
    
    response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

    if response.status_code == 200:
        print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
    else:
        print("Rates fetching from data source is not successful, please try our rates exchange converter later")

while True:
    try:
        user_option = int(input("1. List of Currency code by Currency names\n2. Real Time Convert Converter\n3. Historical Exchange Rate\nPlease select an option: "))
        
        if user_option == 1:
            pprint(available_currency_list)
            nested_user_option = bool(input("Type anything if you want to proceed to currency conversion, or hit Enter if you want to exit the program: "))
            if nested_user_option == True:
                currency_conversion()
            break
    
        elif user_option == 2:
            currency_conversion()
            break
    
        elif user_option == 3:
            pass
            break
        
        else:
            print("Please only select 1, 2 or 3")
            
    except ValueError:
        print("Please input only 1, 2 or 3, not text!")