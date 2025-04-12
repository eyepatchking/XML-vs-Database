import mysql.connector
import xml.etree.ElementTree as ET
from xml.dom import minidom

conn = mysql.connector.connect(
    host="localhost",
    user="foydalanuvchi_nomi",
    password="foydalanuvchi_paroli",
    database="databaza_nomi"
)

cursor = conn.cursor()
cursor.execute("SELECT id, name, email FROM users")
rows = cursor.fetchall()
root = ET.Element("users")

for row in rows:
    user = ET.SubElement(root, "user")
    ET.SubElement(user, "id").text = str(row[0])
    ET.SubElement(user, "name").text = row[1]
    ET.SubElement(user, "email").text = row[2]

xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
with open("users.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)

cursor.close()
conn.close()
print("Ma'lumotlar XML faylga saqlandi.")
