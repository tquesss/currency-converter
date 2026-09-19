import requests

def fetch_currency_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            try_rate = data["rates"]["TRY"]
            eur_usd_rate = data["rates"]["EUR"]
            eur_rate = try_rate / eur_usd_rate

            print("--- LIVE CURRENCY RATES ---")
            print(f"USD/TRY: {try_rate:.2f}")
            print(f"EUR/TRY: {eur_rate:.2f}\n")

            # Simple converter
            usd = float(input("USD Amount: "))
            print(f"{usd} USD = {usd * try_rate:.2f} TRY")
        else:
            print("API Error.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    fetch_currency_rates()