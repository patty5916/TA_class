import pandas as pd
import plotly.express as px
import dash

# Dash ships with supercharged components for interactive user interfaces
# Write HTML or use an HTML templating engine
# dcc: dash core components
from dash import dcc, html

app = dash.Dash(__name__)

# Color settings
colors = {
    'background': '#2c3e50',
    'text': '#3498db'
}

# Create an example data
df = pd.DataFrame({
    'Pet': ['Dog', 'Cat', 'Rabbit', 'Dog', 'Cat', 'Rabbit'],
    'Age': [2, 1, 1, 3, 3, 4],
    'Gender': ['M', 'M', 'M', 'F', 'F', 'F']
})

# Create a bar chart
fig = px.bar(df,
             x='Pet',
             y='Age',
             color='Gender',
             barmode='group'
             )

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# Layout settings
app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        # <h1 style='...'>This is the 1st example of Dash layout</h1>
        html.H1(
            children='This is the 1st example of Dash layout',
            style={
                'textAlign': 'center',  # HTML: text-align
                'color': colors['text']
            }
        ),

        html.Div(
            children='Dash layout describes what the applications looks like.',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        dcc.Graph(
            id='layout-example-graph-1',
            figure=fig
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=False)
