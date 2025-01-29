import os, uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from functions import (
    top_10_drugs_by_sales, sales_over_time, sales_by_manufacturer,quantity_by_city, age_distribution, sales_by_prescription, sales_by_gender, top_insurance_providers, monthly_sales_trends, avg_price_by_manufacturer
)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Main dashboard website:
@app.get("/")
async def read_root(): return FileResponse("static/index.html")


# API Routes:
@app.get("/api/v1/refresh_stats")
async def refresh_stats():
    csv_path = "./data/medicinal_drug_sales.csv"
    image_folder = "./static/images/carousel"

    os.makedirs(image_folder, exist_ok=True)

    try:
        import pandas as pd
        df = pd.read_csv(csv_path)

        plots = [
            {"title": "Top 10 Drugs by Sales", "plot_func": top_10_drugs_by_sales},
            {"title": "Sales Over Time", "plot_func": sales_over_time},
            {"title": "Sales by Manufacturer", "plot_func": sales_by_manufacturer},
            {"title": "Quantity Sold by Pharmacy City", "plot_func": quantity_by_city},
            {"title": "Patient Age Distribution", "plot_func": age_distribution},
            {"title": "Sales by Prescription Requirement", "plot_func": sales_by_prescription},
            {"title": "Sales by Patient Gender", "plot_func": sales_by_gender},
            {"title": "Top Insurance Providers by Sales", "plot_func": top_insurance_providers},
            {"title": "Monthly Sales Trends", "plot_func": monthly_sales_trends},
            {"title": "Average Unit Price by Manufacturer", "plot_func": avg_price_by_manufacturer}
        ]

        print("[LOG] Refreshing stats and saving plots...")
        for idx, plot in enumerate(plots, start=1):
            from matplotlib import pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 6))
            plot["plot_func"](df, ax)
            image_path = os.path.join(image_folder, f"image{idx}.jpg")
            print(f"[LOG] Saving plot: {image_path}")
            plt.savefig(image_path, format="jpg")
            plt.close(fig)
        print("[LOG] All plots saved!")
        return {"message": "Stats refreshed and plots saved!"}

    except Exception as e: return {"error": str(e)}


# Driver Code
if __name__ == '__main__':
    uvicorn.run(app)