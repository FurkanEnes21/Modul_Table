import time
import Mod5_First
import Mod5_Second
import Mod5_Thirth
import Mod5_Fourth
import Goal_Timing5
import Sheets_Birlestirme5
import RankAnd_TotalRankDiff5
from tqdm import tqdm



def main():
    print("Kod 1 çalışıyor...")
    kod1_output = Mod5_First.main()
    print("Kod 1 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 2 çalışıyor...")
    kod2_output = Mod5_Second.main(kod1_output)
    print("Kod 2 tamamlandı.")
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 3 çalışıyor...")
    Mod5_Thirth.main(kod2_output)
    print("Kod 3 tamamlandı.")
    
    
    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 4 çalışıyor...")
    Mod5_Fourth.main(kod2_output)
    print("Kod 4 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 5 çalışıyor...")
    Sheets_Birlestirme5.main(kod2_output)
    print("Kod 5 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 6 çalışıyor...")
    RankAnd_TotalRankDiff5.main(kod2_output)
    print("Kod 6 tamamlandı.")


    for i in tqdm(range(5), desc="Bekliyor"):
        time.sleep(1)

    print("Kod 7 çalışıyor...")
    Goal_Timing5.main(kod2_output)
    print("Kod 7 tamamlandı.")
    
if __name__ == "__main__":
    main()