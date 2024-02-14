# filename: plot_temp.py

import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

# URL of the csv data
data_url = "https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv"

# Step 1: Download the CSV data
response = requests.get(data_url)
response.raise_for_status()  # This will raise an error if the download failed

# Step 2: Load the data into a pandas DataFrame
data = pd.read_csv(StringIO(response.text))

# Step 3: Plot the high and low temperatures
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['temp_max'], label='High Temp (°C)', color='tomato')
plt.plot(data['date'], data['temp_min'], label='Low Temp (°C)', color='dodgerblue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('High and Low Temperatures in Seattle')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig('result.jpg')

# Show the plot if you want to preview it here, otherwise, it's already saved as "result.jpg"
#plt.show()
print("The plot has been saved as 'result.jpg'")