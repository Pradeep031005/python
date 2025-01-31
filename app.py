from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        return {"message": "Data received", "data": data}
    return {"message": "Send a POST request with JSON data"}

if __name__ == '__main__':
    app.run(debug=True)
