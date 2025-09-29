from flask import Flask, render_template, request, redirect, url_for
from Budget import transactions, add_transaction, total_spent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        description = request.form["description"]
        amount = float(request.form["amount"])
        add_transaction(description, amount)
        return redirect(url_for("index"))
    return render_template(
        "index.html",
        transactions=transactions,
        total=total_spent()
    )

if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)), debug=True)


