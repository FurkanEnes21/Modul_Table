import pandas as pd

# Load the output file
output_file = 'Modul9_Genel_sıralama_tablosu.xlsx'
output_df = pd.read_excel(output_file, sheet_name=None)

# Create an Excel writer
writer = pd.ExcelWriter('Final_Modul9_Genel_sıralama_tablosu.xlsx', engine='xlsxwriter')

# Iterate over each sheet in the output file
for sheet_name, weekly_summary in output_df.items():
    # Ensure the DataFrame has the necessary columns
    if 'Pre-Home Rank' in weekly_summary.columns and 'Pre-Away Rank' in weekly_summary.columns:
        # Create columns for storing updated stats
        weekly_summary['Home Team Goal Count'] = 0
        weekly_summary['Home Team Goal Defeated'] = 0
        weekly_summary['Home Team Average'] = 0
        weekly_summary['Home Team Point'] = 0
        weekly_summary['Away Team Goal Count'] = 0
        weekly_summary['Away Team Goal Defeated'] = 0
        weekly_summary['Away Team Average'] = 0
        # weekly_summary['Away Team Point'] = 0
        weekly_summary['Away Team Rank'] = 0
        weekly_summary['Away Team Rank Diff'] = 0
        weekly_summary['Away Team Total Rank Diff'] = 0
        weekly_summary['Match Played'] = 0
        
        # Adjust stats based on Pre-Home Rank and Pre-Away Rank
        for index, row in weekly_summary.iterrows():
            pre_home_rank = row['Pre-Home Rank']
            pre_away_rank = row['Pre-Away Rank']
            if pd.notna(pre_home_rank) and pd.notna(pre_away_rank):  # Ensure ranks are not NaN
                if pre_home_rank < pre_away_rank:
                    # Home team has a lower rank (higher rank number)
                    weekly_summary.at[index, 'Away Team Goal Count'] = row['Away Goals']
                    weekly_summary.at[index, 'Away Team Goal Defeated'] = row['Home Goals']
                    weekly_summary.at[index, 'Away Team Average'] = row['Away Team Average'] = row['Away Goals'] - row['Home Goals']
                    weekly_summary.at[index, 'Away Team Average']
                    weekly_summary.at[index, 'Away Team Point'] = row['Away Team Point']
                    weekly_summary.at[index, 'Away Team Rank'] = row['Away Team Rank']
                    weekly_summary.at[index, 'Away Team Rank Diff'] = row['Away Team Rank Diff']
                    weekly_summary.at[index, 'Away Team Total Rank Diff'] = row['Away Team Total Rank Diff']
                    weekly_summary.at[index, 'Match Played'] = 1
                else:
                    # Away team has a lower rank (higher rank number)
                    weekly_summary.at[index, 'Home Team Goal Count'] = row['Home Goals'] = 0
                    weekly_summary.at[index, 'Home Team Goal Defeated'] = row['Away Goals'] = 0
                    weekly_summary.at[index, 'Home Team Average'] = row['Home Team Average'] = row['Home Goals'] - row['Away Goals']
                    weekly_summary.at[index, 'Home Team Point'] = row['Home Team Point'] = 0
                    weekly_summary.at[index, 'Home Team Rank'] = row['Home Team Rank'] = 0
                    weekly_summary.at[index, 'Home Team Rank Diff'] = row['Home Team Rank Diff'] = 0
                    weekly_summary.at[index, 'Home Team Total Rank Diff'] = row['Home Team Total Rank Diff'] = 0
                    weekly_summary.at[index, 'Match Played'] = 0

    # Write the updated DataFrame to the new Excel file
    weekly_summary.to_excel(writer, sheet_name=sheet_name, index=False)

# Complete the writing process
writer.close()

print("Process completed, please check 'Final_Modul9_Genel_sıralama_tablosu.xlsx'.")