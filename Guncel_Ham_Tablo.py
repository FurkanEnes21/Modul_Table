import pandas as pd
import os

# Klasör yolu (buraya kendi klasör yolunuzu girin)
folder_path = 'C:\\Users\\Dell\\Desktop\\0-90\\Excel Data'

# Ham dosya verisini tutmak için bir DataFrame oluştur
columns = ['File_Name', 'ID', 'home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count', 'Game Week', 'home_team_goal_timings', 'away_team_goal_timings', 'status']
ham_df = pd.DataFrame(columns=columns)

# Klasör içerisindeki dosyaları listele
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        # Dosya yolu
        file_path = os.path.join(folder_path, file_name)
        print(f'Processing file: {file_name}')
        
        # Excel dosyasını oku (1. Sheet'ten)
        try:
            df = pd.read_excel(file_path, sheet_name=0)
            
            # 'status' sütununda 'complete' olan satırları filtrele
            df_complete = df[df['status'] == 'complete']
            
            # İlgili sütunları seç ve yeni DataFrame'e ekle
            selected_columns = df_complete[['ID', 'home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count', 'Game Week', 'home_team_goal_timings', 'away_team_goal_timings', 'status']].copy()
            
            # Dosya adını sütun olarak ekle
            selected_columns.insert(0, 'File_Name', file_name)
            
            # Ham DataFrame'e ekle
            ham_df = pd.concat([ham_df, selected_columns], ignore_index=True)
        except Exception as e:
            print(f'Error processing file {file_name}: {e}')

# Goal Timing sütununu oluştur ve "0-90" ile doldur
ham_df['Goal Timing'] = "0-90"

# Çıktı dosyasını kaydetmek istediğiniz yolu belirtin (buraya kendi dosya yolunuzu girin)
output_file_path = 'C:\\Users\\Dell\\Desktop\\0-90\\Güncel_ham_dosya1.xlsx'

# DataFrame'i Excel dosyasına kaydet
ham_df.to_excel(output_file_path, index=False)

print(f'Ham veriler başarıyla kaydedildi: {output_file_path}')
