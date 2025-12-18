# Spotify_Stats

This is a django based web application that allows the user to view multiple stats regarding their Spotify account via the usage of [Spotify's API](https://developer.spotify.com/documentation/web-api) service.



# Features

- View information about your currently playing track 
- See your top 5 artists & top 5 tracks
- View recently played songs upto a certain limit
- Explore your playlists
- Responsive UI with Django templates
- Usage of ULKIT [front-end framework]

# Tech_Stack

- Python 3
- Django
- HTML
- CSS
- ULKIT
- Spotify API

# Setup_instructions

1. **Clone the repository**

    ```bash
    git clone  https://github.com/Apratimmm/Spotify_Stats.git
    cd Spotify_Stats

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt

4. **Create and regitser your app/project for Spotify**

    - Log into (https://developer.spotify.com/)
    - Create an app
    - Add in redirect URL'S
    - Obtain the Client ID & Client secret

5. **Add your .env file**

    Create a .env file in the root folder and add your Spotify credentials:
    ```bash
    - CLIENT_ID=your_spotify_client_id
    - CLIENT_SECRET=your_spotify_client_secret

7. **Run the server**

    ```bash
    python manage.py runserver
     
    
