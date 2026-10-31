# Ride-Sharing Demand Analysis in Makkah During Ramadan

🌐 **English** | [العربية](README.ar.md)

🏆 **1st Place — Data Camp, Umm Al-Qura University**

A team project exploring ride-sharing demand patterns during Ramadan in Makkah and proposing proactive fleet redistribution to better align supply with demand.

> **Data transparency:** The dataset is statistically simulated. The project starts from public Uber & Lyft ride data from Boston and adds simulated Makkah locations, Ramadan days, prayer periods, and weather features. The results below are outputs from this simulation; they are not real operational measurements of transportation in Makkah.

## The Problem

Demand for transportation can change sharply around prayer and gathering times. Static fleet allocation may not respond quickly to these shifts, creating temporary gaps between available vehicles and ride demand.

## Project Goals

- Explore demand patterns across simulated Makkah locations and time periods.
- Examine how engineered Ramadan and prayer-period features relate to demand.
- Build a data workflow and demonstrate a forecasting approach.
- Suggest ways to redistribute an existing fleet before expected demand peaks.

## Data Workflow

| Stage | Work |
|---|---|
| Data integration | Combine ride records and weather data by timestamp |
| Location simulation | Map source locations to selected Makkah landmarks |
| Feature engineering | Create features such as `ramadan_day`, `prayer_period`, `is_last_ten`, and `dist_to_haram` |
| Data cleaning | Handle missing values, duplicates, and price outliers |
| Analysis & modeling | Explore patterns and demonstrate demand forecasting |

The prepared simulated dataset contains **637,976 records**.

## Reported Results

The following figures are based on the simulated dataset and its assumptions:

| Metric | Reported value |
|---|---:|
| Average demand | 26,582 rides/hour |
| Assumed fleet capacity | 27,000 vehicles |
| Peak demand | 29,872 rides/hour |
| Modeled peak gap | 2,872 rides (10.6%) |
| Random Forest R² | 0.94 |

**Important limitation:** Features such as prayer period, Ramadan day, and weather were generated as part of the simulation. Their importance in the model reflects those simulation assumptions and should not be interpreted as evidence about real-world Makkah transportation. Validation with real operational data would be required.

## Recommendations Explored

- Consider moving fleet capacity from lower-demand areas toward predicted hotspots before expected peaks.
- Include relevant time-based context in demand-planning workflows.
- Evaluate fleet redistribution as an alternative to increasing fleet size.

These are scenario-based recommendations from the simulated analysis, not operational instructions.

## Team Contribution & AI Transparency

The team worked on data preparation in Python, including merging rides with weather, location simulation, feature engineering, cleaning, and the presentation. AI assistance was used for parts of the exploratory analysis, Random Forest forecasting, and interactive-dashboard work after dataset preparation.

## Tech Stack

- **Python**, **Pandas**, **NumPy** — data processing and feature engineering
- **Matplotlib**, **Seaborn** — exploratory analysis and visualization
- **Scikit-learn** — Random Forest modeling

## Repository Structure

```text
makkah-ramadan-rides./
├── README.md
├── README.ar.md
├── .gitignore
├── requirements.txt
├── feature_engineering.py
├── data/
│   └── README.md
└── presentation.pdf
```

The raw CSV files are not included in this repository. See [data/README.md](data/README.md) for the required files and source information.

## Getting Started

1. Clone the repository:
   ```bash
   git clone "https://github.com/by-shooq/makkah-ramadan-rides..git"
   cd "makkah-ramadan-rides."
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the source CSV files described in [data/README.md](data/README.md) and place them in the `data/` folder.

4. Run the feature-engineering script from the repository root:
   ```bash
   python feature_engineering.py
   ```

## Links

- [Project presentation](presentation.pdf)
- [Original Uber & Lyft Boston dataset on Kaggle](https://www.kaggle.com/datasets/ravi72munde/uber-lyft-cab-prices?resource=download)
- [Project post on X](https://x.com/by_shooq/status/2050665660766650570?s=20)
