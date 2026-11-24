# Netflix Recommendation System

A Machine Learning internship project focused on building a content-based recommendation system using Netflix Movies and TV Shows data.

## Project Overview

This project aims to recommend similar Netflix titles based on content features such as genres, directors, countries, and other available attributes.

## Dataset Information

- Total records: 8,790
- Total features: 10
- Movies: 6,126
- TV Shows: 2,664
- Missing values in original dataset: 0

Dataset file expected at:

`data/raw/Dataset.csv`

The dataset is not included in this repository. Add the authorized dataset locally before running the project.

## Work Completed

- Project structure setup
- Python virtual environment setup
- Dependency installation
- Dataset loading
- Exploratory Data Analysis (EDA)
- Duplicate record analysis
- Content type distribution analysis
- Genre and country analysis
- Initial data preprocessing implementation

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

## Project Structure

```text
Task_1_Recommendation_System/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   └── recommendation_engine/
│       ├── data_loader.py
│       ├── preprocessing.py
│       ├── feature_engineering.py
│       ├── recommender.py
│       └── evaluation.py
├── app/
├── tests/
├── artifacts/
├── outputs/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

```bash
git clone YOUR_REPOSITORY_URL
cd Task_1_Recommendation_System

python -m venv .venv
```

Activate environment on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the authorized `Dataset.csv` file inside `data/raw/`.

## Project Status

Currently completed: Dataset loading, EDA, and initial preprocessing.

Recommendation engine development is in progress.

## Author

Chandani Kumari

Machine Learning Intern