# app.py

from flask import Flask, render_template
# flask looks for templates in ./templates by default

app = Flask(__name__)

@app.route("/")
def home():
    #return "Hello, World!"
    return render_template("base.html", title="Jinja and Flask")

max_score = 100
test_name = "Python Challenge"
students = [
        {"name": "Sandrine", "score": 100},
        {"name": "Gergeley", "score": 87},
        {"name": "Frieda", "score": 92},
        {"name": "Fritz", "score": 40},
        {"name": "Sirius", "score": 75}
]

@app.route("/results")
def results():
    context = {
            "students": students,
            "test_name": test_name,
            "max_score": max_score,
    }
    return render_template("results.html", **context)
    # render_template() only accepts one argument, the template name.
    # the **context tells python to unpack the dictionary called context
    # With the asterick operators, you're passing the items of context as
    #   keywork arguments into render_template()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
