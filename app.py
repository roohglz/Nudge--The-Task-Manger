from flask import Flask, render_template, request, redirect, url_for, flash
from tasks import PersonalTask, WorkTask, UrgentWorkTask, TaskManager

app = Flask(__name__)
app.secret_key = "supersecretkey"  # replace with a secure key in production

manager = TaskManager("Nudge")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", tasks=manager.tasks)

@app.route("/add", methods=["POST"])
def add_task():
    try:
        title = request.form.get("title", "").strip()
        priority = request.form.get("priority", "").strip()
        task_type = request.form.get("task_type", "").strip()

        if not title or not priority or not task_type:
            raise ValueError("Title, priority, and task type are required.")

        TaskManager.validate_priority(priority)

        if task_type == "personal":
            category = request.form.get("category", "").strip()
            if not category:
                raise ValueError("Category is required for PersonalTask.")
            task = PersonalTask(title, priority, category)
        elif task_type == "work":
            deadline = request.form.get("deadline", "").strip()
            if not deadline:
                raise ValueError("Deadline is required for WorkTask.")
            task = WorkTask(title, priority, deadline)
        elif task_type == "urgent":
            deadline = request.form.get("deadline", "").strip()
            reason = request.form.get("reason", "").strip()
            if not deadline or not reason:
                raise ValueError("Deadline and reason are required for UrgentWorkTask.")
            task = UrgentWorkTask(title, priority, deadline, reason)
        else:
            raise ValueError("Invalid task type.")

        manager.add_task(task)
        flash(f"Task '{title}' added.", "success")
    except Exception as e:
        flash(str(e), "error")

    return redirect(url_for("index"))

@app.route("/delete/<title>", methods=["POST"])
def delete_task(title):
    try:
        manager.remove_task(title)
        flash(f"Task '{title}' deleted.", "success")
    except Exception as e:
        flash(str(e), "error")

    return redirect(url_for("index"))

@app.route("/status/<title>", methods=["POST"])
def update_status(title):
    try:
        status = request.form.get("status", "").strip()
        if not status:
            raise ValueError("Status is required.")

        task = next(
            (t for t in manager.tasks if t.title == title and isinstance(t, PersonalTask)),
            None,
        )
        if task is None:
            raise ValueError("PersonalTask not found.")

        task.status = status
        flash(f"Status for '{title}' updated to '{status}'.", "success")
    except Exception as e:
        flash(str(e), "error")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)