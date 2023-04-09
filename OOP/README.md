## Property and Setters:
The property decorator `@property` is used to make a class attribute into a property. This useful when we need to change
the internal workings of a class / API and still allow for it to be used in the same way by our users.

e.g. we've created a circle class that has a radius attribute, one of our clients asks for radius to not be exposed, 
instead diameter is exposed.

### Details
Please refer to `lat_long_property.py` for this section.

The example below looks at the situation where if we want to set or define a attribute it must exist inside a range of
values, otherwise the coordinate doesn't make sense.

```python
# lat_long_property.py

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

# OUTPUT
# SETTER LAT: 80
# SETTER LONG: 80
# SETTER LAT: 10
# SETTER LONG: 20
# SETTER LAT: 10
# SETTER LONG: 10
# SETTER LAT: 80
# ValueError: 200 not in range(180, -180)
```

Above we use private attributes as placeholders for our property and setter as well a public attributes, this isn't 
strictly needed, the only functionality it adds is that if we just instantiated a `Coordinate` object the attributes 
would be callable.

In the constructor the latitude and longitude `setters` are called. This checks to see if the values are in a acceptable
range, if so the private variables are set to the value. If we set the public attribute to this it would cause an 
infinite recursion error as the setter would be called again etc etc. Interestingly if we print `a.__dict__` we will
only see the private attributes this is because when we call `self.latitude` or `self.longitude` we're using the 
property decorator to set it to `self._latitude` or `self._longitude`. Conversely if we print `self.longitude` it will 
call the property decorator and return the private attribute.

We can then set attributes to be equal to new values, this will invoke the `setter` methods defined above.