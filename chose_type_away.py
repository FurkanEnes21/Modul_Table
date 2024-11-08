import pandas as pd

def process_file(input_file_path, start_row, start_col_prefix):
    # Dosyayı okuyun
    df = pd.read_excel(input_file_path)

    # 'Home' olan takımları filtreleyin
    home_teams = df[df['Home/Away'] == 'Away']

    # İstenen sütunlar
    columns_to_keep = ['ID', 'Lig ID', 'Team Name','Game Week', 'Match Played', 'Cumulative Point', 'Rank', 'Cumulative Goal Count', 'Total Cumulative Goal Count Ratio', 'Cumulative Goal Defeated', 'Total Cumulative Goal Defeated Ratio', 'Cumulative Average', 'Rank Diff', 'Total Rank Diff']

    # Sütun isimleri için prefix ekleme (ID sütunu hariç)
    prefixed_columns = [f'{start_col_prefix}{i}' if col not in ['ID'] else col for i, col in enumerate(columns_to_keep)]
    
    # Değerleri prefixed sütun isimlerinin altına yerleştirmek için yeni bir DataFrame oluştur
    additional_data = home_teams[columns_to_keep].reset_index(drop=True)

    # İlk satıra sütun isimlerini yerleştir
    header = pd.DataFrame([prefixed_columns], columns=columns_to_keep)

    # Sütun isimlerini ve verileri birleştir
    combined_df = pd.concat([header, additional_data], ignore_index=True)

    # Başlangıç satırını ayarla
    combined_df.index = range(start_row, start_row + len(combined_df))

    return combined_df

# Giriş dosyalarının yollarını belirtin
input_files = [
    'Güncellenmiş_Mod1_sıralama_tablosu.xlsx',
    'Güncellenmiş_Mod2_sıralama_tablosu.xlsx',
    'Güncellenmiş_Mod3_sıralama_tablosu.xlsx',
    'Güncellenmiş_Mod4_sıralama_tablosu.xlsx',
    'Güncellenmiş_Mod5_sıralama_tablosu.xlsx',
    'Güncellenmiş_Mod6_sıralama_tablosu.xlsx',
    'Güncellenmiş_Mod7_sıralama_tablosu.xlsx',
    'Güncellenmiş_Mod8_sıralama_tablosu.xlsx',
    'Güncellenmiş_Mod9_sıralama_tablosu.xlsx'
]

# Her bir dosya için başlangıç satırı ve sütun öneki
start_rows = [31, 31, 31, 31, 31, 31, 31, 31, 31]  # 9 eleman içermeli
start_col_prefixes = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']  # 9 eleman içermeli

# Her bir dosya için işlem yap ve dosyayı kaydet
for i, input_file in enumerate(input_files):
    processed_data = process_file(input_file, start_rows[i], start_col_prefixes[i])
    
    # Çıktı dosya adını oluştur
    output_file_path = f'output_away_{i+1}_{input_file}'
    
    # Veriyi dosyaya yazın
    processed_data.to_excel(output_file_path, index=False, header=True)
    
    print(f'Output saved to {output_file_path}')