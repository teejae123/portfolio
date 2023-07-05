import mysql.connector

#creating and establishing database connection along with database selection
mydb =mysql.connector.connect(
    host= "localhost",
    username= "root",
    password= "",
    database= "summativedb" # database name
)

#print(mydb)
#creating database object connection
mycursor = mydb.cursor()

mycursor.execute("drop table if exists students")
print("table deleted")

#creating tables and coloumns
mycursor.execute("""create table students(id int auto_increment primary key,
                    name varchar(25), email varchar(25), age varchar(25), mobile varchar(10))""")
print("table created")

#inserting values into table
sql = "insert into students (name, email, age, mobile)values(%s,%s,%s,%s)"
val = ('sanderson', 'sandersonmiti@gmail.com','34', '0685264403'),('tiyiselani','tiyi@gmail.com','33','0681234567'),('Goodman','good@gmail.com','27','0713246785'),('Fatimah','Fatmah@gmail.com','26','0835668135'),('Luvuyo Mkhwanazi','vee@gnail.com','23','0763678346')

#executing sql commands
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "Records were inserted")
mydb.close()