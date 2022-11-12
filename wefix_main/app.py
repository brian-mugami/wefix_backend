from website import create_app

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    with app.app_context():
        app.run(host="0.0.0.0")