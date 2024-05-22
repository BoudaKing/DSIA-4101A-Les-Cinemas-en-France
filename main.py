import dashboard

if __name__ == '__main__':

    app = dashboard.launch_app(__name__)
    app.run_server(debug=True)