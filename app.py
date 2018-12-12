from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/superman")
def superman():
    return render_template('superman.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/recipesideas")
def recipesideas():
    return render_template('recipesideas.html')

@app.route("/instagramsuggestions")
def instagramsuggestions():
    return render_template('instagramsuggestions.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/bbcfood", methods=['GET', 'POST'])
def bbcfood():
	return render_template('bbcfood.html')


if __name__ == '__main__':
    app.run(debug=True)

