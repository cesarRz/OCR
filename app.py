# Initialization
from flask import Flask, render_template, request, redirect
from PIL import Image


def openImage(image):
	with Image.open(image) as im:
    		im.show()


# Calling app
app = Flask(__name__)

# Routes
@app.route('/') 
def index():
	return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    s_value = request.form.get('search_value')
    # your code
    return render_template('handle_data.html', search_value=s_value)

@app.route('/upload', methods=['GET','POST']) 
def upload():
	
	if request.method == 'POST':
		if request.files:
			image = request.files["image"]
			print(image)
			# openImage(image)
			
			return redirect(request.url)

	return render_template('upload.html')


# Server Start up
if __name__ == '__main__':
	app.run(debug=True)