from config import conn

curs = conn.cursor()
try:
    create_table_sql = 'create table EnWords (word char(255) PRIMARY KEY, translation char(1024))'
    print(create_table_sql)
    curs.execute(create_table_sql)
    create_table_sql = 'create table user_info (userid char(255) PRIMARY KEY, session_key char(255))'
    print(create_table_sql)
    curs.execute(create_table_sql)
    create_table_sql = 'create table user_easy (userid char(255), word char(255), remarks char(1024), PRIMARY KEY(userid, word), foreign key(userid) references user_info(userid),foreign key(word) references EnWords(word))'
    print(create_table_sql)
    curs.execute(create_table_sql)
    create_table_sql = 'create table user_mid (userid char(255), word char(255), remarks char(1024), PRIMARY KEY(userid, word), foreign key(userid) references user_info(userid),foreign key(word) references EnWords(word))'
    print(create_table_sql)
    curs.execute(create_table_sql)
    create_table_sql = 'create table user_hard (userid char(255), word char(255), remarks char(1024), PRIMARY KEY(userid, word), foreign key(userid) references user_info(userid),foreign key(word) references EnWords(word))'
    print(create_table_sql)
    curs.execute(create_table_sql)
    f = open("data/EnWords.txt", 'r', encoding='utf8')
    reader = f.readline()
    print(reader)
    for row in f:
        reader = f.readline()
        reader = reader[:-2]
        insert_table_sql = 'INSERT INTO EnWords (word, translation) VALUES {}'.format(reader)
        print(insert_table_sql)
        curs.execute(insert_table_sql)
        conn.commit()
except:
    print('发生错误')
    conn.rollback()
finally:
    curs.close()

