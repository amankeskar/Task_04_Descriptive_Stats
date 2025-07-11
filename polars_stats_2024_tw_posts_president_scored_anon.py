"""
polars_stats_2024_tw_posts_president_scored_anon.py
Descriptive statistics for the dataset using Polars.
Dataset used: 2024_tw_posts_president_scored_anon.csv
This script loads the dataset, displays the header and first 5 rows, computes descriptive statistics,
and shows grouped statistics by 'source' and by 'source', 'id'.
Output is written to 'polars_stats_output_2024_tw_posts_president_scored_anon.txt'.
"""
import polars as pl
import sys

filepath = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\datasets_period_03_unzipped\2024_tw_posts_president_scored_anon.csv'
output_path = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\polars_stats_output_2024_tw_posts_president_scored_anon.txt'

def print_section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def main():
    with open(output_path, 'w', encoding='utf-8') as f:
        sys.stdout = f
        df = pl.read_csv(filepath)
        # Explicitly cast numeric columns
        df = df.with_columns([
            pl.col("retweetCount").cast(pl.Float64, strict=False),
            pl.col("replyCount").cast(pl.Float64, strict=False),
            pl.col("likeCount").cast(pl.Float64, strict=False),
            pl.col("quoteCount").cast(pl.Float64, strict=False),
            pl.col("viewCount").cast(pl.Float64, strict=False),
            # Add more numeric columns as needed
        ])
        print_section('Header and First 5 Rows')
        print('Header:', df.columns)
        print('\nFirst 5 rows of data:')
        print(df.head())

        print_section('Descriptive Statistics for Entire Dataset')
        print(df.describe())

        print_section('Value Counts for Non-Numeric Columns (Top 3)')
        top_sources = df.group_by('source').len().sort('len', descending=True).head(3)
        print('\nTop 3 source:')
        print(top_sources)

        print_section('Grouped by source (showing first 3 groups)')
        unique_source = df.select('source').unique().to_series().to_list()
        for i, source in enumerate(unique_source[:3]):
            group = df.filter(pl.col('source') == source)
            print(f'\nGroup: source={source}')
            print(group.describe())

        print_section('Grouped by source and id (showing first 3 groups)')
        unique_source_id = df.select(['source', 'id']).unique().to_dict(as_series=False)
        for i in range(min(3, len(unique_source_id['source']))):
            source = unique_source_id['source'][i]
            id_ = unique_source_id['id'][i]
            group = df.filter((pl.col('source') == source) & (pl.col('id') == id_))
            print(f'\nGroup: source={source}, id={id_}')
            print(group.describe())

        print_section('Script Completed')
        print('All required descriptive statistics and groupings have been displayed.')
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()
