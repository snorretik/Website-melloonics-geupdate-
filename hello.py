from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def index2():
    return render_template("index.html")

@app.route("/onDisplay")
def onDisplay():
    return render_template("onDisplay.html")

@app.route("/dionSchilderWerk")
def dionSchilderWerk():
    return render_template("dionschilderwerk.html")

@app.route("/sudokuProject")
def sudokuProject():
    return render_template("sudokuProject.html")

@app.route("/eigenEinde")
def eigenEinde():
    return render_template("eigenEinde.html")

@app.route("/goedeDoelen")
def goedeDoelen():
    return render_template("goedeDoelen.html")

@app.route("/overalIsGif")
def overalIsGif():
    return render_template("overalIsGif.html")

@app.route("/blog1")
def blog1():
    return render_template("blog1.html")

@app.route("/blog2")
def blog2():
    return render_template("blog2.html")

@app.route("/blog3")
def blog3():
    return render_template("blog3.html")

@app.route("/blog4")
def blog4():
    return render_template("blog4.html")

@app.route("/blog5")
def blog5():
    return render_template("blog5.html")

@app.route("/blog6")
def blog6():
    return render_template("blog6.html")

@app.route("/blog7")
def blog7():
    return render_template("blog7.html")

@app.route("/blog8")
def blog8():
    return render_template("blog8.html")

@app.route("/overMij")
def overMij():
    return render_template("overMij.html")


