import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load dataset
# ----------------------------
drivers = pd.read_csv("drivers.csv")

# ----------------------------
# Create full driver name
# ----------------------------
drivers["full_name"] = (
    drivers["driver_forename"].astype(str) + " " +
    drivers["driver_surname"].astype(str)
)

# ----------------------------
# Calculate career points
# ----------------------------
career_points = (
    drivers.groupby("full_name", as_index=False)["points"]
    .sum()
    .sort_values(by="points", ascending=False)
)

# ----------------------------
# Top 5 drivers
# ----------------------------
top_5 = career_points.head(5)

print("\nTop 5 Drivers by Career Points:\n")
print(top_5)

# ----------------------------
# Visualization
# ----------------------------
plt.figure(figsize=(10, 6))
plt.bar(top_5["full_name"], top_5["points"])
plt.title("Top 5 Formula 1 Drivers by Career Points")
plt.xlabel("Driver")
plt.ylabel("Total Career Points")
plt.xticks(rotation=20)
plt.tight_layout()

plt.show()
