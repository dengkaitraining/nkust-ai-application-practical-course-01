from pathlib import Path

# Finds the folder where your script is saved
script_dir = Path(__file__).parent

# Combines the folder path with your file name
file_path = script_dir / "demofile.txt"

# 建立空陣列
data = []

# 讀取檔案
with open(file_path, "r") as file:
    for line in file:
        data.append(line.strip())

# 初始化變數
total_spend = 0
count = 0

# 跳過第一列標題
for row in data[1:]:
    
    # 使用逗號切割 CSV
    fields = row.split(",")
    
    # spend 為第3個欄位(index=2)
    spend = float(fields[2])
    
    total_spend += spend
    count += 1

# 計算平均
average = total_spend / count if count > 0 else 0

# 印出結果
print("Spend平均數:", average)
print("Spend總數:", total_spend)
print("總筆數:", count)
print(f"Spend平均數:{average:.2f}")
print(f"Spend總數:{total_spend:.2f}")
print(f"總筆數:{count:.2f}")