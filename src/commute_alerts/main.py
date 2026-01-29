import os
from pathlib import Path
import googlemaps as gm

from utils.data import read_csv
from utils.start import load_env

from integrations.google_routes import GoogleRoutes

def main():
    print("Commute Alerts Service is running...")
    load_env()

    # FORMAT: {'home': (lat, long), 'work1': (lat, long), ...}
    coord_file = os.getenv('COORD_FILE')
    if not coord_file:
        raise ValueError("COORD_FILE environment variable not set. Please check your .env file.")
    
    coords = read_csv(coord_file)
    n_work = len(coords) - 1

    g = GoogleRoutes(api_key=os.getenv('GMAPS_API_KEY'))

    dir = g.get_travel_time(
        origin=coords['home'],
        destination=coords['work1'],
        format='text'
    )

    print(f"Travel time to work1: {dir}")

if __name__ == "__main__":
    main()