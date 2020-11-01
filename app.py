import requests
import configparser
from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results',methods=['POST'])
def render_results():
    city_name=request.form['City Name']

    api_key = get_api_key()
    data = get_weather_results(city_name, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather= data['weather'][0]['main']
    location = data["name"]
    weather_icon = data['weather'][0]['icon']

    return render_template('results.html',location=location,temp=temp,feels_like=feels_like,weather=weather,weather_icon=weather_icon)
  

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(city_name, api_key):
    api_url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city_name, api_key)
    r = requests.get(api_url)
    return r.json()
print(get_weather_results("Chennai",get_api_key()))

if __name__ == '__main__':
    app.run()

