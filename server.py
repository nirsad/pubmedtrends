import os
from flask import Flask, render_template, request, session
import datetime
from datetime import date, datetime
import secrets

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

secret_key = secrets.token_hex(16)
app.secret_key = secret_key

#sort dates from least to most recent

def sort_dates():
	files = os.listdir('static/')
	date_list = []
	for file in files:
		datename = file.replace('.png', '')
		date = datetime.strptime(datename, "%b-%d-%Y")
		date_list.append(date)
	date_list.sort()
	return date_list

#helper function to render image

def return_wordcloud_image(session):
	date = session['sorted_dates'][session['image_counter']]
	img = '/static/' + date.strftime("%b-%d-%Y") + '.png'
	return img

#home page

@app.route("/")
def home():
	session['sorted_dates'] = sort_dates()
	session['image_counter'] = -1
	img = return_wordcloud_image(session)
	return render_template("home.html", img_path = img)

#change rendered wordcloud on page, changes the session image counter

@app.route("/changedate", methods = ['POST', 'GET'])
def changedates():
	img = ''
	if request.method == 'POST':
		output = request.form.to_dict()
		if output['direction'] == 'futuredate':
			if session['image_counter'] == -1:
				img = return_wordcloud_image(session)
			else:
				session['image_counter'] = session['image_counter'] + 1 
				img = return_wordcloud_image(session)
	
		elif output['direction'] == 'pastdate':
			if session['image_counter'] == -len(session['sorted_dates']):
				img = return_wordcloud_image(session)
			else:
				session['image_counter'] = session['image_counter'] - 1 
				img = return_wordcloud_image(session)
	else:
		img = return_wordcloud_image(session)
	return render_template("home.html", img_path = img)

#writing feedback

@app.route("/feedbacksubmitted", methods = ['POST', 'GET'])
def feedback():
	img = return_wordcloud_image(session)
	output = request.form.to_dict()
	if (output['Feedback']):
		with open('./feedback.txt', 'a') as feedbackfile:
			feedbackfile.writelines(output['Feedback'] + '\n')
		return render_template("feedbacksubmit.html", img_path = img)
	else:
		return render_template("home.html", img_path = img)
	
if __name__ == "__main__":
    app.run(debug=False)
