from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

from src.constants import Category
from src.managers.source_manager.entrypoint import create_sourcedata_service

service = create_sourcedata_service()

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Input(id="category-input", type="text", placeholder="Category name"),
        html.Button("Add Category", id="add-btn", n_clicks=0),
        html.Div(id="output"),
    ]
)


@app.callback(
    Output("output", "children"),
    [Input("add-btn", "n_clicks")],
    [State("category-input", "value")],
)
def add_category(n_clicks, value):
    if n_clicks is None:
        return ""
    if not value:
        return "Please enter a category name."
    service.insert_category(Category(category=value))
    return f"Inserted {value}"


if __name__ == "__main__":
    app.run_server(debug=True)
