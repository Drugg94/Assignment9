# Compute the volume of a sphere with a radius of 5. 
# The formula for a sphere is 4⁄3πr3. Note: The answer is around 500, not 400 (in case you are using Python 2). 
# Write a function sphere_volume that returns the volume of a sphere when given radius r as a parameter.
# Then write a main program that calls sphere_volume to print the volume of a sphere with a radius of 5. 
# Should the print statement go in the sphere_volume or the main program?


# Revision 1 BEGIN/ 24Mar22
## Begin Derek Ruggirello here (24Mar22)

def sphere_volume(radius):
    volume = ((4/3)*3.14159265359*(radius**3))
    print("The volume of radius:", radius, "is", volume)
    return volume

sphere_volume(5)


# Revision 1 FINAL 24Mar22
## End Derek Ruggirello here
# HALF-LIFE/Ron Bass/John Richards Sr./After-Burner Elite #
