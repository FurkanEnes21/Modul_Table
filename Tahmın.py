# import pandas as pd
# from sklearn.metrics.pairwise import euclidean_distances

# # Dosyaları oku
# parametreler_df = pd.read_excel("incomplete_matches_with_previous_week_parameters.xlsx")
# mac_verileri_df = pd.read_excel("Modul_Tablosu2.xlsx")

# # Sadece sayısal sütunları al ve B2 sütununu çıkart
# parametreler = parametreler_df.select_dtypes(include=['number']).drop(columns=["B2"])
# mac_verileri_parametreler = mac_verileri_df.select_dtypes(include=['number']).drop(columns=["B2"])

# # Eksik değerleri 0 ile doldur (veya dropna ile eksik satırları çıkarabilirsiniz)
# parametreler = parametreler.fillna(0)
# mac_verileri_parametreler = mac_verileri_parametreler.fillna(0)

# # Euklides mesafesi kullanarak en yakın 20 maçı bul
# mesafeler = euclidean_distances(parametreler.values, mac_verileri_parametreler.values)
# en_yakin_indexler = mesafeler.argsort()[0][:20]

# # En yakın 20 maçı filtrele
# en_yakin_maclar = mac_verileri_df.iloc[en_yakin_indexler]

# # B2 değerine göre Win, Draw, Loss belirle
# win_count = 0
# draw_count = 0
# loss_count = 0

# for i in range(len(en_yakin_maclar)):
#     b2_degeri = en_yakin_maclar.iloc[i]["B2"]
    
#     if b2_degeri == 3:  # +3 varsa win
#         win_count += 1
#     elif b2_degeri == 1:  # +1 varsa draw
#         draw_count += 1
#     elif b2_degeri == 0:  # 0 veya değişim yoksa loss
#         loss_count += 1

# # Yüzdeleri hesapla
# total_matches = win_count + draw_count + loss_count
# win_orani = (win_count / total_matches) * 100
# draw_orani = (draw_count / total_matches) * 100
# loss_orani = (loss_count / total_matches) * 100

# print(f"Win oranı: %{win_orani:.2f}")
# print(f"Draw oranı: %{draw_orani:.2f}")
# print(f"Loss oranı: %{loss_orani:.2f}")



# import pandas as pd
# from sklearn.metrics.pairwise import euclidean_distances

# # Dosyaları oku
# parametreler_df = pd.read_excel("incomplete_matches_with_previous_week_parameters.xlsx")
# mac_verileri_df = pd.read_excel("Tahmındeneme.xlsx")

# # ID sütunlarını ayır ve diğer verileri temizle
# parametreler_ids = parametreler_df["ID"]
# parametreler = parametreler_df.drop(columns=["ID", "B2"])
# parametreler_df = parametreler_df.drop(columns=["ID"])

# mac_verileri_ids = mac_verileri_df["ID"]
# mac_verileri_parametreler = mac_verileri_df.drop(columns=["ID", "B2"])
# mac_verileri_df = mac_verileri_df.drop(columns=["ID"])

# # Eksik değerleri temizle
# parametreler = parametreler.apply(pd.to_numeric, errors='coerce').dropna()
# mac_verileri_parametreler = mac_verileri_parametreler.apply(pd.to_numeric, errors='coerce').dropna()

# # Her bir maç için en yakın 20 maçı bul ve win/draw/loss yüzdelerini hesapla
# sonuclar = []

# for i, parametre_satiri in parametreler.iterrows():
#     # En yakın 20 maçı bulmak için Euklides mesafesi hesapla
#     mesafeler = euclidean_distances([parametre_satiri.values], mac_verileri_parametreler.values)
#     en_yakin_indexler = mesafeler.argsort()[0][:20]
    
#     # En yakın 20 maçı filtrele
#     en_yakin_maclar = mac_verileri_df.iloc[en_yakin_indexler]
#     en_yakin_mac_ids = mac_verileri_ids.iloc[en_yakin_indexler]
    
#     # B2 sütununa göre win, draw, loss belirle
#     win_count = ''
#     draw_count = ''
#     loss_count = ''
    
#     for j, mac in en_yakin_maclar.iterrows():
#         onceki_game_week = mac["B1"]
#         sonraki_mac = mac_verileri_df[(mac_verileri_df["B1"] == onceki_game_week + 1) & (mac_verileri_df.index == j)]
        
#         if not sonraki_mac.empty:
#             puan_degisimi = sonraki_mac.iloc[0]["B2"] - mac["B2"]
            
#             if puan_degisimi == 3:  # +3 varsa win
#                 win_count += 1
#             elif puan_degisimi == 1:  # +1 varsa draw
#                 draw_count += 1
#             elif puan_degisimi == 0:  # 0 veya değişim yoksa loss
#                 loss_count += 1
    
#     # Toplam maç sayısını ve yüzdeleri hesapla
#     total_matches = win_count + draw_count + loss_count
#     if total_matches > 0:
#         win_orani = (win_count / total_matches) * 100
#         draw_orani = (draw_count / total_matches) * 100
#         loss_orani = (loss_count / total_matches) * 100
#     else:
#         win_orani = 0
#         draw_orani = 0
#         loss_orani = 0
    
#     # Sonuçları ID ile birlikte sakla
#     sonuclar.append({
#         "ID": parametreler_ids[i],
#         "Win Oranı (%)": win_orani,
#         "Draw Oranı (%)": draw_orani,
#         "Loss Oranı (%)": loss_orani
#     })

# # Sonuçları bir DataFrame'e dönüştür ve bir Excel dosyasına yazdır
# sonuclar_df = pd.DataFrame(sonuclar)
# sonuclar_df.to_excel("mac_sonuclari.xlsx", index=False)





import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

# Dosyaları oku
parametreler_df = pd.read_excel("incomplete_matches_with_previous_week_parameters2.xlsx")
mac_verileri_df = pd.read_excel("Tahmındeneme.xlsx")

# ID sütunlarını ayır ve diğer verileri temizle
parametreler_ids = parametreler_df["ID"]
parametreler = parametreler_df.drop(columns=["ID", "B2", "B92"])  # B92'yi de çıkarıyoruz
mac_verileri_ids = mac_verileri_df["ID"]
mac_verileri_parametreler = mac_verileri_df.drop(columns=["ID", "B2", "B92"])  # B92'yi de çıkarıyoruz

# Eksik değerleri temizle ve verileri sayısal hale getir
parametreler = parametreler.apply(pd.to_numeric, errors='coerce').dropna()
mac_verileri_parametreler = mac_verileri_parametreler.apply(pd.to_numeric, errors='coerce').dropna()

# Her bir maç için en yakın 20 maçı bul ve win/draw/loss yüzdelerini hesapla
sonuclar = []

for i, parametre_satiri in parametreler.iterrows():
    # En yakın 20 maçı bulmak için Euklides mesafesi hesapla
    mesafeler = euclidean_distances([parametre_satiri.values], mac_verileri_parametreler.values)
    en_yakin_indexler = mesafeler.argsort()[0][:100]
    
    # En yakın 20 maçı filtrele
    en_yakin_maclar = mac_verileri_df.iloc[en_yakin_indexler]
    
    # Sonuçları say
    team1_win_count = 0
    draw_count = 0
    team2_win_count = 0
    
    for j, mac in en_yakin_maclar.iterrows():
        onceki_game_week = mac["B1"]
        sonraki_maclar = mac_verileri_df[(mac_verileri_df["B1"] == onceki_game_week + 1) & (mac_verileri_df.index.isin(en_yakin_indexler))]
        
        if not sonraki_maclar.empty:
            for _, sonraki_mac in sonraki_maclar.iterrows():
                # Birinci takımın ve ikinci takımın maç sonucu
                team1_puan_degisimi = sonraki_mac["B2"] - mac["B2"]
                team2_puan_degisimi = mac["B92"] - sonraki_mac["B92"]

                if team1_puan_degisimi == 3:
                    team1_win_count += 1
                elif team1_puan_degisimi == 1:
                    draw_count += 1
                elif team1_puan_degisimi == 0:
                    if team2_puan_degisimi == 3:
                        team2_win_count += 1
                    elif team2_puan_degisimi == 1:
                        draw_count += 1
                    elif team2_puan_degisimi == 0:
                        continue

    # Toplam maç sayısını ve yüzdeleri hesapla
    total_matches = team1_win_count + draw_count + team2_win_count
    if total_matches > 0:
        team1_win_orani = (team1_win_count / total_matches) * 100
        draw_orani = (draw_count / total_matches) * 100
        team2_win_orani = (team2_win_count / total_matches) * 100
    else:
        team1_win_orani = 0
        draw_orani = 0
        team2_win_orani = 0
    
    # Sonuçları ID ile birlikte sakla
    sonuclar.append({
        "ID": parametreler_ids[i],
        "Team1 Kazanma Oranı (%)": team1_win_orani,
        "Draw Oranı (%)": draw_orani,
        "Team2 Kazanma Oranı (%)": team2_win_orani
    })

# Sonuçları bir DataFrame'e dönüştür ve bir Excel dosyasına yazdır
sonuclar_df = pd.DataFrame(sonuclar)
sonuclar_df.to_excel("mac_sonuclari.xlsx", index=False)

print("Sonuçlar başarıyla 'mac_sonuclari.xlsx' dosyasına yazıldı.")
