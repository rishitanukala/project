from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        restaurant_name = request.form['restaurant-name']
        location = request.form['price-range']
        address = request.form['distance']
        cuisine = request.form['cuisine']

        # Process the form data here (e.g., save to database or perform analysis)
        # For now, we'll just print the data to the console
        print(f"Restaurant Name: {restaurant_name}")
        print(f"Location: {location}")
        print(f"Address: {address}")
        print(f"Cuisine: {cuisine}")

        # Redirect to a thank you page or back to the form
        return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)