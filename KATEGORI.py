

# import pandas as pd
# from tqdm import tqdm

# # Read Excel files
# df_ham = pd.read_excel('Güncel_ham_dosya1.xlsx')
# df_mod1 = pd.read_excel('Güncellenmiş_Mod1_sıralama_tablosu.xlsx')
# df_mod2 = pd.read_excel('Güncellenmiş_Mod2_sıralama_tablosu.xlsx')
# df_mod3 = pd.read_excel('Güncellenmiş_Mod3_sıralama_tablosu.xlsx')
# df_mod4 = pd.read_excel('Güncellenmiş_Mod4_sıralama_tablosu.xlsx')
# df_mod5 = pd.read_excel('Güncellenmiş_Mod5_sıralama_tablosu.xlsx')
# df_mod6 = pd.read_excel('Güncellenmiş_Mod6_sıralama_tablosu.xlsx')
# df_mod7 = pd.read_excel('Güncellenmiş_Mod7_sıralama_tablosu.xlsx')
# df_mod8 = pd.read_excel('Güncellenmiş_Mod8_sıralama_tablosu.xlsx')
# df_mod9 = pd.read_excel('Güncellenmiş_Mod9_sıralama_tablosu.xlsx')

# # Manually set column names
# df_ham.columns = ['Lig ID', 'Match ID', 'Game Week', 'home_team_name', 'away_team_name', 'Home Goals', 'Away Goals', 'Goal Times', 'Number of Goals', 'Match Status', 'Goal Timing', 'File Name']
# df_ham = df_ham[1:]  # Remove the first row

# # Convert columns to appropriate data types
# df_ham['Lig ID'] = df_ham['Lig ID'].astype(str)
# df_ham['Game Week'] = df_ham['Game Week'].astype(int)
# df_ham['home_team_name'] = df_ham['home_team_name'].astype(str)
# df_ham['away_team_name'] = df_ham['away_team_name'].astype(str)
# df_ham['Goal Timing'] = df_ham['Goal Timing'].astype(str)

# # Extract values into lists
# a = df_ham['Lig ID'].tolist()
# b = df_ham['Game Week'].tolist()
# c_home = df_ham['home_team_name'].tolist()
# c_away = df_ham['away_team_name'].tolist()
# d = df_ham['Goal Timing'].tolist()

# # Function to match rows
# def match_rows(df_mod):
#     return df_mod[(df_mod['Lig ID'].astype(str).isin(a)) &
#                   (df_mod['Game Week'].astype(int).isin(b)) &
#                   (df_mod['Team Name'].astype(str).isin(c_home + c_away)) &
#                   (df_mod['Goal Timing'].astype(str).isin(d))]

# # Match rows for each file
# matched_rows_mod1 = match_rows(df_mod1)
# matched_rows_mod2 = match_rows(df_mod2)
# matched_rows_mod3 = match_rows(df_mod3)
# matched_rows_mod4 = match_rows(df_mod4)
# matched_rows_mod5 = match_rows(df_mod5)
# matched_rows_mod6 = match_rows(df_mod6)
# matched_rows_mod7 = match_rows(df_mod7)
# matched_rows_mod8 = match_rows(df_mod8)
# matched_rows_mod9 = match_rows(df_mod9)

# # Function to calculate new columns for mod1
# def calculate_b_columns_mod1(df):
#     min_rank_idx = df['Rank'].astype(float).idxmin()
#     max_rank_idx = df['Rank'].astype(float).idxmax()
    
#     b183 = df.at[min_rank_idx, 'Point'] - df.at[max_rank_idx, 'Point']
#     b184 = df['All Team Total Goal']
#     b185 = len(df) / 2 / b184
#     b186 = df.at[min_rank_idx, 'Cumulative Goal Count'] - df.at[max_rank_idx, 'Cumulative Goal Count'] 
#     b187 = df.at[min_rank_idx, 'Cumulative Goal Defeated'] - df.at[max_rank_idx, 'Cumulative Goal Defeated'] 
#     b188 = df.at[min_rank_idx, 'Cumulative Average'] - df.at[max_rank_idx, 'Cumulative Average'] 
#     b189 = df['Rank Diff']
#     b190 = df['Total Rank Diff']

#     return pd.Series([b183, b184, b185, b186, b187, b188, b189, b190], index=['B183', 'B184', 'B185', 'B186', 'B187', 'B188', 'B189', 'B190'])

# # Add new columns to matched rows of mod1
# b_columns_mod1 = calculate_b_columns_mod1(matched_rows_mod1)
# for col, val in b_columns_mod1.items():
#     matched_rows_mod1[col] = val

# # Function to calculate new columns for mod2 to mod9
# def calculate_b_columns_mod2_9(df, base_col):
#     min_rank_idx = df['Rank'].astype(float).idxmin()
#     max_rank_idx = df['Rank'].astype(float).idxmax()
    
#     b_diff = df.at[min_rank_idx, 'Point'] - df.at[max_rank_idx, 'Point']
#     all_team_total_goal = df['All Team Total Goal']
#     len_df_half = len(df) / 2 / all_team_total_goal
#     cumulative_goal_count_diff = df.at[min_rank_idx, 'Cumulative Goal Count'] - df.at[max_rank_idx, 'Cumulative Goal Count'] 
#     cumulative_goal_defeated_diff = df.at[min_rank_idx, 'Cumulative Goal Defeated'] - df.at[max_rank_idx, 'Cumulative Goal Defeated'] 
#     cumulative_average_diff = df.at[min_rank_idx, 'Cumulative Average'] - df.at[max_rank_idx, 'Cumulative Average'] 
#     rank_diff = df['Rank Diff']
#     total_rank_diff = df['Total Rank Diff']

#     return pd.Series([
#         b_diff, all_team_total_goal, len_df_half, cumulative_goal_count_diff, 
#         cumulative_goal_defeated_diff, cumulative_average_diff, rank_diff, total_rank_diff
#     ], index=[f'B{base_col+2}', f'B{base_col+3}', f'B{base_col+4}', f'B{base_col+5}', f'B{base_col+6}', f'B{base_col+7}', f'B{base_col+8}', f'B{base_col+9}'])

# # Add new columns to matched rows of mod2 to mod9
# for i, df_mod in enumerate([matched_rows_mod2, matched_rows_mod3, matched_rows_mod4, matched_rows_mod5, matched_rows_mod6, matched_rows_mod7, matched_rows_mod8, matched_rows_mod9]):
#     base_col = 191 + i * 10
#     df_mod[f'B{base_col}'] = df_mod['Match Play']
#     df_mod[f'B{base_col+1}'] = df_mod['Cumulative Point']
#     b_columns_mod2_9 = calculate_b_columns_mod2_9(df_mod, base_col)
#     for col, val in b_columns_mod2_9.items():
#         df_mod[col] = val

# # Define new and existing columns
# new_columns_mod1 = ['Game Week', 'Cumulative Point', 'B183', 'B184', 'B185', 'B186', 'B187', 'B188', 'B189', 'B190']
# existing_columns_mod1 = ['Game Week', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 'Total Cumulative Goal Count Ratio', 
#                          'Cumulative Goal Defeated', 'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 'Rank Diff', 
#                          'Total Rank Diff']

# # Create a loop to define columns B191 to B279
# columns_mod2_9 = []
# for i in range(191, 271, 10):  # Updated to include 270
#     columns_mod2_9.extend([f'B{i}', f'B{i+1}'] + [f'B{j}' for j in range(i+2, i+10)])

# # Shift dataframe to insert a blank row at the top
# def shift_dataframe(mod_df, columns):
#     empty_row = pd.DataFrame([[''] * len(columns)], columns=columns)
#     return pd.concat([empty_row, mod_df.reset_index(drop=True)], ignore_index=True)

# # Apply the shift to each matched rows DataFrame
# modul_tablo_shifted_mod1 = shift_dataframe(matched_rows_mod1[existing_columns_mod1 + new_columns_mod1], existing_columns_mod1 + new_columns_mod1)
# modul_tablo_shifted_mod2 = shift_dataframe(matched_rows_mod2[columns_mod2_9[:10]], columns_mod2_9[:10])
# modul_tablo_shifted_mod3 = shift_dataframe(matched_rows_mod3[columns_mod2_9[10:20]], columns_mod2_9[10:20])
# modul_tablo_shifted_mod4 = shift_dataframe(matched_rows_mod4[columns_mod2_9[20:30]], columns_mod2_9[20:30])
# modul_tablo_shifted_mod5 = shift_dataframe(matched_rows_mod5[columns_mod2_9[30:40]], columns_mod2_9[30:40])
# modul_tablo_shifted_mod6 = shift_dataframe(matched_rows_mod6[columns_mod2_9[40:50]], columns_mod2_9[40:50])
# modul_tablo_shifted_mod7 = shift_dataframe(matched_rows_mod7[columns_mod2_9[50:60]], columns_mod2_9[50:60])
# modul_tablo_shifted_mod8 = shift_dataframe(matched_rows_mod8[columns_mod2_9[60:70]], columns_mod2_9[60:70])
# modul_tablo_shifted_mod9 = shift_dataframe(matched_rows_mod9[columns_mod2_9[70:80]], columns_mod2_9[70:80])

# # Concatenate all shifted dataframes
# final_df = pd.concat([
#     modul_tablo_shifted_mod1, modul_tablo_shifted_mod2, modul_tablo_shifted_mod3,
#     modul_tablo_shifted_mod4, modul_tablo_shifted_mod5, modul_tablo_shifted_mod6,
#     modul_tablo_shifted_mod7, modul_tablo_shifted_mod8, modul_tablo_shifted_mod9
# ], axis=1)

# # Save the final DataFrame to an Excel file
# output_path = 'Modul_Tablo.xlsx'
# final_df.to_excel(output_path, index=False)

# print("Process completed and results are written to Modul_Tablo.xlsx")








# import pandas as pd
# from tqdm import tqdm

# # Read Excel files
# df_ham = pd.read_excel('Güncel_ham_dosya1.xlsx')
# df_mod1 = pd.read_excel('Mod1.xlsx')
# df_mod2 = pd.read_excel('Mod2.xlsx')
# df_mod3 = pd.read_excel('Mod3.xlsx')
# df_mod4 = pd.read_excel('Mod4.xlsx')
# df_mod5 = pd.read_excel('Mod5.xlsx')
# df_mod6 = pd.read_excel('Mod6.xlsx')
# df_mod7 = pd.read_excel('Mod7.xlsx')
# df_mod8 = pd.read_excel('Mod8.xlsx')
# df_mod9 = pd.read_excel('Mod9.xlsx')

# # Manually set column names
# df_ham.columns = ['File_Name', 'ID', 'Game Week', 'home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count', 'home_team_goal_timings', 'away_team_goal_timings', 'status', 'Lig ID', 'Goal Timing']
# df_ham = df_ham[1:]  # Remove the first row

# # Convert columns to appropriate data types
# df_ham['Lig ID'] = df_ham['Lig ID'].astype(str)
# df_ham['Game Week'] = df_ham['Game Week'].astype(int)
# df_ham['home_team_name'] = df_ham['home_team_name'].astype(str)
# df_ham['away_team_name'] = df_ham['away_team_name'].astype(str)
# df_ham['Goal Timing'] = df_ham['Goal Timing'].astype(str)

# # Extract values into lists
# a = df_ham['Lig ID'].tolist()
# b = df_ham['Game Week'].tolist()
# c_home = df_ham['home_team_name'].tolist()
# c_away = df_ham['away_team_name'].tolist()
# d = df_ham['Goal Timing'].tolist()

# # Function to match rows
# def match_rows(df_mod):
#     return df_mod[(df_mod['Lig ID'].astype(str).isin(a)) &
#                   (df_mod['Game Week'].astype(int).isin(b)) &
#                   (df_mod['Team Name'].astype(str).isin(c_home + c_away)) &
#                   (df_mod['Goal Timing'].astype(str).isin(d))]

# # Match rows for each file
# matched_rows_mod1 = match_rows(df_mod1)
# matched_rows_mod2 = match_rows(df_mod2)
# matched_rows_mod3 = match_rows(df_mod3)
# matched_rows_mod4 = match_rows(df_mod4)
# matched_rows_mod5 = match_rows(df_mod5)
# matched_rows_mod6 = match_rows(df_mod6)
# matched_rows_mod7 = match_rows(df_mod7)
# matched_rows_mod8 = match_rows(df_mod8)
# matched_rows_mod9 = match_rows(df_mod9)

# # Function to calculate new columns for mod1
# def calculate_b_columns_mod1(df):
#     if df.empty or df['Rank'].dropna().empty:
#         return pd.Series([None] * 8, index=['B183', 'B184', 'B185', 'B186', 'B187', 'B188', 'B189', 'B190'])

#     min_rank_idx = df['Rank'].astype(float).idxmin()
#     max_rank_idx = df['Rank'].astype(float).idxmax()
    
#     b183 = df.at[min_rank_idx, 'Point'] - df.at[max_rank_idx, 'Point']
#     b184 = df['All Team Total Goal']
#     b185 = len(df) / 2 / b184
#     b186 = df.at[min_rank_idx, 'Cumulative Goal Count'] - df.at[max_rank_idx, 'Cumulative Goal Count'] 
#     b187 = df.at[min_rank_idx, 'Cumulative Goal Defeated'] - df.at[max_rank_idx, 'Cumulative Goal Defeated'] 
#     b188 = df.at[min_rank_idx, 'Cumulative Average'] - df.at[max_rank_idx, 'Cumulative Average'] 
#     b189 = df['Rank Diff']
#     b190 = df['Total Rank Diff']

#     return pd.Series([b183, b184, b185, b186, b187, b188, b189, b190], index=['B183', 'B184', 'B185', 'B186', 'B187', 'B188', 'B189', 'B190'])

# # Add new columns to matched rows of mod1
# b_columns_mod1 = calculate_b_columns_mod1(matched_rows_mod1)
# for col, val in b_columns_mod1.items():
#     matched_rows_mod1[col] = val

# # Function to calculate new columns for mod2 to mod9
# def calculate_b_columns_mod2_9(df, base_col):
#     if df.empty or df['Rank'].dropna().empty:
#         return pd.Series([None] * 8, index=[f'B{base_col+2}', f'B{base_col+3}', f'B{base_col+4}', f'B{base_col+5}', f'B{base_col+6}', f'B{base_col+7}', f'B{base_col+8}', f'B{base_col+9}'])
    
#     min_rank_idx = df['Rank'].astype(float).idxmin()
#     max_rank_idx = df['Rank'].astype(float).idxmax()
    
#     b_diff = df.at[min_rank_idx, 'Point'] - df.at[max_rank_idx, 'Point']
#     all_team_total_goal = df['All Team Total Goal']
#     len_df_half = len(df) / 2 / all_team_total_goal
#     cumulative_goal_count_diff = df.at[min_rank_idx, 'Cumulative Goal Count'] - df.at[max_rank_idx, 'Cumulative Goal Count'] 
#     cumulative_goal_defeated_diff = df.at[min_rank_idx, 'Cumulative Goal Defeated'] - df.at[max_rank_idx, 'Cumulative Goal Defeated'] 
#     cumulative_average_diff = df.at[min_rank_idx, 'Cumulative Average'] - df.at[max_rank_idx, 'Cumulative Average'] 
#     rank_diff = df['Rank Diff']
#     total_rank_diff = df['Total Rank Diff']

#     return pd.Series([
#         b_diff, all_team_total_goal, len_df_half, cumulative_goal_count_diff, 
#         cumulative_goal_defeated_diff, cumulative_average_diff, rank_diff, total_rank_diff
#     ], index=[f'B{base_col+2}', f'B{base_col+3}', f'B{base_col+4}', f'B{base_col+5}', f'B{base_col+6}', f'B{base_col+7}', f'B{base_col+8}', f'B{base_col+9}'])

# # Add new columns to matched rows of mod2 to mod9
# for i, df_mod in enumerate([matched_rows_mod2, matched_rows_mod3, matched_rows_mod4, matched_rows_mod5, matched_rows_mod6, matched_rows_mod7, matched_rows_mod8, matched_rows_mod9]):
#     base_col = 191 + i * 10
#     df_mod[f'B{base_col}'] = df_mod['Match Played']
#     df_mod[f'B{base_col+1}'] = df_mod['Cumulative Point']
#     b_columns_mod2_9 = calculate_b_columns_mod2_9(df_mod, base_col)
#     for col, val in b_columns_mod2_9.items():
#         df_mod[col] = val

# # Define new and existing columns
# new_columns_mod1 = ['Game Week', 'Cumulative Point', 'B183', 'B184', 'B185', 'B186', 'B187', 'B188', 'B189', 'B190']
# existing_columns_mod1 = ['Game Week', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 'Total Cumulative Goal Count Ratio', 
#                          'Cumulative Goal Defeated', 'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 'Rank Diff', 
#                          'Total Rank Diff']

# # Create a loop to define columns B191 to B279
# columns_mod2_9 = []
# for i in range(191, 271, 10):  # Updated to include 270
#     columns_mod2_9.extend([f'B{i}', f'B{i+1}'] + [f'B{j}' for j in range(i+2, i+10)])

# # Shift dataframe to insert a blank row at the top
# def shift_dataframe(mod_df, columns):
#     empty_row = pd.DataFrame([[''] * len(columns)], columns=columns)
#     return pd.concat([empty_row, mod_df.reset_index(drop=True)], ignore_index=True)

# # Apply the shift to each matched rows DataFrame
# modul_tablo_shifted_mod1 = shift_dataframe(matched_rows_mod1[existing_columns_mod1 + new_columns_mod1], existing_columns_mod1 + new_columns_mod1)
# modul_tablo_shifted_mod2 = shift_dataframe(matched_rows_mod2[columns_mod2_9[:10]], columns_mod2_9[:10])
# modul_tablo_shifted_mod3 = shift_dataframe(matched_rows_mod3[columns_mod2_9[10:20]], columns_mod2_9[10:20])
# modul_tablo_shifted_mod4 = shift_dataframe(matched_rows_mod4[columns_mod2_9[20:30]], columns_mod2_9[20:30])
# modul_tablo_shifted_mod5 = shift_dataframe(matched_rows_mod5[columns_mod2_9[30:40]], columns_mod2_9[30:40])
# modul_tablo_shifted_mod6 = shift_dataframe(matched_rows_mod6[columns_mod2_9[40:50]], columns_mod2_9[40:50])
# modul_tablo_shifted_mod7 = shift_dataframe(matched_rows_mod7[columns_mod2_9[50:60]], columns_mod2_9[50:60])
# modul_tablo_shifted_mod8 = shift_dataframe(matched_rows_mod8[columns_mod2_9[60:70]], columns_mod2_9[60:70])
# modul_tablo_shifted_mod9 = shift_dataframe(matched_rows_mod9[columns_mod2_9[70:80]], columns_mod2_9[70:80])

# # Concatenate all shifted dataframes
# final_df = pd.concat([
#     modul_tablo_shifted_mod1, modul_tablo_shifted_mod2, modul_tablo_shifted_mod3,
#     modul_tablo_shifted_mod4, modul_tablo_shifted_mod5, modul_tablo_shifted_mod6,
#     modul_tablo_shifted_mod7, modul_tablo_shifted_mod8, modul_tablo_shifted_mod9
# ], axis=1)

# # Save the final DataFrame to an Excel file
# output_path = 'Modul_Tablos.xlsx'
# final_df.to_excel(output_path, index=False)

# print("Process completed and results are written to Modul_Tablo.xlsx")










import pandas as pd
from tqdm import tqdm

# Read Excel files
df_ham = pd.read_excel('Güncel_ham_dosya1.xlsx')
df_mod1 = pd.read_excel('Güncellenmiş_Mod1_sıralama_tablosu.xlsx')
df_mod2 = pd.read_excel('Güncellenmiş_Mod2_sıralama_tablosu.xlsx')
df_mod3 = pd.read_excel('Güncellenmiş_Mod3_sıralama_tablosu.xlsx')
df_mod4 = pd.read_excel('Güncellenmiş_Mod4_sıralama_tablosu.xlsx')
df_mod5 = pd.read_excel('Güncellenmiş_Mod5_sıralama_tablosu.xlsx')
df_mod6 = pd.read_excel('Güncellenmiş_Mod6_sıralama_tablosu.xlsx')
df_mod7 = pd.read_excel('Güncellenmiş_Mod7_sıralama_tablosu.xlsx')
df_mod8 = pd.read_excel('Güncellenmiş_Mod8_sıralama_tablosu.xlsx')
df_mod9 = pd.read_excel('Güncellenmiş_Mod9_sıralama_tablosu.xlsx')

# Manually set column names
df_ham = df_ham.reindex(columns=['File_Name', 'Lig ID', 'ID', 'home_team_name', 'away_team_name',
                  'home_team_goal_count', 'away_team_goal_count', 'Game Week', 
                  'home_team_goal_timings', 'away_team_goal_timings', 'status', 
                  'Goal Timing'])

df_ham = df_ham[1:]  # Remove the first row

# Convert columns to appropriate data types
df_ham['Lig ID'] = df_ham['Lig ID'].astype(str)
df_ham['Game Week'] = df_ham['Game Week'].astype(str)
df_ham['home_team_name'] = df_ham['home_team_name'].astype(str)
df_ham['away_team_name'] = df_ham['away_team_name'].astype(str)
df_ham['Goal Timing'] = df_ham['Goal Timing'].astype(str)

# Extract values into lists
a = df_ham['Lig ID'].tolist()
b = df_ham['Game Week'].tolist()
c_home = df_ham['home_team_name'].tolist()
c_away = df_ham['away_team_name'].tolist()
d = df_ham['Goal Timing'].tolist()

# Function to match rows
def match_rows(df_mod):
    # Check for non-empty values in 'Game Week' before using them
    non_empty_game_weeks = df_mod['Game Week'].dropna().astype(str).tolist()
    return df_mod[(df_mod['Lig ID'].astype(str).isin(a)) &
                  # Include condition for 'Game Week' if not empty
                  (df_mod['Game Week'].astype(str).isin(non_empty_game_weeks)) &  # Modify this line to filter only non-empty values
                  (df_mod['Team Name'].astype(str).isin(c_home + c_away)) &
                  (df_mod['Goal Timing'].astype(str).isin(d))]

# Match rows for each file
matched_rows_mod1 = match_rows(df_mod1)
matched_rows_mod2 = match_rows(df_mod2)
matched_rows_mod3 = match_rows(df_mod3)
matched_rows_mod4 = match_rows(df_mod4)
matched_rows_mod5 = match_rows(df_mod5)
matched_rows_mod6 = match_rows(df_mod6)
matched_rows_mod7 = match_rows(df_mod7)
matched_rows_mod8 = match_rows(df_mod8)
matched_rows_mod9 = match_rows(df_mod9)

# Function to calculate new columns for mod1
def calculate_b_columns_mod1(df):
    if df.empty:
        return pd.Series([None] * 8, index=['B183', 'B184', 'B185', 'B186', 'B187', 'B188', 'B189', 'B190'])
    
    min_rank_idx = df['Rank'].astype(float).idxmin()
    max_rank_idx = df['Rank'].astype(float).idxmax()
    
    b183 = df.at[min_rank_idx, 'Point'] - df.at[max_rank_idx, 'Point']
    b184 = df['All Team Total Goal']
    b185 = len(df) / 2 / b184
    b186 = df.at[min_rank_idx, 'Cumulative Goal Count'] - df.at[max_rank_idx, 'Cumulative Goal Count'] 
    b187 = df.at[min_rank_idx, 'Cumulative Goal Defeated'] - df.at[max_rank_idx, 'Cumulative Goal Defeated'] 
    b188 = df.at[min_rank_idx, 'Cumulative Average'] - df.at[max_rank_idx, 'Cumulative Average'] 
    b189 = df['Rank Diff']
    b190 = df['Total Rank Diff']

    return pd.Series([b183, b184, b185, b186, b187, b188, b189, b190], index=['B183', 'B184', 'B185', 'B186', 'B187', 'B188', 'B189', 'B190'])

# Add new columns to matched rows of mod1
b_columns_mod1 = calculate_b_columns_mod1(matched_rows_mod1)
for col, val in b_columns_mod1.items():
    matched_rows_mod1[col] = val

def calculate_b_columns_mod2_9(df, base_col):
    if df.empty or df['Rank'].isnull().all():
        # Return a series with None or appropriate default values if the dataframe is empty or Rank column is invalid
        return pd.Series([None] * 8, index=[f'B{base_col+2}', f'B{base_col+3}', f'B{base_col+4}', f'B{base_col+5}', f'B{base_col+6}', f'B{base_col+7}', f'B{base_col+8}', f'B{base_col+9}'])
    
    min_rank_idx = df['Rank'].astype(float).idxmin()
    max_rank_idx = df['Rank'].astype(float).idxmax()
    
    b_diff = df.at[min_rank_idx, 'Point'] - df.at[max_rank_idx, 'Point']
    all_team_total_goal = df['All Team Total Goal']
    len_df_half = len(df) / 2 / all_team_total_goal
    cumulative_goal_count_diff = df.at[min_rank_idx, 'Cumulative Goal Count'] - df.at[max_rank_idx, 'Cumulative Goal Count'] 
    cumulative_goal_defeated_diff = df.at[min_rank_idx, 'Cumulative Goal Defeated'] - df.at[max_rank_idx, 'Cumulative Goal Defeated'] 
    cumulative_average_diff = df.at[min_rank_idx, 'Cumulative Average'] - df.at[max_rank_idx, 'Cumulative Average'] 
    rank_diff = df['Rank Diff']
    total_rank_diff = df['Total Rank Diff']

    return pd.Series([
        b_diff, all_team_total_goal, len_df_half, cumulative_goal_count_diff, 
        cumulative_goal_defeated_diff, cumulative_average_diff, rank_diff, total_rank_diff
    ], index=[f'B{base_col+2}', f'B{base_col+3}', f'B{base_col+4}', f'B{base_col+5}', f'B{base_col+6}', f'B{base_col+7}', f'B{base_col+8}', f'B{base_col+9}'])

# Add new columns to matched rows of mod2 to mod9
for i, df_mod in enumerate([matched_rows_mod2, matched_rows_mod3, matched_rows_mod4, matched_rows_mod5, matched_rows_mod6, matched_rows_mod7, matched_rows_mod8, matched_rows_mod9]):
    base_col = 191 + i * 10
    df_mod[f'B{base_col}'] = df_mod['Match Played']
    df_mod[f'B{base_col+1}'] = df_mod['Cumulative Point']
    b_columns_mod2_9 = calculate_b_columns_mod2_9(df_mod, base_col)
    for col, val in b_columns_mod2_9.items():
        df_mod[col] = val

# Define new and existing columns
new_columns_mod1 = ['Game Week', 'ID','Cumulative Point', 'B183', 'B184', 'B185', 'B186', 'B187', 'B188', 'B189', 'B190']
existing_columns_mod1 = ['Game Week', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 'Total Cumulative Goal Count Ratio', 
                         'Cumulative Goal Defeated', 'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 'Rank Diff', 
                         'Total Rank Diff','Team Name']

# Create a loop to define columns B191 to B279
columns_mod2_9 = []
for i in range(191, 271, 10):  # Updated to include 270
    columns_mod2_9.extend([f'B{i}', f'B{i+1}'] + [f'B{j}' for j in range(i+2, i+10)])

# Shift dataframe to insert a blank row at the top
def shift_dataframe(mod_df, columns):
    empty_row = pd.DataFrame([[''] * len(columns)], columns=columns)
    return pd.concat([empty_row, mod_df.reset_index(drop=True)], ignore_index=True)

# Apply the shift to each matched rows DataFrame
modul_tablo_shifted_mod1 = shift_dataframe(matched_rows_mod1[existing_columns_mod1 + new_columns_mod1], existing_columns_mod1 + new_columns_mod1)
modul_tablo_shifted_mod2 = shift_dataframe(matched_rows_mod2[columns_mod2_9[:10]], columns_mod2_9[:10])
modul_tablo_shifted_mod3 = shift_dataframe(matched_rows_mod3[columns_mod2_9[10:20]], columns_mod2_9[10:20])
modul_tablo_shifted_mod4 = shift_dataframe(matched_rows_mod4[columns_mod2_9[20:30]], columns_mod2_9[20:30])
modul_tablo_shifted_mod5 = shift_dataframe(matched_rows_mod5[columns_mod2_9[30:40]], columns_mod2_9[30:40])
modul_tablo_shifted_mod6 = shift_dataframe(matched_rows_mod6[columns_mod2_9[40:50]], columns_mod2_9[40:50])
modul_tablo_shifted_mod7 = shift_dataframe(matched_rows_mod7[columns_mod2_9[50:60]], columns_mod2_9[50:60])
modul_tablo_shifted_mod8 = shift_dataframe(matched_rows_mod8[columns_mod2_9[60:70]], columns_mod2_9[60:70])
modul_tablo_shifted_mod9 = shift_dataframe(matched_rows_mod9[columns_mod2_9[70:80]], columns_mod2_9[70:80])

# Concatenate all shifted dataframes
final_df = pd.concat([
    modul_tablo_shifted_mod1, modul_tablo_shifted_mod2, modul_tablo_shifted_mod3,
    modul_tablo_shifted_mod4, modul_tablo_shifted_mod5, modul_tablo_shifted_mod6,
    modul_tablo_shifted_mod7, modul_tablo_shifted_mod8, modul_tablo_shifted_mod9
], axis=1)

# Save the final DataFrame to an Excel file
output_path = 'Modul_Tablo.xlsx'
final_df.to_excel(output_path, index=False)

print("Process completed and results are written to Modul_Tablo.xlsx")



