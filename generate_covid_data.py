import pandas as pd
import random

states = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar",
    "Chhattisgarh","Goa","Gujarat","Haryana",
    "Himachal Pradesh","Jharkhand","Karnataka","Kerala",
    "Madhya Pradesh","Maharashtra","Manipur","Meghalaya",
    "Mizoram","Nagaland","Odisha","Punjab",
    "Rajasthan","Sikkim","Tamil Nadu","Telangana",
    "Tripura","Uttar Pradesh","Uttarakhand","West Bengal"
]

years = [2021, 2022, 2023]

rows = []

for year in years:

    for state in states:

        if year == 2021:
            base = random.randint(200000, 900000)

        elif year == 2022:
            base = random.randint(100000, 500000)

        else:
            base = random.randint(40000, 250000)

        jan = base
        feb = int(base * 1.2)
        mar = int(base * 1.4)
        apr = int(base * 1.8)
        may = int(base * 1.6)
        jun = int(base * 0.9)

        total = jan + feb + mar + apr + may + jun

        deaths = int(total * 0.02)
        recovered = int(total * 0.94)
        active = total - deaths - recovered

        rows.append([
            year,
            state,
            jan,
            feb,
            mar,
            apr,
            may,
            jun,
            total,
            deaths,
            recovered,
            active
        ])

columns = [
    "Year",
    "State",
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Total Cases",
    "Deaths",
    "Recovered",
    "Active Cases"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("covid_india_data.csv", index=False)

print("✅ 28 States COVID Dataset Created Successfully")