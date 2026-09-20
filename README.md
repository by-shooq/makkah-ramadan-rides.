# 🕋 Ride-Sharing Shortage Analysis in Makkah During Ramadan

🌐 **English** | [العربية](README.ar.md)

🏆 **1st Place — [Data camp  / Umm Al-Qura University ]**

> Data analysis and demand forecasting for ride-sharing in Makkah during Ramadan, identifying when and where demand peaks and proposing **proactive fleet redistribution without adding a single vehicle**.

---

## ⚠️ Important note about the data

The data in this project is **statistically simulated** and does **not** represent real operational data from Makkah. We started from the public Uber & Lyft (Boston) rides dataset and built a simulation layer on top of it (localizing locations, generating Ramadan days, prayer periods and weather) to test the idea and build a complete analysis pipeline. All figures below are results on this simulated data; they demonstrate the methodology and are not measurements of real Makkah transport.

---

## 📌 The Problem

Transport in Makkah during Ramadan follows a **"pulsating flow"**: hundreds of thousands of people move within very narrow, sudden time windows tied to the end of prayers (Tarawih, Qiyam, Fajr). This causes:

- **Supply–demand gaps**: sudden demand spikes exhaust available cars immediately.
- **Operational bottlenecks**: driver shortages in peak areas push waiting times (ETA) to unprecedented levels.
- **Hard-to-plan fleet distribution**: static schedules can't adapt to shifting prayer times or weather.

## 🎯 Goals

1. Identify **hotspots** based on proximity to the Haram.
2. Study the effect of the **last ten nights** and weather on the driver shortage.
3. Provide data-driven recommendations to position drivers **before** congestion happens.

---

## 🧪 The Data Journey

**Source:** public Uber & Lyft rides dataset (Boston, Kaggle) + its weather file.

| Stage | What we did |
|---|---|
| **Merging** | Joined rides with weather by timestamp using Pandas |
| **Localization** | Mapped Boston locations to Makkah landmarks (Al-Haram Area, Ajyad, Jabal Omar, Aziziyah, Haramain Station, Umm Al-Qura University, ...) |
| **Feature engineering** | Generated `ramadan_day`, `prayer_period`, `is_last_ten`, `dist_to_haram` |
| **Cleaning** | Handled missing values, duplicates and price outliers — 637,976 clean records |

### Key features

| Feature | Meaning | Analytical value |
|---|---|---|
| `prayer_period` | Prayer windows (Tarawih, Qiyam, Fajr, Iftar, Normal) | Pinpoints demand-explosion moments tied to the religious schedule |
| `dist_to_haram` | Distance (km) from the Haram | Explains congestion and driver shortage in the central zone |
| `surge_multiplier` | Price surge multiplier | Proxy for the supply gap |
| `is_last_ten` | Last ten nights of Ramadan (0 / 1) | Separates regular days from peak season |

---

## 📊 Results

| Metric | Value |
|---|---|
| Average demand | 26,582 rides/hour |
| Fleet capacity (assumed) | 27,000 vehicles |
| Peak demand | 29,872 rides/hour |
| Operational gap at peak | 2,872 rides (**10.6%**) |
| Random Forest model | R² = **0.94** |

**Highlights**

- Demand exceeds fleet capacity in specific hours; supply and demand break down at the same time.
- `prayer_period` (Tarawih, then Fajr) is the strongest demand driver in the model.
- Clock time alone is not enough to predict demand; prayer schedules must be included.

### 💡 Recommendations

1. **Proactive redistribution:** move 10% of the fleet from low-demand areas to gathering points around the Haram 30 minutes before Tarawih ends.
2. **Model-driven dispatch:** replace static distribution schedules with a system that adapts to prayer times and daily congestion.
3. **Efficiency at zero cost:** close the 2,872-ride gap by improving how the current fleet is distributed instead of buying more vehicles.

> **Limitations:** since `prayer_period`, `ramadan_day` and the weather values are generated inside the simulation, their importance in the model reflects the simulation's assumptions. The natural next step is retraining on real operational data.

---

## 🤖 How This Was Built

- **By the team:** data preparation in Python — merging rides with weather, localizing locations to Makkah, feature engineering and cleaning (see `src/feature_engineering.py`) — and the presentation.
- **With AI assistance:** after the dataset was prepared, an AI assistant helped with the exploratory analysis, the Random Forest forecasting step and the interactive dashboard.

We mention this openly so the results can be reviewed with the right context.

---

## 🛠️ Tech Stack

- **Python**, **Pandas**, **NumPy** — data processing and feature engineering
- **Matplotlib**, **Seaborn** — exploratory analysis and charts
- **Scikit-learn** (`RandomForestRegressor`) — demand forecasting (AI-assisted)
- **[Plotly / Dash / dashboard tool used]** — interactive dashboard (AI-assisted)

---

## 📁 Project Structure

```
├── README.md
├── README.ar.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md            # how to get the original data
├── notebooks/               # EDA + modeling notebooks
├── src/
│   └── feature_engineering.py
├── images/                  # result charts
└── docs/
    └── presentation.pdf
```

## ▶️ Getting Started

```bash
# 1. Clone
git clone https://github.com/[USERNAME]/[REPO].git
cd [REPO]

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download the raw data (see data/README.md) into data/

# 4. Build the dataset
python src/feature_engineering.py
```

The script uses a fixed random seed, so the simulated columns are reproducible.

---

## 👥 Team

| Name |
|---|
| Shouq Nasser Al-Baqami |
| Aya Abdullah Al-Harthi |
| Rital Abdulrahman Al-Luhaibi | 
| Layan Mohammed Al-Zahrani |
## 🔗 Links

- 📑 [Presentation](presentation.pdf)

- Original data: Uber & Lyft Dataset (Boston, MA) on Kaggle — (https://www.kaggle.com/datasets/ravi72munde/uber-lyft-cab-prices?resource=download)
