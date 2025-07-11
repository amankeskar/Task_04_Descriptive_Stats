"""
pandas_stats_2024_fb_ads_president_scored_anon.py
Descriptive statistics for the dataset using Pandas.
Dataset used: 2024_fb_ads_president_scored_anon.csv
This script loads the dataset, displays the header and first 5 rows, computes descriptive statistics,
and shows grouped statistics by 'page_id' and by 'page_id, ad_id'.
Output is written to 'pandas_stats_output.txt'.
"""
import pandas as pd
import sys

# File path to the dataset
filepath = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\datasets_period_03_unzipped\2024_fb_ads_president_scored_anon.csv'

# Output file path
output_path = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\pandas_stats_output.txt'

def print_section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def main():
    # Redirect stdout to file
    with open(output_path, 'w', encoding='utf-8') as f:
        sys.stdout = f
        # Load the dataset
        df = pd.read_csv(filepath)
        print_section('Header and First 5 Rows')
        print('Header:', list(df.columns))
        print('\nFirst 5 rows of data:')
        print(df.head().to_string(index=False))

        print_section('Descriptive Statistics for Entire Dataset')
        print(df.describe(include='all').transpose().to_string())

        # Value counts and most frequent for non-numeric columns
        print_section('Value Counts for Non-Numeric Columns (Top 3)')
        for col in df.select_dtypes(include=['object']).columns:
            print(f'\nColumn: {col}')
            print(df[col].value_counts().head(3).to_string())

        # Group by page_id
        print_section('Grouped by page_id (showing first 3 groups)')
        for i, (page_id, group) in enumerate(df.groupby('page_id')):
            print(f'\nGroup: page_id={page_id}')
            print(group.describe(include='all').transpose().to_string())
            if i >= 2:
                break

        # Group by page_id and ad_id
        print_section('Grouped by page_id and ad_id (showing first 3 groups)')
        for i, ((page_id, ad_id), group) in enumerate(df.groupby(['page_id', 'ad_id'])):
            print(f'\nGroup: page_id={page_id}, ad_id={ad_id}')
            print(group.describe(include='all').transpose().to_string())
            if i >= 2:
                break

        print_section('Script Completed')
        print('All required descriptive statistics and groupings have been displayed.')
        sys.stdout = sys.__stdout__  # Reset stdout

if __name__ == "__main__":
    main()
