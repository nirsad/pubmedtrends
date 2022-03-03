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
import subprocess
from bs4 import BeautifulSoup
import csv
import requests
import time
import pymongo
import datetime
from datetime import date
from pymongo import MongoClient

from datetime import datetime, timedelta, date
import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

#setting up functions to call python scripts

def getTitles():
    exec(open(os.path.join(os.getcwd(), '..', 'getTitles.py')).read())
    return None

def dataCleaning():
    exec(open(os.path.join(os.getcwd(), '..', 'dataCleaning.py')).read())
    return None

def generateWordcloud():
    exec(open(os.path.join(os.getcwd(), '..', 'generateCloud.py')).read())
    return None

def LoadToMongoDB():
    exec(open(os.path.join(os.getcwd(), '..', 'mongodb', 'mongoingest.py')).read())
    return None

#writing DAG arguments

with DAG(
    'pubmedmaindag',

    default_args={
	'owner':'airflow',
        'depends_on_past': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=60),
    },

    description='PubMed Data Pipeline',
    schedule_interval=timedelta(days=7),
    start_date=datetime(2022, 2, 25),
    catchup=False

) as dag:

    ScrapeTitles = PythonOperator(
        task_id='ScrapeTitles',
        python_callable= getTitles
    )

    CleanData = PythonOperator(
        task_id='CleanData',
        python_callable= dataCleaning
    )
    
    GenerateCloud = PythonOperator(
        task_id='GenerateCloud',
        python_callable= generateWordcloud
    )

    LoadtoDB = PythonOperator(
        task_id='LoadtoDB',
        python_callable= LoadToMongoDB
    )

#Setting up task dependencies

    ScrapeTitles >> CleanData >> GenerateCloud >> LoadtoDB
