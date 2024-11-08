# import pandas as pd

# # Oranlar dosyasını yükle
# oranlar_df = pd.read_excel('Oran_Tablosu.xlsx')

# # Sadece incomplete olan maçları filtrele
# incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# # Parametreler ve Game Week aralığı
# params = [f'B{i}' for i in range(182, 271)]  # B182'den B270'e kadar olan parametreler
# output_file = 'Modul_Tablo.xlsx'

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

#     # Mod1 dosyasını oku
#     mod_df = pd.read_excel(output_file)

#     # Ev sahibi takım verilerini topla
#     print(f"Processing home team in file: {output_file}")
#     home_team_data = mod_df[(mod_df['Team Name'] == home_team) & (mod_df['Game Week'] == previous_game_week)]

#     if not home_team_data.empty:
#         print(f"Found home team data for {home_team} in {output_file} for Game Week {previous_game_week}")
#         home_team_data_found = True  # Home team için veri bulunduğunu belirt
#         match_data[f'{output_file}_home_ID'] = home_team_data.iloc[0]['ID']  # ID verisi ekle
#         match_data[f'{output_file}_home_Game Week'] = home_team_data.iloc[0]['Game Week']  # Game Week verisi ekle
#         for param in params:
#             match_data[f'{output_file}_home_{param}'] = home_team_data.iloc[0][param]
#     else:
#         print(f"No home team data found for {home_team} in {output_file} for Game Week {previous_game_week}")
    
#     # Deplasman takımı verilerini topla
#     print(f"Processing away team in file: {output_file}")
#     away_team_data = mod_df[(mod_df['Team Name'] == away_team) & (mod_df['Game Week'] == previous_game_week)]

#     if not away_team_data.empty:
#         print(f"Found away team data for {away_team} in {output_file} for Game Week {previous_game_week}")
#         away_team_data_found = True  # Away team için veri bulunduğunu belirt
#         match_data[f'{output_file}_away_ID'] = away_team_data.iloc[0]['ID']  # ID verisi ekle
#         match_data[f'{output_file}_away_Game Week'] = away_team_data.iloc[0]['Game Week']  # Game Week verisi ekle
#         for param in params:
#             match_data[f'{output_file}_away_{param}'] = away_team_data.iloc[0][param]
#     else:
#         print(f"No away team data found for {away_team} in {output_file} for Game Week {previous_game_week}")
    
#     # Eğer her iki takım için de previous_game_week verisi mevcutsa, veriyi ekle
#     if home_team_data_found and away_team_data_found:
#         collected_data = collected_data._append(match_data, ignore_index=True)
#     else:
#         print(f"Skipping match between {home_team} and {away_team} for Game Week {previous_game_week} due to missing data.")

# # Toplanan verileri incomplete_matches DataFrame'ine birleştir
# final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name', 'Game Week'], how='right')

# # Son DataFrame'i yeni bir Excel dosyasına kaydet
# final_df.to_excel('incomplete_matches_with_previous_week_parameters3.xlsx', index=False)

# print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters2.xlsx' dosyası kaydedildi.")

























######## yukarıdaki kodu da kullanıyoruz 



# import pandas as pd

# # Oranlar dosyasını yükle
# oranlar_df = pd.read_excel('Oran_Tablosu.xlsx')

# # Sadece incomplete olan maçları filtrele
# incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# # Parametreler ve Game Week aralığı
# params = [f'B{i}' for i in range(182, 271)]  # B182'den B270'e kadar olan parametreler
# output_file = 'Modul_Tablo.xlsx'

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

#     # Mod1 dosyasını oku
#     mod_df = pd.read_excel(output_file)

#     # Ev sahibi ve deplasman takımı için verileri topla
#     print(f"Processing teams in file: {output_file}")
#     home_away_data = mod_df[((mod_df['Team Name'] == home_team) | (mod_df['Team Name'] == away_team)) & 
#                             (mod_df['Game Week'] == previous_game_week)]

#     if not home_away_data.empty:
#         print(f"Found data for {home_team} or {away_team} in {output_file} for Game Week {previous_game_week}")
#         for param in params:
#             match_data[f'{output_file}_home_away_{param}'] = home_away_data.iloc[0][param]  # Parametre verisi ekle

#         collected_data = collected_data._append(match_data, ignore_index=True)
#     else:
#         print(f"No data found for {home_team} or {away_team} in {output_file} for Game Week {previous_game_week}")

# # Toplanan verileri incomplete_matches DataFrame'ine birleştir
# final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name', 'Game Week'], how='right')

# # Son DataFrame'i yeni bir Excel dosyasına kaydet
# final_df.to_excel('incomplete_matches_with_previous_week_parameters3.xlsx', index=False)

# print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters3.xlsx' dosyası kaydedildi.")





# import pandas as pd

# # Oranlar dosyasını yükle
# oranlar_df = pd.read_excel('Oran_Tablosu.xlsx')

# # Sadece incomplete olan maçları filtrele
# incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# # Parametreler ve Game Week aralığı
# params = [f'B{i}' for i in range(182, 271)]  # B182'den B270'e kadar olan parametreler
# output_file = 'Modul_Tablo.xlsx'

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

#     # Modül dosyasını oku
#     mod_df = pd.read_excel(output_file)

#     # Ev sahibi ve deplasman takımı için verileri topla
#     print(f"Processing teams in file: {output_file}")
#     home_away_data = mod_df[((mod_df['Team Name'] == home_team) | (mod_df['Team Name'] == away_team)) & 
#                             (mod_df['Game Week'] == previous_game_week)]

#     # Eğer her iki takımın da previous_game_week verisi mevcutsa, veriyi ekle
#     if len(home_away_data) == 2:
#         print(f"Found data for both {home_team} and {away_team} in {output_file} for Game Week {previous_game_week}")
        
#         # Parametre verilerini ekle
#         for param in params:
#             match_data[param] = home_away_data.iloc[0][param]  # Aynı parametre setini ekliyoruz

#         collected_data = collected_data._append(match_data, ignore_index=True)
#     else:
#         print(f"No data found for both {home_team} and {away_team} in {output_file} for Game Week {previous_game_week}")

# # Toplanan verileri incomplete_matches DataFrame'ine birleştir
# final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name', 'Game Week'], how='right')

# # Son DataFrame'i yeni bir Excel dosyasına kaydet
# final_df.to_excel('incomplete_matches_with_previous_week_parameters4.xlsx', index=False)

# print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters3.xlsx' dosyası kaydedildi.")














import pandas as pd

# Oranlar dosyasını yükle
oranlar_df = pd.read_excel('Oran_Tablosu.xlsx')

# Sadece incomplete olan maçları filtrele
incomplete_matches = oranlar_df[oranlar_df['status'] == 'incomplete']

# Parametreler ve Game Week aralığı
params = [f'B{i}' for i in range(182, 271)]  # B182'den B270'e kadar olan parametreler
output_file = 'Modul_Tablo.xlsx'

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
        'away_team_name': away_team,
        'Game Week': current_game_week,
        'Previous Game Week': previous_game_week  # Previous Game Week'i ekle
    }

    # Modül dosyasını oku
    mod_df = pd.read_excel(output_file)

    # Ev sahibi ve deplasman takımı için verileri topla
    print(f"Processing teams in file: {output_file}")
    home_away_data = mod_df[((mod_df['Team Name'] == home_team) | (mod_df['Team Name'] == away_team)) & 
                            (mod_df['Game Week'] == previous_game_week)]

    # Eğer her iki takımın da previous_game_week verisi mevcutsa, veriyi ekle
    if len(home_away_data) == 2:
        print(f"Found data for both {home_team} and {away_team} in {output_file} for Game Week {previous_game_week}")
        
        # Parametre verilerini ekle
        for param in params:
            match_data[param] = home_away_data.iloc[0][param]  # Aynı parametre setini ekliyoruz

        collected_data = collected_data._append(match_data, ignore_index=True)
    else:
        print(f"No data found for both {home_team} and {away_team} in {output_file} for Game Week {previous_game_week}")

# Toplanan verileri incomplete_matches DataFrame'ine birleştir
final_df = incomplete_matches.merge(collected_data, on=['home_team_name', 'away_team_name', 'Game Week'], how='right')

# Son DataFrame'i yeni bir Excel dosyasına kaydet
final_df.to_excel('incomplete_matches_with_previous_week_parameters3.xlsx', index=False)

print("Veri çekme ve birleştirme işlemi tamamlandı. 'incomplete_matches_with_previous_week_parameters5.xlsx' dosyası kaydedildi.")
