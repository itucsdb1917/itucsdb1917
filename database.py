from earthquake import earthquake


class Database:
    def __init__(self):
        self.earthquake = {}
        self._last_earthquake_key = 0

    def add_earthquake(self, earthquake):
        self._last_earthquake_key += 1
        self.earthquake[self._last_earthquake_key] = earthquake
        return self._last_earthquake_key

    def delete_earthquake(self, earthquake_key):
        if earthquake_key in self.earthquake:
            del self.earthquake[earthquake_key]

    def get_earthquake(self, earthquake_key):
        earthquake = self.earthquakes.get(earthquake_key)
        if earthquake is None:
            return None
        earthquake_ = earthquake(earthquake.title, year=earthquake.year)
        return earthquake_

    def get_earthquakes(self):
        earthquakes = []
        for earthquake_key, earthquake in self.earthquakes.items():
            earthquake_ = earthquake(earthquake.title, year=earthquake.year)
            earthquakes.append((earthquake_key, earthquake_))
        return earthquakes
