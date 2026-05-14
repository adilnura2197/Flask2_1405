from flask import Flask, render_template

app = Flask(__name__)

university = "TATU"
teacher_name = "Karimov"
student_name = "Ali"
group = "107"


@app.route('/')
def sahifa():
    return render_template('index.html', university=university)

@app.route('/teacher')
def teach():
    return render_template('books.html', teacher_name)

@app.route('/student')
def student():
    return render_template('author.html', student_name=student_name, group=group)

if __name__ == '__main__':
    app.run(debug=True)
