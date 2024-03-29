# Third-party imports
from dash import Dash
from dash.dependencies import Input, Output

# Local imports
from data.session import Session
from layouts.layouts import Layouts


class Router:
    """
    Dash Router
    """

    def __init__(self, app: Dash):
        @app.callback(
            Output(
                component_id='page_content',
                component_property='children'
            ),
            [Input(
                component_id='url',
                component_property='pathname'
            )]
        )
        def redirect(pathname):
            """
            Takes in one arguement(s);
            - <pathname>:   (str)   the url pathname to redirect to

            Returns a layout_page matching requested pathname.
            """
            if pathname == '/':
                Session['page'] = '/'
                return Layouts.index()

            elif pathname == '/hello':
                Session['page'] = '/hello'
                return Layouts.hello()

            else:
                # Default if no pathname is matched
                Session['page'] = '/404'
                return Layouts.not_found()
