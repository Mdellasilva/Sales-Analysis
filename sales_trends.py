# Sales Trends

from numpy import average
import pandas as pd
import matplotlib.pyplot as plt

"""
The main purpose of this program is to analyze sales and visitors data from the csv file named "data_world_farm_stand.csv".
The user can select farm stand or mobile market, depending on what data the user wants to see. Once the user decides what data
to look at, the program will display a line graph that displays the sales data, ordered by date. It will also give a description
of the series "Total Sales". the program is then able to ask the user if they would like to view the "Visitors" series, and it will 
go through a similar process to what it does with "Total Sales". At the end of the program, it will allow you to view the average 
of all of the sales if desired.
"""

def main():

    df = pd.read_csv("data_world_farm_stand.csv")
    df["Month"] = pd.to_datetime(df.month, format="%B").dt.month
    df["Year"] = pd.to_datetime(df.year, format="%Y").dt.year
    df["Month and Year"] = df["Month"].map(str) + "-" + df["Year"].map(str)
    df["Month and Year"] = pd.to_datetime(df["Month and Year"], format="%m-%Y").apply(lambda x: x.strftime("%m-%Y"))
    
    user_input = input("Please enter the data you would like to view. (Farm Stand / Mobile Market) ")
    
    if user_input.lower() == "farm stand":
        total_farm_sales_chart(df)
        total_farm_sales_description(df)
        
        view_farm_visitors_data = input("Would you like to view the visitors data for the Farm Stand? (Yes / No) ")

        if view_farm_visitors_data.lower() == "yes":
            total_farm_visitors_chart(df)
            total_farm_visitors_description(df)
        else:
            print("Analysis Complete")
            
    elif user_input.lower() == "mobile market":
        total_mobile_sales_chart(df)
        total_mobile_sales_description(df)

        view_mobile_visitors_data = input("Would you like to view the visitors data for the Mobile Market? (Yes / No) ")

        if view_mobile_visitors_data.lower() == "yes":
            total_mobile_visitors_chart(df)
            total_mobile_visitors_description(df)
        else:
            print("Analysis Complete")

    else:
        print("Please check the spelling and try again.")

    view_average = input("Would you like to view the average of all of the sales? (Yes / No) ")
    
    if view_average.lower() == "yes":
        total_sales_average(df)
    elif view_average.lower() == "no":
        print("Analysis Complete")
    else:
        print("Please try again.")


def total_farm_sales_chart(df):
    """
    This function filters for the sales data of the farm stand when the user inputs 
    farm stand as the desired data to retrieve, and it produces a line graph of the 
    total sales for the farm stand ordered by the date.
    """
    farm_stand_filtered = df["Farm Stand or Mobile Market"].str.contains("Farm Stand")
    df[farm_stand_filtered].plot(kind = "line", x = "Month and Year", y = "Total Sales")

    plt.title("Total Farm Stand Sales")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.show()

def total_farm_sales_description(df):
    """
    This function filters for the sales data of the farm stand when the user inputs 
    farm stand as the desired data to retrieve, and it produces a description of the 
    total sales for the farm stand.
    """
    total_sales_description = round(df.loc[df["Farm Stand or Mobile Market"] == "Farm Stand"]["Total Sales"].describe(), 2)
    print("Total Farm Stand Sales Description")
    print(f"{total_sales_description}")

def total_farm_visitors_chart(df):
    """
    This function filters for the visitors data of the farm stand when the user inputs 
    farm stand as the desired data to retrieve, and it produces a line graph of the 
    visitors for the farm stand ordered by the date.
    """
    farm_stand_filtered = df["Farm Stand or Mobile Market"].str.contains("Farm Stand")
    df[farm_stand_filtered].plot(kind = "line", x = "Month and Year", y = "Visitors")

    plt.title("Farm Stand Visitors")
    plt.xlabel("Date")
    plt.ylabel("Visitors")
    plt.show()

def total_farm_visitors_description(df):
    """
    This function filters for the visitors of the farm stand when the user inputs 
    farm stand as the desired data to retrieve, and it produces a description of the 
    visitors for the farm stand.
    """
    farm_visitors_description = round(df.loc[df["Farm Stand or Mobile Market"] == "Farm Stand"]["Visitors"].describe(), 2)
    print("Farm Stand Visitors Description")
    print(f"{farm_visitors_description}")




def total_mobile_sales_chart(df):
    """
    This function filters for the sales data of the mobile market when the user inputs 
    mobile market as the desired data to retrieve, and it produces a line graph of the 
    total sales for the mobile market ordered by the date.
    """
    mobile_market_filtered = df["Farm Stand or Mobile Market"].str.contains("Mobile Market")
    df[mobile_market_filtered].plot(kind = "line", x = "Month and Year", y = "Total Sales")
    plt.title("Total Mobile Market Sales")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.show()

def total_mobile_sales_description(df):
    """
    This function filters for the sales data of the mobile market when the user inputs 
    mobile market as the desired data to retrieve, and it produces a description of the 
    total sales for the mobile market.
    """
    total_sales_description = round(df.loc[df["Farm Stand or Mobile Market"] == "Mobile Market"]["Total Sales"].describe(), 2)
    print("Total Mobile Market Sales Description")
    print(f"{total_sales_description}")

def total_mobile_visitors_chart(df):
    """
    This function filters for the visitors data of the mobile market when the user inputs 
    mobile market as the desired data to retrieve, and it produces a line graph of the 
    visitors for the mobile market ordered by the date.
    """
    mobile_market_filtered = df["Farm Stand or Mobile Market"].str.contains("Mobile Market")
    df[mobile_market_filtered].plot(kind = "line", x = "Month and Year", y = "Visitors")

    plt.title("Mobile Market Visitors")
    plt.xlabel("Date")
    plt.ylabel("Visitors")
    plt.show()

def total_mobile_visitors_description(df):
    """
    This function filters for the visitors data of the farm stand when the user inputs 
    mobile market as the desired data to retrieve, and it produces a description of the 
    visitors for the mobile market.
    """
    mobile_visitors_description = round(df.loc[df["Farm Stand or Mobile Market"] == "Mobile Market"]["Visitors"].describe(), 2)
    print("Mobile Market Visitors Description")
    print(f"{mobile_visitors_description}")

def total_sales_average(df):
    average_sales = round(average(df["Total Sales"]), 2)
    print(average_sales)
    return average_sales


if __name__ == "__main__":
    main()

# Source: https://data.world/cityofaustin/cfer-vyii
