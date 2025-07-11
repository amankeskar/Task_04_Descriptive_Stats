"""
Visualization script for 2024_tw_posts_president_scored_anon.csv using Pandas, Matplotlib, and Seaborn.
Generates PNG plots for key descriptive statistics and group-by summaries.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

# Load dataset
DATASET = 'datasets_period_03_unzipped/2024_tw_posts_president_scored_anon.csv'
df = pd.read_csv(DATASET)

# Output directory for plots
PLOT_DIR = 'visualizations_tw_posts'
os.makedirs(PLOT_DIR, exist_ok=True)

# Numeric columns
numeric_cols = df.select_dtypes(include='number').columns.tolist()

def sanitize_filename(name):
    """Replace or remove characters that are invalid in Windows filenames."""
    return re.sub(r'[\\/:*?"<>|]', '_', name)

# 1. Histograms for numeric columns
for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col].dropna(), kde=True, bins=30)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f'{PLOT_DIR}/hist_{sanitize_filename(col)}.png')
    plt.close()

# 2. Bar plot for top 10 most frequent values in a key categorical column (if exists)
cat_cols = df.select_dtypes(include='object').columns.tolist()
if cat_cols:
    for col in cat_cols:
        top_vals = df[col].value_counts().head(10)
        plt.figure(figsize=(8,4))
        sns.barplot(x=top_vals.values, y=top_vals.index, orient='h')
        plt.title(f'Top 10 Most Frequent Values in {col}')
        plt.xlabel('Count')
        plt.ylabel(col)
        plt.tight_layout()
        plt.savefig(f'{PLOT_DIR}/bar_{sanitize_filename(col)}.png')
        plt.close()

# 3. Boxplots for numeric columns grouped by a key categorical column (if exists)
if cat_cols and numeric_cols:
    group_col = cat_cols[0]
    # Limit to top 10 most frequent groups for boxplots
    top_groups = df[group_col].value_counts().head(10).index
    df_box = df[df[group_col].isin(top_groups)]
    for col in numeric_cols:
        if df_box[group_col].nunique() > 1 and df_box[col].notnull().sum() > 0:
            plt.figure(figsize=(10,5))
            sns.boxplot(x=group_col, y=col, data=df_box)
            plt.title(f'Boxplot of {col} by {group_col} (Top 10 groups)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{PLOT_DIR}/box_{sanitize_filename(col)}_by_{sanitize_filename(group_col)}.png')
            plt.close()

print(f'Visualizations saved in {PLOT_DIR}/')
