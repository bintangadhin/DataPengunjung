import sqlite3

if __name__ == '__main__':

    conn = sqlite3.connect('databasenya.db')

    c = conn.cursor()


    c.execute("""CREATE TABLE pengunjung ( nomor_pengunjung INT(100) NOT NULL PRIMARY KEY, 
            nama VARCHAR(100)  , alamat VARCHAR(100) , 
            jenis_kelamin VARCHAR(100)  ,
            no_tlp VARCHAR(100)  ,
            email VARCHAR(100) , 
            tgl_kunjungan VARCHAR(100) , 
            status VARCHAR(100) ) """)

    conn.commit()
    print("Database dan table telah dibuat")