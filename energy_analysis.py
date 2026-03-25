import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("energy_data.csv")

data['Date'] = pd.to_datetime(data['Date'])

print(data.describe())

plt.figure()
plt.plot(data['Date'], data['Energy_Consumption_kWh'])
plt.title("Energy Consumption Trend")
plt.xlabel("Date")
plt.ylabel("Energy Consumption")
plt.show()