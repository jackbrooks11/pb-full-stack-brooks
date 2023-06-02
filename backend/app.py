from app import app, setup_database

from config import Config
            
if __name__ == '__main__':
    setup_database(app)
    app.run()