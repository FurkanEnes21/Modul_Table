import time
import Mod6_First
import Mod6_Second
import Mod6_Thirth
import Mod6_Fourth
import Goal_Timing6
import Sheets_Birlestirme6
import RankAnd_TotalRankDiff6
from tqdm import tqdm
 
 

def main():
    print("Kod 1 çalışıyor...")
    kod1_output = Mod6_First.main()
    print("Kod 1 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 2 çalışıyor...")
    kod2_output = Mod6_Second.main(kod1_output)
    print("Kod 2 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 3 çalışıyor...")
    Mod6_Thirth.main(kod2_output)
    print("Kod 3 tamamlandı.")
    
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 4 çalışıyor...")
    Mod6_Fourth.main(kod2_output)
    print("Kod 4 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 5 çalışıyor...")
    Sheets_Birlestirme6.main(kod2_output)
    print("Kod 5 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 6 çalışıyor...")
    RankAnd_TotalRankDiff6.main(kod2_output)
    print("Kod 6 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 7 çalışıyor...")
    Goal_Timing6.main(kod2_output)
    print("Kod 7 tamamlandı.")
    
if __name__ == "__main__":
    main()