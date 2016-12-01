# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():
    ### MAKE THE THREE PARAMETERS FOR THE SIDE LENGTHS ###
    def __init__(self,a_side,b_side,c_side):
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side
    ### SURFACE ###
    def getSurface(self):
        return self.a_side*self.b_side*2 + self.a_side*self.c_side*2 + self.b_side*self.c_side*2
    ### VOLUME ###
    def getVolume(self):
        return self.a_side*self.b_side*self.c_side


x =Cuboid(4,5,6)
x.getSurface()
x.getVolume()
