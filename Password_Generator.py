from flask import Flask, render_template, request, redirect, url_for
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

app = Flask(__name__)

# In-memory lists to store tasks.
password1 = []

# Route to display tasks
@app.route("/")
def display_tasks():
    return render_template("password.html", tasks=password1)

# Route to add a new task
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    length = int(request.form.get("length", 12))  # Default length is 12 if not provided

    # Generate a password with the specified length
    password = generate_password(length)

    password1.append({"title": title, "password": password})
    return redirect(url_for("display_tasks"))

# Route to remove a task
@app.route("/remove/<int:index>")
def remove_task(index):
    if 1 <= index <= len(password1):
        completed_task = password1.pop(index - 1)
    return redirect(url_for("display_tasks"))

if __name__ == "__main__":
    app.run(debug=True)
