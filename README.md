# meteorite-study-2026
# Global Meteorite Landings Analysis 2026

# Overview
This project explores a global meteorite landings dataset using Python.
The goal was to practice data cleaning, exploratory data analysis,
and visualisation while answering a small set of analysis questions.

# Questions explored
- How many meteorite discoveries were there per year?
- What are the most common meteorite types?
- What are the largest meteorites discovered?
- How many meteorites have been recorded over time?
- Where do meteorites land most often?

# Tools used
- Python
- pandas
- matplotlib
- Jupyter Notebook

# Dataset
Source: Kaggle meteorite landings dataset

The dataset includes:
- name
- id
- nametype
- recclass
- mass (g)
- fall
- year
- reclat
- reclong
- GeoLocation

# Data cleaning
The dataset was cleaned by:
- removing rows with missing coordinates,
- removing zero-value coordinates,
- converting year and mass columns to numeric values,
- removing invalid year values,
- keeping the raw CSV unchanged.

# Project structure
- `data/meteorite_landings.csv`
- `notebooks/meteorite_analysis.ipynb`
- `src/analysis.py`
- `outputs/figures/`
- `outputs/tables/`

# Key findings
- Most meteorites in the dataset are recorded as found rather than fell.
- The dataset contains many different meteorite classes.
- Some meteorites are extremely large compared to the rest.
- Meteorite discoveries vary significantly by year.
- A few records contain unusual or invalid year values, which were handled during cleaning.

# How to run
1. Install the required packages.
2. Place the dataset in the `data/` folder.
3. Run the notebook or execute `src/analysis.py`.

# Future improvements
- Add a map visualisation.
- Build a Power BI dashboard.
- Add more validation checks.
- Create a more detailed analysis of location data.
