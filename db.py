import psycopg2

#? To check the function in docker setup

def pgdbins(chatid,prgm):
    conn = psycopg2.connect(database="BTech_Demo", user = "postgres", password = "postgresql", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    sem="S"
    try: 
      cur.execute("INSERT INTO BTECH_DEMO VALUES(%s,%s,%s)",(chatid,prgm,sem))    
    except Exception as e:
      print(e)
    conn.commit()
    conn.close()

# pgdbins('456765434','B.Des')
def pgdb(list):
    rows2=[]
    pk=0

    conn = psycopg2.connect(database="BTech_Demo", user = "postgres", password = "postgresql", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    for i in range(len(list)):
      pk=0
      if list[i]["ptype"]=="(R)":
        cur.execute("SELECT CID FROM BTECH_DEMO WHERE PRGM=%s AND SEM=%s",(list[i]["program"],list[i]["semester"]))
      
      elif list[i]["ptype"]=="(S)":
        cur.execute("SELECT CID FROM SUPPLI_DEMO WHERE PRGM=%s AND SEM=%s",(list[i]["program"],list[i]["semester"]))     
      
      elif list[i]["ptype"] =="(R,S)":
        pk=1
        cur.execute("SELECT CID FROM BTECH_DEMO WHERE PRGM=%s AND SEM=%s",(list[i]["program"],list[i]["semester"]))
        rows=cur.fetchall()
        for row in rows:
          rows2.append(row[0])     
        cur.execute("SELECT CID FROM SUPPLI_DEMO WHERE PRGM=%s AND SEM=%s",(list[i]["program"],list[i]["semester"]))     
        rows=cur.fetchall()
        for row in rows:
          rows2.append(row[0]) 



      if pk==0:
        rows=cur.fetchall()
        for row in rows:
          rows2.append(row[0])
      # print(rows2)
      # rows1.append(rows)

    # print(" /// \n ")
    # print(rows2)    
    print("\n /// \n ")
    for i in rows2:
      
      print(i)
    # last = convertTuple(rows2)
    # print(last)
    print("\n /// \n ")
    conn.close()

    return rows2

# pgdb(b)

def pgdbupd(chatid,sem):
    conn = psycopg2.connect(database="BTech_Demo", user = "postgres", password = "postgresql", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    chidstr=str(chatid)
    cur.execute("UPDATE BTECH_DEMO SET SEM=%s WHERE CID=%s",(sem,chidstr))    
    conn.commit()
    conn.close()

# pgdbins('456765434','B.Des')
