import os
from pathlib import Path
import googlemaps as gm

from utils.data import read_csv
from utils.start import load_env


def main():
    print("Commute Alerts Service is running...")
    load_env()

    # FORMAT: {'home': (lat, long), 'work1': (lat, long), ...}
    coord_file = os.getenv('COORD_FILE')
    if not coord_file:
        raise ValueError("COORD_FILE environment variable not set. Please check your .env file.")
    
    coords = read_csv(coord_file)
    n_work = len(coords) - 1

    gmaps = gm.Client(key=os.getenv('GMAPS_API_KEY'))

    home_addr = gmaps.reverse_geocode(coords['home'])
    work_addrs = [gmaps.reverse_geocode(coords[f'work{i+1}']) for i in range(n_work)]

    print(home_addr[0]['formatted_address'])
    for i, addr in enumerate(work_addrs):
        print(f"Work {i+1}: {addr[0]['formatted_address']}")

if __name__ == "__main__":
    main()