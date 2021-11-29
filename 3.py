# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:04:17 2021

@author: lenovo
"""
import matplotlib 
import matplotlib.pyplot as plt

import requests
import json

import os
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

from IPython.core.display import HTML, display

d = requests.get('http://opendata.iprpraha.cz/CUR/OVZ/OVZ_Klima_ZnecOvzdusi_p/WGS_84/OVZ_Klima_ZnecOvzdusi_p.json').json()
print(d['features'][0]['properties'])

xml = '''
<?xml version="1.0" encoding="utf-8"?>
<ies_data>
    <courses>
        <course id="JEM005" ects="6" name="Advanced Econometrics">
           <teacher-id>3421</teacher-id>
           <teacher-id>1234</teacher-id>
        </course>
        <course id="JEM207" ects="5" name="Data Processing in Python">
            <teacher-id>3421</teacher-id>
        </course>
            <course id="JEM116" ects="6" name="Applied Econometrics I.">
            <teacher-id>1234</teacher-id>
        </course>
        <course id="JEM059" ects="6" name="Quantitative Finance I.">
            <teacher-id>1234</teacher-id>
            <teacher-id>5678</teacher-id>
        </course>
        <course id="JEM061" ects="6" name="Quantitative Finance II.">
            <teacher-id>1234</teacher-id>
            <teacher-id>5678</teacher-id>
        </course>
    </courses>
    <teachers>
        <teacher teacher-id="3421">
            <name>Martin Hronec</name>
        </teacher>
        <teacher teacher-id="1234">
            <name>Jozef Baruník</name>
        </teacher>
        <teacher teacher-id="5678">
            <name>Lukáš Vácha</name>
        </teacher>
    </teachers>
</ies_data>
'''

soup = BeautifulSoup(xml, features="lxml")
jem059 = soup.find('course',{'id':'JEM059'})
print(jem059)
jem059.findAll('teacher-id')
print(jem059['ects'])
print(jem059['name'])
print(soup.findAll('teacher-id'))
print(jem059.findNext('course'))
teacher_ids = [int(t.text) for t in soup.findAll('teacher-id')]
print(teacher_ids)
course = soup.find('course')
d = {
    'id':course['id'],
    'name':course['name'],
    'ects':course['ects'],
    'teachers':[int(t.text) for t in course.findAll('teacher-id')]
}

print(d)
e = pd.DataFrame(d)
print(e)

l = [{
    'id':course['id'],
    'name':course['name'],
    'ects':course['ects'],
    'teachers':[int(t.text) for t in course.findAll('teacher-id')]
} for course in soup.findAll('course')]

niki = pd.DataFrame(l)
print(niki)

html = '''
<html>
    <head>
        <title>Sample page</title>
    <script>
        function click_button() {
            alert('Button clicked!')
        }
    </script>
    <style>
        #content div {
            color:black;
        }
        .firstRow {
            background-color:#ddd;
        }

        .normalRow {
            background-color:white;
        }
    </style>
    </head>
    
    <body>
        <div id="header">
            My page header
        </div>
        <div id="table_container">
            <table>
                <tr class="firstRow">
                    <td>name</td>
                    <td>number</td>
                </tr>
                <tr class="normalRow">
                    <td>B</td>
                    <td>2</td>
                </tr>
                <tr class="normalRow">
                    <td>C</td>
                    <td>3</td>
                </tr>
            </table>
        </div>
        <div id="button_container">
            <button id="btn" onclick="click_button()">Click Me!</button>
        </div
    </body>
</html>
'''
display(HTML(html))
soup = BeautifulSoup(html,'lxml')
response = requests.get('https://en.wikipedia.org/wiki/Charles_University')
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('div',{'id':'mw-content-text'}) #  #mw-content-text > div > p:nth-child(10)texts)
article = ' '.join([p.text for p in div.find_all('p')])
print(article)

r = requests.get('https://cs.wikipedia.org/wiki/Institut_ekonomick%C3%BDch_studi%C3%AD_Fakulty_soci%C3%A1ln%C3%ADch_v%C4%9Bd_Univerzity_Karlovy')
print(r.text)

niki = requests.get("https://en.wikipedia.org/wiki/Agatha_Christie")
n_soup = BeautifulSoup(niki.text, 'lxml')
n_div = n_soup.find('div',{'class':'mw-parser-output'})
print(n_div)
n_article = ' '.join([p.text for p in n_div.find_all('p')])
print(n_article)










