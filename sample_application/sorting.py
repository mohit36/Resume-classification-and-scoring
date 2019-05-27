import fileinput
import os
import re
from time import gmtime, strftime
import datetime
import string
from nltk import word_tokenize
import pandas as pd
import numpy as np

# key = raw_input("Please enter the word you with to search for: ")
# print "You've selected: ", key, " as you're key-word."

import glob, os

os.chdir(r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\622019\New folder")
file_list = []
for file in glob.glob("*.pdf"):
    print(file)
    path = file

    import PyPDF2

    pdfName = path
    read_pdf = PyPDF2.PdfFileReader(pdfName)

    content = ""
    read_list = []
    for i in range(read_pdf.getNumPages()):
        page = read_pdf.getPage(i)
        # print( 'Page No - ' + str(1+read_pdf.getPageNumber(page)))
        page_content = [page.extractText()]
        # content+=page_content
        # print(page_content)
        read_list.append(page_content)

    print(read_list)
    cont = []
    for i in read_list:
        for j in i:
            pri = (j.replace("\n", ""))
            cont.append(pri)
    content = "".join(cont)

    # import docx2txt
    # my_text = docx2txt.process(r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\SampleCVs\Chandru_Resume.docx")
    # print(my_text)
    # content=my_text

    path_file = r'C:\Users\Milan\Downloads\New folder\resume_mohit.txt'
    with open(path_file, 'r') as f:
        # content = str(f.readlines())
        content2 = f.read()
        content1 = content
        re = word_tokenize(content)
        # print("re=",re)
        d = {}
        # print(content)
        try:
            content = content.lower()
            # print(content)
            content = content.lower()
            education = ["academic qualification", "Education qualification", "Educational qualification",
                         "qualification", "education", "academic"]
            for i in education:
                word = i
                word = word.lower()
                list1 = content.split(' ')
                try:
                    position = content.index(word)
                except:
                    continue
                d[position] = word
                print(d)
                break
        except:
            print("education not found")
        # print(d)
        try:
            word = ("personal")
            word = word.lower()
            list1 = content.split(' ')
            position = content.index(word)
            d[position] = word
        # print(d)
        except:
            print("personal not found")

        try:
            word = ("Academic project")
            word = word.lower()
            list1 = content.split(' ')
            position = content.index(word)
            d[position] = word
        # print(position, word)
        except:
            print("project not found")

        try:
            word = ("certificate")
            word = word.lower()
            list1 = content.split(' ')
            position = content.index(word)
            d[position] = word
        # print(position, word)
        except:
            print("certificate not found")

        try:

            content = content.lower()
            skill = ["technical skills", "technical skill", "Technical Competencies", "technical qualities",
                     "Software Skill", "IT Skill", "COMPUTER KNOWLEDGE", "skills", "skill"]
            for i in skill:
                word = i
                word = word.lower()
                list1 = content.split(' ')
                try:
                    position = content.index(word)
                except:
                    continue
                d[position] = word
                print(d)
                break
            # print(d)
        except:
            print("skill not found")

        try:
            content = content.lower()
            # print(content)
            content = content.lower()
            education = ["work experience"]
            for i in education:
                word = i
                word = word.lower()
                list1 = content.split(' ')
                try:
                    position = content.index(word)
                except:
                    continue
                d[position] = word
                print(d)
                break
        except:
            print("work experience not found")
        l = [value for (key, value) in sorted(d.items())]
        # print("l value",l[0],l[1],l[2],l[3])

        print("val", [value for (key, value) in sorted(d.items())])

        d = sorted(d)
        print("d=", d)
        print(len(d))
        # print(d,key=d.__getitem__())
        o = tuple(zip(d, l))
        # print(o)
        an = []
        app = str(datetime.datetime.now().timestamp())
        # words = app.split()
        # table = str.maketrans('', '', string.punctuation)
        # app = str([w.translate(table) for w in words])
        os.makedirs(r'C:\Users\Milan\Downloads\resume-' + app)
        current_path = (r'C:\Users\Milan\Downloads\resume-' + app)

        for i in range(0, len(d)):
            # print(l[i])
            # print(os.getcwd())
            # print("current path"+str(current_path))
            print("l" + l[i], i)
            if (l[i] == l[-1]):
                start = l[i]
                end = l[i]
                print("start", start, end, i)
                pri = (content[content.find(start) + len(start):] + "\n\n")
                # print(i, pri)





            else:
                start = l[i]
                end = l[i + 1]
                print("ens", start, end, i)
                prin = (content[content.find(start) + len(start):content.find(end)] + "\n\n")
                # print(i,prin)

            if (i == 0):
                print("open", l[i], start, end)
                w = open(current_path + "\\" + l[0] + ".txt", "w", encoding='unicode-escape')
                # print(current_path)
                w.write(prin)
            elif (l[i] == l[-1]):
                print("openthis", l[i], start, end)
                s = len(d) - 1
                print("s", s)
                w = open(current_path + "\\" + l[s] + ".txt", "w", encoding='unicode-escape')
                w.write(pri)

                # w=open(current_path + "\per.txt", "w")
                # pr=("line....",content1[d[0]:d[1]])
                # w.write(str(pr))


            elif (i == 1):
                # print("open work")
                print("open ", l[i], start, end)
                w = open(current_path + "\\" + l[1] + ".txt", "w", encoding='unicode-escape')
                w.write(prin)
                # print(prin)
            elif (i == 2):
                print("open", l[i], start, end)
                # print("open education")
                w = open(current_path + "\\" + l[2] + ".txt", "w", encoding='unicode-escape')
                w.write(prin)
                # print(prin)
            elif (i == 3):
                print("open", l[i], start, end)
                # print("open skill")
                w = open(current_path + "\\" + l[3] + ".txt", "w", encoding='unicode-escape')
                w.write(prin)
                # print(prin)
            elif (i == 4):
                print("open", l[i], start, end)
                # print("open certificate")
                w = open(current_path + "\\" + l[4] + ".txt", "w", encoding='unicode-escape')
                w.write(pri)

            elif (i == 5):
                print("open", l[i], start, end)
                # print("open certificate")
                w = open(current_path + "\\" + l[4] + ".txt", "w", encoding='unicode-escape')
                w.write(pri)

    # location

    # email,phone number
    try:
        import re

        ope = open(path_file)

        text = content

        mobileno = re.findall('(\d{9,})', text)
        print("mobile no", mobileno)
        s = set(mobileno)

        regex_email = "(\S+@)"

        regex_email = re.findall('\S+@\S+', text)
        print("email id", regex_email)
        s1 = set(regex_email)
    except:
        print("personal file not found")

    import csv
    from nltk.tokenize import sent_tokenize, word_tokenize

    file = r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\skills.csv"
    with open(file, "r", encoding='utf-8')as w:
        read1 = csv.reader(w)
        # print('read1')
        lis = list(read1)
        # print(lis)
    flatlist = []
    for sublist in lis:
        for item in sublist:
            item = item.lower()
            item = item.replace(" ", "-")
            flatlist.append(item)

    # print("flat")

    skill = ["technical skills", "technical skill", "Technical Competencies", "technical qualities",
             "Software Skill", "IT Skill", "COMPUTER KNOWLEDGE", "skills", "skill"]
    for i in skill:
        # print("parh")
        path = current_path + "\\" + i + ".txt"
        # print("path")
        if os.path.exists(path):
            print("file")
            ope = open(path, 'r')
            read = ope.read()
            resume_string = read
            # print("resume_string")
            resume_string = (resume_string.lower())
            # resume_string=resume_string.replace(" ","-")
            # print("resume",resume_string)
            sent = sent_tokenize(resume_string)
            # print("sent")

        else:
            continue
    data = []
    for s in sent:
        # print(s)
        word = word_tokenize(s)
        data.append(word)
        # print("word",word)
    # print("data",data)
    skill_hi = []
    for i in data:
        for j in i:
            for f in flatlist:
                # print("flatlist")
                if j == f:
                    if j not in skill_hi:
                        skill_hi.append(j)
    tech_skill = []
    # print(skill_hi)
    for s in skill_hi:
        k = "".join(re.findall('[a-z][A-Z]*', s))
        tech_skill.append(k)
    print("technical skill", tech_skill)

    kall = []
    for d in tech_skill:
        # for k in d:
        kall.append(d)
    print("degree", kall)

    data = pd.read_csv(r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\skills.csv")
    # dat=data["Degree"]

    data['protected'] = pd.Series(flatlist)
    df = pd.DataFrame(columns=['Degree'])
    for i in flatlist:
        df = df.append({'Degree': i}, ignore_index=True)

    ls = []
    lst = kall
    for l in lst:
        data4 = data.loc[data['protected'] == l]
        data5 = data4["Weight"]
        b = list(data5)
        ls.extend(b)
    print("ls", ls)





    # tech skill
    try:
        import csv
        from nltk.tokenize import sent_tokenize, word_tokenize

        file = r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\skills.csv"
        with open(file, "r", encoding='utf-8')as w:
            read1 = csv.reader(w)
            # print('read1')
            lis = list(read1)
            # print(lis)
        flatlist = []
        for sublist in lis:
            for item in sublist:
                item = item.lower()
                item = item.replace(" ", "-")
                flatlist.append(item)

        # print("flat")

        skill = ["technical skills", "technical skill", "Technical Competencies", "technical qualities",
                 "Software Skill", "IT Skill", "COMPUTER KNOWLEDGE", "skills", "skill"]
        for i in skill:
            # print("parh")
            path = current_path + "\\" + i + ".txt"
            # print("path")
            if os.path.exists(path):
                print("file")
                ope = open(path, 'r')
                read = ope.read()
                resume_string = read
                # print("resume_string")
                resume_string = (resume_string.lower())
                # resume_string=resume_string.replace(" ","-")
                # print("resume",resume_string)
                sent = sent_tokenize(resume_string)
                # print("sent")

            else:
                continue
        data = []
        for s in sent:
            # print(s)
            word = word_tokenize(s)
            data.append(word)
            # print("word",word)
        # print("data",data)
        skill_hi = []
        for i in data:
            for j in i:
                for f in flatlist:
                    # print("flatlist")
                    if j == f:
                        if j not in skill_hi:
                            skill_hi.append(j)
        tech_skill = []
        # print(skill_hi)
        for s in skill_hi:
            k = "".join(re.findall('[a-z][A-Z]*', s))
            tech_skill.append(k)
        print("technical skill", tech_skill)

        kall = []
        for d in tech_skill:
            #for k in d:
                kall.append(d)
        print("degree", kall)

        data = pd.read_csv(r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\skills.csv")
        # dat=data["Degree"]

        data['protected'] = pd.Series(flatlist)
        df = pd.DataFrame(columns=['Degree'])
        for i in flatlist:
            df = df.append({'Degree': i}, ignore_index=True)

        ls = []
        lst = kall
        for l in lst:
            data4 = data.loc[data['protected'] == l]
            data5 = data4["Weight"]
            b = list(data5)
            ls.extend(b)
        print("ls", ls)


    except:
        print("")

        # kall3=[]
        # for d in tech_skill:
        #         #for k in d:
        #     kall3.append(d)
        # print("technical skill",kall3)
        #
        # data3=pd.read_csv(r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\skills.csv")
        #     #dat=data["Degree"]
        #
        # data3['protected'] = pd.Series(flatlist)
        # df = pd.DataFrame(columns=['Degree'])
        # for i in flatlist:
        #         df = df.append({'Degree': i}, ignore_index=True)
        #
        # ls=[]
        # lst=kall3
        # for l in lst:
        #         data4=data3.loc[data3['protected']==l]
        #         data5=data4["Weight"]
        #         b=list(data5)
        #         ls.extend(b)
        # print("ls",ls)

    #except:
       # print("skill not found")
       # tech_skill = []

    # eduaction degree
    try:
        import csv
        from nltk.tokenize import sent_tokenize, word_tokenize

        file = r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\degreelist3.csv"
        # with open(file,"r")as w:
        w = open(file, 'r')
        read = csv.reader(w)
        # print(read)
        # print(read)
        # print(read)
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

        # print(flatlist)

        education = ["academic qualification", "Education qualification", "Educational qualification", "qualification",
                     "education", "academic"]
        for i in education:
            path = current_path + "\\" + i + ".txt"

            if os.path.exists(path):
                ope = open(path, 'r')
                resume_string = ope.read()
                resume_string = (resume_string.lower())
                resume_string = resume_string.replace(" ", "")
                # print("resume",resume_string)
                sent = sent_tokenize(resume_string)
                # print("sent",sent)
        dataw = []
        for s in sent:
            # print(s)
            word = word_tokenize(s)
            # print("word",word)
            for w in word:
                w = w.replace("-", " ")
                w = w.replace(".", "")
                # print(w)
                dataw.append(w)
        # print("degree",dataw)
        # word=word.remove("-","")
        degree = []
        degree1 = []
        for f in flatlist:
            for d in dataw:
                if f in d:
                    if f not in degree1:
                        s = re.findall('[a-z].*', f)
                        if s:
                            degree1.append(s)
        kall = []
        for d in degree1:
            for k in d:
                kall.append(k)
        print("degree", kall)

        data = pd.read_csv(r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\degreelist3.csv")
        # dat=data["Degree"]

        data['protected'] = pd.Series(flatlist)
        df = pd.DataFrame(columns=['Degree'])
        for i in flatlist:
            df = df.append({'Degree': i}, ignore_index=True)

        ls = []
        lst = kall
        for l in lst:
            data4 = data.loc[data['protected'] == l]
            data5 = data4["Weight"]
            b = list(data5)
            ls.extend(b)
        print("ls", ls)




    except:
        print("degree not found")
    # university name
    try:
        import csv
        from nltk.tokenize import sent_tokenize, word_tokenize

        file = r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\univer26.csv"
        w = open(file, "r", encoding='utf-8')
        read = csv.reader(w)
        # print(read)
        lis = list(read)
        # print(list)
        flatlist = []
        for sublist in lis:
            for item in sublist:
                item = item.lower()
                item = item.replace(" ", "")
                # item=item.replace(" ","")
                # item=item.replace(".","")
                flatlist.append(item)

        # print(flatlist)

        education = ["academic qualification", "Education qualification", "Educational qualification", "qualification",
                     "education", "academic"]
        for i in education:
            path = current_path + "\\" + i + ".txt"

            if os.path.exists(path):
                op = open(path, 'r')
                resume_string = op.read()
                # print(resume_string)
                resume_string = (resume_string.lower())
                # print("split",resume_string.split(" "))
                resume_string = resume_string.replace(" ", "")
                # print("resume",resume_string)
                sent = sent_tokenize(resume_string)
                # print("sent",sent)

        # print("sent",sent)
        dataw = []
        for s in sent:
            # print(s)
            word = word_tokenize(s)
            # print("word",word)
            for w in word:
                w = w.replace(" ", "")
                # w=w.replace(".","")
                # print(w)
                dataw.append(w)
        # print("education",dataw)
        # word=word.remove("-","")
        university = []

        for f in flatlist:
            for d in dataw:
                if f in d:
                    if f not in university:
                        s = re.findall('[a-z].*', f)
                        if s:
                            university.append(f)
        print("university", university)

        kall2 = []
        for d in university:
            # for k in d:
            kall2.append(d)
        print("university", kall2)

        datau = pd.read_csv(r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\univer26.csv")

        datau['protected'] = pd.Series(flatlist)
        df = pd.DataFrame(columns=['Degree'])
        for i in flatlist:
            df = df.append({'Degree': i}, ignore_index=True)

        ls = []
        lst = kall2
        for l in lst:
            data4 = datau.loc[datau['protected'] == l]
            data5 = data4["Weight"]
            b = list(data5)
            ls.extend(b)
        print("ls", ls)

    except:
        print("university  not found")

    # project technology

    try:
        import csv
        from nltk.tokenize import sent_tokenize, word_tokenize

        file = r"C:\Users\Milan\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\skills.csv"
        with open(file, "r", encoding='utf-8')as w:
            read = csv.reader(w)
            # print(read)
            lis = list(read)
            # print(list)
        flatlist = []
        for sublist in lis:
            for item in sublist:
                item = item.lower()
                item = item.replace(" ", "")
                # item=item.replace(" ","")
                # item=item.replace(".","")
                flatlist.append(item)

        # print(flatlist)

        path = current_path + "\acedamic project.txt"
        open1 = open(path, 'r')
        resume_string = open1.read()
        # print(resume_string)
        resume_string = (resume_string.lower())
        # print("split",resume_string.split(" "))
        resume_string = resume_string.replace(" ", "")
        # print("resume",resume_string)
        sent = sent_tokenize(resume_string)
        # print("sent",sent)

        # print("sent",sent)
        dataw = []
        for s in sent:
            # print(s)
            word = word_tokenize(s)
            # print("word",word)
            for w in word:
                w = w.replace(" ", "")
                # w=w.replace(".","")
                # print(w)
                dataw.append(w)
        # print("dataw",dataw)
        # word=word.remove("-","")

        project_tech = []

        for f in flatlist:
            if f in dataw:
                project_tech.append(f)
        print("project technologies", project_tech)
    except:
        print("project not found")
        project_tech = []

    # certificate

    try:
        import csv
        from nltk.tokenize import sent_tokenize, word_tokenize

        file = r"C:\Users\Milan\Downloads\certi.csv"

        w = open(file, "r", encoding='utf-8')

        read = csv.reader(w)

        lis = list(read)
        # print("list")
        flatlist = []
        for sublist in lis:
            for item in sublist:
                item = item.lower()
                item = item.replace(" ", "")
                # item=item.replace(" ","")
                # item=item.replace(".","")
                flatlist.append(item)

        # print(flatlist)

        path = current_path + "\certificate.txt"
        op = open(path, 'r')
        resume_string = op.read()
        # print(resume_string)
        resume_string = (resume_string.lower())
        # print("split",resume_string.split(" "))
        resume_string = resume_string.replace(" ", "")
        # print("resume",resume_string)
        sent = sent_tokenize(resume_string)
        # print("sent",sent)

        # print("sent",sent)
        dataw = []
        for s in sent:
            # print(s)
            word = word_tokenize(s)
            # print("word",word)
            for w in word:
                w = w.replace(" ", "")
                # w=w.replace(".","")
                # print(w)
                dataw.append(w)
        # print("dataw",dataw)
        # word=word.remove("-","")
        certificate = []

        for f in flatlist:
            for d in dataw:
                if f in d:
                    certificate.append(f)
        print("certificate", certificate)
    except:
        print("certificate  not found")
        certificate = []


