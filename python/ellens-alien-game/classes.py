"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    x_coordinate = 0
    y_coordinate = 0
    health = 3

    def __init__(self, x_coordinate, y_coordinate):
        Alien.total_aliens_created += 1

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
    
    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
    
    def collision_detection(self, obj):
        pass
        # return self.x_coordinate == Alien.x_coordinate and self.y_coordinate == Alien.y_coordinate


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(aliens):
    return [Alien(*alien) for alien in aliens]