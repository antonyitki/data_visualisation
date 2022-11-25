# https://www.kaggle.com/code/siddheshmahajan/covid-19-data-visualization
import pandas as pd
import plotly.io as pio
import plotly.express as px


df = pd.read_csv("WHO-COVID-19-global-table-data.csv")
df_countries = df.groupby(['WHO Region']).max().reset_index()
df_countries = df_countries.drop_duplicates(subset = ['WHO Region'])
#the classic pie chart
fig = px.pie(df_countries, values = 'Deaths - cumulative total', names='Name', height=800, title='Comulative death by continent')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(
    title_x = 0.5,
    autosize = True,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))
fig.update_layout(legend=dict(
    title="WHO Regions"
)) # write a title for the legend on the right
fig.show()
pio.write_image(fig, "output4.png")