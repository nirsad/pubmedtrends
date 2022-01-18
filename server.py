import multidict as multidict
import numpy as np
import os
import lxml
import re
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import csv
import requests
import time

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

#home page

@app.route("/")
def home():
    return render_template("home.html")

#generating an updated wordcloud

@app.route("/generateWordcloud", methods = ['POST', 'GET'])
def wordcloud():
	exec(open("getTitles.py").read())
	exec(open("dataCleaning.py").read())
	exec(open("generateCloud.py").read())
	return render_template("home.html")

#writing feedback

@app.route("/feedbacksubmitted", methods = ['POST', 'GET'])
def feedback():
	output = request.form.to_dict()
	if (output['Feedback']):
		with open('./feedback.txt', 'a') as feedbackfile:
			print(output['Feedback'])
			feedbackfile.writelines(output['Feedback'] + '\n')
		return render_template("feedbacksubmit.html")
	else:
		return render_template("home.html")
	
if __name__ == "__main__":
    app.run()
