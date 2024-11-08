import pandas as pd
from tqdm import tqdm

# Load the Excel file
df = pd.read_excel('Güncel_ham_dosya1.xlsx', engine='openpyxl')

# Get unique League IDs and weeks
lig_ids = df['Lig ID'].unique()
weeks = sorted(df['Game Week'].dropna().unique())  # Get weeks sorted

# Create an Excel writer
writer = pd.ExcelWriter('Automate_Home_haftalık_sıralama_tablosu.xlsx', engine='xlsxwriter')

# Create an empty DataFrame to store the previous week's ranking
previous_week_summaries = {lig_id: pd.DataFrame() for lig_id in lig_ids}

# Create a dictionary to store the total rank differences
total_rank_diff = {lig_id: {} for lig_id in lig_ids}

# Initialize a dictionary to keep track of the number of matches played by each team
matches_played = {lig_id: {} for lig_id in lig_ids}

# Initialize a counter to keep track of the number of sheets created
sheet_count = 0

# Total number of iterations
total_iterations = len(lig_ids) * len(weeks)

# Use tqdm for progress bar
with tqdm(total=total_iterations, desc="Processing") as pbar:
    for lig_id in lig_ids:
        cumulative_points = {}
        cumulative_average = {}
        cumulative_goals = {}
        cumulative_goals_defeated = {}
        cumulative_win = {}
        cumulative_draw = {}
        cumulative_loss = {}
        cumulative_matches_played = {}
        all_team_total_goal = 0  # Initial value for All Team Total Goal

        for week in weeks:
            # Select the specific League ID and week
            df_week = df[(df['Game Week'] == week) & (df['Lig ID'] == lig_id)]
            
            if df_week.empty:
                pbar.update(1)
                continue  # Skip this week if df_week is empty
            
            # Select home teams and their goals
            home_teams = df_week[['Game Week', 'home_team_name', 'home_team_goal_count', 'away_team_goal_count']].copy()

            # Rename columns for consistency
            home_teams.columns = ['Game Week', 'Team Name', 'Goal Count', 'Goal Defeated']

            # Calculate the Average column
            home_teams['Average'] = home_teams['Goal Count'] - home_teams['Goal Defeated']

            # Calculate the Point column
            home_teams['Point'] = home_teams.apply(lambda row: 3 if row['Goal Count'] > row['Goal Defeated'] else (1 if row['Goal Count'] == row['Goal Defeated'] else 0), axis=1)

            # Calculate Win, Draw, Loss columns
            home_teams['Win'] = home_teams['Point'].apply(lambda x: 1 if x == 3 else 0)
            home_teams['Draw'] = home_teams['Point'].apply(lambda x: 1 if x == 1 else 0)
            home_teams['Loss'] = home_teams['Point'].apply(lambda x: 1 if x == 0 else 0)

            # Add "Lig ID" column and set it to lig_id
            home_teams['Lig ID'] = lig_id

            # Add "Lig Tipi" column and set it to 2
            home_teams['Lig Tipi'] = 2

            # Initialize "Match Played" column to 0
            home_teams['Match Played'] = 0

            # Select away teams and set their statistics to zero
            away_teams = df_week[['Game Week', 'away_team_name']].copy()
            away_teams.columns = ['Game Week', 'Team Name']
            away_teams['Goal Count'] = 0
            away_teams['Goal Defeated'] = 0
            away_teams['Average'] = 0
            away_teams['Point'] = 0
            away_teams['Win'] = 0
            away_teams['Draw'] = 0
            away_teams['Loss'] = 0
            away_teams['Lig ID'] = lig_id
            away_teams['Lig Tipi'] = 2
            away_teams['Match Played'] = 0

            # Combine home and away teams
            combined_teams = pd.concat([home_teams, away_teams])

            # Combine results for teams playing more than one match in the same week
            weekly_summary = combined_teams.groupby(['Game Week', 'Team Name', 'Lig ID', 'Lig Tipi'], as_index=False).agg({
                'Goal Count': 'sum',
                'Goal Defeated': 'sum',
                'Average': 'sum',
                'Point': 'sum',
                'Win': 'sum',
                'Draw': 'sum',
                'Loss': 'sum'
            })

            # Update "Match Played" column and calculate cumulative matches played
            for team in weekly_summary['Team Name']:
                if team in home_teams['Team Name'].values:
                    matches_played[lig_id][team] = matches_played[lig_id].get(team, 0) + 1
                else:
                    matches_played[lig_id].setdefault(team, 0)
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Match Played'] = matches_played[lig_id][team]
                cumulative_matches_played[team] = cumulative_matches_played.get(team, 0) + weekly_summary.loc[weekly_summary['Team Name'] == team, 'Match Played'].sum()

            # Calculate cumulative values
            for team in weekly_summary['Team Name']:
                previous_point = cumulative_points.get(team, 0)
                previous_average = cumulative_average.get(team, 0)
                previous_goals = cumulative_goals.get(team, 0)
                previous_goals_defeated = cumulative_goals_defeated.get(team, 0)
                previous_win = cumulative_win.get(team, 0)
                previous_draw = cumulative_draw.get(team, 0)
                previous_loss = cumulative_loss.get(team, 0)
                previous_matches_played = cumulative_matches_played.get(team, 0)

                current_point = weekly_summary.loc[weekly_summary['Team Name'] == team, 'Point'].sum()
                current_average = weekly_summary.loc[weekly_summary['Team Name'] == team, 'Average'].sum()
                current_goals = weekly_summary.loc[weekly_summary['Team Name'] == team, 'Goal Count'].sum()
                current_goals_defeated = weekly_summary.loc[weekly_summary['Team Name'] == team, 'Goal Defeated'].sum()
                current_win = weekly_summary.loc[weekly_summary['Team Name'] == team, 'Win'].sum()
                current_draw = weekly_summary.loc[weekly_summary['Team Name'] == team, 'Draw'].sum()
                current_loss = weekly_summary.loc[weekly_summary['Team Name'] == team, 'Loss'].sum()
                current_matches_played = weekly_summary.loc[weekly_summary['Team Name'] == team, 'Match Played'].sum()

                cumulative_points[team] = previous_point + current_point
                cumulative_average[team] = previous_average + current_average
                cumulative_goals[team] = previous_goals + current_goals
                cumulative_goals_defeated[team] = previous_goals_defeated + current_goals_defeated
                cumulative_win[team] = previous_win + current_win
                cumulative_draw[team] = previous_draw + current_draw
                cumulative_loss[team] = previous_loss + current_loss
                cumulative_matches_played[team] = previous_matches_played + current_matches_played

                # Add cumulative values to the weekly_summary
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Cumulative Point'] = cumulative_points[team]
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Cumulative Average'] = cumulative_average[team]
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Cumulative Goal Count'] = cumulative_goals[team]
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Cumulative Goal Defeated'] = cumulative_goals_defeated[team]
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Cumulative Win'] = cumulative_win[team]
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Cumulative Draw'] = cumulative_draw[team]
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Cumulative Loss'] = cumulative_loss[team]
                weekly_summary.loc[weekly_summary['Team Name'] == team, 'Cumulative Matches Played'] = cumulative_matches_played[team]

                # Calculate cumulative ratios
                matches_played_team = matches_played[lig_id].get(team, 1)
                if matches_played_team != 0:
                    weekly_summary.loc[weekly_summary['Team Name'] == team, 'Total Cumulative Goal Count Ratio'] = cumulative_goals[team] / matches_played_team
                    weekly_summary.loc[weekly_summary['Team Name'] == team, 'Total Cumulative Goal Defeated Ratio'] = cumulative_goals_defeated[team] / matches_played_team
                else:
                    weekly_summary.loc[weekly_summary['Team Name'] == team, 'Total Cumulative Goal Count Ratio'] = 0
                    weekly_summary.loc[weekly_summary['Team Name'] == team, 'Total Cumulative Goal Defeated Ratio'] = 0

            # Calculate All Team Total Goal and add it to the summary
            all_team_total_goal = home_teams['Goal Count'].sum() + home_teams['Goal Defeated'].sum()
            weekly_summary['All Team Total Goal'] = all_team_total_goal

            # Sort teams by their rank
            weekly_summary = weekly_summary.sort_values(by=['Total Cumulative Goal Count Ratio', 'Cumulative Average'], ascending=[False, False])
            weekly_summary['Rank'] = range(1, len(weekly_summary) + 1)

            # Add Cumulative Point Ratio column
            weekly_summary['Cumulative Point Ratio'] = weekly_summary['Cumulative Point'] / weekly_summary['Match Played'].replace(0, 1)  # Avoid division by zero

            # Reorder columns to match the order in the provided Word document
            column_order = [
                'Lig ID', 'Lig Tipi', 'Game Week', 'Match Played', 'Team Name', 'Goal Count', 
                'Cumulative Goal Count', 'Total Cumulative Goal Count Ratio', 'Goal Defeated', 
                'Cumulative Goal Defeated', 'Total Cumulative Goal Defeated Ratio', 'Average', 
                'Cumulative Average', 'Win', 'Cumulative Win', 'Draw', 'Cumulative Draw', 'Loss', 
                'Cumulative Loss', 'Point', 'Cumulative Point', 'Cumulative Point Ratio', 'All Team Total Goal', 'Cumulative Matches Played', 'Rank'
            ]
            weekly_summary = weekly_summary[column_order]

            # Write the weekly summary to the Excel file
            final_sheet_name = f'Week{int(week)}_F_Lig_2_{lig_id}'[:31]
            weekly_summary.to_excel(writer, sheet_name=final_sheet_name, index=False)

            # Save this week for the next week's reference
            previous_week_summaries[lig_id] = weekly_summary

            # Increment the sheet count
            sheet_count += 1

            # Update progress bar
            pbar.update(1)

# Complete the writing process
writer.close()

print(f"Process completed, please check 'Home_haftalık_sıralama_tablosu.xlsx'. Number of sheets created: {sheet_count}")
