import os
from flask import Flask, abort, render_template, request, send_file

app = Flask(__name__, static_folder=None)


@app.before_request
def check_path():
    url_path = request.path
    relative_path = url_path.lstrip("/")

    if (
        "//" in url_path
        or relative_path.startswith(("~", ".."))
        or ".." in relative_path.split("/")
    ):
        abort(403)


@app.route("/")
@app.route("/<path:relative_path>")
def respond(relative_path=""):
    if not relative_path.endswith((".html", ".css")):
        abort(404)

    docroot = os.path.realpath(os.path.join(app.root_path, "pages"))
    file_path = os.path.realpath(os.path.join(docroot, relative_path))

    if os.path.commonpath([docroot, file_path]) != docroot:
        abort(403)

    if not os.path.isfile(file_path):
        abort(404)

    return send_file(file_path)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html"), 403


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')