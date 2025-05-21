import sympy as sp
import streamlit as st

# Simbol
x, y = sp.symbols('x y')

# Parameter waktu
R = 0.15  # Allowance
I = 3     # Waktu tambahan tetap

# Waktu normal dan waktu baku
Tn = 0.7 * x + 0.3 * y
Ts = Tn * (1 + R) + I

# Turunan parsial
dTs_dx = sp.simplify(sp.diff(Ts, x))
dTs_dy = sp.simplify(sp.diff(Ts, y))

# Tampilan di Streamlit
st.title("Analisis Turunan Parsial Waktu Baku Produksi")

st.subheader("Fungsi Waktu Baku:")
st.latex(f"T_s = ({sp.latex(Tn)}) \\cdot (1 + {R}) + {I}")

st.subheader("Turunan Parsial:")
st.latex(f"\\frac{{\\partial T_s}}{{\\partial x}} = {sp.latex(dTs_dx)}")
st.latex(f"\\frac{{\\partial T_s}}{{\\partial y}} = {sp.latex(dTs_dy)}")

# Input pengguna
x_val = st.number_input("Masukkan waktu kerja mesin (x) [menit]:", value=10)
y_val = st.number_input("Masukkan waktu kerja operator (y) [menit]:", value=5)

# Evaluasi
Ts_val = Ts.subs({x: x_val, y: y_val})
dTs_dx_val = dTs_dx.subs({x: x_val, y: y_val})
dTs_dy_val = dTs_dy.subs({x: x_val, y: y_val})

# Tampilkan hasil evaluasi
st.subheader("Evaluasi di Titik:")
st.write(f"x = {x_val} menit, y = {y_val} menit")
st.write(f"Waktu Baku (Ts) = {Ts_val} menit")

st.subheader("Evaluasi Turunan Parsial di Titik Tersebut:")
st.write(f"∂Ts/∂x = {dTs_dx_val} → dampak perubahan waktu mesin")
st.write(f"∂Ts/∂y = {dTs_dy_val} → dampak perubahan waktu operator")
