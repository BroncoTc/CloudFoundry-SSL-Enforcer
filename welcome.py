import os
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/')
def Welcome():
    return str(request.headers)
    # return app.send_static_file('index.html')


port = os.getenv('PORT', '5000')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port),debug=True)
