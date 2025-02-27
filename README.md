**Weather App**

A Django Weather app that allows users to check real-time weather, and bookmark their favorite cities.
With a CustomUser model for user authentication and profile customization.

**Features**

- Search for weather by city name
- Display current weather details (temperature and condition)
- Save favorite cities for quick access
- Resgistration and editing account
- Weather unit selector (°C/F)
- Users can add profile image
- Responsive design using Bootstrap


**Technologies Used**

- **Python** for backend logic
- **Django** for backend development
- **Bootstrap CDN** for styling
- **OpenWeatherMap API** for fetching weather data
- **SQLite** for database


**Installation**

1- Clone the repository:
  git clone https://github.com/MohammadEslahi/Weather-app
  
2- Navigate to the project directory:
  cd Weather-app
  
3- Create a virtual environment and activate it:
  python -m venv env
  On Windows: env\Scripts\activate
  on Mac: source env/bin/activate

4- Install the required dependencies:
  pip install -r requirements.txt

5- Add your OpenWeatherMap API key
   on Windows: set WeatherAPI-key=your_api_key_here
   on Mac: export WeatherAPI-key=your_api_key_here
  (Sign up at OpenWeatherMap (https://openweathermap.org/) to get your API key.)

6- Run the development server:
  python manage.py runserver

7- Open the app in your browser at http://127.0.0.1:8000/

8- Have fun exploring my Weather app :)