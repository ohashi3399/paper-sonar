import os
import json
import openreview


client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")
submissions = client.get_all_notes(
    invitation="ICLR.cc/2025/Conference/-/Submission",
    details="directReplies",
)

abstracts = list()
id2paper = dict()
for submission in submissions:
    truncated_abst = submission.content["abstract"]["value"].replace("\n", "")[:800]
    abstracts.append(f"{truncated_abst}<BEGIN_ID>{submission.id}<END_ID>")
    attribute = submission.content
    attribute["directReplies"] = submission.details
    id2paper[submission.id] = attribute

root_dir = "./data/iclr2025/all_submissions/txt"
os.makedirs(root_dir, exist_ok=True)

with open(f"{root_dir}/iclr2025.txt", "w") as o:
    o.write("\n".join(abstracts))

with open(f"{root_dir}/iclr2025_id2paper.json", "w") as o:
    json.dump(id2paper, o, indent=2)
