import itertools

import sqlalchemy

database_username = 'root'
database_password = ''
database_ip = '127.0.0.1'
database_name = 'resume_store'
db = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                              format(database_username, database_password,
                                     database_ip, database_name))
import csv


def count_accuracy(no, email, skills, work, project, deg, uni, certificate):
    accuracy = 0
    score = 0
    if no is not None:
        if len(no) != 0:
            accuracy += 10
        else:
            accuracy += 0
    if email is not None:
        if len(email) != 0:
            accuracy += 10
        else:
            accuracy += 0
    if project is not None:

        if len(project) != 0:
            accuracy += 20
        else:
            accuracy += 0

    if deg is not None:
        if len(deg) != 0:
            accuracy += 10
            file = r"E:\flask\sample_application\degreelist3.csv"
            w = open(file, 'r')
            read = csv.reader(w)
            lis = list(read)
            # print(list)
            flatlist = []
            for sublist in lis:
                for item in sublist:
                    item = item.lower()
                    # item=item.replace(" ","-")
                    item = item.replace(" ", "")
                    item = item.replace(".", "")
                    flatlist.append(item)

            h = dict(itertools.zip_longest(*[iter(flatlist)] * 2, fillvalue=""))
            ls = []

            lst = deg
            for l in lst:
                for key in h.keys():
                    if (key == l):
                        data5 = h[key]
                        b = list(data5)
                        ls.extend(b)
            print("ls", ls)

            if len(ls) != 0:
                for i in ls:
                    score += int(i)
            else:
                score += 0
        else:
            accuracy += 0
    if uni is not None:

        if len(uni) != 0:
            accuracy += 10
            file = r"E:\flask\sample_application\univer2.csv"
            w = open(file, 'r',encoding='unicode-escape')
            read = csv.reader(w)
            lis = list(read)
            # print(list)
            flatlist = []
            for sublist in lis:
                for item in sublist:
                    item = item.lower()
                    # item=item.replace(" ","-")
                    item = item.replace(" ", "")
                    item = item.replace(".", "")
                    flatlist.append(item)

            h = dict(itertools.zip_longest(*[iter(flatlist)] * 2, fillvalue=""))
            ls = []
            lst = uni
            for l in lst:
                for key in h.keys():
                    if (key == l):
                        data5 = h[key]
                        b = list(data5)
                        ls.extend(b)
            print("ls", ls)

            if len(ls) != 0:
                for i in ls:
                    score += int(i)
            else:
                score += 0
        else:
            accuracy += 0
    if skills is not None:
        import pandas as pd
        if len(skills) != 0:
            accuracy += 20
            user1 = pd.read_csv(r"E:\flask\sample_application\skills.csv",index_col=None)

            file = r"E:\flask\sample_application\skills1.csv"
            w = open(file, 'r',encoding='unicode-escape')
            read = csv.reader(w)

            lis =  list(read)
            # print(list)
            flatlist = []
            for sublist in lis:
                for item in sublist:
                    item = item.lower()
                    # item=item.replace(" ","-")
                    item = item.replace(" ", "")
                    item = item.replace(".", "")
                    flatlist.append(item)

            # h = dict(itertools.zip_longest(*[iter(flatlist)] * 2, fillvalue=""))
            ls = []
            # dem_match= user1.iloc[:,[0,2]]
            # lis2= dem_match.values.tolist()
            # flatlist2 = []
            # for sublist in lis2:
            #     for item in sublist:
            #         item = item.lower()
            #         # item=item.replace(" ","-")
            #         item = item.replace(" ", "")
            #         item = item.replace(".", "")
            #         flatlist2.append(item)

            # h2 = dict(itertools.zip_longest(*[iter(flatlist2)] * 2, fillvalue=""))
            user1['p']=pd.Series(flatlist)
            demand=[]
            lst = skills
            # for l in lst:
            #     for key in h.keys():
            #         if (key == l):
            #             data5 = h[key]
            #             b = list(data5)
            #             ls.extend(b)
            #             dar=h2[key]
            #             demand.extend(dar)
            # print("ls", demand)
            ls = []
            demand = []
            entt= []
            comm= []
            bankk= []
            lst = skills
            for l in lst:
                data4 = user1.loc[user1['p'] == l]
                data5 = data4["Weight"]
                data6 = data4["demand"]
                data7 = data4["Entertainment"]
                data8 = data4["computer"]
                data9 = data4["bankloans"]
                wi = list(data5)
                dem = list(data6)
                ent = list(data6)
                com = list(data6)
                bank = list(data6)
                ls.extend(wi)
                demand.extend(dem)
                entt.extend(ent)
                comm.extend(com)
                bankk.extend(bank)

            if len(ls) != 0:
                for i in ls:
                    score += int(i)
            else:
                score += 0
        else:
            accuracy += 0
    if work is not None:

        if work != '0 years':
            if len(work) != 0:
                accuracy += 20
                score+=50
        else:
            accuracy += 0
            score+=0
    if certificate is not None:

        if len(certificate) != 0:
            accuracy += 20

            file = r"E:\flask\sample_application\certificate.csv"
            w = open(file, 'r',encoding='unicode-escape')
            read = csv.reader(w)
            lis = list(read)
            # print(list)
            flatlist = []
            for sublist in lis:
                for item in sublist:
                    item = item.lower()
                    # item=item.replace(" ","-")
                    item = item.replace(" ", "")
                    item = item.replace(".", "")
                    flatlist.append(item)

            h = dict(itertools.zip_longest(*[iter(flatlist)] * 2, fillvalue=""))
            ls = []
            lst = certificate
            for l in lst:
                for key in h.keys():
                    if (key == l):
                        data5 = h[key]
                        b = list(data5)
                        ls.extend(b)
            print("ls", ls)
        else:
            accuracy += 0
    percent = 0
    status = ""
    if accuracy <= 120 and accuracy >= 80:
        if accuracy <= 120 and accuracy >= 100:

            percent = 100
        else:
            percent = accuracy
        status = "completed"
    elif accuracy > 80 and accuracy < 40:
        percent = accuracy
        status = "parsed with error"
    elif accuracy > 60 and accuracy < 40:
        percent = accuracy
        status = "parsed with error"
    else:
        percent = accuracy
        status = "parsed with error"
    per=0
    print("score:",score)
    score=int(score)
    global grade
    grade = ""
    print("grade:", grade)
    if score <= 100 and score >= 90:
        grade="A+"

        print("grade:", grade)
    elif score < 90 and score >= 80:
        grade = "A"

        print("grade:", grade)
    elif score < 80 and score >= 75:

        grade = "B+"
    elif score < 75 and score >= 70:

        grade = "B"
    elif score < 70 and score >= 60:

        grade = "B-"
    elif score < 60 and score >= 40:

        grade = "C"

        print("grade:", grade)
    elif score < 40 and score >= 30:

        grade = "C-"

        print("grade C-:", grade)
    else:
        grade = "F"

        print("grade F:", grade)
    co=0
    for i in comm:
        co+=i
    en=0
    for i in entt:
        en+=i
    bk=0
    for i in bankk:
        bk+=i
    return status, percent,score,grade,co,en,bk
