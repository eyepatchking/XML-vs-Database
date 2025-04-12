import mysql.connector
import xml.etree.ElementTree as ET

conn = mysql.connector.connect(
    host="localhost",
    user="foydalanuvchi_nomi",
    password="foydalanuvchi_proli",
    database="databaza_nomi"
)

cursor = conn.cursor()


tree = ET.parse("users.xml")
root = tree.getroot()


for user in root.findall("user"):
    id_val = user.find("id").text
    name_val = user.find("name").text
    email_val = user.find("email").text
    
    query = "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)"
    values = (id_val, name_val, email_val)
    cursor.execute(query, values)


conn.commit()


cursor.close()
conn.close()

print("XML ma'lumotlari MBga yozildi.")
