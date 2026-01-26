from pathlib import Path

from utils.data import read_csv

COORD_FILE = Path('data\latlong.csv')

def main():
    print("Commute Alerts Service is running...")

    # FORMAT: {'home': (lat, long), 'work1': (lat, long), ...}
    data = read_csv(COORD_FILE)
    n_work = len(data) - 1

    print(data)

if __name__ == "__main__":
    main()