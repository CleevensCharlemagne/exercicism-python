class SpaceAge:
    earthYears = 31557600
    mercuryYears = 0.2408467 * earthYears
    venusYears = 0.61519726 * earthYears
    marsYears = 1.8808158 * earthYears
    jupiterYears = 11.862615 * earthYears
    saturnYears = 29.447498 * earthYears
    uranusYears = 84.016846 * earthYears
    neptuneYears = 164.79132 * earthYears


    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / self.earthYears, 2)

    def on_mercury(self):
        return round(self.seconds / self.mercuryYears, 2)

    def on_venus(self):
        return round(self.seconds / self.venusYears, 2)

    def on_mars(self):
        return round(self.seconds / self.marsYears, 2)

    def on_jupiter(self):
        return round(self.seconds / self.jupiterYears, 2)

    def on_saturn(self):
        return round(self.seconds / self.saturnYears, 2)

    def on_uranus(self):
        return round(self.seconds / self.uranusYears, 2)

    def on_neptune(self):
        return round(self.seconds / self.neptuneYears, 2)