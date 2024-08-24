import requests
import pyodbc

# Replace with the latitude and longitude of your city
LATITUDE = '11.0168'
LONGITUDE = '76.9558'
URL = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&hourly=temperature_2m"

conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=weather-analysis.database.windows.net;"
    "Database=real-time-weather-analysis;"
    "Uid=Riya;"
    "Pwd=R2i4y0@1;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

def get_weather_data():
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
        # Extracting the first hour's data for simplicity
        return {
            "city": "Coimbatore",  # Open-Meteo doesn't provide city names directly
            "temperature": data['hourly']['temperature_2m'][0],
            }
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def store_weather_data(weather):
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Weather_Data(city, temperature) VALUES (?, ?)",
                weather["city"], weather["temperature"]
            )
        conn.commit()

def main():
    weather = get_weather_data()
    if weather:
        store_weather_data(weather)

if __name__ == "__main__":
    main()