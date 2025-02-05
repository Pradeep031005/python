from flask import Flask, jsonify, request

app = Flask(__name__)

menu = {}  # In-memory dictionary to store menu items

# Get all menu items
@app.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)  # Use jsonify to return the menu as JSON

# Add a new item to the menu
@app.route('/api/menu', methods=['POST'])
def add_item():
    data = request.get_json()  # Get the JSON data from the request
    
    name = data.get('name')  # Extract name from the request data
    description = data.get('description')
    price = data.get('price')
    
    if not name or not description or not price:
        return jsonify({'message': 'Missing required fields'}), 400  # Return error if fields are missing
    
    menu[name] = {'description': description, 'price': price}  # Add item to the menu
    return jsonify({'message': f'Item {name} added successfully'}), 201  # Return success message

# Run the app
if __name__ == '__main__':
    app.run(debug=True)