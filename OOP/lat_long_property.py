class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        # used as a placeholder to allow for initial non-private attributes to be called after initialisation,
        # this would still work if removed, but as good practice all attributes should be included in __init__.
        self._latitude = self._longitude = None

        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        print(f"PROPERTY LAT: {self._latitude}")
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90+1):
            raise ValueError(f"{lat_value} not in range(90, -90")
        self._latitude = lat_value
        print(f"SETTER LAT: {self._latitude}")

    @property
    def longitude(self) -> float:
        print(f"PROPERTY LONG: {self._longitude}")
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-180, 180+1):
            raise ValueError(f"{long_value} not in range(180, -180)")
        self._longitude = long_value
        print(f"SETTER LONG: {self._longitude}")


if __name__ == "__main__":
    a = Coordinate(80, 80)
    a.latitude = 10
    a.longitude = 20

    b = Coordinate(10, 10)
    b.latitude = 80
    b.longitude = 200

