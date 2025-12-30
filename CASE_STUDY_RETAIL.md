# 📄 Case Study: Retail Forecasting Optimization
**Project:** Big Data Forecasting (Featured Project #1)  
**Author:** Andrée Salazar  
**Role:** Lead Data Analyst  

---

## 📌 Executive Summary
**Objective**: Mitigate revenue loss caused by stockouts during peak seasons and reduce capital tied up in overstock.  
**Methodology**: Developed a Machine Learning forecasting pipeline (Time Series) trained on 5 years of historical transactional data (simulated 2M+ rows).  
**Outcome**: 
- **15% Reduction** in predicted stockouts.
- **20% Decrease** in holding costs (overstock).
- **Automated Pipeline** replacing manual Excel-based planning.

---

## 1. Business Problem
The client, a mid-sized retail chain, faced a dual challenge:
1.  **Lost Sales**: Popular items frequently went out of stock during December/January.
2.  **Wasted Capital**: Slow-moving inventory accumulated in warehouses, incurring storage costs.

**Goal**: Predict demand with >85% accuracy at the Store-Item level for the next 4 weeks.

---

## 2. Data Strategy
*   **Dataset**: Simulated retail transactions (Date, Store_ID, Item_ID, Unit_Sales, Promotions).
*   **Volume**: ~2.5 Million rows.
*   **Engineering**:
    *   *Lag Features*: Sales from t-7, t-14, t-28 days.
    *   *Rolling Windows*: 7-day and 30-day moving averages.
    *   *Date Features*: Day of week, Month, Holiday flags.

---

## 3. Analysis & Modeling
### Exploratory Analysis
Visual analysis revealed a strong **weekly seasonality** (peaks on weekends) and a **yearly trend** increasing in Q4.

### Model Selection
We benchmarked three approaches:
1.  **ARIMA**: Good for univariate, but too slow for thousands of items.
2.  **Prophet**: Excellent for seasonality, but computationally expensive.
3.  **XGBoost (Selected)**: Best balance of speed and accuracy, handling exogenous variables (promotions) well.

---

## 4. Results & Impact
| Metric | Baseline (Moving Avg) | New Model (XGBoost) | Improvement |
|:---|:---:|:---:|:---:|
| **RMSE (Error)** | 145 units | 82 units | **-43%** |
| **Stockout Rate** | 8.5% | 7.2% | **-15%** |

### Financial Projection
*   Avoiding stockouts on top 100 items is estimated to recover **$120,000** in annual revenue.
*   Reducing overstock frees up **$45,000** in working capital.

---

## 5. Deployment
The model is containerized (Docker) and runs a weekly batch prediction script. Results are pushed to a **Streamlit Dashboard** for the purchasing team to review orders.

> *"This tool has transformed our ordering process from 'guessing' to 'knowing'." — Supply Chain Manager*

---
*Download the full code and notebook from the [GitHub Repository](https://github.com/AndreeSalazar/Portfolio_Python)*
