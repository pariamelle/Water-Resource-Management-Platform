import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import requests

# Initialize the Dash app
app = dash.Dash(__name__)

# URL of the GeoJSON data
geojson_url = ''



# Fetch the GeoJSON data
geojson_data = requests.get(geojson_url).json()

# Create the map figure
fig = go.Figure(go.Choroplethmapbox(
    geojson=geojson_data,
    locations=['28210', 'another_series_id'],  # Replace with actual IDs present in your GeoJSON data
    z=[1, 2],  # Replace with the values you want to display
    colorscale="Viridis",
    marker_opacity=0.5,
    marker_line_width=0
))

# Set the layout for the map
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=10,
    mapbox_center={"lat": 45.758606, "lon": 11.006637}  # Center the map around Provincia di Trento
)

# Define the layout of the Dash app
app.layout = html.Div([
    dcc.Graph(id='map', figure=fig),
    html.Div(id='info', style={'float': 'right', 'width': '60%'})  # Space for displaying stats
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

