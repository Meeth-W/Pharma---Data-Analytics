import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

# Function to generate a random RGB color
def random_color(): return (random.random(), random.random(), random.random())

# Plotting functions
def top_10_drugs_by_sales(df, ax):
    top_drugs = df.groupby("drug_name")["total_price"].sum().nlargest(10)
    ax.barh(top_drugs.index, top_drugs.values, color=random_color())
    ax.set_title("Top 10 Drugs by Sales")
    ax.set_xlabel("Total Sales")

def sales_over_time(df, ax):
    df["sale_date"] = pd.to_datetime(df["sale_date"])
    sales_over_time = df.groupby("sale_date")["total_price"].sum()
    ax.plot(sales_over_time.index, sales_over_time.values, color=random_color())
    ax.set_title("Sales Over Time")
    ax.set_ylabel("Total Sales")
    ax.set_xlabel("Date")

def sales_by_manufacturer(df, ax):
    manufacturer_sales = df.groupby("manufacturer")["total_price"].sum()
    ax.barh(manufacturer_sales.index, manufacturer_sales.values, color=random_color())
    ax.set_title("Sales by Manufacturer")
    ax.set_xlabel("Total Sales")

def quantity_by_city(df, ax):
    city_quantity = df.groupby("pharmacy_city")["quantity_sold"].sum().nlargest(10)
    ax.barh(city_quantity.index, city_quantity.values, color=random_color())
    ax.set_title("Quantity Sold by Pharmacy City")
    ax.set_xlabel("Total Quantity Sold")

def age_distribution(df, ax):
    sns.histplot(df["patient_age"], bins=20, kde=True, color=random_color(), ax=ax)
    ax.set_title("Patient Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")

def sales_by_prescription(df, ax):
    prescription_sales = df.groupby("prescription_required")["total_price"].sum()
    ax.bar(prescription_sales.index, prescription_sales.values, color=random_color())
    ax.set_title("Sales by Prescription Requirement")
    ax.set_xlabel("Prescription Required")
    ax.set_ylabel("Total Sales")

def sales_by_gender(df, ax):
    gender_sales = df.groupby("patient_gender")["total_price"].sum()
    ax.bar(gender_sales.index, gender_sales.values, color=random_color())
    ax.set_title("Sales by Patient Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Total Sales")

def top_insurance_providers(df, ax):
    insurance_sales = df.groupby("insurance_provider")["total_price"].sum().nlargest(10)
    ax.barh(insurance_sales.index, insurance_sales.values, color=random_color())
    ax.set_title("Top Insurance Providers by Sales")
    ax.set_xlabel("Total Sales")

def monthly_sales_trends(df, ax):
    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["month"] = df["sale_date"].dt.to_period("M")
    monthly_sales = df.groupby("month")["total_price"].sum()
    ax.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o", color=random_color())
    ax.set_title("Monthly Sales Trends")
    ax.set_ylabel("Total Sales")
    ax.set_xlabel("Month")

def avg_price_by_manufacturer(df, ax):
    avg_price = df.groupby("manufacturer")["unit_price"].mean().nlargest(10)
    ax.barh(avg_price.index, avg_price.values, color=random_color())
    ax.set_title("Average Unit Price by Manufacturer")
    ax.set_xlabel("Average Unit Price")
