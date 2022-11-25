#https://www.geeksforgeeks.org/covid-19-analysis-and-visualization-using-plotly-express/
import plotly.express as px
import pandas as pd
import plotly.io as pio


df = pd.read_csv("WHO-COVID-19-global-table-data.csv")
figure3 = px.scatter(df.head(100), x='Name', y= 'Deaths - cumulative total',
		hover_data=['WHO Region'],
		color='Name', size= 'Deaths - cumulative total', size_max=80, hover_name="Name",
        title=("100 Countries gruped by continent showing number of cumulative deaths"))
figure3.update_xaxes(title_font_family="Helvetica")
figure3.show()
# export as static image
pio.write_image(figure3, "output3.png")