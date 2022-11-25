# https://towardsdatascience.com/covid-19-vaccination-progress-analysis-around-the-world-736d7e57f198
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


sns.set_style('whitegrid')
df = pd.read_csv("vaccination-data.csv")
plt.figure(1, figsize=(15, 7),facecolor="#5b92e5")
plt.subplot(211)
cols = ['COUNTRY', 'TOTAL_VACCINATIONS', 'ISO3', 'VACCINES_USED','TOTAL_VACCINATIONS_PER100']
vacc_amount = df[cols].groupby('COUNTRY').max().sort_values('TOTAL_VACCINATIONS', ascending=False).dropna(subset=['TOTAL_VACCINATIONS'])
vacc_amount = vacc_amount.iloc[:11]
vacc_amount = vacc_amount.sort_values('TOTAL_VACCINATIONS_PER100', ascending=False)
plt.bar(vacc_amount.index, vacc_amount.TOTAL_VACCINATIONS_PER100, color = 'r')
plt.xticks(rotation = 10)
plt.title("Which country is vaccinating its citizens the fastest?", color = "r", fontweight="bold")
plt.ylabel('Amount of vaccinated people per hundred')
plt.subplot(212)
cols = ['COUNTRY', 'TOTAL_VACCINATIONS', 'ISO3', 'VACCINES_USED']
vacc_amount = df[cols].groupby('COUNTRY').max().sort_values('TOTAL_VACCINATIONS', ascending=False).dropna(subset=['TOTAL_VACCINATIONS'])
vacc_amount = vacc_amount.iloc[:11]
plt.bar(vacc_amount.index, vacc_amount.TOTAL_VACCINATIONS, color = 'g')
plt.title('Which country has the highest number of vaccinated people?', color ="#025839", fontweight="bold")
plt.ylabel('Amount of vaccinated citizens')
plt.xlabel('NOTE: Countries are not the same for both figures. Total number of countries in each figure = 11')
plt.xticks(rotation = 10)
plt.tight_layout()
plt.show()
plt.savefig("output2.png")