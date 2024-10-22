
from pathlib import Path
import re
import os

def classify_round(round_type):
    exempt_rounds = {"ミスティックムーン", "トワイライト", "ソルスティス", "Mystic Moon", "Twilight", "Solstice"}
    special_rounds = {"霧", "パニッシュ", "サボタージュ", "狂気", "オルタネイト", "ブラッドバス", "ミッドナイト", "8ページ", "アンバウンド", "ゴースト", "ダブル・トラブル", "Fog", "Punished", "Sabotage", "Cracked", "Alternate", "Bloodbath", "Midnight", "8 Pages", "Unbound", "Ghost", "Double Trouble"}
    classic_rounds = {"クラシック", "ブラッドムーン", "Classic", "Blood Moon"}
    
    if round_type in exempt_rounds:
        return "Exempt"
    elif round_type in special_rounds:
        return "特殊"
    elif round_type in classic_rounds:
        return "クラシック"
    else:
        return "?"

def Read_Log(line_list):
    for i in range(len(line_list)):
        line = line_list[i]
        if "This round is taking place at" in line:
            match_location = re.search(r"at ([\w\s()]+) and", line)
            match_round_type = re.search(r"the round type is ([\w・()]+)", line)
            location = match_location.group(1) if match_location else None
            round_type = match_round_type.group(1) if match_round_type else None
            if (round_type != None):
                classification = classify_round(round_type)

            print("マップ名: " + location + " ラウンドタイプ: " + round_type + "（" + classification + "）")

        if "Lived in round." in line:
            print("勝利！")
        if "Died in round." in line:
            print("全滅...")

def Read_LogFile(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    line_list = [s.rstrip() for s in f.readlines()]
    Read_Log(line_list)
    f.close()

# ログディレクトリを取得
log_directory = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "VRChat", "VRChat")

p = Path(log_directory)
files = list(p.glob("output_log_*.txt"))
print("ログファイルを検索中...")
for file_path in files:
    print("\nファイル名: " + str(file_path))
    Read_LogFile(file_path)