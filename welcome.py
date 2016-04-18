import os
from flask import Flask, request, redirect

app = Flask(__name__, static_folder=".")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path == "":
        newpath = "index.html"
    else:
        newpath = path
    if request.headers['$Wssc'] == "https":
        return app.send_static_file(newpath)
    else:
        return redirect("https://" + request.headers['Host'] + "/" + newpath)


port = os.getenv('PORT', '5000')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)
