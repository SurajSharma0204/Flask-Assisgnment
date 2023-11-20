from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('product_info.html')

@app.route('/product')
def product_info():
    # Get the 'product' parameter from the URL
    product_name = request.args.get('product')

    # Dummy product data (replace with your actual data)
    products = {
        'laptop': {'name': 'Laptop', 'price': '$999'},
        'phone': {'name': 'Phone', 'price': '$699'},
        'tablet': {'name': 'Tablet', 'price': '$399'},
    }

    # Get product information or display a default message
    product_info = products.get(product_name, {'name': 'Unknown', 'price': 'N/A'})

    return render_template('product_info.html', product_info=product_info)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050)

