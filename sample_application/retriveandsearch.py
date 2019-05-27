import csv as csv
import  pandas as pd
import csv as csv

import pandas as pd

lskill = ['java', 'ui']
lexp = 3
d5 = dict()
d4 = dict()
d2 = dict()
d3 = dict()
d6 = dict()
d8 = dict()

def find_resumes(search_list):
    df=pd.read_csv(r"E:\flask\sample_application\allresumes.csv",encoding='unicode_escape',error_bad_lines=False)
    list_skill=[]
    list_certificate=[]
    list_Expereince=[]
    countt=[]

    with open(r"E:\flask\sample_application\allresumes.csv", 'r+') as f, open('file2.csv', 'w+') as g:
            reader = csv.DictReader(f)
            c1,c2,c3,c4,c5,c6,c7,c8,c9,c10, c11, c12,c13 = reader.fieldnames
            writer = csv.DictWriter(g, fieldnames=(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10, c11, c12,c13))
            s=[]

            rowcount=0
            for row in reader:

                for  r in row[c10].split():
                    s=r.split(",")
                for j in s:
                    for i in search_list:
                        search_string = i
                        rowcount+=1
                        if j == search_string :
                            # writer.writerow({c10: row[c10], c11: row[c11], c12: row[c12]})
                            writer.writerow(row)
                            d2[j+str(rowcount)]=str(row)



    print(len(d2))


    # for key, values in d2.items():
    #     count[key] = len(values)
    # print(count)
    df=pd.read_csv("file2.csv",encoding='unicode_escape')
    df2=df.copy()
    df2=df2.iloc[:,1:]
    df2=pd.DataFrame(df2)
    listdc=[]
    listrow=[]
    coun = {}
    d4=d2.copy()
    for key, values in d2.items():
        for keyy, value in d4.items():
            if values==value:
                coun[key+keyy]=values
                listdc.append(key)
                listrow.append(values)

    c=pd.DataFrame.from_dict(coun,orient='index')
    c.to_csv('fil.csv')
    s=pd.read_csv('fil.csv',names=["key","row"])
    s=s.dropna()
    s.to_csv('fill.csv',index=False)
    lis=s['key'].tolist()
    newlis=[]
    nnlis=[]
    jp=''
    mas=''
    with open("fill.csv", 'r+') as f:
        reader = csv.reader(f)
        for raw in reader:
            mas=','.join(raw)
            for i in mas[2:19]:
                if i.isalpha():
                    jp+=''.join(i)
            nnlis.append(jp+"/"+mas)
    print(nnlis)
    for i in lis:
        st = ''
        for j in str(i):

            if str(j).isalpha():
                st+=''.join(j)
        if st=="androidjava" or st=="javaandroid":

            newlis.append(st)
    print(newlis)
    df2.to_csv('file3.csv', index=False,
                  header=['accuracy', 'Status', 'Name', 'Location', 'phoneno', 'email', 'degree', 'university','skills', 'work_exp', 'certification', 'project'])
    d3=pd.read_csv("file3.csv",encoding='unicode_escape')

find_resumes(["java","android"])

# def resume_finder_skills(d1):
#     count = 0
#     w = csv.writer(open(r"ds.csv", "w",encoding='unicode_escape'))  ##shortlisted resumes
#     w.writerow(['CandidateId', 'skill'])
#     w1 = csv.writer(open(r"sample_application\allresumes.csv","w",encoding='unicode_escape'))  ##integer values with count weightage
#     for k in d1.keys():
#         count = 0
#         for l in lskill:
#             if l in d1[k]:
#                 count = count + 1
#
#         if count <= len(lskill) and count != 0:
#             w.writerow([k, d1[k]])
#
#             if 'ui' in d1[k] and 'java' in d1[k]:
#                 w1.writerow([k, d1[k].count('java'), d1[k].count('ui')])
#                 d4.update({k: [d1[k].count('java'), d1[k].count('ui')]})
#             elif 'ui' in d1[k] and 'java' not in d1[k]:
#                 w1.writerow([k, 0, d1[k].count('ui')])
#                 d4.update({k: [0, d1[k].count('ui')]})
#             else:
#                 w1.writerow([k, d1[k].count('java'), 0])
#                 d4.update({k: [d1[k].count('java'), 0]})
#
# def retrieve_exp(d):
#     for k in d.keys():
#         match = re.search(
#             r'(?:\d?|\d\d?)+\s+(?:years?|yrs?)\s+(?:and\s*)?(?:\d?|\d\d?)+\s+months?|(?:\d?|\d\d?|\d\d\d?)+\s+(?:months?|years?|yrs?)|(?:\d?|\d\d?)\.?(?:\d?|\d\d?)+\s+(?:yrs?|years?|months)|(?:\d?|\d\d?)\.?(?:\d?|\d\d?)(?:\+?)+\s+(?:yrs?|years?|months)|(?:\d?|\d\d?|\d\d\d?)(?:\+?)+\s+(?:months?|years?|yrs?)',
#             str(d[k]), re.I)
#         if match:
#             experience = match.group(0)
#         else:
#             experience = "NULL"
#         d3.update({k: str(experience)})
# import string
# def resume_finder_exp():
#     w2 = csv.writer(open(r"shortlisted.csv", "w",encoding='unicode_escape'))
#     w2.writerow(['CandidateId', 'EmailId', 'Experience', 'Java', 'UI', 'Skillset', 'Positions held'])
#     mono=getpersonalinfo()
#     deg=geteduinfo()
#     skills=getskillinfo()
#     pro=getprojectinfo()
#     certi=getcertificateinfo()
#     email=[]
#     ph=[]
#     for i in mono.values():
#         for k in i.values():
#             print(k)
#             if "@" in k:
#                 email.append(k)
#             else:
#                 ph.append(k)
#     print(email)
#
#     print(ph)
#     university=[]
#     degree=[]
#     for i in deg.values():
#         for k in i.values():
#
#             if "uni" in k:
#                university.append(k)
#             else:
#                 degree.append(k)
#     print(degree)
#     print(university)
#     skill=[]
#     for i in skills.values():
#         for k in i.values():
#             skill.append([k])
#     print(skill)
#     project=[]
#     for i in pro.values():
#         for k in i.values():
#             project.append([k])
#     print(project)
#     print(certi)
# resume_finder_exp()
