from application import create_app
from config.config import CONF
app = create_app()

if __name__ == '__main__':
    app.run()
