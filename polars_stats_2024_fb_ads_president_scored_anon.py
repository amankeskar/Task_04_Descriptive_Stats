"""
polars_stats_2024_fb_ads_president_scored_anon.py
Descriptive statistics for the dataset using Polars.
Dataset used: 2024_fb_ads_president_scored_anon.csv
This script loads the dataset, displays the header and first 5 rows, computes descriptive statistics,
and shows grouped statistics by 'page_id' and by 'page_id, ad_id'.
Output is written to 'polars_stats_output.txt'.
"""
import polars as pl
import sys

# File path to the dataset
filepath = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\datasets_period_03_unzipped\2024_fb_ads_president_scored_anon.csv'

# Output file path
output_path = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\polars_stats_output.txt'

def print_section(title):
    """Prints a section header."""
    print(f"\n{'='*10} {title} {'='*10}")

def main():
    """Main function to execute the descriptive statistics analysis."""
    with open(output_path, 'w', encoding='utf-8') as f:
        sys.stdout = f  # Redirect print output to the file
        # Load the dataset
        df = pl.read_csv(filepath)
        # Explicitly cast numeric columns
        df = df.with_columns([
            pl.col("estimated_audience_size").cast(pl.Float64, strict=False),
            pl.col("estimated_impressions").cast(pl.Float64, strict=False),
            pl.col("scam_illuminating").cast(pl.Float64, strict=False),
            # Add more numeric columns as needed
        ])
        print_section('Header and First 5 Rows')
        print('Header:', df.columns)
        print('\nFirst 5 rows of data:')
        print(df.head())

        # Descriptive statistics for the entire dataset
        print_section('Descriptive Statistics for Entire Dataset')
        print(df.describe())

        # Value counts for non-numeric columns
        print_section('Value Counts for Non-Numeric Columns (Top 3)')
        # Use group_by().len() for value counts
        top_page_ids = df.group_by('page_id').len().sort('len', descending=True).head(3)
        print('\nTop 3 page_id:')
        print(top_page_ids)

        # Group by page_id
        print_section('Grouped by page_id (showing first 3 groups)')
        unique_page_ids = df.select('page_id').unique().to_series().to_list()
        for i, page_id in enumerate(unique_page_ids[:3]):
            group = df.filter(pl.col('page_id') == page_id)
            print(f'\nGroup: page_id={page_id}')
            print(group.describe())

        # Group by page_id and ad_id
        print_section('Grouped by page_id and ad_id (showing first 3 groups)')
        unique_page_ad_ids = df.select(['page_id', 'ad_id']).unique().to_dict(as_series=False)
        for i in range(min(3, len(unique_page_ad_ids['page_id']))):
            page_id = unique_page_ad_ids['page_id'][i]
            ad_id = unique_page_ad_ids['ad_id'][i]
            group = df.filter((pl.col('page_id') == page_id) & (pl.col('ad_id') == ad_id))
            print(f'\nGroup: page_id={page_id}, ad_id={ad_id}')
            print(group.describe())

        print_section('Script Completed')
        print('All required descriptive statistics and groupings have been displayed.')
        sys.stdout = sys.__stdout__  # Reset print output to console

if __name__ == "__main__":
    main()
