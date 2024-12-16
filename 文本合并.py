import json
data=[]
with open("dataset.jsonl","r",encoding="utf-8") as file:
    for line in file:
        data.append(json.loads(line.strip()))
for i in range(10):
    print(data[i])
merged_data = []
cur_input = ""
cur_output = ""
cur_instruction = ""

# 合并逻辑
for item in data:
    if len(cur_input) + len(item["input"]) <= 350:  # 检查input总长度是否超过350
        cur_input += item["input"] + " "
        cur_output += item["output"] + " "
        cur_instruction = item["instruction"]  # 保持指令一致
    else:
        # 如果超过350，则保存当前的合并数据，并开始新的段落
        merged_data.append({
            "input": cur_input.strip(),
            "output": cur_output.strip(),
            "instruction": cur_instruction
        })
        cur_input = item["input"] + " "
        cur_output = item["output"] + " "
        cur_instruction = item["instruction"]

# 保存最后剩余的数据
if cur_input:
    merged_data.append({
        "input": cur_input.strip(),
        "output": cur_output.strip(),
        "instruction": cur_instruction
    })

output_file = "new_dataset.jsonl"

# 保存到 JSONL 文件
with open(output_file, "w", encoding="utf-8") as file:
    for item in merged_data:
        file.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"数据已成功保存到 {output_file}")