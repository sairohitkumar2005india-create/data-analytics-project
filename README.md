# Sales Data Analytics with Python & Power BI

A small end-to-end analytics project: clean raw sales data with **Python/Pandas**,
summarize it, and visualize it in **Power BI**.

## What's in this folder

| File | Purpose |
|---|---|
| `sales_data.csv` | Raw (slightly messy) sample sales data |
| `analyze.py` | Cleans the data and produces summary CSVs + a chart |
| `cleaned_sales_data.csv` | Output: clean dataset (import this into Power BI) |
| `summary_by_region.csv` | Output: total revenue per region |
| `summary_by_product.csv` | Output: total revenue per product |
| `summary_monthly_trend.csv` | Output: revenue trend by month |
| `revenue_overview.png` | Quick Python-generated chart |
| `requirements.txt` | Python packages needed |

## Step 1 — Set up Python

```bash
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 2 — Run the analysis

```bash
python analyze.py
```

This reads `sales_data.csv`, removes duplicates, fills missing values, and writes
the cleaned file plus three summary CSVs and a chart image.

## Step 3 — Build the Power BI dashboard

1. Open **Power BI Desktop** → **Get Data** → **Text/CSV**.
2. Import `cleaned_sales_data.csv`.
3. Go to the **Report** view and add visuals:
   - **Bar chart**: `Region` (axis) vs sum of `Revenue` (values)
   - **Bar/Pie chart**: `Product` (axis) vs sum of `Revenue` (values)
   - **Line chart**: `Date` (axis, set to Month) vs sum of `Revenue` (values)
4. Optionally import the three `summary_*.csv` files too and use them directly
   for faster-loading visuals on large datasets.
5. Arrange the visuals on one page and save as `SalesDashboard.pbix`.

## Step 4 — Push the project to GitHub

```bash
# 1. Move into the project folder
cd data-analytics-project

# 2. Initialize a git repository (skip if already a repo)
git init

# 3. Create a .gitignore so you don't commit the virtual environment
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore

# 4. Stage and commit everything
git add .
git commit -m "Add sales data analytics project (Python + Power BI)"

# 5. Create a new empty repository on GitHub (via the website), then:
git branch -M main
git remote add origin https://github.com/<your-username>/data-analytics-project.git
git push -u origin main
```

After that, refresh your GitHub profile page — the repo and its files should
appear there, and you can link it from your resume.

### If you add the `.pbix` Power BI file later
GitHub doesn't preview `.pbix` files, but it's fine to commit it so others can
download and open it in Power BI Desktop:

```bash
git add SalesDashboard.pbix
git commit -m "Add Power BI dashboard file"
git push
```
