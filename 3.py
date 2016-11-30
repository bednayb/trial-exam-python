# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def getSurface(self):
        return self.a*self.b*2 + self.a*self.c*2 + self.b*self.c*2

    def getVolume(self):
        return self.a*self.b*self.c

x =Cuboid(4,5,6)
x.getSurface()
x.getVolume()
