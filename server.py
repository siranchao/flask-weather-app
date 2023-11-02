from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def getWeather():
    city = request.args.get("city")
    
    #check user inputs
    if not bool(city.strip()):
        city = "Toronto"
        
    data = get_weather(city)

    if data['cod'] != 200:
        return render_template('not-found.html')

    return render_template(
        'weather.html', 
        title = data['name'], 
        status = data['weather'][0]['description'].capitalize(), 
        temp = f"{data['main']['temp']:.1f}", 
        feels_like = f"{data['main']['feels_like']:.1f}"
    )


if __name__ == '__main__':
    serve(app, host="127.0.0.1", port=5000)