import pandas as pd

# Mod1.xlsx'den Mod9.xlsx'e kadar olan dosyaları oku ve ayrı ayrı işle
dosya_listesi = [f'Mod{i}.xlsx' for i in range(1, 10)]

# Güncel ham dosya (bu sabit kaldı)
ham_dosya = pd.read_excel('C:\\Users\\Dell\\Desktop\\0-90\\Güncel_ham_dosya1.xlsx')

# Home/Away sütununu ekle
def home_away_status(row):
    game_week = row['Game Week']
    team_name = row['Team Name']
    lig_id = row['Lig ID']
    
    # İlgili Lig ID ve Game Week için home ve away takımlarını bul
    home_teams = ham_dosya.loc[(ham_dosya['Game Week'] == game_week) & (ham_dosya['Lig ID'] == lig_id), 'home_team_name'].values
    away_teams = ham_dosya.loc[(ham_dosya['Game Week'] == game_week) & (ham_dosya['Lig ID'] == lig_id), 'away_team_name'].values

    if team_name in home_teams:
        return 'Home'
    elif team_name in away_teams:
        return 'Away'
    else:
        return 'None'

# Her dosya için işlemleri gerçekleştir
for i, dosya in enumerate(dosya_listesi, start=1):
    haftalik_genel_siralama = pd.read_excel(dosya)
    haftalik_genel_siralama['Home/Away'] = haftalik_genel_siralama.apply(home_away_status, axis=1)
    
    # Sonuçları her dosya için ayrı olarak kaydet
    cikti_dosya_adi = f'Mod{i}.xlsx'
    haftalik_genel_siralama.to_excel(cikti_dosya_adi, index=False)
    
    print(f"İşlem tamamlandı ve sonuçlar {cikti_dosya_adi} dosyasına kaydedildi.")
