import math 

def shaft_twist(t, l, j, g=79.3e9):
    """
    Calculate the angle of twist of a shaft subjected to torque.

    Parameters:
    t (float): Torque applied to the shaft (in N*m).
    l (float): Length of the shaft (in meters).
    j (float): Polar moment of inertia of the shaft cross-section (in m^4).
    g (float): Shear modulus of the material (in Pa). Default is 79.3 GPa for steel.

    Returns:
    float: Angle of twist in radians.
    """
    return (t * l) / (j * g)

#steel 
steeltwist = shaft_twist(500,1.5,2*10**-7)
print(f"steel_twist: {math.degrees(steeltwist):.2f} degrees")

