import pandas as pd
from tqdm import tqdm

# Load the Excel file
df = pd.read_excel('Güncel_ham_dosya1.xlsx', engine='openpyxl')

lig_ids = df['Lig ID'].unique()
weeks = sorted(df['Game Week'].dropna().unique())[:10234]  # Get only the first 100 weeks

# Create an Excel writer
writer = pd.ExcelWriter('Modul9_Genel_sıralama_tablosu.xlsx', engine='xlsxwriter')

# Create an empty DataFrame to store the previous week's ranking
previous_week_summaries = {lig_id: pd.DataFrame() for lig_id in lig_ids}

# Create a dictionary to store the total rank differences
total_rank_diff = {lig_id: {} for lig_id in lig_ids}

# Initialize a counter to keep track of the number of sheets created
sheet_count = 0

for lig_id in tqdm(lig_ids, desc='Processing Lig IDs'):
    for week in tqdm(weeks, desc=f'Processing weeks for Lig ID {lig_id}', leave=False):
        # Select the specific League ID and week
        df_week = df[(df['Game Week'] == week) & (df['Lig ID'] == lig_id)]
        
        if df_week.empty:
            continue  # Skip this week if df_week is empty

        # Create DataFrame for matches
        matches = df_week[['Game Week', 'home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count']].copy()
        matches.columns = ['Game Week', 'Home Team', 'Away Team', 'Home Goals', 'Away Goals']

        # Calculate statistics for home teams
        home_stats = matches[['Game Week', 'Home Team', 'Home Goals', 'Away Goals']].copy()
        home_stats['Team'] = home_stats['Home Team']
        home_stats['Goals Scored'] = home_stats['Home Goals']
        home_stats['Goals Conceded'] = home_stats['Away Goals']
        home_stats['Points'] = home_stats.apply(lambda row: 3 if row['Goals Scored'] > row['Goals Conceded'] else (1 if row['Goals Scored'] == row['Goals Conceded'] else 0), axis=1)

        # Calculate statistics for away teams
        away_stats = matches[['Game Week', 'Away Team', 'Away Goals', 'Home Goals']].copy()
        away_stats['Team'] = away_stats['Away Team']
        away_stats['Goals Scored'] = away_stats['Away Goals']
        away_stats['Goals Conceded'] = away_stats['Home Goals']
        away_stats['Points'] = away_stats.apply(lambda row: 3 if row['Goals Scored'] > row['Goals Conceded'] else (1 if row['Goals Scored'] == row['Goals Conceded'] else 0), axis=1)

        # Combine home and away statistics
        combined_stats = pd.concat([home_stats, away_stats], ignore_index=True)
        combined_stats = combined_stats[['Game Week', 'Team', 'Goals Scored', 'Goals Conceded', 'Points']]
        
        # Calculate aggregates
        aggregated_stats = combined_stats.groupby(['Game Week', 'Team']).agg({
            'Goals Scored': 'sum',
            'Goals Conceded': 'sum',
            'Points': 'sum'
        }).reset_index()

        # Calculate average and rank
        aggregated_stats['Average'] = aggregated_stats['Goals Scored'] - aggregated_stats['Goals Conceded']
        aggregated_stats = aggregated_stats.sort_values(by=['Points', 'Average', 'Goals Scored'], ascending=[False, False, False])
        aggregated_stats['Rank'] = range(1, len(aggregated_stats) + 1)

        # Handle previous week's ranking
        if not previous_week_summaries[lig_id].empty:
            previous_week_summary = previous_week_summaries[lig_id][['Team', 'Rank']].rename(columns={'Rank': 'Previous Rank'})
            aggregated_stats = aggregated_stats.merge(previous_week_summary, on='Team', how='left')
            aggregated_stats['Rank Diff'] = aggregated_stats['Previous Rank'] - aggregated_stats['Rank']
            aggregated_stats.drop(columns=['Previous Rank'], inplace=True)
        else:
            aggregated_stats['Rank Diff'] = 0  # Rank Diff is 0 for the first week

        # Calculate Total Rank Difference and add it to the summary
        for team in aggregated_stats['Team']:
            total_rank_diff[lig_id][team] = total_rank_diff[lig_id].get(team, 0) + aggregated_stats.loc[aggregated_stats['Team'] == team, 'Rank Diff'].values[0]
            aggregated_stats.loc[aggregated_stats['Team'] == team, 'Total Rank Diff'] = total_rank_diff[lig_id][team]

        # Merge with original matches to include Home Team and Away Team statistics
        final_summary = matches.copy()
        final_summary = final_summary.merge(aggregated_stats, left_on='Home Team', right_on='Team', how='left', suffixes=('', '_Home'))
        final_summary = final_summary.merge(aggregated_stats, left_on='Away Team', right_on='Team', how='left', suffixes=('', '_Away'))

        # Add previous ranks
        if not previous_week_summaries[lig_id].empty:
            previous_week_summary_home = previous_week_summaries[lig_id][['Team', 'Rank']].rename(columns={'Team': 'Home Team', 'Rank': 'Pre-Home Rank'})
            previous_week_summary_away = previous_week_summaries[lig_id][['Team', 'Rank']].rename(columns={'Team': 'Away Team', 'Rank': 'Pre-Away Rank'})
            final_summary = final_summary.merge(previous_week_summary_home, on='Home Team', how='left')
            final_summary = final_summary.merge(previous_week_summary_away, on='Away Team', how='left')
        else:
            final_summary['Pre-Home Rank'] = None
            final_summary['Pre-Away Rank'] = None

        # Add Lig ID to final_summary
        final_summary['Lig ID'] = lig_id

        # Rename columns for clarity
        final_summary.rename(columns={
            'Goals Scored': 'Home Team Goal Count',
            'Goals Conceded': 'Home Team Goal Defeated',
            'Points': 'Home Team Point',
            'Average': 'Home Team Average',
            'Goals Scored_Away': 'Away Team Goal Count',
            'Goals Conceded_Away': 'Away Team Goal Defeated',
            'Points_Away': 'Away Team Point',
            'Average_Away': 'Away Team Average',
            'Rank': 'Home Team Rank',
            'Rank_Away': 'Away Team Rank',
            'Rank Diff': 'Home Team Rank Diff',
            'Rank Diff_Away': 'Away Team Rank Diff',
            'Total Rank Diff': 'Home Team Total Rank Diff',
            'Total Rank Diff_Away': 'Away Team Total Rank Diff'
        }, inplace=True)

        # Select the final columns for output
        final_columns = [
            'Lig ID', 'Game Week', 'Home Team', 'Away Team', 'Home Goals', 'Away Goals',
            'Home Team Goal Count', 'Home Team Goal Defeated', 'Home Team Average', 'Home Team Point',
            'Away Team Goal Count', 'Away Team Goal Defeated', 'Away Team Average', 'Away Team Point',
            'Home Team Rank', 'Away Team Rank', 'Home Team Rank Diff', 'Away Team Rank Diff',
            'Home Team Total Rank Diff', 'Away Team Total Rank Diff', 'Pre-Home Rank', 'Pre-Away Rank'
        ]
        final_summary = final_summary[final_columns]

        # Write the weekly summary to the Excel file
        final_sheet_name = f'Week{int(week)}_F_Lig_9_{lig_id}'[:31]
        final_summary.to_excel(writer, sheet_name=final_sheet_name, index=False)

        # Save this week for the next week's reference
        previous_week_summaries[lig_id] = aggregated_stats

        # Increment the sheet count
        sheet_count += 1

# Complete the writing process
writer.close()

print(f"Process completed, please check 'Modul9_Genel_sıralama_tablosu.xlsx'. Number of sheets created: {sheet_count}")
