import math

angle_F=int(input("enter the angle near F"))
angle_Z=int(input("enter the angle with rod"))
load=input("enter weight of load(positive value only!!)")
h_A=input("enter distanc ef A from ground(in mm)")
x_AB=input("enter total distance(in mm)")
x_GB=input("enter distance from G to B(in mm)")

def number(v):
    try:
        float(v)
        return True
    except:
        return False
if number(load) and number(h_A) and number(x_AB) and number(x_GB):
    load=float(load)
    h_A=float(h_A)
    x_AB=float(x_AB)
    x_GB=float(x_GB)
    angle=angle_F+angle_Z
    numerator=load*9.81*x_GB
    denominator=(math.sin(math.radians(angle))*x_AB)-(math.cos(math.radians(angle))*h_A)
    F=numerator/denominator
    print("force required= ",F)
else:
    print(f"Force required= ({load}9.81{x_GB})/(sin({angle_F}+{angle_Z}){x_AB}-cos({angle_F}+{angle_Z}){h_A}")