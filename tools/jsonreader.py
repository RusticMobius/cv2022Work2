import json
f = open('../datasets/test/openpose-json/07445_00_keypoints.json', encoding="utf-8")
x = json.load(f)
print(x)
print(len(x['people'][0]['pose_keypoints_2d']))
