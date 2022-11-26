
class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        #self.x += other.x
        #self.y += other.y
        return Vec2D(self.x + other.x, self.y + other.y)

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


vec1 = Vec2D(2, 5)
vec2 = Vec2D(4, 3)

#vec1.add(vec2)
vec3 = vec1.add(vec2)
vec4 = vec1 + vec2

print(vec3)
print(vec4)
