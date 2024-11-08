import pandas as pd

# Dosyaları yükle
guncel_ham_dosya1 = pd.read_excel('C:\\Users\\Dell\\Desktop\\0-90\\Güncel_ham_dosya1.xlsx')

# Mod dosyaları isim formatı
mod_dosyasi_format = 'Mod{}.xlsx'

# Kaç adet mod dosyası olduğunu belirleyin (mod1'den mod9'a kadar)
mod_sayisi = 9

for i in range(1, mod_sayisi + 1):
    mod_dosyasi_adi = mod_dosyasi_format.format(i)
    mod = pd.read_excel(mod_dosyasi_adi)

    ids = guncel_ham_dosya1[['Game Week', 'ID', 'home_team_name', 'away_team_name', 'Lig ID']]

    mod_id_list = []

    for entry in range(len(mod)):
        home_index = guncel_ham_dosya1[(guncel_ham_dosya1['Lig ID'] == mod['Lig ID'][entry]) & (guncel_ham_dosya1['Game Week'] == mod['Game Week'][entry]) & (guncel_ham_dosya1['home_team_name'] == mod['Team Name'][entry])].index.tolist()
        away_index = guncel_ham_dosya1[(guncel_ham_dosya1['Lig ID'] == mod['Lig ID'][entry]) & (guncel_ham_dosya1['Game Week'] == mod['Game Week'][entry]) & (guncel_ham_dosya1['away_team_name'] == mod['Team Name'][entry])].index.tolist()
        if(len(home_index) == 0):
            mod_id_list.append(guncel_ham_dosya1['ID'][away_index[0]])
        else:
            mod_id_list.append(guncel_ham_dosya1['ID'][home_index[0]])

    mod['ID'] = mod_id_list

    # Çıktı dosya ismi
    output_dosyasi_adi = f'Güncellenmiş_Mod{i}_sıralama_tablosu.xlsx'
    mod.to_excel(output_dosyasi_adi, index=False)

    print(f'{output_dosyasi_adi} dosyası oluşturuldu.')


