import os
import json


path = "./data/iclr2025.json"
with open(path, "r") as f:
    lines = json.load(f)

txts = list()
for line in lines:
    chunk = f"{line['name']}\\n{line['abstract']}"
    content = f"{chunk[:500]}<BEGIN_URL>{line['virtualsite_url']}<END_URL>"
    txts.append(content[:600])

save_dir = "./data/txt"
os.makedirs(save_dir, exist_ok=True)
with open(f"{save_dir}/iclr2025.txt", "w") as o:
    o.write("\n".join(txts))
