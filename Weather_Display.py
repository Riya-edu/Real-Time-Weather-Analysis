import pyodbc
import matplotlib.pyplot as plt

# Azure SQL Database connection details
conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=weather-analysis.database.windows.net;"
    "Database=real-time-weather-analysis;"
    "Uid=Riya;"
    "Pwd=R2i4y0@1;"
)

cursor = conn.cursor()

# Query to fetch city names and temperatures
cursor.execute("SELECT city, temperature FROM Weather_Data")
data = cursor.fetchall()

# Store the data in lists
city_names = [row[0] for row in data]
temperatures = [row[1] for row in data]

# 1. Line Plot for Temperature Trends Across Cities
plt.figure(figsize=(10, 6))
plt.plot(city_names, temperatures, marker='o')
plt.title('Temperature Trends Across Cities')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)  # Rotate city names for better readability
plt.grid(True)
plt.tight_layout()  # Prevent overlapping issues
plt.show()

# 2. Bar Chart for Average Temperatures Across Cities
plt.figure(figsize=(10, 6))
plt.bar(city_names, temperatures, color='skyblue')
plt.title('Average Temperature Across Cities')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()  # Prevent overlapping issues
plt.show()


# 3. Histogram for Temperature Distribution Across Cities
plt.figure(figsize=(10, 6))
plt.hist(temperatures, bins=10, color='purple', edgecolor='black')
plt.title('Temperature Distribution Across Cities')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()  
plt.show()
