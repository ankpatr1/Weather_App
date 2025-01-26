#####                                            Weather App                        #######

This is a Python-based Weather App that fetches real-time weather information from OpenWeatherMap API. The app uses Flask for its backend, SQLite for data storage, and provides a simple and interactive user interface.

####                                              Features                          ########

- Real-time Weather Updates : Users can enter a location and get redirected to OpenWeatherMap's website for detailed weather information.
- Cloud-Themed Interface : The app includes a visually appealing cloud-themed background with interactive buttons.
- CRUD Functionality:
  - Create: Save user weather queries into a database.
  - Read: View stored weather records.
  - Update: Modify existing records in the database.
  - Delete: Remove records from the database.

####                                             Technologies Used                   ########

- Python
- Flask: For the web framework.
- SQLite: For database storage.
- HTML & CSS: For the user interface.
- OpenWeatherMap API: To fetch weather data.

####                                                 Installation                   ##########

1. Clone the repository:
   """  bash """"
   git clone https://github.com/your-repo/weather-app.git
   cd weather-app
   

2. Create a virtual environment and activate it:
   "" bash ""
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   

3. Install the required dependencies:
   """"   bash """""
   pip install -r requirements.txt
   

4. Set up your OpenWeatherMap API key:
   - Replace 'your_openweathermap_api_key' in the 'get_weather_data' function with your actual API key.

5. Run the application:
   """"""""""""""" bash """""""""""""""""""
   python3 app.py
   

6. Open your browser and go to:
   
   http://127.0.0.1:8000/
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8000
* Running on http://192.168.1.180:8000
   

## File Structure

weather-app/
├── app.py                 # Main Flask application
├── weather.db             # SQLite database (created automatically)
├── templates/             # HTML templates folder
│   └── index.html         # Main UI template
├── static/                # (Optional) Static files (CSS, JS, Images)
├── requirements.txt       # Python dependencies
└── README.md              # Documentation


####                                                 How It Works                               ######

1. Home Page:
   - Displays an input form for the user to enter a city or country.
   - Redirects the user to OpenWeatherMap with the query when they click "Get Weather."

2. Database Operations:
   - The app allows storing, viewing, updating, and deleting weather-related queries in the SQLite database.

3. Redirection:
   - When the user submits a location, they are redirected to `https://openweathermap.org/find?q=<location>`.

#####                                                API Integration                            #######

The app integrates with the OpenWeatherMap API to:
- Fetch real-time weather data for a given location.
- Provide detailed information via redirection to OpenWeatherMap.

####                                                 Example Usage                              ######

1. Enter a city (e.g., "New York") in the input box.
2. Click "Get Weather."
3. The app redirects you to OpenWeatherMap's search page with results for "New York."

[OpenWeatherMap](https://openweathermap.org/)
