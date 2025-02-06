import os
import json


path = "./data/iclr2025.json"
with open(path, "r") as f:
    lines = json.load(f)

txts = list()
for line in lines:
    txts.append(f"{line['name']}\\n{line['abstract']}")

save_dir = "./data/db"
os.makedirs(save_dir, exist_ok=True)
with open(f"{save_dir}/iclr2025.txt", "w") as o:
    o.write("\n".join(txts))
