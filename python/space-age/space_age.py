# In earth years
ORBITAL_PERIODS = {
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "earth": 1.0, #365.25 earth days, or 31557600 seconds
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}

EARTH_YEARS_PER_SECOND = 0.000000031688088

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    
    def calculate_years(self, planet):
        if planet in ORBITAL_PERIODS:
            return round((self.seconds * EARTH_YEARS_PER_SECOND) / ORBITAL_PERIODS[planet], 2)
        return 0
    
    def on_mercury(self):
        return self.calculate_years('mercury')

    def on_venus(self):
        return self.calculate_years('venus')

    def on_earth(self):
        return self.calculate_years('earth')

    def on_mars(self):
        return self.calculate_years('mars')

    def on_jupiter(self):
        return self.calculate_years('jupiter')

    def on_saturn(self):
        return self.calculate_years('saturn')

    def on_uranus(self):
        return self.calculate_years('uranus')

    def on_neptune(self):
        return self.calculate_years('neptune')
