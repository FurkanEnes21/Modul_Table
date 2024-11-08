import os
import pandas as pd
from datetime import datetime
import time

def update_goal_timings(df):
    range_defs_home = ["0-30-home", "0-45-home", "0-90-home",
                        "15-45-home", "15-75-home", "15-90-home",
                        "30-90-home",
                        "45-75-home", "45-90-home"]

    range_defs_away = ["0-30-away", "0-45-away","0-90-away",
                        "15-45-away","15-75-away", "15-90-away",
                        "30-90-away",
                        "45-75-away", "45-90-away"]

    for range_def in range_defs_home:
        if range_def not in df.columns:
            df[range_def] = 0

    for range_def in range_defs_away:
        if range_def not in df.columns:
            df[range_def] = 0

    process_goal_timings(df, 'home_team_goal_timings', range_defs_home)
    process_goal_timings2(df, 'away_team_goal_timings', range_defs_away)

    return df

def process_goal_timings(df, column_name, range_defs):
    for index, row in df.iterrows():
        goal_timings = row[column_name]
        if pd.notna(goal_timings):
            goal_timings = str(goal_timings).replace('.', ',')
            parts = goal_timings.split(',')

            for part in parts:
                try:
                    minute_str = part.split("'")[0] if "'" in part else part.strip()
                    minute = int(minute_str)
                    for range_def in range_defs:
                        num_range = range_def.split('-home')[0]
                        range_start, range_end = map(int, num_range.split('-'))
                        if range_start <= minute <= range_end:
                            df.at[index, range_def] += 1
                except ValueError:
                    continue

def process_goal_timings2(df, column_name, range_defs):
    for index, row in df.iterrows():
        goal_timings = row[column_name]
        if pd.notna(goal_timings):
            goal_timings = str(goal_timings).replace('.', ',')
            parts = goal_timings.split(',')

            for part in parts:
                try:
                    minute_str = part.split("'")[0] if "'" in part else part.strip()
                    minute = int(minute_str)
                    for range_def in range_defs:
                        num_range = range_def.split('-away')[0]
                        range_start, range_end = map(int, num_range.split('-'))
                        if range_start <= minute <= range_end:
                            df.at[index, range_def] += 1
                except ValueError:
                    continue

# İşlenecek tek dosya yolu
input_file_path = 'C:/Users/Dell/Desktop/0-90/Güncel_ham_dosya1.xlsx'
output_file_path = 'C:/Users/Dell/Desktop/0-90/Güncel_ham_dosya1.xlsx'

start_time = time.time()

# Dosyanın ikinci sayfasını oku
sheet_names = pd.ExcelFile(input_file_path).sheet_names
sheet_name = sheet_names[0]
df = pd.read_excel(input_file_path, sheet_name=sheet_name)

# Gol zamanlamalarını güncelle
df = update_goal_timings(df)

# Güncellenmiş veriyi yeni bir Excel dosyasına kaydet
df.to_excel(output_file_path, index=False)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Dosya işlenmesi {elapsed_time:.2f} saniye sürdü.")







