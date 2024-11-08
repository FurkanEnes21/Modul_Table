import time
import Mod4_First
import Mod4_Second
import Mod4_Thirth
import Mod4_Fourth
import Goal_Timing4
import Sheets_Birlestirme4
import RankAnd_TotalRankDiff4
from tqdm import tqdm



def main():
    print("Kod 1 çalışıyor...")
    kod1_output = Mod4_First.main()
    print("Kod 1 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 2 çalışıyor...")
    kod2_output = Mod4_Second.main(kod1_output)
    print("Kod 2 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 3 çalışıyor...")
    Mod4_Thirth.main(kod2_output)
    print("Kod 3 tamamlandı.")
    
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 4 çalışıyor...")
    Mod4_Fourth.main(kod2_output)
    print("Kod 4 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 5 çalışıyor...")
    Sheets_Birlestirme4.main(kod2_output)
    print("Kod 5 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 6 çalışıyor...")
    RankAnd_TotalRankDiff4.main(kod2_output)
    print("Kod 6 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 7 çalışıyor...")
    Goal_Timing4.main(kod2_output)
    print("Kod 7 tamamlandı.")
    
if __name__ == "__main__":
    main()

