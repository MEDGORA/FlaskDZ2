from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = b"cb1d24e1054dfdb9a1ccabba369c3f3008964512dcb39325bdfc2849227fd153"

@app.route("/")
@app.route("/form/", methods =["GET", "POST"])
def form():
    if request.method == "POST":
        if not request.form["name"] or not request.form["email"]:
            flash("Введите имя и электронную почту", "danger")
            return redirect(url_for("form"))
        response = redirect(url_for("welcome", name = request.form["name"]))
        response.set_cookie("name", str(request.form["name"]))
        response.set_cookie("email", str(request.form["email"]))
        return response
    return render_template("form.html")
    
@app.route("/welcome/<name>/", methods =["GET", "POST"])
def welcome(name):
    contex = {"name": str(name)}
    if request.method == "POST":
        response = redirect(url_for("form"))
        response.set_cookie("name", max_age=0)
        response.set_cookie("email", max_age=0)
        return response
    return render_template("welcome.html", **contex)

if __name__ == "__main__":
    app.run(debug= True)

