from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory lists to store tasks and completed tasks
tasks = []
completed_tasks = []

# Route to display tasks
@app.route("/")
def display_tasks():
    return render_template("tasks.html", tasks=tasks)

# Route to add a new task
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    tasks.append({"title": title, "status": "Incomplete"})
    return redirect(url_for("display_tasks"))

# Route to remove a task
@app.route("/remove/<int:index>")
def remove_task(index):
    if 1 <= index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        completed_task["status"] = "Completed"
        completed_tasks.append(completed_task)
    return redirect(url_for("display_tasks"))

# Route to display completed tasks in tabular form
@app.route("/complete")
def display_completed_tasks():
    return render_template("complete.html", completed_tasks=completed_tasks)

if __name__ == "__main__":
    app.run(debug=True)
