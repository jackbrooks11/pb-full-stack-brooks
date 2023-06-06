from app import create_app, setup_database
          
if __name__ == '__main__':
    app = create_app()
    app.run()