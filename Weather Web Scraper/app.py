import os
import requests
from bs4 import BeautifulSoup

def get_weather_data():
    # Unset the proxy environment variables
    os.environ['http_proxy'] = ''
    os.environ['https_proxy'] = ''

    url = "https://www.metoffice.gov.uk/weather/forecast/gcwghuyms"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the necessary weather data
        temperature = soup.find('span', class_='temperate-cell-value').text.strip()
        description = soup.find('div', class_='day-label').text.strip()

        return {
            "temperature": temperature,
            "description": description
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Flask route
@app.route("/")
def index():
    weather_data = get_weather_data()
    return render_template("index.html", weather=weather_data)
