# Real-Time-Weather-Analysis
Real-Time Weather Analysis using Azure and Python




Project Title: Real-Time Weather Data Collection and Storage System

Overview: This project involves creating a system that collects real-time weather data from an API and stores it in an Azure SQL Database. The system fetches weather information such as temperature, humidity, and weather conditions for a specified city and stores this data for future analysis or reporting. This project highlights the use of Python, Azure SQL Database, and API integration.

Objectives:

Fetch Real-Time Weather Data: Use the OpenMeteo API to obtain weather information for a specific city.
Store Data in Azure SQL Database: Save the fetched weather data into an Azure SQL Database for storage and retrieval.
Develop a Data Processing Script: Create a Python script that integrates with the API, processes the data, and interacts with the database.


Components:

Weather Data API:

API Used: OpenMeteo API (free option)
Data Collected: Current temperature, humidity, and weather conditions.

Database:

Database Used: Azure SQL Database

Table Schema: A table to store weather data with columns for city, temperature, humidity, and weather conditions.
Python Script:

Functions:

get_weather_data(): Fetches weather data from the OpenMeteo API.
store_weather_data(weather): Stores the fetched data in the Azure SQL Database.

This project is suitable for use cases where real-time weather data is required for applications like weather forecasting, historical weather analysis, or integration into other systems that depend on weather conditions. It provides a foundational example of data collection and storage that can be expanded with additional features or integrated into larger systems.
