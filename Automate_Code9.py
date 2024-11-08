import time
import Mod9_First
import Mod9_Second
import Mod9_Thirth
import Mod9_Fourth
import Goal_Timing9
import Sheets_Birlestirme9
import RankAnd_TotalRankDiff9
from tqdm import tqdm



def main():
    print("Kod 1 çalışıyor...")
    kod1_output = Mod9_First.main()
    print("Kod 1 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 2 çalışıyor...")
    kod2_output = Mod9_Second.main(kod1_output)
    print("Kod 2 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 3 çalışıyor...")
    Mod9_Thirth.main(kod2_output)
    print("Kod 3 tamamlandı.")
    
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 4 çalışıyor...")
    Mod9_Fourth.main(kod2_output)
    print("Kod 4 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 5 çalışıyor...")
    Sheets_Birlestirme9.main(kod2_output)
    print("Kod 5 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 6 çalışıyor...")
    RankAnd_TotalRankDiff9.main(kod2_output)
    print("Kod 6 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 7 çalışıyor...")
    Goal_Timing9.main(kod2_output)
    print("Kod 7 tamamlandı.")
    
if __name__ == "__main__":
    main()