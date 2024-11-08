
import pandas as pd

# Excel dosyasının yolunu belirtin
excel_dosyasi = 'Mod6.xlsx'
output_dosyasi = 'Mod6.xlsx'

# Excel dosyasını okuyun
excel_dosyasi = pd.ExcelFile(excel_dosyasi)

# Tüm sheet isimlerini alın
sheet_isimleri = excel_dosyasi.sheet_names

# Tüm sheet'leri birleştirmek için boş bir liste oluşturun
dataframes = []

# Her bir sheet'i oku ve listeye ekle
for sheet in sheet_isimleri:
    df = pd.read_excel(excel_dosyasi, sheet_name=sheet)
    df['Sheet_Name'] = sheet  # Opsiyonel: Hangi sheet'ten geldiğini takip etmek için bir sütun ekleyin
    dataframes.append(df)

# Tüm dataframe'leri birleştir
birlesmis_df = pd.concat(dataframes, ignore_index=True)

# Yeni bir Excel dosyasına yaz
birlesmis_df.to_excel(output_dosyasi, index=False)

print(f"Tüm sheet'ler {output_dosyasi} dosyasında birleştirildi.")