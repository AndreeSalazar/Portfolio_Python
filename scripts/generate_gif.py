import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import seaborn as sns

# Configurar el estilo
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle("Real-Time Sales & Analytics Dashboard (Simulated)", fontsize=16, color='white', fontweight='bold')

# Datos iniciales
x = np.linspace(0, 10, 100)
line, = ax1.plot(x, np.sin(x), color='#00ff41', linewidth=2)
ax1.set_title("Live Revenue Trend", fontsize=12)
ax1.set_ylim(-2000, 12000)
ax1.grid(True, alpha=0.2)

# Bar chart inicial
categories = ['North', 'South', 'East', 'West']
values = [5000, 7000, 3000, 8000]
bars = ax2.bar(categories, values, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
ax2.set_title("Sales by Region", fontsize=12)
ax2.set_ylim(0, 15000)

# Función de animación
def update(num):
    # Update Line
    new_y = np.sin(x + num / 5.0) * 2000 + 5000 + np.random.normal(0, 500, 100)
    line.set_ydata(new_y)
    
    # Update Bars
    for bar in bars:
        bar.set_height(bar.get_height() + np.random.randint(-500, 500))
    
    return line, *bars

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=False)

# Guardar como GIF
print("Generando GIF (esto puede tardar unos segundos)...")
ani.save('images/dashboard_preview.gif', writer='pillow', fps=15)
print("GIF generado exitosamente en images/dashboard_preview.gif")
