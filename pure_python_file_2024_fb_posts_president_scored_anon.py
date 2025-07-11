"""
pure_python_file_2024_fb_posts_president_scored_anon.py
Descriptive statistics for the dataset using only the Python standard library.
Dataset used: 2024_fb_posts_president_scored_anon.csv
This script loads the dataset, displays the header and first 5 rows, computes descriptive statistics,
and shows grouped statistics by 'Facebook_Id' and by 'Facebook_Id', 'post_id'.
Output is written to 'pure_python_output_2024_fb_posts_president_scored_anon.txt'.
"""
import csv
from collections import Counter, defaultdict
from math import sqrt
import sys

def pure_python(file_path):
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            data.append(row)
    return header, data

def is_float(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def detect_numeric_columns(header, data, threshold=0.8):
    numeric_cols = set()
    for col in header:
        col_data = [row[col] for row in data if row[col] not in (None, '', 'NA', 'N/A')]
        if not col_data:
            continue
        num_numeric = sum(1 for x in col_data if is_float(x))
        if num_numeric / len(col_data) >= threshold:
            numeric_cols.add(col)
    return numeric_cols

def print_table(headers, rows):
    col_widths = [max(len(str(h)), *(len(str(row[i])) for row in rows)) for i, h in enumerate(headers)]
    header_line = ' | '.join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    sep_line = '-+-'.join('-' * col_widths[i] for i in range(len(headers)))
    print(header_line)
    print(sep_line)
    for row in rows:
        print(' | '.join(str(row[i]).ljust(col_widths[i]) for i in range(len(headers))))

def describe_data(header, data, numeric_cols, group_name=None):
    if group_name:
        print(f'\n===== Descriptive Statistics for group: {group_name} =====')
    else:
        print('\n===== Descriptive Statistics for Entire Dataset =====')
    stats_rows = []
    for col in header:
        col_data = [row[col] for row in data if row[col] not in (None, '', 'NA', 'N/A')]
        if col in numeric_cols:
            numeric_data = [float(x) for x in col_data if is_float(x)]
            if numeric_data:
                mean = sum(numeric_data) / len(numeric_data)
                min_val = min(numeric_data)
                max_val = max(numeric_data)
                std = sqrt(sum((x - mean) ** 2 for x in numeric_data) / len(numeric_data)) if len(numeric_data) > 1 else 0.0
                stats_rows.append([
                    col, len(numeric_data), f"{mean:.2f}", min_val, max_val, f"{std:.2f}", '', ''
                ])
            else:
                stats_rows.append([col, 0, '', '', '', '', '', ''])
        else:
            unique_counts = Counter(col_data)
            most_common = unique_counts.most_common(1)[0] if unique_counts else (None, 0)
            stats_rows.append([
                col, len(col_data), '', '', '', '', len(unique_counts), f"{most_common[0]} (Count: {most_common[1]})"
            ])
    headers = [
        'Column', 'Count', 'Mean', 'Min', 'Max', 'Std', 'Unique', 'Most Frequent'
    ]
    print_table(headers, stats_rows)

def group_by(data, keys):
    groups = defaultdict(list)
    for row in data:
        key = tuple(row[k] for k in keys)
        groups[key].append(row)
    return groups

if __name__ == "__main__":
    filepath = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\datasets_period_03_unzipped\2024_fb_posts_president_scored_anon.csv'
    output_path = r'C:\Users\amank\OneDrive - Syracuse University\Syracuse Master Folder\Research Analyst Project for OPT\pure_python_output_2024_fb_posts_president_scored_anon.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        sys.stdout = f
        header, raw_data = pure_python(filepath)
        print('Header:', header)
        print('\nFirst 5 rows of raw data:')
        for i in range(min(5, len(raw_data))):
            print(raw_data[i])

        numeric_cols = detect_numeric_columns(header, raw_data)
        print(f'\nDetected numeric columns: {sorted(numeric_cols)}')

        describe_data(header, raw_data, numeric_cols)

        groups_facebook = group_by(raw_data, ['Facebook_Id'])
        print('\n===== Grouped by Facebook_Id (showing first 3 groups) =====')
        for group_key, group_data in list(groups_facebook.items())[:3]:
            describe_data(header, group_data, numeric_cols, group_name=f'Facebook_Id={group_key[0]}')

        groups_facebook_post = group_by(raw_data, ['Facebook_Id', 'post_id'])
        print('\n===== Grouped by Facebook_Id and post_id (showing first 3 groups) =====')
        for group_key, group_data in list(groups_facebook_post.items())[:3]:
            describe_data(header, group_data, numeric_cols, group_name=f'Facebook_Id={group_key[0]}, post_id={group_key[1]}')

        print('\n===== Script Completed =====')
        print('All required descriptive statistics and groupings have been displayed.')
        sys.stdout = sys.__stdout__
