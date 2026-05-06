# NFL Betting Model

> Personal NFL betting model that generates weekly spread and over/under picks with confidence rankings.

## Overview

This model analyzes weekly NFL matchup data and produces ranked betting recommendations. Results and trends are visualized on [Tableau Public](https://public.tableau.com/app/profile/matt.gilgo/vizzes).

## Features

- Generates spread and over/under picks each week
- Flask web apps to view best bets and play-of-the-day picks
- Multi-season historical tracking (2023–present)

## Requirements

- Python 3.9+
- `pandas`, `numpy`, `nfl_data_py`, `flask`
- Team stat CSVs exported from [Pro Football Reference](https://www.pro-football-reference.com)

## Installation

```bash
git clone https://github.com/mattgilgo/nfl_betting_model.git
cd nfl_betting_model
pip install pandas numpy nfl_data_py flask
```

## Usage

**Run the best bets web app:**

```bash
cd best_bets_website
python app.py
```

Navigate to `http://localhost:5000` and click "Get Picks" to fetch this week's best bets.

**Run the play-of-the-day web app:**

```bash
cd play_of_the_day_website
python app.py
```

**Update for a new season** (see `Year_to_Year_Changes.txt` for the full checklist):

1. Archive the previous season's team data and weekly picks
2. Download fresh stat CSVs from Pro Football Reference
3. Update the year and week number constants in each `choose_bets.py`

## Results

Historical weekly results are tracked below. Full interactive visualizations are on [Tableau Public](https://public.tableau.com/app/profile/matt.gilgo/vizzes).

### 2023

| Week | Total Units | Play of the Day | Result | Best Bets |
|------|-------------|-----------------|--------|-----------|
| Week 1 | N/a | N/a | -- | -- |
| Week 2 | N/a | N/a | -- | -- |
| Week 3 | -1.39 | DEN/MIA OVER 47.5 | YES (90 pts) | 3-2-0 |
| Week 4 | 2.62 | BUF/MIA OVER 53.5 | YES (68 pts) | 4-1-0 |
| Week 5 | 4.46 | MIA -11 | YES (Win by 15) | 6-1-0 |
| Week 6 | 2.62 | MIA -13.5 | YES (Win by 21) | 5-2-0 |
| Week 7 | -1.00 | PHI/MIA OVER 52 | NO (48 pts) | 0-1-0 |
| Week 8 | -2.09 | SF -5.5 | NO (Loss by 14) | 1-3-0 |
| Week 9 | -- | N/a | -- | -- |
| Week 10 | -0.09 | DEN/BUF OVER 47 | NO (46 pts) | 1-1-0 |
| Week 11 | 0.82 | BAL -3.5 | YES (Win by 14) | 2-1-0 |
| Week 12 | 1.82 | SF -6.5 | YES (Win by 18) | 2-0-0 |
| Week 13 | 1.82 | MIA -9.5 | YES (Win by 30) | 2-0-0 |
| Week 14 | 0.91 | SF -10.5 | YES (Win by 12) | 1-0-0 |
| Week 15 | 0.91 | SF -10 | YES (Win by 16) | 1-0-0 |
| Week 16 | 0 | None | N/a | 0-0-0 |
| Week 17 | -1.09 | SF -13.5 | YES (Win by 17) | 1-2-0 |
| Week 18 | -- | N/a | -- | -- |

## Contributing

PRs and issues welcome. Please open an issue before large changes.

## License

GPL-3.0 — see [LICENSE](LICENSE)
