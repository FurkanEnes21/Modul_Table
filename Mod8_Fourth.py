import pandas as pd
from tqdm import tqdm

# Load the cumulative statistics file
file_path = 'Modul8_Cumulative_Statistics.xlsx'
df = pd.read_excel(file_path, sheet_name=None)

# Initialize a dictionary to store the processed data
processed_data = {}

# Get the total number of sheets to process
total_sheets = len(df)

# Iterate through each sheet and process the data with progress tracking
for sheet_name, sheet_df in tqdm(df.items(), total=total_sheets, desc="Processing sheets"):
    # Extract relevant columns for Home Team and Away Team
    home_team_df = sheet_df[['Home Team', 'Home Team Goal Count', 'Home Team Goal Defeated', 'Cumulative Home Team Goal Count', 'Cumulative Home Team Goal Defeated',
                             'Cumulative Home Team Average', 'Cumulative Home Team Point', 'Cumulative Home Team Match Played',
                             'Cumulative Home Team Win', 'Cumulative Home Team Draw', 'Cumulative Home Team Loss',
                             'Cumulative Home Team Point Ratio', 'Home Win', 'Home Draw', 'Home Loss', 'Lig ID', 'Game Week', 
                             'Home Team Point', 'Home Team Average', 'Cumulative Home Team Match Played', 'All Team Total Goal', 'Lig Tipi','Total Cumulative Home Team Goal Count Ratio',
                             'Total Cumulative Home Team Goal Defeated Ratio']].copy()
    
    home_team_df.columns = ['Team Name', 'Goal Count', 'Goal Defeated', 'Cumulative Goal Count', 'Cumulative Goal Defeated', 'Cumulative Average',
                            'Cumulative Point', 'Cumulative Match Played', 'Cumulative Win', 'Cumulative Draw',
                            'Cumulative Loss', 'Cumulative Point Ratio', 'Win', 'Draw', 'Loss', 'Lig ID', 'Game Week', 
                            'Point', 'Average', 'Match Played', 'All Team Total Goal', 'Lig Tipi','Total Cumulative Goal Count Ratio',
                            'Total Cumulative Goal Defeated Ratio']
    home_team_df.loc[:, 'Home/Away'] = 'Home'
    
    away_team_df = sheet_df[['Away Team', 'Away Team Goal Count', 'Away Team Goal Defeated', 'Cumulative Away Team Goal Count', 'Cumulative Away Team Goal Defeated',
                             'Cumulative Away Team Average', 'Cumulative Away Team Point', 'Cumulative Away Team Match Played',
                             'Cumulative Away Team Win', 'Cumulative Away Team Draw', 'Cumulative Away Team Loss',
                             'Cumulative Away Team Point Ratio', 'Away Win', 'Away Draw', 'Away Loss', 'Lig ID', 'Game Week', 
                             'Away Team Point', 'Away Team Average', 'Cumulative Away Team Match Played', 'All Team Total Goal', 'Lig Tipi','Total Cumulative Away Team Goal Count Ratio',
                             'Total Cumulative Away Team Goal Defeated Ratio']].copy()
    
    away_team_df.columns = ['Team Name', 'Goal Count', 'Goal Defeated', 'Cumulative Goal Count', 'Cumulative Goal Defeated', 'Cumulative Average',
                            'Cumulative Point', 'Cumulative Match Played', 'Cumulative Win', 'Cumulative Draw',
                            'Cumulative Loss', 'Cumulative Point Ratio', 'Win', 'Draw', 'Loss', 'Lig ID', 'Game Week', 
                            'Point', 'Average', 'Match Played', 'All Team Total Goal', 'Lig Tipi','Total Cumulative Goal Count Ratio',
                            'Total Cumulative Goal Defeated Ratio']
    away_team_df.loc[:, 'Home/Away'] = 'Away'
    
    # Combine home and away team data
    combined_df = pd.concat([home_team_df, away_team_df], ignore_index=True)
    
    # Remove any duplicates in case the same team appears multiple times in the same sheet
    combined_df = combined_df.drop_duplicates(subset=['Team Name', 'Lig ID', 'Game Week', 'Home/Away'])
    
    # Sort the DataFrame by 'Cumulative Point Ratio' in descending order
    combined_df = combined_df.sort_values(by='Cumulative Point Ratio', ascending=False).reset_index(drop=True)
    
    # Add a new Rank column based on the sorted order
    combined_df['Rank'] = combined_df.index + 1
    
    # Store the processed DataFrame in the dictionary with the sheet name as the key
    processed_data[sheet_name] = combined_df

# Create a new Excel writer object
output_path = 'Mod8.xlsx'
with pd.ExcelWriter(output_path) as writer:
    # Write each processed DataFrame to its respective sheet
    for sheet_name, processed_df in processed_data.items():
        processed_df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Process completed, please check '{output_path}'.")

