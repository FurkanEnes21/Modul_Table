import time
import Mod8_First
import Mod8_Second
import Mod8_Thirth
import Mod8_Fourth
import Goal_Timing8
import Sheets_Birlestirme8
import RankAnd_TotalRankDiff8
from tqdm import tqdm



def main():
    print("Kod 1 çalışıyor...")
    kod1_output = Mod8_First.main()
    print("Kod 1 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 2 çalışıyor...")
    kod2_output = Mod8_Second.main(kod1_output)
    print("Kod 2 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 3 çalışıyor...")
    Mod8_Thirth.main(kod2_output)
    print("Kod 3 tamamlandı.")
    
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 4 çalışıyor...")
    Mod8_Fourth.main(kod2_output)
    print("Kod 4 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)
        
    print("Kod 5 çalışıyor...")
    Sheets_Birlestirme8.main(kod2_output)
    print("Kod 5 tamamlandı.")
        

    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 6 çalışıyor...")
    RankAnd_TotalRankDiff8.main(kod2_output)
    print("Kod 6 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 7 çalışıyor...")
    Goal_Timing8.main(kod2_output)
    print("Kod 7 tamamlandı.")
    
if __name__ == "__main__":
    main()