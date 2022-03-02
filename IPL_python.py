import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="12345")

if(mycon.is_connected()):
    print("\nConnection Secure\n")
else:
    print("\nConnection Unsecure, Please Try Again\n")


cursor=mycon.cursor()


def reset_database(ty="start"):
    cursor.execute("show databases like 'ipl';")
    database_exist_check=cursor.fetchone()

    if((database_exist_check is not None) and (ty=="reset")):
        cursor.execute("drop database ipl;")
    if(database_exist_check is None or ty=="reset"):
        #print("\nCreating Database and Subsequent tables\n")
        cursor.execute("create database ipl;")
        cursor.execute("use ipl;")
        cursor.execute("""

create table AllPlayers
(
TeamName varchar(50) NOT NULL,
PlayerName varchar(50) PRIMARY KEY,
ShirtNumber int(4),
Economy float(5,2), 
BattingAvg float(5,2), 
Role varchar(25) NOT NULL, 
HighestScore int(4), 
MostWickets int(4), 
Debut date
);

""")
    
        cursor.execute("""

create table Teamstats
(TeamName varchar(50) NOT NULL,
YearsPlayed int(3) NOT NULL,
Wins int(4) NOT NULL, 
FinalsLost int(4) NOT NULL, 
Captain varchar(25), 
Owner varchar(25)
);

""")
    
        cursor.execute("""

create table PlayerRecords 
(TeamName varchar(50), 
PlayerName varchar(50) PRIMARY KEY, 
ShirtNumber int(3), 
Salary float(10,2) NOT NULL, 
Role varchar(30),
Age int(3) NOT NULL,
Record varchar(50),
FOREIGN KEY (PlayerName) REFERENCES AllPlayers(PlayerName)
);

""")
    else:
        cursor.execute("use ipl;")


reset_database()

def filterplayers(s,o):
    if o!="Choose Filter":
        if o=="DebutYear":
            query="select * from allplayers where year(Debut)={}".format(s)
        else:
            query="select * from allplayers where {}={}".format(o,s)
        cursor.execute(query)
        records=cursor.fetchall()
        return records
    else:
        return displayplayers()

def displayplayers():
    query="select * from allplayers order by teamname"
    cursor.execute(query)
    records=cursor.fetchall()
    #print("Displaying all players in IPL\n")
    return records

def displayteamstats(t="."):
    if t==".":
        query="select * from teamstats "
        cursor.execute(query)
        record=cursor.fetchall()
        #print("Displaying all teams in IPL\n")
        return record
    else:
        query="select * from teamstats where TeamName='{}'".format(t)
        cursor.execute(query)
        record=cursor.fetchall()
        #print("Displaying all teams in IPL\n")
        return record

def displayrecords(t="."):
    if t==".":
        query="select * from playerrecords"
        cursor.execute(query)
        record=cursor.fetchall()
        #print("Displaying all Records made in IPL\n")
        return record
    else:
        query="select * from playerrecords where TeamName='{}'".format(t)
        cursor.execute(query)
        record=cursor.fetchall()
        #print("Displaying all Records made in IPL\n")
        return record

def updateplayer(data,s):
    team=data[0]
    name=data[1]
    shirtn=data[2]
    eco=data[3]
    bavg=data[4]
    role=data[5]
    runs=data[6]
    wickets=data[7]
    debut=data[8]
    ogplayername=s
    #print("Updating data of player "+ogplayername)
    query="Update Allplayers set teamname='{}',playername='{}',ShirtNumber='{}',Economy={},BattingAvg={},Role='{}',HighestScore={},MostWickets={},Debut='{}' where playername='{}'".format(team,name, shirtn, eco, bavg, role, runs, wickets, debut, ogplayername)
    cursor.execute(query)
    mycon.commit()
    query="Update playerrecords set playername='{}' where playername='{}'".format(team, ogplayername)
    #print(query)
    cursor.execute(query)
    mycon.commit()

def updateteam(data,s):
    team=data[0]
    year=data[1]
    wins=data[2]
    lost=data[3]
    cap=data[4]
    owner=data[5]
    ogteamname=s
    #print("Updating data of "+ogteamname)
    query="Update Teamstats set TeamName='{}',YearsPlayed={},Wins={},FinalsLost={},Captain='{}',Owner='{}' where TeamName='{}'".format(team,year,wins,lost,cap,owner,ogteamname)
    cursor.execute(query)
    mycon.commit()
    query="Update Allplayers set TeamName='{}'where TeamName='{}'".format(team,ogteamname)
    cursor.execute(query)
    mycon.commit()
    query="Update playerrecords set TeamName='{}'where TeamName='{}'".format(team,ogteamname)
    cursor.execute(query)
    mycon.commit()

def updaterecord(data,s):
    team=data[0]
    name=data[1]
    shirt=data[2]
    salary=data[3]
    role=data[4]
    age=data[5]
    record1=data[6]
    ogname=s

    query="Update playerrecords set TeamName='{}',PlayerName='{}',ShirtNumber={},Salary={},PlayerType='{}',Age={},Record='{}' where PlayerName='{}'".format(team,name,shirt,salary,role,age,record1,ogname)
    cursor.execute(query)
    mycon.commit()

def addplayer(data):
    team=data[0]
    name=data[1]
    shirtn=data[2]
    eco=data[3]
    bavg=data[4]
    role=data[5]
    runs=data[6]
    wickets=data[7]
    debut=data[8]

    player_insert="insert into allplayers values('{}','{}',{},{},{},'{}',{},{},'{}')".format(team, name, shirtn, eco, bavg, role, runs, wickets, debut)
    cursor.execute(player_insert)
    mycon.commit()
    #print("Player "+name+" added\n")

def addrecord(data):
    #print("Adding Record Holder "+data[1])
    team=data[0]
    name=data[1]
    shirt=data[2]
    salary=data[3]
    role=data[4]
    age=data[5]
    rec=data[6]
   
    record_insert="insert into playerrecords values('{}','{}',{},{},'{}',{},'{}')".format(team,name,shirt,salary,role,age,rec)
    cursor.execute(record_insert)
    mycon.commit()

def addteam(data):
    team=data[0]
    year=data[1]
    wins=data[2]
    lost=data[3]
    capt=data[4]
    owner=data[5]

    team_insert="insert into teamstats values('{}',{},{},{},'{}','{}')".format(team,year,wins,lost,capt,owner)
    cursor.execute(team_insert)
    mycon.commit()
    #print(team+" Added")

def deleteplayer(name,do="first"):
    
    if do=="first":
        #print("Deleting Player "+name)
        query="select * from allplayers where PlayerName='{}'".format(name)
        cursor.execute(query)
        record=cursor.fetchone()
        return record
    else:
        query="delete from allplayers where PlayerName='{}'".format(name)
        cursor.execute(query)
        query="delete from playerrecords where PlayerName='{}'".format(name)
        cursor.execute(query)
        mycon.commit()
   
def deleteteam(team,do="first"):
    if do=="first":
        #print("Deleting Team "+team)
        query="select * from teamstats where TeamName='{}'".format(team)
        cursor.execute(query)
        record=cursor.fetchone()
        return record
    else:
        query="delete from teamstats where TeamName='{}'".format(team)
        cursor.execute(query)
        query="delete from allplayers where TeamName='{}'".format(team)
        cursor.execute(query)
        query="delete from playerrecords where TeamName='{}'".format(team)
        cursor.execute(query)
        mycon.commit()


def deleterecord(name,do="first"):
    
    if do=="first":
        #print("Deleting Record of "+name)
        query="select * from playerrecords where PlayerName='{}'".format(name)
        cursor.execute(query)
        record=cursor.fetchone()
        return record
    else:
        query="delete from playerrecords where PlayerName='{}'".format(name)
        cursor.execute(query)
        mycon.commit()


def findplayer(name):
    #print("Finding Player "+name)
    query="select * from allplayers where PlayerName='{}'".format(name)
    cursor.execute(query)
    record=cursor.fetchone()
    return record

def findrecord(rec):
    query="select * from playerrecords where PlayerName='{}'".format(rec)
    cursor.execute(query)
    record=cursor.fetchone()
    return record
    #print(record)

def findteam(team):
    #print("Displaying "+team+"\n")
    query="select * from allplayers where teamname='{}'".format(team)
    cursor.execute(query)
    record1=cursor.fetchall()
    query="select * from teamstats where teamname='{}'".format(team)
    cursor.execute(query)
    record2=cursor.fetchone()
    return (record1,record2)





