import pandas as pd
import numpy as np
import nfl_data_py as nfl
import sys
sys.path.insert(1, 'choose_bets.py')
import choose_bets

def play_of_the_day(print_play_of_the_day=True):
    weekly_game_info_df = choose_bets.choose_bets(print_picks=False, input=10)
    best_spread_pick = weekly_game_info_df['spread_confidence_score'].max()
    best_over_under_pick = weekly_game_info_df['over_under_confidence_score'].max()

    if best_spread_pick >= best_over_under_pick:
        best_pick_row = weekly_game_info_df[weekly_game_info_df['spread_confidence_score'] == best_spread_pick]
        best_pick = best_pick_row['team_and_spread_to_bet']
        best_pick_val= best_pick.values[0]
        confidence = str(best_pick_row['spread_confidence_score']) + "%"
        if print_play_of_the_day:
            print('')
            print('####################')
            print('Pick: ' + best_pick_val)
            print('Confidence: ' + confidence)
            print('####################')
            print('')
        else:
            pass
        return best_pick_val, confidence
    else:
        best_pick_row = weekly_game_info_df[weekly_game_info_df['over_under_confidence_score'] == best_over_under_pick]
        best_pick = best_pick_row['away_team'] + '/' + best_pick_row['home_team'] + ' ' + best_pick_row['bet_for_over_under'] + ' ' + str(best_pick_row['total_line'].values[0]) + 'pts'
        best_pick_val= best_pick.values[0]
        confidence = str(best_pick_row['over_under_confidence_score'].values[0]) + "%"
        if print_play_of_the_day:
            print('')
            print('####################')
            print('Pick: ' + best_pick_val)
            print('Confidence: ' + confidence)
            print('####################')
            print('')
        else:
            pass
        return best_pick_val, confidence

if __name__ == "__main__":
    play_of_the_day()