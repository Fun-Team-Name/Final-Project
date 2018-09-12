import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='admin',
                             password='equifax',
                             db='classes')

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `testclass` (`name`, `password`, 'score') VALUES (%s, %s, 0)"
        cursor.execute(sql, ('testuser', 'testpassword'))
        connection.commit()

    with connection.cursor() as cursor:
        sql = "SELECT `name`, `password` FROM `testclass` WHERE `name`=%s"
        cursor.execute(sql, ('testuser'))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
