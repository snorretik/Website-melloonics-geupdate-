from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# @app.route("/favicon.ico", methods=["GET"])
# def favicon():
#     return app.send_from_directory("static/images", "favicon.ico")

@app.route("/index.html", methods=["GET"])
def index2():
    return render_template("index.html")

@app.route("/onDisplay.html", methods=["GET"])
def onDisplay():
    return render_template("onDisplay.html")

@app.route("/dionSchilderWerk.html", methods=["GET"])
def dionSchilderWerk():
    return render_template("dionschilderwerk.html")

@app.route("/sudokuProject.html", methods=["GET"])
def sudokuProject():
    return render_template("sudokuProject.html")

@app.route("/eigenEinde.html", methods=["GET"])
def eigenEinde():
    return render_template("eigenEinde.html")

@app.route("/goedeDoelen.html", methods=["GET"])
def goedeDoelen():
    return render_template("goedeDoelen.html")

@app.route("/overalIsGif.html", methods=["GET"])
def overalIsGif():
    return render_template("overalIsGif.html")

@app.route("/blog1.html", methods=["GET"])
def blog1():
    return render_template("blog1.html")

@app.route("/blog2.html", methods=["GET"])
def blog2():
    return render_template("blog2.html")

@app.route("/blog3.html", methods=["GET"])
def blog3():
    return render_template("blog3.html")

@app.route("/blog4.html", methods=["GET"])
def blog4():
    return render_template("blog4.html")

@app.route("/blog5.html", methods=["GET"])
def blog5():
    return render_template("blog5.html")

@app.route("/blog6.html", methods=["GET"])
def blog6():
    return render_template("blog6.html")

@app.route("/blog7.html", methods=["GET"])
def blog7():
    return render_template("blog7.html")

@app.route("/blog8.html", methods=["GET"])
def blog8():
    return render_template("blog8.html")

@app.route("/overMij.html", methods=["GET"])
def overMij():
    return render_template("overMij.html")

if __name__ == "__main__":
    app.run(port=8000)
