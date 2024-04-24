# Import packages
from dash import Dash, html, dcc
import pandas as pd

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

dropdown_options = df.brand.unique().tolist()
radio_values = sorted(df.group.unique())
radio_labels = ["Fenty Beauty's PRO FILT'R Foundation Only",
                "Make Up For Ever's Ultra HD Foundation Only",
                "US Best Sellers",
                "BIPOC-recommended Brands with BIPOC Founders",
                "BIPOC-recommended Brands with White Founders",
                "Nigerian Best Sellers",
                "Japanese Best Sellers",
                "Indian Best Sellers"]
radio_options = []
for label, value in zip(radio_labels, radio_values):
    radio_options.append({'label': label, 'value': value})

# Initialize the app
app = Dash(__name__)

# App layout
#app.layout = html.Div([
#    dcc.Dropdown(dropdown_options, 'Revlon'),
#    dcc.RadioItems(options=radio_options)
#])

app.layout = html.Div([
    dcc.Dropdown(options=dropdown_options, value='Revlon'),
    dcc.RadioItems(options=radio_options)
])

# Run the app
if __name__ == '__main__':
   app.run(debug=True)

