import sympy as sp
import streamlit as st




x, y = sp.symbols('x y')


R = 0.15  
I = 3     


Tn = 0.7 * x + 0.3 * y


Ts = Tn * (1 + R) + I  # Ts = (0.7x + 0.3y)(1.15) + 3


dTs_dx = sp.diff(Ts, x)
dTs_dy = sp.diff(Ts, y)


dTs_dx = sp.simplify(dTs_dx)
dTs_dy = sp.simplify(dTs_dy)


print("Turunan parsial waktu baku terhadap x (waktu kerja mesin):")
print("∂Ts/∂x =", dTs_dx)

print("\nTurunan parsial waktu baku terhadap y (waktu kerja operator):")
print("∂Ts/∂y =", dTs_dy)


x_val = 10
y_val = 5

Ts_val = Ts.subs({x: x_val, y: y_val})
dTs_dx_val = dTs_dx.subs({x: x_val, y: y_val})
dTs_dy_val = dTs_dy.subs({x: x_val, y: y_val})

print(f"\nEvaluasi waktu baku di titik x = {x_val} menit, y = {y_val} menit:")
print(f"Ts = {Ts_val} menit")

print("\nEvaluasi turunan di titik tersebut:")
print(f"∂Ts/∂x = {dTs_dx_val} → dampak perubahan waktu mesin")
print(f"∂Ts/∂y = {dTs_dy_val} → dampak perubahan waktu operator")
