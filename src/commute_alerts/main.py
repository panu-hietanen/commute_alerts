import os
from pathlib import Path
import googlemaps as gm

from utils.data import read_csv
from utils.start import load_env


def main():
    load_env()
    print("Commute Alerts Service is running...")

    # FORMAT: {'home': (lat, long), 'work1': (lat, long), ...}
    coord_file = os.getenv('COORD_FILE')
    if not coord_file:
        raise ValueError("COORD_FILE environment variable not set. Please check your .env file.")
    
    coords = read_csv(coord_file)
    n_work = len(coords) - 1

    gmaps = gm.Client(key=os.getenv('GMAPS_API_KEY'))

    print(coords)

if __name__ == "__main__":
    main()