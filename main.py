# Required Flask Libraries
from flask import Flask, request, render_template, redirect

# Imports the Google Cloud client library
from google.cloud import datastore
client = datastore.Client()
kind = 'Custinfo'

# Start Flask app
app = Flask(__name__)


# Index Page
@app.route('/', methods=['GET'])
def index():
    # Get Customer List
    query = client.query(kind=kind)
    results = list(query.fetch())

    # Render index page
    return render_template('index.html', customers=results)


# CRUD ENDPOINTS
# Create
@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)      # Data from form

        # Put customer record
        complete_key = client.key(kind, data['Name'])
        customer = datastore.Entity(key=complete_key)
        customer.update({
            'Name': data['Name'],
            'address': data['address'],
            'instructions': data['instructions'],
            'address_type': data['address_type']
        })
        client.put(customer)

        # Redirect to customer page
        return redirect("/" + data['Name'])
    else:
        # GET - Render customer creation form
        return render_template('create.html')


# Read
@app.route('/<name>', methods=['GET'])
def read(name):
    # Retrieve Customer Data
    key = client.key(kind, name)
    customer = client.get(key)

    # Render the page
    return render_template('customer.html', name=customer['Name'], address=customer['address'],
                           instructions=customer['instructions'], address_type=customer['address_type'])


# Update
@app.route('/<name>/update', methods=['GET', 'POST'])
def update(name):
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)      # Data from form

        # Update Customer Data
        key = client.key(kind, name)
        customer = client.get(key)
        customer['address'] = data['address']
        customer['instructions'] = data['instructions']
        customer['address_type'] = data['address_type']

        # Redirect to customer page
        return redirect("/" + name)

    else:
        # Get customer data
        key = client.key(kind, name)
        customer = client.get(key)

        # Renders update page with existing data
        return render_template('update.html', name=customer['Name'], address=customer['address'],
                               instructions=customer['instructions'], address_type=customer['address_type'])


# Delete
@app.route('/<name>/delete', methods=['GET'])
def delete(name):
    # Delete Customer Record
    key = client.key(kind, name)
    client.delete(key)

    # Redirect to index page
    return redirect('/')


# Don't worry about this part
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
