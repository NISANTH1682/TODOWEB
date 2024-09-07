from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global task lists
completed_tasks = []
incomplete_tasks = []

@app.route('/')
def index():
    return render_template('index.html', incomplete_tasks=incomplete_tasks, completed_tasks=completed_tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        incomplete_tasks.append(task)
    return redirect(url_for('index'))

@app.route('/complete_task/<task>')
def complete_task(task):
    if task in incomplete_tasks:
        incomplete_tasks.remove(task)
        completed_tasks.append(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

