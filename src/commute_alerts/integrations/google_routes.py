import googlemaps as gm

class GoogleRoutes:
    def __init__(self, api_key: str):
        self.gmaps = gm.Client(key=api_key)

    def get_address(self, coordinates: tuple, num_results: int = 1):
        geocode_result = self.gmaps.reverse_geocode(coordinates)
        if geocode_result:
            if num_results == 1:
                return geocode_result[0]['formatted_address']
            return [geocode_result[i]['formatted_address'] 
                    for i in range(min(num_results, len(geocode_result)))]
        return None

    def get_directions(self, origin: tuple, destination: tuple, mode: str = 'driving'):
        directions = self.gmaps.directions(origin, destination, mode=mode)
        return directions

    def get_travel_time(
            self, 
            origin: tuple, 
            destination: tuple, 
            mode: str = 'driving',
            n_results: int = 1, 
            format: str = 'value'
        ):
        if format not in ['value', 'text']:
            raise ValueError("Format must be either 'value' or 'text'.")
        directions = self.get_directions(origin, destination, mode)
        if directions:
            if n_results == 1:
                return directions[0]['legs'][0]['duration'][format]
            travel_time = [directions[i]['legs'][0]['duration'][format] 
                           for i in range(min(n_results, len(directions)))]
            return travel_time
        return None