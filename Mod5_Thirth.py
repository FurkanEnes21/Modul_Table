import pandas as pd
from tqdm import tqdm

# Load the Excel file with the previous data
df = pd.read_excel('Final_Modul5_Genel_sıralama_tablosu.xlsx', engine='openpyxl', sheet_name=None)

# Create a new Excel writer for the cumulative calculations
writer = pd.ExcelWriter('Modul5_Cumulative_Statistics1.xlsx', engine='xlsxwriter')

# Initialize cumulative data storage
cumulative_data = {}

for sheet_name in tqdm(df.keys(), desc='Processing Sheets'):
    sheet_df = df[sheet_name]

    # Separate rows based on Match Play value
    match_play_1_df = sheet_df[sheet_df['Match Played'] == 1].copy()
    match_play_0_df = sheet_df[sheet_df['Match Played'] == 0].copy()
    
    # Extract the Lig ID
    lig_id = sheet_df['Lig ID'].iloc[0]
    
    # Initialize cumulative data if not already done
    if lig_id not in cumulative_data:
        cumulative_data[lig_id] = {
            'Cumulative Goal Count': {},
            'Cumulative Goal Defeated': {},
            'Cumulative Average': {},
            'Cumulative Point': {},
            'Cumulative Match Play': {},
            'Cumulative Win': {},
            'Cumulative Draw': {},
            'Cumulative Loss': {},
            'Rank': {}
        }

    # Calculate Win, Draw, and Loss for Home Team
    match_play_1_df['Home Win'] = match_play_1_df['Home Team Point'].apply(lambda x: 1 if x == 3 else 0)
    match_play_1_df['Home Draw'] = match_play_1_df['Home Team Point'].apply(lambda x: 1 if x == 1 else 0)
    match_play_1_df['Home Loss'] = match_play_1_df['Home Team Point'].apply(lambda x: 1 if x == 0 else 0)

    # Calculate Win, Draw, and Loss for Away Team
    match_play_1_df['Away Win'] = match_play_1_df['Away Team Point'].apply(lambda x: 1 if x == 3 else 0)
    match_play_1_df['Away Draw'] = match_play_1_df['Away Team Point'].apply(lambda x: 1 if x == 1 else 0)
    match_play_1_df['Away Loss'] = match_play_1_df['Away Team Point'].apply(lambda x: 1 if x == 0 else 0)

    # Calculate cumulative values for each team
    for index, row in match_play_1_df.iterrows():
        home_team = row['Home Team']
        away_team = row['Away Team']
        
        # Initialize cumulative data for the home team if not already done
        if home_team not in cumulative_data[lig_id]['Cumulative Goal Count']:
            cumulative_data[lig_id]['Cumulative Goal Count'][home_team] = 0
            cumulative_data[lig_id]['Cumulative Goal Defeated'][home_team] = 0
            cumulative_data[lig_id]['Cumulative Average'][home_team] = 0
            cumulative_data[lig_id]['Cumulative Point'][home_team] = 0
            cumulative_data[lig_id]['Cumulative Match Play'][home_team] = 0
            cumulative_data[lig_id]['Cumulative Win'][home_team] = 0
            cumulative_data[lig_id]['Cumulative Draw'][home_team] = 0
            cumulative_data[lig_id]['Cumulative Loss'][home_team] = 0
            cumulative_data[lig_id]['Rank'][home_team] = []

        # Initialize cumulative data for the away team if not already done
        if away_team not in cumulative_data[lig_id]['Cumulative Goal Count']:
            cumulative_data[lig_id]['Cumulative Goal Count'][away_team] = 0
            cumulative_data[lig_id]['Cumulative Goal Defeated'][away_team] = 0
            cumulative_data[lig_id]['Cumulative Average'][away_team] = 0
            cumulative_data[lig_id]['Cumulative Point'][away_team] = 0
            cumulative_data[lig_id]['Cumulative Match Play'][away_team] = 0
            cumulative_data[lig_id]['Cumulative Win'][away_team] = 0
            cumulative_data[lig_id]['Cumulative Draw'][away_team] = 0
            cumulative_data[lig_id]['Cumulative Loss'][away_team] = 0
            cumulative_data[lig_id]['Rank'][away_team] = []

        # Update cumulative data for the home team
        cumulative_data[lig_id]['Cumulative Goal Count'][home_team] += row['Home Goals']
        cumulative_data[lig_id]['Cumulative Goal Defeated'][home_team] += row['Home Team Goal Defeated']
        cumulative_data[lig_id]['Cumulative Average'][home_team] += row['Home Team Average']
        cumulative_data[lig_id]['Cumulative Point'][home_team] += row['Home Team Point']
        cumulative_data[lig_id]['Cumulative Match Play'][home_team] += 1
        cumulative_data[lig_id]['Cumulative Win'][home_team] += row['Home Win']
        cumulative_data[lig_id]['Cumulative Draw'][home_team] += row['Home Draw']
        cumulative_data[lig_id]['Cumulative Loss'][home_team] += row['Home Loss']

        # Update cumulative data for the away team
        cumulative_data[lig_id]['Cumulative Goal Count'][away_team] += row['Away Team Goal Count']
        cumulative_data[lig_id]['Cumulative Goal Defeated'][away_team] += row['Away Team Goal Defeated']
        cumulative_data[lig_id]['Cumulative Average'][away_team] += row['Away Team Average']
        cumulative_data[lig_id]['Cumulative Point'][away_team] += row['Away Team Point']
        cumulative_data[lig_id]['Cumulative Match Play'][away_team] += 1
        cumulative_data[lig_id]['Cumulative Win'][away_team] += row['Away Win']
        cumulative_data[lig_id]['Cumulative Draw'][away_team] += row['Away Draw']
        cumulative_data[lig_id]['Cumulative Loss'][away_team] += row['Away Loss']

    # Set Home Win, Home Draw, Home Loss, Away Win, Away Draw, Away Loss to 0 for match_play_0_df
    match_play_0_df['Home Win'] = 0
    match_play_0_df['Home Draw'] = 0
    match_play_0_df['Home Loss'] = 0
    match_play_0_df['Away Win'] = 0
    match_play_0_df['Away Draw'] = 0
    match_play_0_df['Away Loss'] = 0

    # Merge match_play_1_df and match_play_0_df for final output
    final_df = pd.concat([match_play_1_df, match_play_0_df], ignore_index=True)

    # Calculate rankings for each team
    home_ranking_df = final_df[['Home Team', 'Home Team Point']].groupby('Home Team').sum().reset_index()
    home_ranking_df = home_ranking_df.sort_values(by='Home Team Point', ascending=False).reset_index(drop=True)
    home_ranking_df['Home Team Rank'] = home_ranking_df.index + 1

    away_ranking_df = final_df[['Away Team', 'Away Team Point']].groupby('Away Team').sum().reset_index()
    away_ranking_df = away_ranking_df.sort_values(by='Away Team Point', ascending=False).reset_index(drop=True)
    away_ranking_df['Away Team Rank'] = away_ranking_df.index + 1

    # Assign ranks to the home and away teams
    final_df['Home Team Rank'] = final_df['Home Team'].map(home_ranking_df.set_index('Home Team')['Home Team Rank'])
    final_df['Away Team Rank'] = final_df['Away Team'].map(away_ranking_df.set_index('Away Team')['Away Team Rank'])

    # Calculate rank differences
    final_df['Home Team Rank Diff'] = final_df['Home Team Rank'] - final_df['Away Team Rank']
    final_df['Away Team Rank Diff'] = final_df['Away Team Rank'] - final_df['Home Team Rank']

    # Calculate total rank differences
    final_df['Home Team Total Rank Diff'] = final_df.groupby('Home Team')['Home Team Rank Diff'].cumsum()
    final_df['Away Team Total Rank Diff'] = final_df.groupby('Away Team')['Away Team Rank Diff'].cumsum()

    # Add cumulative values to the DataFrame for match_play_1_df only
    for col in ['Goal Count', 'Goal Defeated', 'Average', 'Point', 'Match Played', 'Win', 'Draw', 'Loss']:
        final_df[f'Cumulative Home Team {col}'] = final_df.apply(
            lambda row: cumulative_data[lig_id][f'Cumulative {col}'][row['Home Team']] if row['Match Played'] == 1 else 0,
            axis=1
        )
        final_df[f'Cumulative Away Team {col}'] = final_df.apply(
            lambda row: cumulative_data[lig_id][f'Cumulative {col}'][row['Away Team']] if row['Match Played'] == 1 else 0,
            axis=1
        )

    # Calculate All Team Total Goal for the week
    all_team_total_goal = (final_df['Home Team Goal Count'] + final_df['Away Team Goal Count']).sum()
    final_df['All Team Total Goal'] = all_team_total_goal

    # Calculate Cumulative Point Ratio for home and away teams
    final_df['Cumulative Home Team Point Ratio'] = final_df.apply(
        lambda row: row['Cumulative Home Team Point'] / row['Cumulative Home Team Match Played'] if row['Cumulative Home Team Match Played'] != 0 else 0,
        axis=1
    )
    final_df['Cumulative Away Team Point Ratio'] = final_df.apply(
        lambda row: row['Cumulative Away Team Point'] / row['Cumulative Away Team Match Played'] if row['Cumulative Away Team Match Played'] != 0 else 0,
        axis=1
    )

    # Calculate Cumulative Goal Defeated Ratio for home and away teams
    final_df['Total Cumulative Home Team Goal Defeated Ratio'] = final_df.apply(
        lambda row: row['Cumulative Home Team Goal Defeated'] / row['Cumulative Home Team Match Played'] if row['Cumulative Home Team Match Played'] != 0 else 0,
        axis=1
    )
    final_df['Total Cumulative Away Team Goal Defeated Ratio'] = final_df.apply(
        lambda row: row['Cumulative Away Team Goal Defeated'] / row['Cumulative Away Team Match Played'] if row['Cumulative Away Team Match Played'] != 0 else 0,
        axis=1
    )

    # Calculate Cumulative Goal Count Ratio for home and away teams
    final_df['Total Cumulative Home Team Goal Count Ratio'] = final_df.apply(
        lambda row: row['Cumulative Home Team Goal Count'] / row['Cumulative Home Team Match Playeded'] if row['Cumulative Home Team Match Played'] != 0 else 0,
        axis=1
    )
    final_df['Total Cumulative Away Team Goal Count Ratio'] = final_df.apply(
        lambda row: row['Cumulative Away Team Goal Count'] / row['Cumulative Away Team Match Played'] if row['Cumulative Away Team Match Played'] != 0 else 0,
        axis=1
    )

    # Add 'Lig Tipi' column
    final_df['Lig Tipi'] = 5

    # Reorder the columns to include the new cumulative columns
    column_order = [
        'Lig ID', 'Lig Tipi', 'Game Week', 'Match Played', 'Home Team', 'Away Team', 'Home Team Goal Count', 'Away Team Goal Count', 'Home Team Goal Defeated', 'Away Team Goal Defeated',
        'Home Team Average', 'Away Team Average', 'Home Team Point', 'Away Team Point', 'Home Win', 'Home Draw', 'Home Loss', 'Away Win', 'Away Draw', 'Away Loss',
        'Cumulative Home Team Goal Count', 'Total Cumulative Home Team Goal Count Ratio', 'Cumulative Home Team Goal Defeated', 'Total Cumulative Home Team Goal Defeated Ratio',
        'Cumulative Home Team Average', 'Cumulative Home Team Point', 'Cumulative Home Team Match Played', 'Cumulative Home Team Win', 'Cumulative Home Team Draw', 'Cumulative Home Team Loss',
        'Cumulative Away Team Goal Count', 'Total Cumulative Away Team Goal Count Ratio', 'Cumulative Away Team Goal Defeated', 'Total Cumulative Away Team Goal Defeated Ratio',
        'Cumulative Away Team Average', 'Cumulative Away Team Point', 'Cumulative Away Team Match Played', 'Cumulative Away Team Win', 'Cumulative Away Team Draw', 'Cumulative Away Team Loss',
        'All Team Total Goal', 'Home Team Rank', 'Away Team Rank', 'Cumulative Home Team Point Ratio', 'Cumulative Away Team Point Ratio',
        'Home Team Rank', 'Away Team Rank', 'Home Team Rank Diff', 'Home Team Total Rank Diff', 'Away Team Rank Diff', 'Away Team Total Rank Diff'
    ]
    final_df = final_df[column_order]

    # Write the cumulative statistics to the new Excel file
    final_df.to_excel(writer, sheet_name=sheet_name, index=False)

# Complete the writing process
writer.close()

print(f"Cumulative statistics calculation completed. Please check 'Modul5_Cumulative_Statistics.xlsx'.")
