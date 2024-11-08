# import pandas as pd
# import glob

# # Oranlar dosyasını yükle
# oranlar_df = pd.read_excel('Oranlar.xlsx')

# # Sadece incomplete olan maçları filtrele
# incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# # Output dosyalarını belirle
# output_files = glob.glob('output_home_*_Güncellenmiş_Mod*_sıralama_tablosu.xlsx')

# # İlgili parametreler
# params = [
#     'Match Played', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 
#     'Total Cumulative Goal Count Ratio', 'Cumulative Goal Defeated', 
#     'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 
#     'Rank Diff', 'Total Rank Diff'
# ]

# # Veri toplamak için boş bir DataFrame oluştur
# collected_data = pd.DataFrame()

# # Her bir incomplete maçı döngüye al
# for index, row in incomplete_matches.iterrows():
#     home_team = row['home_team_name']
#     away_team = row['away_team_name']
#     current_game_week = row['Game Week']
#     previous_game_week = current_game_week - 1

#     # Bu satır için toplanan verileri tutmak için bir dictionary oluştur
#     match_data = {
#         'home_team_name': home_team,
#         'away_team_name': away_team,
#         'Game Week': current_game_week
#     }

#     # Takım verilerinin bulunup bulunmadığını kontrol etmek için bayraklar
#     home_team_data_found = False
#     away_team_data_found = False

#     # Her bir output dosyasını döngüye al ve önce home_team_name verilerini çek
#     for output_file in output_files:
#         print(f"Processing file: {output_file}")
#         mod_df = pd.read_excel(output_file)

#         # Bir önceki oyun haftası ve ev sahibi takım için verileri filtrele
#         home_team_data = mod_df[(mod_df['Team Name'] == home_team) & (mod_df['Game Week'] == previous_game_week)]

#         # Ev sahibi takım için parametreleri topla
#         if not home_team_data.empty:
#             print(f"Found home team data for {home_team} in {output_file} for Game Week {previous_game_week}")
#             home_team_data_found = True  # Home team için veri bulunduğunu belirt
#             for param in params:
#                 match_data[f'{output_file}_home_{param}'] = home_team_data.iloc[0][param]
#         else:
#             print(f"No home team data found for {home_team} in {output_file} for Game Week {previous_game_week}")

#         # Bir önceki oyun haftası ve deplasman takımı için verileri filtrele
#         away_team_data = mod_df[(mod_df['Team Name'] == away_team) & (mod_df['Game Week'] == previous_game_week)]

#         # Deplasman takımı için parametreleri topla
#         if not away_team_data.empty:
#             print(f"Found away team data for {away_team} in {output_file} for Game Week {previous_game_week}")
#             away_team_data_found = True  # Away team için veri bulunduğunu belirt
#             for param in params:
#                 match_data[f'{output_file}_away_{param}'] = away_team_data.iloc[0][param]
#         else:
#             print(f"No away team data found for {away_team} in {output_file} for Game Week {previous_game_week}")
    
#     # Eğer her iki takım için de previous_game_week verisi mevcutsa, veriyi ekle
#     if home_team_data_found and away_team_data_found:
#         collected_data = collected_data._append(match_data, ignore_index=True)
#     else:
#         print(f"Skipping match between {home_team} and {away_team} for Game Week {previous_game_week} due to missing data.")

# # Toplanan verileri incomplete_matches DataFrame'ine birleştir
# final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name', 'Game Week'], how='right')

# # Son DataFrame'i yeni bir Excel dosyasına kaydet
# final_df.to_excel('incomplete_matches_with_previous_week_parameters.xlsx', index=False)

# print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters.xlsx' dosyası kaydedildi.")










# import pandas as pd

# # Oranlar dosyasını yükle
# oranlar_df = pd.read_excel('Oran_Tablosu.xlsx')

# # Sadece incomplete olan maçları filtrele
# incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# # İlgili parametreler
# params = [
#     'Match Played', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 
#     'Total Cumulative Goal Count Ratio', 'Cumulative Goal Defeated', 
#     'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 
#     'Rank Diff', 'Total Rank Diff'
# ]

# # Veri toplamak için boş bir DataFrame oluştur
# collected_data = pd.DataFrame()

# # Her bir incomplete maçı döngüye al
# for index, row in incomplete_matches.iterrows():
#     home_team = row['home_team_name']
#     away_team = row['away_team_name']
#     current_game_week = row['Game Week']
#     previous_game_week = current_game_week - 1

#     # Bu satır için toplanan verileri tutmak için bir dictionary oluştur
#     match_data = {
#         'home_team_name': home_team,
#         'away_team_name': away_team,
#         'Game Week': current_game_week
#     }

#     # Takım verilerinin bulunup bulunmadığını kontrol etmek için bayraklar
#     home_team_data_found = False
#     away_team_data_found = False

#     # Her bir output dosyasını döngüye al ve önce home_team_name verilerini çek
#     for mod_num in range(1, 10):  # 1'den 9'a kadar olan modları döngüye al
#         output_file = f'Güncellenmiş_Mod{mod_num}_sıralama_tablosu.xlsx'
#         print(f"Processing file: {output_file}")
#         mod_df = pd.read_excel(output_file)

#         # Bir önceki oyun haftası ve ev sahibi takım için verileri filtrele
#         home_team_data = mod_df[(mod_df['Team Name'] == home_team) & (mod_df['Game Week'] == previous_game_week)]

#         # Ev sahibi takım için parametreleri topla
#         if not home_team_data.empty:
#             print(f"Found home team data for {home_team} in {output_file} for Game Week {previous_game_week}")
#             home_team_data_found = True  # Home team için veri bulunduğunu belirt
#             for param in params:
#                 match_data[f'{output_file}_home_{param}'] = home_team_data.iloc[0][param]
#         else:
#             print(f"No home team data found for {home_team} in {output_file} for Game Week {previous_game_week}")

#         # Bir önceki oyun haftası ve deplasman takımı için verileri filtrele
#         away_team_data = mod_df[(mod_df['Team Name'] == away_team) & (mod_df['Game Week'] == previous_game_week)]

#         # Deplasman takımı için parametreleri topla
#         if not away_team_data.empty:
#             print(f"Found away team data for {away_team} in {output_file} for Game Week {previous_game_week}")
#             away_team_data_found = True  # Away team için veri bulunduğunu belirt
#             for param in params:
#                 match_data[f'{output_file}_away_{param}'] = away_team_data.iloc[0][param]
#         else:
#             print(f"No away team data found for {away_team} in {output_file} for Game Week {previous_game_week}")
    
#     # Eğer her iki takım için de previous_game_week verisi mevcutsa, veriyi ekle
#     if home_team_data_found and away_team_data_found:
#         collected_data = collected_data._append(match_data, ignore_index=True)
#     else:
#         print(f"Skipping match between {home_team} and {away_team} for Game Week {previous_game_week} due to missing data.")

# # Toplanan verileri incomplete_matches DataFrame'ine birleştir
# final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name', 'Game Week'], how='right')

# # Son DataFrame'i yeni bir Excel dosyasına kaydet
# final_df.to_excel('incomplete_matches_with_previous_week_parameters.xlsx', index=False)

# print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters.xlsx' dosyası kaydedildi.")





# import pandas as pd

# # Oranlar dosyasını yükle
# oranlar_df = pd.read_excel('Oran_Tablosu.xlsx')

# # Sadece incomplete olan maçları filtrele
# incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# # İlgili parametreler
# params = [
#     'Match Played', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 
#     'Total Cumulative Goal Count Ratio', 'Cumulative Goal Defeated', 
#     'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 
#     'Rank Diff', 'Total Rank Diff'
# ]

# # Veri toplamak için boş bir DataFrame oluştur
# collected_data = pd.DataFrame()

# # Her bir incomplete maçı döngüye al
# for index, row in incomplete_matches.iterrows():
#     home_team = row['home_team_name']
#     away_team = row['away_team_name']
#     current_game_week = row['Game Week']
#     previous_game_week = current_game_week - 1

#     # Bu satır için toplanan verileri tutmak için bir dictionary oluştur
#     match_data = {
#         'home_team_name': home_team,
#         'away_team_name': away_team,
#         'Game Week': current_game_week
#     }

#     # Takım verilerinin bulunup bulunmadığını kontrol etmek için bayraklar
#     home_team_data_found = False
#     away_team_data_found = False

#     # Her bir output dosyasını döngüye al ve önce home_team_name verilerini çek
#     for mod_num in range(1, 10):  # 1'den 9'a kadar olan modları döngüye al
#         output_file = f'Güncellenmiş_Mod{mod_num}_sıralama_tablosu.xlsx'
#         print(f"Processing file: {output_file}")
#         mod_df = pd.read_excel(output_file)

#         # Bir önceki oyun haftası ve ev sahibi takım için verileri filtrele
#         home_team_data = mod_df[(mod_df['Team Name'] == home_team) & (mod_df['Game Week'] == previous_game_week)]

#         # Ev sahibi takım için parametreleri ve ID'yi topla
#         if not home_team_data.empty:
#             print(f"Found home team data for {home_team} in {output_file} for Game Week {previous_game_week}")
#             home_team_data_found = True  # Home team için veri bulunduğunu belirt
#             match_data[f'{output_file}_home_ID'] = home_team_data.iloc[0]['ID']  # ID verisi ekle
#             for param in params:
#                 match_data[f'{output_file}_home_{param}'] = home_team_data.iloc[0][param]
#         else:
#             print(f"No home team data found for {home_team} in {output_file} for Game Week {previous_game_week}")

#         # Bir önceki oyun haftası ve deplasman takımı için verileri filtrele
#         away_team_data = mod_df[(mod_df['Team Name'] == away_team) & (mod_df['Game Week'] == previous_game_week)]

#         # Deplasman takımı için parametreleri ve ID'yi topla
#         if not away_team_data.empty:
#             print(f"Found away team data for {away_team} in {output_file} for Game Week {previous_game_week}")
#             away_team_data_found = True  # Away team için veri bulunduğunu belirt
#             match_data[f'{output_file}_away_ID'] = away_team_data.iloc[0]['ID']  # ID verisi ekle
#             for param in params:
#                 match_data[f'{output_file}_away_{param}'] = away_team_data.iloc[0][param]
#         else:
#             print(f"No away team data found for {away_team} in {output_file} for Game Week {previous_game_week}")
    
#     # Eğer her iki takım için de previous_game_week verisi mevcutsa, veriyi ekle
#     if home_team_data_found and away_team_data_found:
#         collected_data = collected_data._append(match_data, ignore_index=True)
#     else:
#         print(f"Skipping match between {home_team} and {away_team} for Game Week {previous_game_week} due to missing data.")

# # Toplanan verileri incomplete_matches DataFrame'ine birleştir
# final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name', 'Game Week'], how='right')

# # Son DataFrame'i yeni bir Excel dosyasına kaydet
# final_df.to_excel('incomplete_matches_with_previous_week_parameters2.xlsx', index=False)

# print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters.xlsx' dosyası kaydedildi.")









# import pandas as pd

# # Oranlar dosyasını yükle
# oranlar_df = pd.read_excel('Oran_Tablosu.xlsx')

# # Sadece incomplete olan maçları filtrele
# incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# # İlgili parametreler
# params = [
#     'Match Played', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 
#     'Total Cumulative Goal Count Ratio', 'Cumulative Goal Defeated', 
#     'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 
#     'Rank Diff', 'Total Rank Diff'
# ]

# # Veri toplamak için boş bir DataFrame oluştur
# collected_data = pd.DataFrame()

# # Her bir incomplete maçı döngüye al
# for index, row in incomplete_matches.iterrows():
#     home_team = row['home_team_name']
#     away_team = row['away_team_name']
#     current_game_week = row['Game Week']
#     previous_game_week = current_game_week - 1

#     # Bu satır için toplanan verileri tutmak için bir dictionary oluştur
#     match_data = {
#         'home_team_name': home_team,
#         'away_team_name': away_team,
#         'Game Week': current_game_week
#     }

#     # Takım verilerinin bulunup bulunmadığını kontrol etmek için bayraklar
#     home_team_data_found = False
#     away_team_data_found = False

#     # İlk olarak home_team_name verilerini topla
#     for mod_num in range(1, 10):  # 1'den 9'a kadar olan modları döngüye al
#         output_file = f'Güncellenmiş_Mod{mod_num}_sıralama_tablosu.xlsx'
#         print(f"Processing home team in file: {output_file}")
#         mod_df = pd.read_excel(output_file)

#         # Bir önceki oyun haftası ve ev sahibi takım için verileri filtrele
#         home_team_data = mod_df[(mod_df['Team Name'] == home_team) & (mod_df['Game Week'] == previous_game_week)]

#         # Ev sahibi takım için parametreleri ve ID'yi topla
#         if not home_team_data.empty:
#             print(f"Found home team data for {home_team} in {output_file} for Game Week {previous_game_week}")
#             home_team_data_found = True  # Home team için veri bulunduğunu belirt
#             match_data[f'{output_file}_home_ID'] = home_team_data.iloc[0]['ID']  # ID verisi ekle
#             for param in params:
#                 match_data[f'{output_file}_home_{param}'] = home_team_data.iloc[0][param]
#         else:
#             print(f"No home team data found for {home_team} in {output_file} for Game Week {previous_game_week}")
    
#     # Daha sonra away_team_name verilerini topla
#     for mod_num in range(1, 10):  # 1'den 9'a kadar olan modları döngüye al
#         output_file = f'Güncellenmiş_Mod{mod_num}_sıralama_tablosu.xlsx'
#         print(f"Processing away team in file: {output_file}")
#         mod_df = pd.read_excel(output_file)

#         # Bir önceki oyun haftası ve deplasman takımı için verileri filtrele
#         away_team_data = mod_df[(mod_df['Team Name'] == away_team) & (mod_df['Game Week'] == previous_game_week)]

#         # Deplasman takımı için parametreleri ve ID'yi topla
#         if not away_team_data.empty:
#             print(f"Found away team data for {away_team} in {output_file} for Game Week {previous_game_week}")
#             away_team_data_found = True  # Away team için veri bulunduğunu belirt
#             match_data[f'{output_file}_away_ID'] = away_team_data.iloc[0]['ID']  # ID verisi ekle
#             for param in params:
#                 match_data[f'{output_file}_away_{param}'] = away_team_data.iloc[0][param]
#         else:
#             print(f"No away team data found for {away_team} in {output_file} for Game Week {previous_game_week}")
    
#     # Eğer her iki takım için de previous_game_week verisi mevcutsa, veriyi ekle
#     if home_team_data_found and away_team_data_found:
#         collected_data = collected_data._append(match_data, ignore_index=True)
#     else:
#         print(f"Skipping match between {home_team} and {away_team} for Game Week {previous_game_week} due to missing data.")

# # Toplanan verileri incomplete_matches DataFrame'ine birleştir
# final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name', 'Game Week'], how='right')

# # Son DataFrame'i yeni bir Excel dosyasına kaydet
# final_df.to_excel('incomplete_matches_with_previous_week_parameters2.xlsx', index=False)

# print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters2.xlsx' dosyası kaydedildi.")




import pandas as pd

# Oranlar dosyasını yükle
oranlar_df = pd.read_excel('Oran_Tablosu.xlsx')

# Sadece incomplete olan maçları filtrele
incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# İlgili parametreler
params = [
    'Match Played', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 
    'Total Cumulative Goal Count Ratio', 'Cumulative Goal Defeated', 
    'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 
    'Rank Diff', 'Total Rank Diff'
]

# Veri toplamak için boş bir DataFrame oluştur
collected_data = pd.DataFrame()

# Her bir incomplete maçı döngüye al
for index, row in incomplete_matches.iterrows():
    home_team = row['home_team_name']
    away_team = row['away_team_name']
    current_game_week = row['Game Week']
    previous_game_week = current_game_week - 1

    # Bu satır için toplanan verileri tutmak için bir dictionary oluştur
    match_data = {
        'home_team_name': home_team,
        'away_team_name': away_team
    }

    # Takım verilerinin bulunup bulunmadığını kontrol etmek için bayraklar
    home_team_data_found = False
    away_team_data_found = False

    # İlk olarak home_team_name verilerini topla
    for mod_num in range(1, 10):  # 1'den 9'a kadar olan modları döngüye al
        output_file = f'Güncellenmiş_Mod{mod_num}_sıralama_tablosu.xlsx'
        print(f"Processing home team in file: {output_file}")
        mod_df = pd.read_excel(output_file)

        # Bir önceki oyun haftası ve ev sahibi takım için verileri filtrele
        home_team_data = mod_df[(mod_df['Team Name'] == home_team) & (mod_df['Game Week'] == previous_game_week)]

        # Ev sahibi takım için parametreleri ve ID'yi topla
        if not home_team_data.empty:
            print(f"Found home team data for {home_team} in {output_file} for Game Week {previous_game_week}")
            home_team_data_found = True  # Home team için veri bulunduğunu belirt
            match_data[f'{output_file}_home_ID'] = home_team_data.iloc[0]['ID']  # ID verisi ekle
            for param in params:
                match_data[f'{output_file}_home_{param}'] = home_team_data.iloc[0][param]
        else:
            print(f"No home team data found for {home_team} in {output_file} for Game Week {previous_game_week}")
    
    # Daha sonra away_team_name verilerini topla
    for mod_num in range(1, 10):  # 1'den 9'a kadar olan modları döngüye al
        output_file = f'Güncellenmiş_Mod{mod_num}_sıralama_tablosu.xlsx'
        print(f"Processing away team in file: {output_file}")
        mod_df = pd.read_excel(output_file)

        # Bir önceki oyun haftası ve deplasman takımı için verileri filtrele
        away_team_data = mod_df[(mod_df['Team Name'] == away_team) & (mod_df['Game Week'] == previous_game_week)]

        # Deplasman takımı için parametreleri ve ID'yi topla
        if not away_team_data.empty:
            print(f"Found away team data for {away_team} in {output_file} for Game Week {previous_game_week}")
            away_team_data_found = True  # Away team için veri bulunduğunu belirt
            match_data[f'{output_file}_away_ID'] = away_team_data.iloc[0]['ID']  # ID verisi ekle
            for param in params:
                match_data[f'{output_file}_away_{param}'] = away_team_data.iloc[0][param]
        else:
            print(f"No away team data found for {away_team} in {output_file} for Game Week {previous_game_week}")
    
    # Eğer her iki takım için de previous_game_week verisi mevcutsa, veriyi ekle
    if home_team_data_found and away_team_data_found:
        collected_data = collected_data._append(match_data, ignore_index=True)
    else:
        print(f"Skipping match between {home_team} and {away_team} due to missing data.")

# Toplanan verileri incomplete_matches DataFrame'ine birleştir (Game Week olmadan)
final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name'], how='right')

# Son DataFrame'i yeni bir Excel dosyasına kaydet
final_df.to_excel('incomplete_matches_with_previous_week_parameters2.xlsx', index=False)

print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters2.xlsx' dosyası kaydedildi.")





