import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import random

# Crear directorio de imágenes
Path("images").mkdir(exist_ok=True)

# Configuración de estilo
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# --- 1. Gráfico de Ventas Mensuales (Sales Trend) ---
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="M")
sales = np.random.normal(loc=50000, scale=10000, size=len(dates)) + np.linspace(0, 30000, len(dates))
df_sales = pd.DataFrame({"Date": dates, "Sales": sales})

plt.figure()
sns.lineplot(data=df_sales, x="Date", y="Sales", marker="o", linewidth=2.5, color="#2ecc71")
plt.title("Monthly Sales Growth (2023)", fontsize=16, fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("images/monthly_sales_growth.png")
plt.close()

# --- 2. Gráfico de Churn por Segmento (Churn Analysis) ---
segments = ["Bronze", "Silver", "Gold", "Platinum"]
churn_rates = [0.25, 0.15, 0.05, 0.02]
colors = sns.color_palette("Reds_r", len(segments))

plt.figure()
sns.barplot(x=segments, y=churn_rates, palette=colors)
plt.title("Customer Churn Rate by Segment", fontsize=16, fontweight='bold')
plt.xlabel("Customer Segment")
plt.ylabel("Churn Rate")
plt.ylim(0, 0.3)
for i, v in enumerate(churn_rates):
    plt.text(i, v + 0.01, f"{v:.0%}", ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig("images/churn_by_segment.png")
plt.close()

# --- 3. Heatmap de Correlación (Business Factors) ---
data_corr = pd.DataFrame(np.random.rand(5, 5), columns=["Price", "Discount", "Sales", "Satisfaction", "Retention"])
corr_matrix = data_corr.corr()

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title("Feature Correlation Matrix", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig("images/correlation_matrix.png")
plt.close()

# --- 4. Comparativa de Rendimiento (Performance Rust vs Python) ---
labels = ['Python (Pandas)', 'Rust (Polars)']
times = [30.5, 0.6]  # Segundos

plt.figure()
bars = plt.bar(labels, times, color=['#3498db', '#e74c3c'])
plt.title("ETL Processing Time Comparison (50M Rows)", fontsize=16, fontweight='bold')
plt.ylabel("Time (seconds)")
plt.yscale("log")
plt.bar_label(bars, fmt='%.1f s', padding=3)
plt.tight_layout()
plt.savefig("images/performance_benchmark.png")
plt.close()

# --- 5. Distribución de LTV (Customer Lifetime Value) ---
ltv_data = np.random.lognormal(mean=5, sigma=0.8, size=1000)

plt.figure()
sns.histplot(ltv_data, bins=30, kde=True, color="#9b59b6")
plt.title("Distribution of Customer Lifetime Value (LTV)", fontsize=16, fontweight='bold')
plt.xlabel("LTV ($)")
plt.xlim(0, 1000)
plt.tight_layout()
plt.savefig("images/ltv_distribution.png")
plt.close()

print("✅ 5 Gráficos generados exitosamente en la carpeta 'images/'")
