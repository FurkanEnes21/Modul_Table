
import pandas as pd
import os
from datetime import datetime

# Klasördeki tüm Excel dosyalarını okuyacak ve istenen sütunları birleştirecek fonksiyon
def combine_excel_sheets(folder_path, output_file, start_date, end_date):
    # Birleştirilecek sütunları belirle
    columns_to_extract = [
        'ID',                 # ID sütunu 
        'odds_ft_home_team_win', 
        'odds_ft_draw', 
        'odds_ft_away_team_win',
        'status',            # status sütunu
        'Game Week',          # Game Week sütunu
        'date_GMT',
        'home_team_name',
        'away_team_name'        # date_GMT sütunu
    ]
    
    # Boş bir liste oluştur
    combined_data = []

    # Klasördeki tüm Excel dosyalarını oku
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx") or file.endswith(".xls"):
            file_path = os.path.join(folder_path, file)
            # Dosyayı oku
            df = pd.read_excel(file_path, usecols=columns_to_extract)
            
            # date_GMT sütununu datetime formatına çevir
            df['date_GMT'] = pd.to_datetime(df['date_GMT'], format='%b %d %Y - %I:%M%p', errors='coerce')
            
            # Tarih aralığına göre filtrele
            mask = (df['date_GMT'] >= start_date) & (df['date_GMT'] <= end_date)
            df = df.loc[mask]
            
            combined_data.append(df)

    # Tüm verileri tek bir DataFrame'de birleştir
    combined_df = pd.concat(combined_data, ignore_index=True)
    
    # Birleştirilen veriyi yeni bir Excel dosyasına kaydet
    combined_df.to_excel(output_file, index=False)

    print(f"Data has been combined and saved to {output_file}")


# Tarih aralığını belirle (ay/gün/yıl formatında)
start_date = "11/07/2024"
end_date = "11/12/2024"

# Tarihleri datetime formatına çevir
start_date = datetime.strptime(start_date, '%m/%d/%Y')
end_date = datetime.strptime(end_date, '%m/%d/%Y')

# Kullanım örneği
folder_path = "C:\\Users\\Dell\\Desktop\\0-90\\Excel Data"  # Klasör yolunu buraya yaz
output_file = "Oran_Tablosu.xlsx"  # Çıktı dosyasının adı

combine_excel_sheets(folder_path, output_file, start_date, end_date)








# import pandas as pd
# import os
# from datetime import datetime

# # Klasördeki tüm Excel dosyalarını okuyacak ve istenen sütunları birleştirecek fonksiyon
# def combine_excel_sheets(folder_path, output_file, start_date, end_date):
#     # Birleştirilecek sütunları belirle
#     columns_to_extract = [
#         'ID',                 # ID sütunu 
#         'odds_ft_home_team_win', 
#         'odds_ft_draw', 
#         'odds_ft_away_team_win',
#         'status',            # status sütunu
#         'Game Week',          # Game Week sütunu
#         'date_GMT',
#         'home_team_name',
#         'away_team_name'        # date_GMT sütunu
#     ]
    
#     # Boş bir liste oluştur
#     combined_data = []

#     # Klasördeki tüm Excel dosyalarını oku
#     for file in os.listdir(folder_path):
#         if file.endswith(".xlsx") or file.endswith(".xls"):
#             file_path = os.path.join(folder_path, file)
#             # Dosyayı oku
#             df = pd.read_excel(file_path, usecols=columns_to_extract)
            
#             # date_GMT sütununu datetime formatına çevir
#             df['date_GMT'] = pd.to_datetime(df['date_GMT'], format='%b %d %Y - %I:%M%p', errors='coerce')
            
#             # Tarih aralığına göre filtrele
#             mask = (df['date_GMT'] >= start_date) & (df['date_GMT'] <= end_date)
#             df = df.loc[mask]
            
#             combined_data.append(df)

#     # Tüm verileri tek bir DataFrame'de birleştir
#     combined_df = pd.concat(combined_data, ignore_index=True)
    
#     # Birleştirilen veriyi yeni bir Excel dosyasına kaydet
#     combined_df.to_excel(output_file, index=False)
#     print(f"Data has been combined and saved to {output_file}")

#     return combined_df  # DataFrame'i döndür

# # İkinci fonksiyon: Güncel_ham_dosya1 dosyasındaki ID'ye karşılık gelen 0-90-result sütununu eklemek
# def add_result_column(output_file, result_file):
#     # Oran_Tablosu.xlsx dosyasını oku
#     oran_df = pd.read_excel(output_file)
    
#     # Güncel_ham_dosya1 dosyasını oku
#     result_df = pd.read_excel(result_file, usecols=['ID', '0-90-result'])
    
#     # ID sütununa göre birleştir (merge)
#     merged_df = pd.merge(oran_df, result_df, on='ID', how='left')
    
#     # Birleştirilen sonucu tekrar aynı dosyaya kaydet
#     merged_df.to_excel(output_file, index=False)
#     print(f"0-90-result column has been added to {output_file}")

# # Tarih aralığını belirle (ay/gün/yıl formatında)
# start_date = "10/31/2024"
# end_date = "11/4/2024"

# # Tarihleri datetime formatına çevir
# start_date = datetime.strptime(start_date, '%m/%d/%Y')
# end_date = datetime.strptime(end_date, '%m/%d/%Y')

# # Kullanım örneği
# folder_path = "C:\\Users\\Dell\\Desktop\\0-90\\Excel Data"  # Klasör yolunu buraya yaz
# output_file = "Oran_Tablosu.xlsx"  # Çıktı dosyasının adı
# result_file = "C:\\Users\\Dell\\Desktop\\0-90\\Güncel_ham_dosya1.xlsx"  # Güncel_ham_dosya1 dosyasının yolu

# # İlk olarak, Excel dosyalarını birleştir
# combine_excel_sheets(folder_path, output_file, start_date, end_date)

# # Ardından, 0-90-result sütununu ekle
# add_result_column(output_file, result_file)
