import math

# --- INPUT PARAMETERS ---
d1_mm = 100.0  # Main inlet diameter (mm)
u1 = 0.4  # Main inlet velocity (m/s)
t1_c = 20.0  # Main inlet temperature (°C)

d2_mm = 25.0  # Branch inlet diameter (mm)
u2 = 1.2  # Branch inlet velocity (m/s)
t2_c = 40.0  # Branch inlet temperature (°C)

rho = 1000.0  # Fluid density (kg/m^3)

# --- CALCULATIONS ---
# Convert diameters from mm to meters
d1 = d1_mm / 1000.0
d2 = d2_mm / 1000.0

# Cross-sectional Areas (m^2)
a1 = (math.pi / 4.0) * (d1**2)
a2 = (math.pi / 4.0) * (d2**2)

# Mass Flow Rates (kg/s) -> m_dot = rho * A * U
m_dot1 = rho * a1 * u1
m_dot2 = rho * a2 * u2
m_dot_out = m_dot1 + m_dot2

# Mass-weighted Average Temperature (°C and K)
t_out_c = (m_dot1 * t1_c + m_dot2 * t2_c) / m_dot_out
t_out_k = t_out_c + 273.15

# --- PRINT RESULTS ---
print("--- OUTLET TEMPERATURE CALCULATION ---")
print(f"Main Inlet Mass Flow (m1):   {m_dot1:.4f} kg/s")
print(f"Branch Inlet Mass Flow (m2): {m_dot2:.4f} kg/s")
print(f"Total Mass Flow (m_out):    {m_dot_out:.4f} kg/s")
print("-" * 38)
print(f"Calculated Outlet Temp:     {t_out_c:.2f} °C")
print(f"Calculated Outlet Temp:     {t_out_k:.2f} K")