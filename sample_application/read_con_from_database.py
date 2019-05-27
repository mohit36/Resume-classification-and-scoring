import csv

import pandas as pd
import pymysql

# dummy values
connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')

def getuni():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT University FROM edu_uni_set"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l = df.to_string(index=False)
        return l
    finally:
        connection.close()

def getedu():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT Degree FROM edu_degree_set"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l = df.to_string(index=False)
        return l
    finally:
        connection.close()
def getskill():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT skills FROM skill_set"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        return df
    finally:
        connection.close()
def getskill_seg():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT skills FROM skill_seg"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l=df['skills'].tolist()

        return l
    finally:
        connection.close()
def getedu_seg():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT edu FROM edu_seg"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l=df['edu'].tolist()

        return l
    finally:
        connection.close()

def getpersonalinfo():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT p_mo_no,p_email  FROM personal_info"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l = df.to_dict()
        return l
    finally:
        connection.close()


def geteduinfo():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT e_degree,e_university  FROM education"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l = df.to_dict()
        return l
    finally:
        connection.close()


def getskillinfo():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT s_technical_skill FROM skill"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l = df.to_dict()
        return l
    finally:
        connection.close()

def getcertificateinfo():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT certificate_name FROM certificate"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l = df.to_dict()
        return l
    finally:
        connection.close()

def getprojectinfo():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:
            query = "SELECT p_project_tech FROM project"

            cursor.execute(query)

        df = pd.read_sql(query, connection)
        l = df.to_dict()
        return l
    finally:
        connection.close()

def getall():
    try:
        connection = pymysql.connect(user='root', password='', database='resume_store', host='127.0.0.1')
        with connection.cursor() as cursor:

            sql_max = "SELECT p_id FROM resume_master"
            id = cursor.execute(sql_max)
            result = cursor.fetchall()
            s = []

            for i in result:

                for j in range(1, i[0]):
                    sql_all = "select p.p_id,r.accuracy,r.status,p.p_name,p.p_location,p.p_mo_no,p.p_email,e.e_degree,e.e_university,s.s_technical_skill,w.expirenece,c.certificate_name,k.p_project_tech,r.scor from personal_info p INNER JOIN resume_master r ON p.p_id =r.p_id INNER JOIN education e ON p.p_id =e.p_id INNER JOIN skill s ON p.p_id=s.p_id INNER JOIN work_exp_info w ON p.p_id=w.p_id INNER JOIN certificate c ON p.p_id=c.p_id INNER JOIN project k ON p.p_id=k.p_id where p.p_id = '%s'"
                    adj = j
                    cursor.execute(sql_all, adj)
                    myresult = cursor.fetchall()
                    w = csv.writer(open(r"allresume.csv", 'a+'), dialect='excel')
                    for x in myresult:
                        s.append(x)
                    s=set(s)
                    s=list(s)
                    s=sorted(s)
            for i in s:
                w.writerow(i)



    finally:
        connection.close()
def get_ar():
    try:
        df = pd.read_csv(r'allresume.csv', encoding='unicode_escape', error_bad_lines=False)
        df = df.drop_duplicates()
        df.to_csv(r'sample_application\allresumes.csv', index=False,
                  header=['p_id', 'accuracy', 'Status', 'Name', 'Location', 'phoneno', 'email', 'degree', 'university','skills', 'work_exp', 'certification', 'project','scor'])
        df2 = pd.read_csv(r'sample_application\allresumes.csv', encoding='unicode_escape', error_bad_lines=False)
        print(df2[6:9])
    except:
        print("fail")
