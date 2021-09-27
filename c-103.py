import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
print(df)
fig=px.line(df,x="date",y="cases")
fig.show()