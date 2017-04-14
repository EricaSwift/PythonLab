

pi = 3.141
import circle

def area(radius):
    """This method computes the area of a circle. Input radius parameter."""
    return pi*(radius**2)

def circumference(radius):
    """This method computes the circumference. Input radiud parameter."""
    return 2*pi*radius 

def sphereSurface(radius):
    """This method computes a sphere's surface. Input the radius."""
    return 4.0*area(radius)

def sphereVolume(radius):
    """This method computes a sphere's volume. Input the radius."""
    return (4.0/3.0)*pi*(radius**3)


