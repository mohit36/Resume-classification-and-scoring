import os
import statistics
from statistics import *

import PyPDF2
import pandas as pd

from sample_application.nlpops import *
from sample_application.pathconfig import make_dir, get_download_path
from sample_application.read_con_from_database import getskill_seg
from sample_application.Resultstodatabase import master

def find_max_mode(list1):
    list_table = statistics._counts(list1)
    len_table = len(list_table)

    if len_table == 1:
        max_mode = statistics.mode(list1)
    else:
        new_list = []
        for i in range(len_table):
            new_list.append(list_table[i][0])
        max_mode = max(new_list)  # use the max value here
    return int(max_mode)


def get_textfile():
    # importing required modules

    # creating a pdf file object
    pdfFileObj = open(r'49A_Form_Updated.pdf', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    documents = []
    # printing number of pages in pdf file

    # creating a page object
    for i in range(0, pdfReader.numPages()):
        pageObj = pdfReader.getPage(i)

        # extracting text from page
        documents.append(pageObj.extractText())
        print(documents)

        # closing the pdf file object
    pdfFileObj.close()


def input_file_classification(path, filename):
    with open(path + filename, 'rb') as f:
        # content = str(f.readlines())
        content = []
        pdfReader = PyPDF2.PdfFileReader(f)
        pages = pdfReader.getNumPages()
        print(pages)
        for i in range(0, pages):
            pageObj = pdfReader.getPage(i)
            ncontent = []
            # extracting text from page

            cont = [pageObj.extractText()]
            content.append(cont)

        for i in content:
            for j in i:
                nc = j.replace("\n", "")
                ncontent.append(nc)

        content = ''.join(ncontent)
        # content=content.replace(")","")
        # content=content.replace("(","")
        print(content)
        # closing the pdf file object
        f.close()

        # content = f.read()
        ree = word_tokenize(content.lower())

        d = {}
        print(content)
        # Education section search in resume
        word_list = []
        content = content.lower()
        try:
            list_find_edu = []
            list_find_edu2 = []
            list_find_uni = []
            list_find_uni2 = []
            # file_edu_match = r'education_segment.csv'
            # with open(file_edu_match, 'r') as read_edu:
            #     edu_match_read = read_edu.read().lower().split()
            # edu_match_read=getedu_seg()
            tcontent = "%s" % content

            tcontent = re.sub('\s+', ' ', tcontent).strip()
            tcontent = tcontent.replace(" ", "-")

            print(tcontent)
            data = pd.read_csv(r'E:\flask\sample_application\university_segment.csv', encoding='utf-8')
            # print("data",data['skills'].tolist())
            uni_match_read = data['uni'].tolist()
            # print("skill_macth",skill_match_read)
            uni_match_read = ",".join(uni_match_read)
            uni_match_read = uni_match_read.replace(" ", "-")
            uni_match_read = uni_match_read.replace(",", " ")
            uni_match_read = uni_match_read.split()
            data = pd.read_csv(r'E:\flask\sample_application\education_segment.csv', encoding='utf-8')
            # print("data",data['skills'].tolist())
            edu_match_read = data['edu'].tolist()
            edu_match_read = ",".join(edu_match_read)
            edu_match_read = edu_match_read.replace(" ", "-")
            edu_match_read = edu_match_read.replace(",", " ")
            edu_match_read = edu_match_read.split()
            # read_edu.close()
            # print(tcontent)
            flag = False
            for i in edu_match_read:
                for j in uni_match_read:
                    word = str(i)
                    i = i.lower()
                    j = j.lower()
                    list_find_edu.append([m.start() for m in re.finditer(i, tcontent)])
                    list_find_uni.append([m.start() for m in re.finditer(j, tcontent)])
                    list1 = ree
                    # print(i,content)
                    if flag is False:

                        if content.find(str(i)) >= 0:
                            flag = True
                            if word in list1:
                                word_list.append(i)



                    elif flag is True:
                        continue
                    else:
                        with open(path + "dumpfile.txt", 'w') as w:
                            w.write("Education section not found")
            for i in list_find_edu:
                for j in i:
                    list_find_edu2.append(j)
            for i in list_find_uni:
                for j in i:
                    list_find_uni2.append(j)
            list_find_edu2 = sorted(list_find_edu2)
            list_find_uni2 = sorted(list_find_uni2)
            list_find_uni2 = set(list_find_uni2)
            list_find_uni2 = list(list_find_uni2)
            # print(list_find_uni2,list_find_edu2)
            word = "education"
            print(list_find_uni2, list_find_edu2)
            min = abs(list_find_uni2[0] - list_find_edu2[0])
            h = 0
            for i in list_find_edu2:
                for j in list_find_uni2:
                    k = j - i
                    k = abs(k)
                    #print(k, "=", j, "-", i)
                    if (min >= k):
                        min = k
                        h = i
                        # word_foundd = ree[i]
            print("uni:", list_find_uni2, h)
            word_index_found = list_find_edu2.index(h)
            word_found = list_find_edu2[word_index_found]

            # print("wordfound",word_foundd)
            d[word_found] = word
        except:
            print("education not found")

            word = ("education")
            word = word.lower()
            position = content.index(word)
            d[position] = word
        # personal information section search in resume

        #
        # word = ("personal")
        # word = word.lower()
        #
        word = ""
        # Education section search in resume

        try:
            word = ("personal")
            word = word.lower()
            position = content.index(word)
            d[position] = word
        except:
            print("personal not found")
            word = ("personal")
            position = 0
            d[position] = word
        try:
            word = ("project")
            word = word.lower()
            position = content.index(word)
            d[position] = word
        except:
            print("project not found")
        try:
            word = ("certificate")
            word = word.lower()
            position = content.index(word)
            d[position] = word
        except:
            print("certificate not found")

        word = ("skill")

        word = ""
        try:

        # Education section search in resume
            word_list = []
            content = content.lower()

            list_find_work = []
            list_find_work2 = []
            list_find_date = []
            list_find_date2 = []
            # file_work_match = r'workcation_segment.csv'
            # with open(file_work_match, 'r') as read_work:
            #     work_match_read = read_work.read().lower().split()
            # work_match_read=getwork_seg()
            tcontent = "%s" % content

            tcontent = re.sub('\s+', ' ', tcontent).strip()
            tcontent = tcontent.replace(" ", "-")

            #print(tcontent)
            data = pd.read_csv(r'E:\flask\sample_application\datemonth.csv', encoding='utf-8')
            # print("data",data['skills'].tolist())
            date_match_read = data['Months'].tolist()
            # print("skill_macth",skill_match_read)
            date_match_read = ",".join(date_match_read)
            date_match_read = date_match_read.replace(" ", "-")
            date_match_read = date_match_read.replace(",", " ")
            date_match_read = date_match_read.split()
            data = pd.read_csv(r'E:\flask\sample_application\work_experience_segment.csv', encoding='utf-8')
            # print("data",data['skills'].tolist())
            work_match_read = data['work'].tolist()
            work_match_read = ",".join(work_match_read)
            work_match_read = work_match_read.replace(" ", "-")
            work_match_read = work_match_read.replace(",", " ")
            work_match_read = work_match_read.split()
            # read_work.close()
            # print(tcontent)
            ree = word_tokenize(content.lower())
            flag = False
            for i in work_match_read:
                for j in date_match_read:
                    word = str(i)
                    i = i.lower()
                    j = j.lower()
                    list_find_work.append([m.start() for m in re.finditer(i, tcontent)])
                    list_find_date.append([m.start() for m in re.finditer(j, tcontent)])
                    list1 = ree
                    # print(i,content)
                    if flag is False:

                        if content.find(str(i)) >= 0:
                            flag = True
                            if word in list1:
                                word_list.append(i)
                    elif flag is True:
                        continue
                    else:
                        with open(path + "dumpfile.txt", 'w') as w:
                            w.write("Education section not found")
            for i in list_find_work:
                for j in i:
                    list_find_work2.append(j)
            for i in list_find_date:
                for j in i:
                    list_find_date2.append(j)
            list_find_work2 = sorted(list_find_work2)
            list_find_date2 = sorted(list_find_date2)
            list_find_date2 = set(list_find_date2)
            list_find_date2 = list(list_find_date2)
            # print(list_find_date2,list_find_work2)
            word = "work"
            # print(list_find_date2, list_find_work2)
            min = abs(list_find_date2[0] - list_find_work2[0])
            h = 0
            for i in list_find_work2:
                for j in list_find_date2:
                    k = j - i
                    k = abs(k)
                    # print(k, "=", j, "-", i)
                    if (min >= k):
                        min = k
                        # print("min",min)
                        h = i
                        # word_foundd = ree[i]
            # print("min", min)
            # print("date:", list_find_date2, h)
            word_index_found = list_find_work2.index(h)
            word_found = list_find_work2[word_index_found]

            # print("wordfound",word_foundd)
            d[word_found] = word
        except:
            print("certificate not found")


        content = content.lower()
        content = content.strip()

        tempcontent = "%s" % content
        tempcontent = tempcontent.replace(" ", "-")
        try:
            list_find_skill = []
            list_find_skill2 = []
            list_find_skills = []
            list_find_skills2 = []
            file_skill_match = r'skill_segment.csv'
            data = pd.read_csv(r'E:\flask\sample_application\skill_segment.csv', encoding='utf-8')
            # print("data",data['skills'].tolist())
            skill_match_read = data['skills'].tolist()
            # print("skill_macth",skill_match_read)
            skill_match_read = ",".join(skill_match_read)
            skill_match_read = skill_match_read.replace(" ", "-")
            skill_match_read = skill_match_read.replace(",", " ")
            skill_match_read = skill_match_read.split()
            # print(skill_match_read)
            file_skill2_match = getskill_seg()
            # with open(file_skill_match, 'r+',encoding='utf-8') as read_skill:
            #     skill_match_read = read_skill.read().lower().split()
            #     print(skill_match_read)
            #     read_skill.close()
            # with open(file_skill2_match, 'r+',encoding='utf-8') as read_skill2:
            skill_match_read2 = file_skill2_match
            m = {}
            listj = []
            #     read_skill2.close()
            flag = False
            #print(tempcontent)
            for i in skill_match_read:
                for j in skill_match_read2:
                    word = str(i)
                    i = i.lower()
                    j = j.lower()
                    # j=remove_punctuation(j)
                    # word = word.lower()
                    listj.append(i)
                    list_find_skill.append([m.start() for m in re.finditer(i, tempcontent)])
                    list_find_skills.append([m.start() for m in re.finditer(j, tempcontent)])
                    # position = tempcontent.index(i)
                    # print(tempcontent)
                    # d[position] = word

                    if i in tempcontent:
                        pos = tempcontent.index(i)

                        m[pos] = i
                    list1 = ree
            for i in list_find_skill:
                for j in i:
                    list_find_skill2.append(j)
            for i in list_find_skills:
                for j in i:
                    list_find_skills2.append(j)
            list_find_skill2 = sorted(list_find_skill2)
            list_find_skill2 = set(list_find_skill2)
            list_find_skill2 = list(list_find_skill2)
            list_find_skills2 = sorted(list_find_skills2)
            list_find_skills2 = set(list_find_skills2)
            list_find_skills2 = list(list_find_skills2)
            #print("this:", list_find_skill2)
            word = "skill"

            # min = list_find_skills2[0] - list_find_skill2[0]

            avg_med = int(median(list_find_skills2))

            h = 0
            avg_mode = find_max_mode(list_find_skills2)
            avg_mean = mean(list_find_skills2)
            max = avg_mode
            min = 0
            if (avg_mean == avg_med):
                min = int(avg_mean)
            elif avg_mean > avg_med:
                min = int(avg_med)

            else:
                min = int(avg_mean)

            new = []
            new2 = []
            for i in range(min, max):
                new.append(i)
            x = []
            for i in new:
                for j in list_find_skills2:
                    if i == j and j not in x:
                        x.append(j)

            list_find_skills2 = []
            for i in x:
                list_find_skills2.append(i)
            list_find_skills2 = sorted(list_find_skills2)
            # print(avg_mode,avg_mean,avg_med)
            # for s in list_find_skill2:
            #    for j in list_find_skills2:
            #         k = j - s
            #         k=abs(k)
            #         if (min >= k):
            #             min = k
            #             h = s

            y = abs(avg_med - list_find_skill2[0])
            #print(y)
            list_find_skill2 = sorted(list_find_skill2)

            #print("to this:", list_find_skill2)
            for s in list_find_skill2:

                k = avg_med - s

                #print(avg_med, "-", s, "K1:", k)
                k = abs(k)
                #print("K2:", k)
                if y >= k:
                    y = k
                    #print("y:", y)
                    h = s

            #print("\nM:", h, m)
            word_index_found = list_find_skill2.index(h)
            word_found = list_find_skill2[word_index_found]
            # print("\nword:", word_found)
            d[word_found] = word
        except:
            print("invalid format")
        #print(d)
        l = [value for (key, value) in sorted(d.items())]

        d = sorted(d)
        print(d)

        o = tuple(zip(d, l))


        try:
            path = make_dir(get_download_path())
            for i in range(0, len(d)):
                if d[i] == d[-1]:
                    start = d[i]
                    end = d[i]
                    #print(start, end)
                    pri = content[start:]
                    #print(pri)
                else:
                    start = d[i]
                    end = d[i + 1]
                    #print(start, end)
                    prin = content[start:end]

                #print(d[i])
                #print("len", len(l))
                if l[i] == l[-1]:
                    start = l[i]
                    end = l[i]
                    # pri = (content[content.find(start) + len(start):] + "\n\n")
                else:
                    start = l[i]
                    end = l[i + 1]
                    # prin = (content[content.find(start) + len(start):content.find(end)] + "\n\n")

                if (i == 0 and i != len(l)):
                    w = open(path + "\\" + l[0] + ".txt", "w", encoding='utf-8', errors='ignore')
                    w.write(prin)
                elif (i == 1 and i != len(l) - 1):
                    w = open(path + "\\" + l[1] + ".txt", "w", encoding='utf-8', errors='ignore')
                    w.write(prin)

                elif (i == 2 and i != len(l) - 1):

                    w = open(path + "\\" + l[2] + ".txt", "w", encoding='utf-8', errors='ignore')
                    w.write(prin)

                elif (i == 3 and i != len(l) - 1):
                    w = open(path + "\\" + l[3] + ".txt", "w", encoding='utf-8', errors='ignore')
                    w.write(prin)

                elif (i == 4 and i != len(l) - 1):
                    w = open(path + "\\" + l[4] + ".txt", "w", encoding='utf-8', errors='ignore')
                    w.write(prin)
                    files = os.listdir(path)
                elif (i == 5 and i != len(l) - 1):
                    w = open(path + "\\" + l[5] + ".txt", "w", encoding='utf-8', errors='ignore')
                    w.write(prin)
                elif (i == len(l) - 1):
                    w = open(path + "\\" + l[-1] + ".txt", "w", encoding='utf-8', errors='ignore')
                    w.write(pri)
                    files = os.listdir(path)
            return path
        except:
            print("invalid format")
            master("dropcase",0)
            import sys
            sys.exit(...)


def input_file_sent(path, filename):
    with open(path + filename, 'rb') as f:
        pdfReader = PyPDF2.PdfFileReader(f)
        for i in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(i)

            # extracting text from page
            newcontent = str(pageObj.extractText())

            # closing the pdf file object
        f.close()

    content = '%s' % newcontent
    newret = special_fun(content)
    return newret
