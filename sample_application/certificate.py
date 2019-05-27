import csv
import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
import os.path
from sample_application.stringops import *
from pathlib import Path



path2=r"E:\flask\sample_application"
def extract_certificate_info(path,mainpath,mainfile):
    my_file = Path(path+ "\certificate.txt")
    if my_file.is_file():
        matched_certificate = match_certificate(path + "\certificate.txt")
        return matched_certificate
    else:
        matched_certificate=find_certificate(mainpath , mainfile)
        return matched_certificate

def match_certificate(path):

        file = path2+r"\certificate.csv"
        with open(file, "r", encoding='unicode-escape')as w:
            read = csv.reader(w)
            lis = list(read)

        flatlist = []
        flatlist2 = []
        for sublist in lis:
            for item in sublist:
                item = item.lower()
                flatlist2.append(item)
                item = item.replace(" ", "-")
                flatlist.append(item)

        # path=r"C:\Users\lenovo\Downloads\personal.txt"
        # open=open(path,'r',encoding='utf-8')
        op = open(path, 'r')

        resume_string = op.read()
        resume_string = new_pun(resume_string)
        resume_string = resume_string.replace(" ", "-")
        resume_string = (resume_string.lower())
        # print("resume",resume_string)
        sent = sent_tokenize(resume_string)
        # print("sent",sent)
        data = []

        for s in sent:
            # print(s)
            word = word_tokenize(s)

            for w in word:
                # w = w.replace(" ", "")
                # w=w.replace(".","")
                # print(w)
                data.append(w)
            # print("dataw",dataw)
            # word=word.remove("-","")

        match = []
        for f in flatlist:
            for d in data:
                if f in d:
                    if f not in match and f != 'certificate':
                        if len(f) >= 5:
                            match.append(f)
        pos = []
        for i in data:
            # print("word",i)
            if i in flatlist:
                pos.append(flatlist.index(i))

        for i in pos:
            match.append(flatlist2[i])
        # for i in data:
        #         for f in flatlist:
        #             if i in f:
        #                 if i not in match:
        #                     match.append(i)
        if len(match)!=0:
            return list(match)

def find_certificate(mainpath,mainfile):
    f = open(mainpath + mainfile, "rb")

    content = []
    pdfReader = PyPDF2.PdfFileReader(f)
    pages = pdfReader.getNumPages()

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

    string = ''.join(ncontent)

    # closing the pdf file object
    f.close()

    # string=(u
    string = str(string)
    string = string.replace("\\n", " ")
    string = string.replace("/", " ")
    file = path2+r"\certificate.csv"
    with open(file, "r", encoding='unicode-escape')as w:
        read = csv.reader(w)
        lis = list(read)

    flatlist = []
    flatlist2 = []
    for sublist in lis:
        for item in sublist:
            item = item.lower()
            flatlist2.append(item)
            item = item.replace(" ", "-")
            flatlist.append(item)

    # path=r"C:\Users\lenovo\Downloads\personal.txt"
    # open=open(path,'r',encoding='utf-8')

    resume_string = string
    resume_string = resume_string.replace(" ", "-")
    resume_string = (resume_string.lower())
    # print("resume",resume_string)
    sent = sent_tokenize(resume_string)
    # print("sent",sent)
    data = []

    for s in sent:
        # print(s)
        word = word_tokenize(s)

        for w in word:
            # w = w.replace(" ", "")
            # w=w.replace(".","")
            # print(w)
            data.append(w)
        # print("dataw",dataw)
        # word=word.remove("-","")

    match = []
    for f in flatlist:
        for d in data:
            if f in d:
                if f not in match:
                    if len(f)>=7:
                        match.append(f)
    pos = []
    for i in data:
        # print("word",i)
        if i in flatlist:
            pos.append(flatlist.index(i))

    for i in pos:
        if len(flatlist2[i])>=5:
            print(flatlist2[i])
            match.append(flatlist2[i])
    # for i in data:
    #         for f in flatlist:
    #             if i in f:
    #                 if i not in match:
    #                     match.append(i)
    if len(match) != 0:
        return list(match)
    else:
        if match is None:
            return str('')