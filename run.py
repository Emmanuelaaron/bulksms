app = create_app()
db = DatabaseConnection()


if __name__ == '__main__':
    db.create_db_tables()
    app.run(debug=True)