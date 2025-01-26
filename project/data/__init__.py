# Data Generation Script


import csv
from faker import Faker

fake = Faker()

# Define the fields
fields = [
    "drug_id", "drug_name", "manufacturer", "batch_number", "expiry_date",
    "sale_date", "quantity_sold", "unit_price", "total_price", "pharmacy_name",
    "pharmacy_address", "pharmacy_city", "pharmacy_state", "pharmacy_zip",
    "pharmacist_name", "prescription_required", "patient_age", "patient_gender",
    "patient_id", "insurance_provider"
]

# Generate the data
rows = []
for _ in range(1000):
    drug_id = fake.uuid4()
    drug_name = fake.word()
    manufacturer = fake.company()
    batch_number = fake.bothify(text='??#####')
    expiry_date = fake.date_between(start_date='today', end_date='+2y')
    sale_date = fake.date_between(start_date='-1y', end_date='today')
    quantity_sold = fake.random_int(min=1, max=100)
    unit_price = fake.random_number(digits=2)
    total_price = quantity_sold * unit_price
    pharmacy_name = fake.company()
    pharmacy_address = fake.street_address()
    pharmacy_city = fake.city()
    pharmacy_state = fake.state()
    pharmacy_zip = fake.zipcode()
    pharmacist_name = fake.name()
    prescription_required = fake.boolean()
    patient_age = fake.random_int(min=0, max=100)
    patient_gender = fake.random_element(elements=('Male', 'Female'))
    patient_id = fake.uuid4()
    insurance_provider = fake.company()

    rows.append([
        drug_id, drug_name, manufacturer, batch_number, expiry_date,
        sale_date, quantity_sold, unit_price, total_price, pharmacy_name,
        pharmacy_address, pharmacy_city, pharmacy_state, pharmacy_zip,
        pharmacist_name, prescription_required, patient_age, patient_gender,
        patient_id, insurance_provider
    ])

# Write to CSV
with open('medicinal_drug_sales.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)