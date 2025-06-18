import json
with open('qwenvl_Diagnosis_output.json','r',encoding="utf-8") as f:
    result=json.load(f)

def contains(key,s):
    key_lower = key.lower()
    s_lower = s.lower()
    return key_lower in s_lower

crop=0
disease=0
qwen_crop=0
qwen_disease=0
ii=0
cropmap = {}
diseasemap = {}

for item in result:
    question_id = item['question_id']
    question = item['question']
    image = item['image'] 
    annotation = item['answer']
    answer_qw = item['qwenvl']
    crop_l,disease_l=image.split('/')[-2].split(',') 

    crop+=contains(crop_l,annotation)
    disease+=contains(disease_l,annotation)
    qwen_crop+=contains(crop_l,answer_qw)
    qwen_disease+=contains(disease_l,answer_qw)

    if crop_l in cropmap.keys():
        cropmap[crop_l]+=1
    else:
        cropmap[crop_l]=1
    if disease_l in diseasemap.keys():
        diseasemap[disease_l]+=1
    else:
        diseasemap[disease_l]=1

    ii+=1

print(qwen_crop/crop,qwen_disease/disease)