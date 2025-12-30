import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.patches as patches

# Configuración: Estilo "Streamlit Dark Theme"
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

# Crear la figura simulando una interfaz de Dashboard
fig = plt.figure(figsize=(12, 7), facecolor='#0E1117') # Color de fondo típico de Streamlit Dark
gs = fig.add_gridspec(2, 3, width_ratios=[1, 2, 2])

# --- Elementos de UI (Estáticos) ---
# 1. Sidebar (Simulada con un eje vacío o rectángulo)
ax_sidebar = fig.add_subplot(gs[:, 0])
ax_sidebar.set_facecolor('#262730') # Sidebar color
ax_sidebar.set_xticks([])
ax_sidebar.set_yticks([])
ax_sidebar.text(0.1, 0.95, "📊 Portfolio Demo", fontsize=14, fontweight='bold', color='white')
ax_sidebar.text(0.1, 0.85, "Navigation:", fontsize=12, color='#FAFAFA')
ax_sidebar.text(0.1, 0.80, "🔘 Home", fontsize=10, color='#FF4B4B') # Streamlit Red highlight
ax_sidebar.text(0.1, 0.75, "⚪ Sales Analysis", fontsize=10, color='gray')
ax_sidebar.text(0.1, 0.70, "⚪ Tech Stack", fontsize=10, color='gray')
ax_sidebar.text(0.1, 0.10, "Status: ● Online", fontsize=10, color='#00FF00')
for spine in ax_sidebar.spines.values():
    spine.set_visible(False)

# 2. Header (Texto en la figura)
fig.text(0.35, 0.92, "Real-Time Sales Intelligence Dashboard", fontsize=20, fontweight='bold', color='white')
fig.text(0.35, 0.88, "Live data stream simulation • 2023-2024 Performance", fontsize=12, color='#A0A0A0')

# --- Gráficos Animados ---

# KPI Card (Texto dinámico)
ax_kpi = fig.add_subplot(gs[0, 1])
ax_kpi.set_facecolor('#0E1117')
ax_kpi.axis('off')
kpi_text = ax_kpi.text(0.5, 0.5, "$0", fontsize=40, fontweight='bold', color='#00CC96', ha='center', va='center')
ax_kpi.text(0.5, 0.2, "Total Revenue (Live)", fontsize=14, color='gray', ha='center')

# KPI Card 2
ax_kpi2 = fig.add_subplot(gs[0, 2])
ax_kpi2.set_facecolor('#0E1117')
ax_kpi2.axis('off')
orders_text = ax_kpi2.text(0.5, 0.5, "0", fontsize=40, fontweight='bold', color='#636EFA', ha='center', va='center')
ax_kpi2.text(0.5, 0.2, "Active Orders", fontsize=14, color='gray', ha='center')

# Gráfico de Línea (Sales Trend)
ax_line = fig.add_subplot(gs[1, 1:])
ax_line.set_facecolor('#0E1117')
ax_line.set_title("Revenue Trend (Last 30 Days)", fontsize=12, color='white', loc='left')
ax_line.grid(True, color='#404040', linestyle='--', linewidth=0.5)
ax_line.spines['bottom'].set_color('#404040')
ax_line.spines['left'].set_color('#404040')
ax_line.spines['top'].set_visible(False)
ax_line.spines['right'].set_visible(False)

# Datos iniciales
x_data = np.arange(50)
y_data = np.linspace(1000, 3000, 50) + np.random.normal(0, 200, 50)
line, = ax_line.plot(x_data, y_data, color='#FF4B4B', linewidth=2.5, marker='o', markersize=4, markerfacecolor='white')
fill = ax_line.fill_between(x_data, y_data, alpha=0.2, color='#FF4B4B')

# Función de animación
def update(frame):
    global fill
    # Simular nuevos datos (Shift a la izquierda)
    new_val = y_data[-1] + np.random.randint(-400, 500)
    if new_val < 500: new_val = 500
    
    # Shift arrays
    y_data[:-1] = y_data[1:]
    y_data[-1] = new_val
    
    # Actualizar línea
    line.set_ydata(y_data)
    
    # Actualizar área bajo la curva (borrar y redibujar es costoso, pero simple para GIF corto)
    fill.remove()
    fill = ax_line.fill_between(x_data, y_data, 0, alpha=0.2, color='#FF4B4B')
    
    # Actualizar KPIs
    current_total = int(np.sum(y_data) * (1 + frame/1000)) # Simular acumulado creciente
    kpi_text.set_text(f"${current_total:,.0f}")
    
    current_orders = int(y_data[-1] / 50)
    orders_text.set_text(f"{current_orders}")
    
    return line, kpi_text, orders_text

# Generar Animación
ani = animation.FuncAnimation(fig, update, frames=60, interval=80, blit=False)

print("Generando GIF High-Fidelity (esto tomará unos segundos)...")
ani.save('images/dashboard_preview.gif', writer='pillow', fps=15)
print("GIF generado en images/dashboard_preview.gif")
