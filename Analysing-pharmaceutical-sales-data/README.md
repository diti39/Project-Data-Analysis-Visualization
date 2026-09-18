# Pharmaceutical Sales Analysis

Exploratory analysis of daily pharmaceutical sales data (2014–2019) to identify which drug categories drive volume, how demand shifts across the calendar, and where category leadership changed over time.

## Business Question

A pharmacy chain or distributor needs to know which drug categories to prioritize for inventory and promotion. This analysis answers:

- Which drug categories account for the largest share of total sales?
- Which categories lead sales in specific months across different years?
- Which category sold the most in 2017, and how concentrated is that lead?
- Which categories have the highest average daily demand (relevant for stock replenishment)?

## Data

- **Source:** Daily sales records for 8 ATC-classified drug categories (`salesdaily1.csv`)
- **Period:** Jan 2014 – Oct 2019 (2,106 daily records)
- **Categories:** M01AB, M01AE (anti-inflammatories), N02BA, N02BE (analgesics), N05B, N05C (anxiolytics/sedatives), R03 (respiratory), R06 (antihistamines)

## Method

Using pandas, sales were aggregated by category across the full period, by specific month/year windows, and by calendar year, then compared using totals and daily averages. Matplotlib was used for category-level visualizations.

## Key Findings

- **N02BE dominates the portfolio**, accounting for ~63,000 units of total sales — more than 3x the next-largest category (N05B, ~18,600) and nearly 6x the overall category average. It also holds the highest average daily sales (≈30 units/day, vs. single digits for every other category).
- **This dominance is stable over time, not a one-off spike.** N02BE ranked #1 in every sampled window — January 2015, July 2016, September 2017 — and again as the single highest-volume category for the full 2017 calendar year (9,259 units, more than 3.6x the runner-up).
- **The remaining categories cluster into two tiers:** a "mid" tier (N05B, R03, M01AB) each contributing roughly 10,000–19,000 units total, and a "long tail" (M01AE, N02BA, R06, N05C) each under 8,500 units, with N05C consistently the smallest category (~1,250 total, ~0.6 units/day).

## Recommendation

Inventory and reorder priority should weight heavily toward N02BE — it isn't just the top seller, it's structurally dominant and consistent across years and seasons, making it a low-risk, high-volume stocking priority. The long-tail categories (particularly N05C) warrant minimal safety stock given consistently low and stable demand.

## Extended Analysis: Seasonality, Trend, and Forecast

### Weekday effects

The dataset includes an `Hour` field, but it turns out to be constant within each month (only 2 distinct values across the whole dataset) — it records something like monthly operating hours, not a per-day timestamp, so it can't support a time-of-day check. `Weekday Name` does vary daily and shows a real pattern: N02BE sales run noticeably higher on weekends (~33.5 units/day) than midweek (~28.1 units/day on Wednesdays), a swing of about 5.3 units/day after removing the underlying trend. No holiday flag exists in the raw data, so holiday effects would need an external calendar — noted as a next step below.

### Is N02BE's lead growing or shrinking?

Tracking N02BE's share of total category sales on a trailing 12-month basis shows the lead is **stable and slightly growing**: 46.7% of total sales in the first available 12-month window (mid-2014) vs. 48.0% in the most recent window (through Oct 2019), with the share ranging 44.3%–54.0% over the full period. This reinforces the inventory recommendation above — N02BE's dominance isn't fading.

### Next-quarter forecast

A damped-trend exponential smoothing model (Holt's method, damped to avoid unrealistic long-horizon extrapolation) was fit per category and projected 90 days forward. N02BE and N05B are forecast to account for **~78% of combined demand** over the next quarter, closely tracking their historical shares — no category shows a forecast reversal in ranking.

_This is a lightweight, non-seasonal baseline — it smooths level and trend but doesn't explicitly use the weekly pattern found above. A production forecast would use Holt-Winters or Prophet with weekly seasonality built in._

## Tools

Python, pandas, matplotlib

## Files

- `Analysing-pharmaceutical-sales-data.ipynb` — full analysis notebook
- `data/salesdaily1.csv` — source data
