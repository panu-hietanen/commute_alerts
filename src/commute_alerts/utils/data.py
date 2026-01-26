import csv

def read_csv(file_path: str) -> dict[str, tuple[float, float]]:
    out = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if i == 0:
                key = 'home'
            else:
                key = f'work{i}'
            out[key] = (float(row['latitude']), float(row['longitude']))
    return out
            