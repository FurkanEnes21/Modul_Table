import time
import Home_Sıralama
import Sheets_Birlestirme2
import RankAnd_TotalRankDiff2
import Goal_Timing2
from tqdm import tqdm



def main():
    print("Kod 1 çalışıyor...")
    kod1_output = Home_Sıralama.main()
    print("Kod 1 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 2 çalışıyor...")
    kod2_output = Sheets_Birlestirme2.main(kod1_output)
    print("Kod 2 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 3 çalışıyor...")
    RankAnd_TotalRankDiff2.main(kod2_output)
    print("Kod 3 tamamlandı.")
    
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 4 çalışıyor...")
    Goal_Timing2.main(kod2_output)
    print("Kod 4 tamamlandı.")
    
if __name__ == "__main__":
    main()
