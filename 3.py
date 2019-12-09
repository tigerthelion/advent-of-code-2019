class Translation:
    def __init__(self, move_str):
        
        self._directions = {
            "L": self.left,
            "R": self.right,
            "U": self.up,
            "D": self.down
        }

    
        assert move_str[0] in list(self._directions.keys())

        self._direction = move_str[0]
        self._magnitude = move_str[1:]

        self._directions[self._direction]()

    def left(self):
        return -1 * self._magnitude, 0
    
    def right(self):
        return self._magnitude, 0
    
    def up(self):
        return 0, self._magnitude
    
    def down(self):
        return 0, -1 * self._magnitude

    def __str__(self):
        x, y = self._directions[self._direction]()
        return f"({x} , {y})"

print(Translation('U2'))
print(Translation("D17"))
print(Translation("L3"))
print(Translation("R45"))