from dash import Dash, html

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = [html.Div(children='Hello World')]

def main():
    app = Dash()

    # Requires Dash 2.17.0 or later
    app.layout = [html.Div(children='Hello World')]  
    app.run(debug=True)

if __name__ == '__main__':
    main()
