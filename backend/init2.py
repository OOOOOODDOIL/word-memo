from config import conn

curs = conn.cursor()
try:
    f = open("data/EnWords.txt", 'r', encoding='utf8')
    reader = f.readline()
    print(reader)
    # reader = f.readline()
    # print(reader)
    # print(type(reader))
    # reader1 = reader.split(',')
    # print(reader1)
    # print(type(reader1))
    # print(reader1[0][1:])
    # print(type(reader1[0][1:]))
    for row in f:
        reader = f.readline()
        reader = reader[:-2]
        reader1 = reader.split(',')
        reader2 = reader1[0][1:]
        search_sql = "select * from EnWords where word = {}".format(reader2)
        print(search_sql)
        curs.execute(search_sql)
        result = curs.fetchall()
        if result:
            continue
        else:
            insert_table_sql = 'INSERT INTO EnWords (word, translation) VALUES {}'.format(reader)
            print(insert_table_sql)
            curs.execute(insert_table_sql)
        conn.commit()
except:
    print('发生错误')
    conn.rollback()
finally:
    curs.close()

if __name__ == '__main__':
    curs.execute("select * from EnWords where word = 'abandon'")
    result = curs.fetchall()
    if result:
        pass
    else:
        print("no")
