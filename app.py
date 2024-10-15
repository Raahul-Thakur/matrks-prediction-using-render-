from flask import Flask, render_template, request
import marks as m

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    mk = None
    if request.method == 'POST':
        try:
            # Convert the input from the form to a float
            hrs = float(request.form['hrs'])
            # Get the predicted marks
            marks_pred = m.marks_prediction(hrs)
            mk = marks_pred
        except ValueError:
            print("Invalid input. Please enter a valid number of hours.")
    
    return render_template('index.html', my_marks=mk)

if __name__ == '__main__':
    app.run(debug=True)
