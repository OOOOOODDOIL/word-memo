import json
import requests
import psycopg2

# curs = conn.cursor()
conn = psycopg2.connect(database='mydb', user='gx',
                        password='GaussDB@123', host='120.46.159.207', port=26000)

def getword(word) -> str:
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    result = "failed"
    try:
        search_sql = "select word,translation from EnWords where word like '{}%'".format(word)
        print(search_sql)
        curs.execute(search_sql)
        print(curs.rowcount)
        result = curs.fetchall()
        # print(type(result))
        # print(type(result[0]))
        # print(type(str(result[0])))
        # print(str(result[0])[2:])
        # result = str(result[0])[2:]
        conn.commit()
    except:
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return result

def getuser(openid, session_key)->str:
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    res = ""
    try:
        search_sql = "select * from user_info where userid = '{}'".format(openid)
        print(search_sql)
        curs.execute(search_sql)
        print(curs.rowcount)
        result = curs.fetchall()
        if result:
            res = "exists"
        else:
            insert_table_sql = "INSERT INTO user_info (userid, session_key) VALUES ('{}','{}')".format(openid, session_key)
            print(insert_table_sql)
            curs.execute(insert_table_sql)
            res = "register"
        conn.commit()
    except:
        res = "error"
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return res

def findmemo(openid, word)->str:
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    res = "none"
    try:
        list = ["easy", "mid", "hard"]
        for each in list:
            search_sql = "select * from user_{} where userid = '{}'and word ='{}'".format(each, openid, word)
            print(search_sql)
            curs.execute(search_sql)
            print(curs.rowcount)
            result = curs.fetchall()
            print(result)
            if result:
                res = each
                break
        conn.commit()
    except:
        res = "error"
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return res

def insertmemo(openid, word, level)->str:
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    res = ""
    try:
        insert_table_sql = "INSERT INTO user_{} (userid, word) VALUES ('{}','{}')".format(level, openid, word)
        print(insert_table_sql)
        curs.execute(insert_table_sql)
        res = "insert"
        conn.commit()
    except:
        res = "error"
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return res

def deletememo(openid, word, level)->str:
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    res = ""
    try:
        delete_table_sql = "delete from user_{} where userid = '{}' and word = '{}'".format(level, openid, word)
        print(delete_table_sql)
        curs.execute(delete_table_sql)
        res = "delete"
        conn.commit()
    except:
        res = "error"
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return res

def getmemo(openid, level) -> str:
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    result = "failed"
    try:
        search_sql = "select user_{}.word,translation from user_{},EnWords where userid = '{}' and user_{}.word = EnWords.word".format(level, level, openid, level)
        print(search_sql)
        curs.execute(search_sql)
        print(curs.rowcount)
        result = curs.fetchall()
        # print(type(result))
        # print(type(result[0]))
        # print(type(str(result[0])))
        # print(str(result[0])[2:])
        # result = str(result[0])[2:]
        conn.commit()
    except:
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return result

def getmemoword(openid, word, level) -> str:
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    result = "failed"
    try:
        search_sql = "select user_{}.word,translation from user_{},EnWords where userid = '{}' and user_{}.word like '{}%' and user_{}.word = EnWords.word".format(level, level, openid, level, word, level)
        print(search_sql)
        curs.execute(search_sql)
        print(curs.rowcount)
        result = curs.fetchall()
        # print(type(result))
        # print(type(result[0]))
        # print(type(str(result[0])))
        # print(str(result[0])[2:])
        # result = str(result[0])[2:]
        conn.commit()
    except:
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return result

def getid(js_code) -> any:
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx8671d9a8031b4cff&secret=de1765b63fdb38d17ccc25bc6d4ddebc&grant_type=authorization_code'
    url = url + '&js_code=' + js_code
    # data = {"appid": "wx8671d9a8031b4cff", "secret": "de1765b63fdb38d17ccc25bc6d4ddebc", "grant_type": "authorization_code", "js_code": js_code}
    # res = requests.get(url, data=data)
    res = requests.get(url)
    print(res.status_code)
    print(res)
    text = json.loads(res.text)
    print(text)
    return text["openid"], text["session_key"]

if __name__ == '__main__':
    pass