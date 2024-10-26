from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return render_template('result.html', result="Error: Division by zero is not allowed.")
            result = num1 / num2
        else:
            return render_template('result.html', result="Invalid operation.")
        
        return render_template('result.html', result=f"The result is: {result}")

    except ValueError:
        return render_template('result.html', result="Invalid input. Please enter numbers only.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
