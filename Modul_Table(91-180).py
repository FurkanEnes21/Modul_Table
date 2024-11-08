import pandas as pd
from tqdm import tqdm

# Excel dosyalarını oku
df_ham = pd.read_excel('Güncel_ham_dosya2.xlsx')
df_mod1 = pd.read_excel('Güncellenmiş_Mod1_sıralama_tablosu.xlsx')
df_mod2 = pd.read_excel('Güncellenmiş_Mod2_sıralama_tablosu.xlsx')
df_mod3 = pd.read_excel('Güncellenmiş_Mod3_sıralama_tablosu.xlsx')
df_mod4 = pd.read_excel('Güncellenmiş_Mod4_sıralama_tablosu.xlsx')
df_mod5 = pd.read_excel('Güncellenmiş_Mod5_sıralama_tablosu.xlsx')
df_mod6 = pd.read_excel('Güncellenmiş_Mod6_sıralama_tablosu.xlsx')
df_mod7 = pd.read_excel('Güncellenmiş_Mod7_sıralama_tablosu.xlsx')
df_mod8 = pd.read_excel('Güncellenmiş_Mod8_sıralama_tablosu.xlsx')
df_mod9 = pd.read_excel('Güncellenmiş_Mod9_sıralama_tablosu.xlsx')

# Sütun adlarını manuel olarak ayarlayın
df_ham.columns = ['File_Name', 'Lig ID', 'ID', 'home_team_name', 'away_team_name',
                  'home_team_goal_count', 'away_team_goal_count', 'Game Week', 
                  'home_team_goal_timings', 'away_team_goal_timings', 'status', 
                  'Goal Timing', '0-30-home', '0-45-home', '0-90-home', '15-45-home', 
                  '15-75-home', '15-90-home', '30-90-home', '45-75-home', '45-90-home', 
                  '0-30-away', '0-45-away', '0-90-away', '15-45-away', '15-75-away', 
                  '15-90-away', '30-90-away', '45-75-away', '45-90-away']
df_ham = df_ham[1:]  # İlk satırı çıkar

# rw listesindeki değerleri al
a = df_ham['Lig ID'].astype(str).tolist()
b = df_ham['Game Week'].astype(str).tolist()
c_home = df_ham['home_team_name'].astype(str).tolist()
c_away = df_ham['away_team_name'].astype(str).tolist()
d = df_ham['Goal Timing'].astype(str).tolist()

# İlerleme çubuğu için tqdm kullanarak işlem
print("Mod1 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod1 = df_mod1[(df_mod1['Lig ID'].astype(str).isin(tqdm(a, desc='Lig ID'))) &
                            (df_mod1['Game Week'].astype(str).isin(tqdm(b, desc='Game Week'))) &
                            (df_mod1['Team Name'].astype(str).isin(tqdm(c_home + c_away, desc='Team Name'))) &
                            (df_mod1['Goal Timing'].astype(str).isin(tqdm(d, desc='Goal Timing'))) &
                            (df_mod1['Home/Away'] == 'Away')]

# Diğer dosyalar için aynı işlemler
def match_rows(df_mod):
    return df_mod[(df_mod['Lig ID'].astype(str).isin(a)) &
                  (df_mod['Team Name'].astype(str).isin(c_home + c_away)) &
                  (df_mod['Goal Timing'].astype(str).isin(d)) &
                  (df_mod['Home/Away'] == 'Away')]

print("Mod2 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod2 = match_rows(df_mod2)
print("Mod3 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod3 = match_rows(df_mod3)
print("Mod4 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod4 = match_rows(df_mod4)
print("Mod5 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod5 = match_rows(df_mod5)
print("Mod6 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod6 = match_rows(df_mod6)
print("Mod7 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod7 = match_rows(df_mod7)
print("Mod8 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod8 = match_rows(df_mod8)
print("Mod9 dosyasındaki satırları kontrol ediyoruz...")
matched_rows_mod9 = match_rows(df_mod9)

# Yeni sütun isimlerini oluştur
new_columns_mod1 = ['B91', 'B92', 'B93', 'B94', 'B95', 'B96', 'B97', 'B98', 'B99', 'B101']
existing_columns_mod1 = ['Game Week', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 'Total Cumulative Goal Count Ratio', 'Cumulative Goal Defeated', 'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 'Rank Diff', 'Total Rank Diff']

new_columns_mod2 = ['B' + str(i) for i in range(101, 111)]
new_columns_mod3 = ['B' + str(i) for i in range(111, 121)]
new_columns_mod4 = ['B' + str(i) for i in range(121, 131)]
new_columns_mod5 = ['B' + str(i) for i in range(131, 141)]
new_columns_mod6 = ['B' + str(i) for i in range(141, 151)]
new_columns_mod7 = ['B' + str(i) for i in range(151, 161)]
new_columns_mod8 = ['B' + str(i) for i in range(161, 171)]
new_columns_mod9 = ['B' + str(i) for i in range(171, 181)]
existing_columns_mod2_9 = ['Match Played', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 'Total Cumulative Goal Count Ratio', 'Cumulative Goal Defeated', 'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 'Rank Diff', 'Total Rank Diff']

# Sadece gerekli sütunları al
game_week_1_rows_mod1 = matched_rows_mod1[existing_columns_mod1]
game_week_1_rows_mod2 = matched_rows_mod2[existing_columns_mod2_9]
game_week_1_rows_mod3 = matched_rows_mod3[existing_columns_mod2_9]
game_week_1_rows_mod4 = matched_rows_mod4[existing_columns_mod2_9]
game_week_1_rows_mod5 = matched_rows_mod5[existing_columns_mod2_9]
game_week_1_rows_mod6 = matched_rows_mod6[existing_columns_mod2_9]
game_week_1_rows_mod7 = matched_rows_mod7[existing_columns_mod2_9]
game_week_1_rows_mod8 = matched_rows_mod8[existing_columns_mod2_9]
game_week_1_rows_mod9 = matched_rows_mod9[existing_columns_mod2_9]

# İlk satırı bir satır aşağı kaydırmak için boş bir satır ekle
def shift_dataframe(mod_df, columns):
    empty_row = pd.DataFrame([[''] * len(columns)], columns=columns)
    return pd.concat([empty_row, mod_df.reset_index(drop=True)], ignore_index=True)

modul_tablo_shifted_mod1 = shift_dataframe(game_week_1_rows_mod1, existing_columns_mod1)
modul_tablo_shifted_mod2 = shift_dataframe(game_week_1_rows_mod2, existing_columns_mod2_9)
modul_tablo_shifted_mod3 = shift_dataframe(game_week_1_rows_mod3, existing_columns_mod2_9)
modul_tablo_shifted_mod4 = shift_dataframe(game_week_1_rows_mod4, existing_columns_mod2_9)
modul_tablo_shifted_mod5 = shift_dataframe(game_week_1_rows_mod5, existing_columns_mod2_9)
modul_tablo_shifted_mod6 = shift_dataframe(game_week_1_rows_mod6, existing_columns_mod2_9)
modul_tablo_shifted_mod7 = shift_dataframe(game_week_1_rows_mod7, existing_columns_mod2_9)
modul_tablo_shifted_mod8 = shift_dataframe(game_week_1_rows_mod8, existing_columns_mod2_9)
modul_tablo_shifted_mod9 = shift_dataframe(game_week_1_rows_mod9, existing_columns_mod2_9)

# Yeni sütun isimlerini ekle
def set_new_columns(mod_df, new_columns):
    mod_df.columns = new_columns + list(mod_df.columns[len(new_columns):])
    return mod_df

modul_tablo_shifted_mod1 = set_new_columns(modul_tablo_shifted_mod1, new_columns_mod1)
modul_tablo_shifted_mod2 = set_new_columns(modul_tablo_shifted_mod2, new_columns_mod2)
modul_tablo_shifted_mod3 = set_new_columns(modul_tablo_shifted_mod3, new_columns_mod3)
modul_tablo_shifted_mod4 = set_new_columns(modul_tablo_shifted_mod4, new_columns_mod4)
modul_tablo_shifted_mod5 = set_new_columns(modul_tablo_shifted_mod5, new_columns_mod5)
modul_tablo_shifted_mod6 = set_new_columns(modul_tablo_shifted_mod6, new_columns_mod6)
modul_tablo_shifted_mod7 = set_new_columns(modul_tablo_shifted_mod7, new_columns_mod7)
modul_tablo_shifted_mod8 = set_new_columns(modul_tablo_shifted_mod8, new_columns_mod8)
modul_tablo_shifted_mod9 = set_new_columns(modul_tablo_shifted_mod9, new_columns_mod9)

final_df = pd.concat([
    modul_tablo_shifted_mod1, modul_tablo_shifted_mod2, modul_tablo_shifted_mod3,
    modul_tablo_shifted_mod4, modul_tablo_shifted_mod5, modul_tablo_shifted_mod6,
    modul_tablo_shifted_mod7, modul_tablo_shifted_mod8, modul_tablo_shifted_mod9
], axis=1)

# Modul_Tablo dosyasını oluştur ve yaz
print("Sonuçları Modul_Tablo.xlsx dosyasına yazıyoruz...")
with pd.ExcelWriter('Modul_Tablo2.xlsx') as writer:
    final_df.to_excel(writer, index=False, sheet_name='Sheet1')
    
    worksheet = writer.sheets['Sheet1']
    
    # Yeni sütun isimlerini ekle
    for col_num, value in enumerate(new_columns_mod1 + new_columns_mod2 + new_columns_mod3 + new_columns_mod4 + new_columns_mod5 + new_columns_mod6 + new_columns_mod7 + new_columns_mod8 + new_columns_mod9):
        worksheet.write(0, col_num, value)
    
    # Mevcut sütun isimlerini ekle
    for col_num, value in enumerate(existing_columns_mod1):
        worksheet.write(1, col_num, value)
    
    for col_num, value in enumerate(existing_columns_mod2_9):
        worksheet.write(1, col_num + len(existing_columns_mod1), value)
    
    for col_num, value in enumerate(existing_columns_mod2_9):
        worksheet.write(1, col_num + len(existing_columns_mod1) + len(existing_columns_mod2_9), value)
    
    for col_num, value in enumerate(existing_columns_mod2_9):
        worksheet.write(1, col_num + len(existing_columns_mod1) + 2 * len(existing_columns_mod2_9), value)
    
    for col_num, value in enumerate(existing_columns_mod2_9):
        worksheet.write(1, col_num + len(existing_columns_mod1) + 3 * len(existing_columns_mod2_9), value)
    
    for col_num, value in enumerate(existing_columns_mod2_9):
        worksheet.write(1, col_num + len(existing_columns_mod1) + 4 * len(existing_columns_mod2_9), value)
    
    for col_num, value in enumerate(existing_columns_mod2_9):
        worksheet.write(1, col_num + len(existing_columns_mod1) + 5 * len(existing_columns_mod2_9), value)
    
    for col_num, value in enumerate(existing_columns_mod2_9):
        worksheet.write(1, col_num + len(existing_columns_mod1) + 6 * len(existing_columns_mod2_9), value)
    
    for col_num, value in enumerate(existing_columns_mod2_9):
        worksheet.write(1, col_num + len(existing_columns_mod1) + 7 * len(existing_columns_mod2_9), value)

print("İşlem tamamlandı ve sonuçlar Modul_Tablo.xlsx dosyasına yazıldı.")
