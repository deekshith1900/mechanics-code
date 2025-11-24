'''#UNIT 1
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
    print(f"Force required= ({load}9.81{x_GB})/(sin({angle_F}+{angle_Z}){x_AB}-cos({angle_F}+{angle_Z}){h_A}")'''

#unit 2
compression_force = input("Enter the compression force (N): ")
distance_a= input("Enter the distance of A (mm): ")
distance_b = input("Enter the distance of B (mm): ")

def is_number(value):
    try:
        float (value)
        return True
    except:
        return False

if is_number(compression_force) and is_number(distance_a) and is_number(distance_b):
    CF = float(compression_force)
    da = float(distance_a)
    db = float(distance_b)
    total_distance = da + db
    force_A = (CF * total_distance) / db
    print("Force in screw A =", force_A, "N")
else:
    print(f"Force in screw A = ({compression_force} * ({distance_a} + {distance_b})) / {distance_b}")

#unit 3
'''
a=input("enter the load(in KN/m)")
b=input("enter the distance from A(in m)")
c=input("enter the distance from B(in m)")
d=input("enter the distance where it should be found (in m)")
def number(v):
    try:
        float(v)
        return True
    except:
        return False
if number(a) and number(b) and number(c) and number(d):
    a=float(a)
    b=float(b)
    c=float(c)
    d=float(d)
    if a<0:
        print("give positive value")
    else:

        W=0.5*b*a
        xdis=2/3*b
        RB=(W*xdis)/6
        VA=W-RB
        x=(a*d)/b
        d=xdis-(2/3*xdis)
        BM=(VA*xdis)-(x*d)  
        SF=VA-x
        print("Bending moment: " ,BM)
        print("Shear Force: ",SF)
else:
    print(f"Shear Force= ((18-2{b})({b}*{a}))/36")
    print(f"Bending Moment= ({b}(18-2{b})/36)*(a+2/3)-2{a}{b}{d}/9")'''
