import plotly.express as ps
import pandas as spb

data = spb.read_csv("data.csv")

fig = ps.scatter(data, x = "date", y = "cases", color = "country", size_max = 60, title = "Internet users Per country")

fig.show()  