from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return 'Database connection successful!'
    except SQLAlchemyError as e:
        return f'Database connection failed: {str(e)}'

if __name__ == '__main__':
    app.run()