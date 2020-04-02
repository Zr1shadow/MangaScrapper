import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="your username",
  passwd="your password",
  database="your database"
)

mycursor = mydb.cursor() 

def generateDB(title, currentChapter, latestChapter):
  
  # sql = "INSERT INTO mangaChapters (chapter) VALUES (%s)"
  # val = (1)
  # mycursor.execute(sql,val)
  id = 1 
  mycursor.execute("INSERT INTO manga (id, title, currentChapter, latestChapter) VALUES (%s, %s, %s, %s)", (id ,title, currentChapter, latestChapter))
  mydb.commit()
  
  print(mycursor.rowcount, "record inserted.")  
