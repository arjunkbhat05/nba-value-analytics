# NBA Salary-to-Impact Analytics

A Python-based data analytics project that evaluates NBA player contract efficiency by quantifying on-court impact per salary dollar using advanced performance metrics.

This project simulates how front offices and analytics teams assess **player value, cost efficiency, and return on investment** during an active NBA season.

---

## 📌 Project Overview

NBA teams operate under strict salary cap constraints, making contract efficiency just as important as raw performance.  
This project builds an end-to-end analytics pipeline that merges **NBA salary data** with **advanced player performance metrics** to rank players by their **Salary-to-Impact Value Index**.

The analysis is designed to support:
- In-season player evaluation
- Contract value comparison
- Data-driven roster and spending decisions

All results are reproducible, tested, and automated using modern Python tooling and CI practices.

---

## 📊 Key Metrics Engineered

- **Cost per Win Share**  
  > Salary divided by Win Shares to measure cost efficiency

- **Efficiency Index**  
  > Weighted impact score combining:
  - VORP (Value Over Replacement Player)
  - BPM (Box Plus/Minus)
  - Win Shares

- **Salary-to-Impact Value Index**  
  > Normalized (0–100) metric measuring impact per dollar spent  
  > Includes edge-case handling for partial or equal-value datasets

---

## 🛠️ Technical Implementation

- **Language:** Python
- **Core Libraries:** pandas, numpy, matplotlib
- **Architecture:** `src/`-based package structure
- **Testing:** pytest (unit tests for metrics & edge cases)
- **Automation:** GitHub Actions CI for continuous testing
- **Data Flow:**  
  Raw CSV → ETL merge → KPI computation → Ranked results output

---

## ▶️ How to Run

Clone the repository and run:

```bash
pip install -r requirements.txt
python -m nba_value.viz
