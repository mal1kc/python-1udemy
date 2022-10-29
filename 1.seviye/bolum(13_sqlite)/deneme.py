import sqlite3
# 
# 
# def veritabanindakiler():
#     sorg = "SELECT * FROM deneme"
# 
#     cursor.execute(sorg)
#     return cursor.fetchall()
# 
# 
# baglanti = sqlite3.connect("deneme.db")
#
# cursor = baglanti.cursor()
# 
# sorgu = "CREATE TABLE IF NOT EXISTS deneme (id INT,isim TEXT,yazar TEXT)"
# 
# isim = input("gir : ")
# isim = isim.split(",")
# if len(veritabanindakiler()) == 0:
#     sonid = 1
# else:
#     sorgu = "SELECT MAX(id) FROM deneme"
#     cursor.execute(sorgu)
#     sonid = cursor.fetchall()
#     sonid = sonid[0][0] + 1
# sorgu = "INSERT INTO deneme VALUES(?,?,?)"
# cursor.execute(sorgu, (sonid, isim[0], isim[1],))
# baglanti.commit()
# 
# for i in veritabanindakiler():
#     print(i)

# sorgu = "CREATE TABLE IF NOT EXISTS sanatçılar (id INT,isim TEXT,sarkilar TEXT,albumler TEXT)"
# baglanti = sqlite3.connect("müzikkütüphanesi.db")
# baglanti.cursor().execute(sorgu)
# baglanti.commit()
# sorgu = "CREATE TABLE IF NOT EXISTS şarkılar (id INT,isim TEXT,album TEXT,tur TEXT,uzunluk TEXT,sanatci TEXT," \
#                 "sozler TEXT) "
# baglanti.cursor().execute(sorgu)
# baglanti.commit()
# sorgu = "CREATE TABLE IF NOT EXISTS albümler (id INT,isim TEXT,sanatçı TEXT,tur TEXT,uzunluk INT,sarkilar TEXT)"
# baglanti.cursor().execute(sorgu)
# baglanti.commit()
# baglanti.close()
