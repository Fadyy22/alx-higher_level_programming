#!/usr/bin/python3

"""module containing square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the instances"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the rectangle by given arguments,
        whether args or kwargs
        """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        except Exception:
            pass
        for name in kwargs:
            setattr(self, name, kwargs[name])

    def to_dictionary(self):
        """returns the dictionary representation of the instance"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
