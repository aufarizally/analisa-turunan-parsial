import sympy as sp
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup simbol
x, y = sp.symbols('x y')

# Parameter
R = 0.15  # Allowance
I = 3     # Waktu tambahan tetap

# Waktu normal dan waktu baku
Tn = 0.7 * x + 0.3 * y
Ts = Tn * (1 + R) + I

# Turunan parsial
dTs_dx = sp.simplify(sp.diff(Ts, x))
dTs_dy = sp.simplify(sp.diff(Ts, y))

# Tampilan di Streamlit
st.title("🛠️ Analisis Waktu Baku Produksi dengan Turunan Parsial")
st.markdown("Aplikasi ini membantu Anda memahami bagaimana waktu mesin (x) dan operator (y) mempengaruhi total waktu baku produksi.")

st.subheader("🔹 Rumus Waktu Baku:")
st.latex(f"T_s = ({sp.latex(Tn)}) \\cdot (1 + {R}) + {I}")

st.subheader("🔹 Turunan Parsial:")
st.latex(f"\\frac{{\\partial T_s}}{{\\partial x}} = {sp.latex(dTs_dx)}")
st.latex(f"\\frac{{\\partial T_s}}{{\\partial y}} = {sp.latex(dTs_dy)}")

# Input pengguna
x_val = st.number_input("Masukkan waktu kerja mesin (x) [menit]:", value=10.0, min_value=0.0)
y_val = st.number_input("Masukkan waktu kerja operator (y) [menit]:", value=5.0, min_value=0.0)

# Evaluasi nilai
Ts_val = Ts.subs({x: x_val, y: y_val}).evalf()
dTs_dx_val = dTs_dx.subs({x: x_val, y: y_val}).evalf()
dTs_dy_val = dTs_dy.subs({x: x_val, y: y_val}).evalf()

# Tampilkan hasil evaluasi
st.subheader("📊 Evaluasi di Titik yang Diberikan:")
st.write(f"**x = {x_val} menit, y = {y_val} menit**")
st.success(f"🕒 Waktu Baku (Ts) = **{Ts_val:.2f} menit**")
st.info(f"∂Ts/∂x = **{dTs_dx_val:.2f}** → pengaruh perubahan waktu mesin")
st.info(f"∂Ts/∂y = **{dTs_dy_val:.2f}** → pengaruh perubahan waktu operator")

# ===== Grafik Permukaan Ts(x, y) =====
st.subheader("📈 Visualisasi Fungsi Waktu Baku dalam Grafik 3D")

# Buat grid x dan y
x_range = np.linspace(0, 20, 50)
y_range = np.linspace(0, 20, 50)
X, Y = np.meshgrid(x_range, y_range)

# Hitung Ts untuk setiap titik (x, y)
Ts_func = sp.lambdify((x, y), Ts, 'numpy')
Z = Ts_func(X, Y)

# Plot menggunakan Matplotlib
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)
ax.set_xlabel('Waktu Mesin (x)')
ax.set_ylabel('Waktu Operator (y)')
ax.set_zlabel('Waktu Baku (Ts)')
ax.set_title('Grafik 3D Waktu Baku Produksi')

st.pyplot(fig)
