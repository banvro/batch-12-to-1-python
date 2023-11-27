import mysql.connector

con = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "amazon")

if con.is_connected():
    print("your database connect sucessfully.!")

curser = con.cursor()

curser.execute("insert into savemydataa values('hlo', 'hlo@gmail.com', '98126312', 'this is message');")

con.commit()
# ''
# ""
# """"""