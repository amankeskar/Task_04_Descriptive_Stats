"""
polars_stats_2024_fb_posts_president_scored_anon.py
Descriptive statistics for the dataset using Polars.
Dataset used: 2024_fb_posts_president_scored_anon.csv
This script loads the dataset, displays the header and first 5 rows, computes descriptive statistics,
and shows grouped statistics by 'Facebook_Id' and by 'Facebook_Id', 'post_id'.
Output is written to 'polars_stats_output_2024_fb_posts_president_scored_anon.txt'.
"""
import polars as pl
import sys

filepath = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\datasets_period_03_unzipped\2024_fb_posts_president_scored_anon.csv'
output_path = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\polars_stats_output_2024_fb_posts_president_scored_anon.txt'

def print_section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def main():
    with open(output_path, 'w', encoding='utf-8') as f:
        sys.stdout = f
        df = pl.read_csv(filepath)
        # Explicitly cast numeric columns
        df = df.with_columns([
            pl.col("Likes").cast(pl.Float64, strict=False),
            pl.col("Comments").cast(pl.Float64, strict=False),
            pl.col("Shares").cast(pl.Float64, strict=False),
            pl.col("Overperforming Score").cast(pl.Float64, strict=False),
            # Add more numeric columns as needed
        ])
        print_section('Header and First 5 Rows')
        print('Header:', df.columns)
        print('\nFirst 5 rows of data:')
        print(df.head())

        print_section('Descriptive Statistics for Entire Dataset')
        print(df.describe())

        print_section('Value Counts for Non-Numeric Columns (Top 3)')
        top_facebook_ids = df.group_by('Facebook_Id').len().sort('len', descending=True).head(3)
        print('\nTop 3 Facebook_Id:')
        print(top_facebook_ids)

        print_section('Grouped by Facebook_Id (showing first 3 groups)')
        unique_facebook_id = df.select('Facebook_Id').unique().to_series().to_list()
        for i, facebook_id in enumerate(unique_facebook_id[:3]):
            group = df.filter(pl.col('Facebook_Id') == facebook_id)
            print(f'\nGroup: Facebook_Id={facebook_id}')
            print(group.describe())

        print_section('Grouped by Facebook_Id and post_id (showing first 3 groups)')
        unique_facebook_post_id = df.select(['Facebook_Id', 'post_id']).unique().to_dict(as_series=False)
        for i in range(min(3, len(unique_facebook_post_id['Facebook_Id']))):
            facebook_id = unique_facebook_post_id['Facebook_Id'][i]
            post_id = unique_facebook_post_id['post_id'][i]
            group = df.filter((pl.col('Facebook_Id') == facebook_id) & (pl.col('post_id') == post_id))
            print(f'\nGroup: Facebook_Id={facebook_id}, post_id={post_id}')
            print(group.describe())

        print_section('Script Completed')
        print('All required descriptive statistics and groupings have been displayed.')
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()
