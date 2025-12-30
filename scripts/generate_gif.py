import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Configurar el estilo
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 4))

# Datos simulados
x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x), color='#00ff41', linewidth=3)
ax.set_title("Real-Time Sales Monitor (Dashboard Simulation)", fontsize=14, color='white', fontweight='bold')
ax.set_xlabel("Time (s)", color='gray')
ax.set_ylabel("Revenue ($)", color='gray')
ax.grid(True, alpha=0.3)

# Función de animación
def update(num, x, line):
    line.set_ydata(np.sin(x + num / 10.0) * 1000 + 5000 + np.random.normal(0, 200, 100))
    return line,

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, line],
                              interval=50, blit=True)

# Guardar como GIF
ani.save('images/dashboard_preview.gif', writer='pillow', fps=20)
print("GIF generado en images/dashboard_preview.gif")
