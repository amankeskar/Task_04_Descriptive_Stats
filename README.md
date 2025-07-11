# Task 04: Descriptive Statistics

Welcome! This project explores descriptive statistics for three datasets from the 2024 US presidential election, using three different approaches: pure Python, Pandas, and Polars. The goal is to compare these methods, highlight their strengths and quirks, and share what I learned along the way.

## Datasets Analyzed

- Facebook Ads: `2024_fb_ads_president_scored_anon.csv`
- Facebook Posts: `2024_fb_posts_president_scored_anon.csv`
- Twitter Posts: `2024_tw_posts_president_scored_anon.csv`

## How to Run the Analyses

1. Make sure the datasets (not included here) are in the `datasets_period_03_unzipped` folder, as described in the assignment.
2. Run each script for each dataset and method:

   **Pure Python:**
   - `python pure_python_file_2024_fb_ads_president_scored_anon.py`
   - `python pure_python_file_2024_fb_posts_president_scored_anon.py`
   - `python pure_python_file_2024_tw_posts_president_scored_anon.py`

   **Pandas:**
   - `python pandas_stats_2024_fb_ads_president_scored_anon.py`
   - `python pandas_stats_2024_fb_posts_president_scored_anon.py`
   - `python pandas_stats_2024_tw_posts_president_scored_anon.py`

   **Polars:**
   - `python polars_stats_2024_fb_ads_president_scored_anon.py`
   - `python polars_stats_2024_fb_posts_president_scored_anon.py`
   - `python polars_stats_2024_tw_posts_president_scored_anon.py`

Each script will create a results file specific to the dataset and method.

## Output Files

- `pure_python_output_2024_fb_ads_president_scored_anon.txt`
- `pure_python_output_2024_fb_posts_president_scored_anon.txt`
- `pure_python_output_2024_tw_posts_president_scored_anon.txt`
- `pandas_stats_output_2024_fb_ads_president_scored_anon.txt`
- `pandas_stats_output_2024_fb_posts_president_scored_anon.txt`
- `pandas_stats_output_2024_tw_posts_president_scored_anon.txt`
- `polars_stats_output_2024_fb_ads_president_scored_anon.txt`
- `polars_stats_output_2024_fb_posts_president_scored_anon.txt`
- `polars_stats_output_2024_tw_posts_president_scored_anon.txt`

## What I Learned (and What Surprised Me)

- All three approaches (pure Python, Pandas, Polars) give you the basics: count, mean, min, max, standard deviation, unique counts, and most frequent values. Group-by analysis works well in all of them.
- **Standard deviation isn’t always the same!** Pure Python’s statistics module uses the population standard deviation by default, while Pandas and Polars use the sample version. I had to adjust for this to make the results match.
- **Polars is fast, but picky.** At first, Polars thought some numeric columns were strings, so stats came out as null. Explicitly casting columns to numbers fixed this. Also, getting the top value counts in Polars required a different approach than Pandas.
- **Which is best?** For big data and speed, Polars is impressive. Pandas is the most user-friendly and flexible for most real-world work. Pure Python is great for learning and understanding what’s happening under the hood.

## Reflections & Advice

- **Was it hard to get identical results?**
  - Yes! The standard deviation difference and Polars’ type quirks took some careful debugging. But with explicit type casting and matching the std calculation, I got there.
- **Which approach would I recommend?**
  - For most analysts, start with Pandas. It’s powerful, readable, and has a huge community. Use Polars if you’re working with really large datasets or need extra speed. Pure Python is great for building intuition.
- **If I were coaching a junior analyst:**
  - Learn Pandas first, but don’t skip the basics—understanding how things work in pure Python will make you a better analyst in the long run.

## How AI Coding Tools Helped

I used AI coding assistants (like GitHub Copilot and Gemini) to:
- Draft and refine scripts for each method and dataset
- Debug tricky issues with Polars’ type inference and value counts
- Polish the code and make sure outputs were consistent and clear
- Double-check that everything matched the assignment requirements

All code was reviewed and tested to make sure it’s correct and reproducible.

## Notes

- The datasets themselves are not included here—please add them to the correct folder before running the scripts.
- If you have questions or run into issues, check the assignment instructions or reach out to the instructor.
