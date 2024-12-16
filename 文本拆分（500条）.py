import json

# 读取原始的 JSONL 文件
input_file = "new_dataset.jsonl"
output_profix = "new_dataset"
output_ext = ".jsonl"

# 读取数据
data = []
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        data.append(json.loads(line.strip()))

# 分割逻辑
batch_size = 500
new_data = []
file_index = 0

for item in data:
    new_data.append(item)
    if len(new_data) == batch_size:  # 如果当前批次满 500 条
        file_index += 1
        output_file = f"{output_profix}{file_index}{output_ext}"
        with open(output_file, "w", encoding="utf-8") as file:
            for entry in new_data:
                file.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"保存文件: {output_file}")
        new_data = []  # 清空当前批次

# 处理剩余数据
if new_data:
    file_index += 1
    output_file = f"{output_profix}{file_index}{output_ext}"
    with open(output_file, "w", encoding="utf-8") as file:
        for entry in new_data:
            file.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"保存文件: {output_file}")
