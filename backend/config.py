import psycopg2

# dbname = 'mydb'
# user = 'gx'
# password = 'GaussDB@123'
# host = '120.46.159.207'
# port = 26000

conn = psycopg2.connect(database='mydb', user='gx',
                        password='GaussDB@123', host='120.46.159.207', port=26000)