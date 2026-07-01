currency = {
    "usd": 1,          # United States Dollar (Base Value)
    "eur": 0.86,       # Euro
    "gbp": 0.74,       # British Pound
    "inr": 86.0,       # Indian Rupee
    "jpy": 146.0,      # Japanese Yen
    "cny": 7.17,       # Chinese Yuan
    "rub": 78.0,       # Russian Ruble
    "cad": 1.37,       # Canadian Dollar
    "aud": 1.53,       # Australian Dollar
    "nzd": 1.67,       # New Zealand Dollar
    "chf": 0.80,       # Swiss Franc
    "sgd": 1.28,       # Singapore Dollar
    "aed": 3.67,       # UAE Dirham
    "sar": 3.75,       # Saudi Riyal
    "krw": 1388.0,     # South Korean Won
    "hkd": 7.85,       # Hong Kong Dollar
    "sek": 9.52,       # Swedish Krona
    "nok": 10.05,      # Norwegian Krone
    "dkk": 6.43,       # Danish Krone
    "zar": 17.8,       # South African Rand
    "brl": 5.4,        # Brazilian Real
    "mxn": 18.6,       # Mexican Peso
    "try": 40.2,       # Turkish Lira
    "thb": 32.5,       # Thai Baht
    "idr": 16300.0     # Indonesian Rupiah
}


from voice_hub import ask,say,speak,get_float

def currency_conversions():
    while True:
        print("-------------------------------------------------------------")
        print("--------Welcome to the Styfer AI Currency Converter----------")
        print("-------------------------------------------------------------")
        print("Supported Currencies:")
        print()
        print("USD - US Dollar")
        print("EUR - Euro")
        print("GBP - British Pound")
        print("INR - Indian Rupee")
        print("JPY - Japanese Yen")
        print("CNY - Chinese Yuan")
        print("RUB - Russian Ruble")
        print("CAD - Canadian Dollar")
        print("AUD - Australian Dollar")
        print("NZD - New Zealand Dollar")
        print("CHF - Swiss Franc")
        print("SGD - Singapore Dollar")
        print("AED - UAE Dirham")
        print("SAR - Saudi Riyal")
        print("KRW - South Korean Won")
        print("HKD - Hong Kong Dollar")
        print("SEK - Swedish Krona")
        print("NOK - Norwegian Krone")
        print("DKK - Danish Krone")
        print("ZAR - South African Rand")
        print("BRL - Brazilian Real")
        print("MXN - Mexican Peso")
        print("TRY - Turkish Lira")
        print("THB - Thai Baht")
        print("IDR - Indonesian Rupiah")

        unknown_field = ask("Please enter currency to convert into: ").lower()
        known_field = ask("Please enter currency you currently have: ").lower()

        if known_field not in currency or unknown_field not in currency:
            say("Please enter a valid currency.")
            continue

        speak("Please enter the amount")
        known_value = get_float(("Please enter the amount: "))
        
        if known_field == unknown_field:
            say(f"Resultant: {known_value}")
            break
        value_in_usd = known_value / currency[known_field]
        answer = value_in_usd * currency[unknown_field]

        say(f"{known_value} {known_field.upper()} = {answer:.2f} {unknown_field.upper()}")
        say("\nNote: Exchange rates are fixed and may not reflect current market values.")
        break