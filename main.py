# built-in package

# project package
from application import create_app

# third package
from flask import make_response

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6500)
