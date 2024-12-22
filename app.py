from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/is_prime', methods=['GET'])
def check_prime():
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({"error": "Please provide a number"}), 400
    result = is_prime(number)
    return jsonify({"number": number, "is_prime": result})

@app.route('/')
def index():
    return '''
        <!doctype html>
        <html>
            <head><title>Prime Checker</title></head>
            <body>
                <h1>Check if a number is prime</h1>
                <form action="/is_prime" method="get">
                    <label for="number">Enter a number:</label>
                    <input type="text" id="number" name="number" required>
                    <input type="submit" value="Check">
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

# Example:
# curl http://localhost:5000/is_prime?number=7
# {"number": 7, "is_prime": true}
