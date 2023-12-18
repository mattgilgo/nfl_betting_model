import pandas as pd
import numpy as np
import nfl_data_py as nfl
import choose_bets

def best_bets():
    weekly_game_info_df = choose_bets.choose_bets(print_picks=False, input=15)
    best_bets_df = pd.DataFrame()
    spread_df = weekly_game_info_df[['game_id','team_and_spread_to_bet','spread_confidence_score']]
    spread_best_bets_df = spread_df[spread_df['spread_confidence_score'] >= 30]
    o_u_df = weekly_game_info_df[['game_id','points_and_over_under_to_bet','over_under_confidence_score']]
    o_u_best_bets_df = o_u_df[o_u_df['over_under_confidence_score'] >= 30]
    spread_best_bets_df = spread_best_bets_df.rename(columns={"team_and_spread_to_bet": "bet", "spread_confidence_score": "confidence_score"})
    o_u_best_bets_df = o_u_best_bets_df.rename(columns={"points_and_over_under_to_bet": "bet", "over_under_confidence_score": "confidence_score"})
    best_bets_df = pd.concat([spread_best_bets_df,o_u_best_bets_df])
    best_bets_df_sorted = best_bets_df.sort_values('confidence_score', ascending=False)
    best_bets_df_sorted_reduced = best_bets_df_sorted[['game_id','bet']]
    best_bets_df_html = best_bets_df_sorted_reduced.to_html()
    return best_bets_df_html

if __name__ == "__main__":
    best_bets()