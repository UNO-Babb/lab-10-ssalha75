#MapPlot.py
#Name: Sara Salha
#Date: 4/20/2025
#Assignment: Lab 10

import food
import pandas
import matplotlib.pyplot as plt

report = food.get_report()

records = []
for item in report:
    data = item["Data"]
    sugar = data.get("Sugar Total")
    fat = data.get("Fat", {}).get("Total Lipid")

    if sugar and fat:
        records.append({
            "Sugar": sugar,
            "Fat": fat
        })
 
df = pandas.DataFrame(records)

df = df[(df["Sugar"] < 80) & (df["Fat"] < 80)]

plt.figure(figsize=(10, 6))
plt.scatter(df["Sugar"], df["Fat"], alpha=0.5)
plt.title("Sugar vs Fat Content in Foods")
plt.xlabel("Sugar (g)")
plt.ylabel("Fat (g)")
plt.grid(True)
plt.tight_layout()
plt.savefig("lab10")

"""
Step 5 - Explanation:
This graph shows the relationship between sugar and fat in different foods. Most items are low in both, so they cluster in the bottom left.
Some have high sugar and low fat, or the opposite. There doesn't seem to be a strong correlation between sugar and fat.
The graph helped me see that foods can be high in one but not the other, and that the two aren't always related.
"""