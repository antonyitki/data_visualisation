import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("vaccination-data.csv") #reading the database
print(data.head(), data.columns)
integer_vaccines_type = data["NUMBER_VACCINES_TYPES_USED"]
integer_vaccines_type.fillna(0)
print(integer_vaccines_type, len(integer_vaccines_type), integer_vaccines_type.unique())
region = data["WHO_REGION"]
print(region, len(region), region.unique())
# print(max(data["NUMBER_VACCINES_TYPES_USED"]))
print(data['NUMBER_VACCINES_TYPES_USED'].nlargest(n=12)) #untill 11 inclusive
print(data.loc[data['NUMBER_VACCINES_TYPES_USED']>10, 'COUNTRY'])
top_variety = data.loc[data['NUMBER_VACCINES_TYPES_USED']>10, 'COUNTRY']
print(top_variety, len(top_variety))
top_varietylist = np.array(top_variety)
fig, axe = plt.subplots(figsize=(14, 7))
plt.bar(data["WHO_REGION"], data["NUMBER_VACCINES_TYPES_USED"], color = "blue")
plt.xlabel('Regional Offices (EMRO = Eastern Mediterranean, WPRO = Western Pacific, AMRO = Americas, SEARO = South-East Asia, Other = Liechtenstein)')
plt.ylabel('Number of different vaccines used')
plt.title("How many types of vaccines by region", color = "#091b82", fontsize = 22)
plt.axhline(y = 6, color = 'r', linestyle = '-')
axe.text(4.8, 8.8, f" Countries whith highest variety of vaccines (12 & 11)  \n{top_variety}", bbox=dict(facecolor='red', alpha=0.5),fontsize = 9)
plt.tight_layout(pad=1.1, w_pad=0.5, h_pad=0.2)
plt.show()
fig.savefig("output1.png")
plt.close(fig)