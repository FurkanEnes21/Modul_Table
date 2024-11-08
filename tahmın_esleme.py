import pandas as pd

# Dosyaları oku
df1 = pd.read_excel('Eval_15-16-Eylul.xlsx')  # Birinci dosya
df2 = pd.read_excel('Oran_Tablosu.xlsx')  # İkinci dosya

# İkinci dosyadan gerekli sütunları (ID, home_team_name, away_team_name) al
df2_filtered = df2[['ID', 'home_team_name', 'away_team_name']]

# Birinci dosya ile ikinci dosya arasında ID bazında merge işlemi yap
merged_df = pd.merge(df1, df2_filtered, left_on='Match_ID', right_on='ID', how='left')

# Birleştirilen veriyi yeni Excel dosyasına kaydet
merged_df.to_excel('birlesmis_dosya.xlsx', index=False)

print("Eşleşen veriler yeni dosyaya başarıyla eklendi.")
