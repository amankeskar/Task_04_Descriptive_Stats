"""
pandas_stats_2024_tw_posts_president_scored_anon.py
Descriptive statistics for the dataset using Pandas.
Dataset used: 2024_tw_posts_president_scored_anon.csv
This script loads the dataset, displays the header and first 5 rows, computes descriptive statistics,
and shows grouped statistics by 'source' and by 'source', 'id'.
Output is written to 'pandas_stats_output_2024_tw_posts_president_scored_anon.txt'.
"""
import pandas as pd
import sys

filepath = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\datasets_period_03_unzipped\2024_tw_posts_president_scored_anon.csv'
output_path = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\pandas_stats_output_2024_tw_posts_president_scored_anon.txt'

def print_section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def main():
    with open(output_path, 'w', encoding='utf-8') as f:
        sys.stdout = f
        df = pd.read_csv(filepath)
        print_section('Header and First 5 Rows')
        print('Header:', list(df.columns))
        print('\nFirst 5 rows of data:')
        print(df.head().to_string(index=False))

        print_section('Descriptive Statistics for Entire Dataset')
        print(df.describe(include='all').transpose().to_string())

        print_section('Value Counts for Non-Numeric Columns (Top 3)')
        for col in df.select_dtypes(include=['object']).columns:
            print(f'\nColumn: {col}')
            print(df[col].value_counts().head(3).to_string())

        print_section('Grouped by source (showing first 3 groups)')
        for i, (source, group) in enumerate(df.groupby('source')):
            print(f'\nGroup: source={source}')
            print(group.describe(include='all').transpose().to_string())
            if i >= 2:
                break

        print_section('Grouped by source and id (showing first 3 groups)')
        for i, ((source, id_), group) in enumerate(df.groupby(['source', 'id'])):
            print(f'\nGroup: source={source}, id={id_}')
            print(group.describe(include='all').transpose().to_string())
            if i >= 2:
                break

        print_section('Script Completed')
        print('All required descriptive statistics and groupings have been displayed.')
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()
