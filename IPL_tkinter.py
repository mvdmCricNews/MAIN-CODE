import tkinter as tk
from tkinter import ttk
from IPL_python import * 
from Tooltip import *
import requests
import io
from PIL import Image, ImageTk
from functools import partial

tk_start=tk.Tk()
tk_start.iconify()
t=1
teams={"CSK": "Chennai Super Kings","DC":"Delhi Capitals","KKR":"Kolkata Knight Riders","MI":"Mumbai Indians","PK":"Punjab Kings","RR":"Rajasthan Royals","RCB":"Royal Challengers Bangalore","SRH":"Sunrisers Hyderabad"}
def O_Reset():
    url = "https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/allplayers.txt"
    req = requests.get(url, 'html.parser')
    player_record=req.text.split("\n")
    reset_database("reset")
    for i in player_record:
        try:
            p1=i.split("datetime.date(")[0]
            p2=i.split("datetime.date(")[1].replace("))","").split(",")
            p2="-".join(p2).replace(" ","") 
        except:
            break
        command="insert into allplayers values"+p1[5:]+'"'+p2+'");'
        cursor.execute(command)
        mycon.commit()
    
    url = "https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/teamstats.txt"
    req = requests.get(url, 'html.parser')
    player_record=req.text.split("\n")
    for i in player_record:
        try:
            command="insert into teamstats values"+i.split("  ")[1]+";"
        except:
            break
        cursor.execute(command)
        mycon.commit()

    url = "https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/playerrecords.txt"
    req = requests.get(url, 'html.parser')
    player_record=req.text.split("\n")
    for i in player_record:
        try:
            command="insert into playerrecords values"+i.split("  ")[1]+";"
        except:
            break
        cursor.execute(command)
        mycon.commit()
    print("\nFinished Extracting data from online\n")

def FrontPage():
    global start_page,front_page,all_player_page,all_team_page,all_record_page
    try:
        start_page.destroy()
    except:
        pass
    try:
        all_player_page.destroy()
    except:
        pass
    try:
        all_team_page.destroy()
    except:
        pass
    try:
        all_record_page.destroy()
    except:
        pass
    front_page = tk.Toplevel()

    width=front_page.winfo_screenwidth()               
    height=front_page.winfo_screenheight()               
    
    front_page.geometry("%dx%d" % (width, height))
    front_page.state('zoomed')
    front_page.title("Front Page")


    x_start_logo_pos=300
    y_start_logo_pos=380

    Show_tables = tk.Label(front_page, text="mvdmCricNews",width=20,font=("Times New Roman", 35,"bold"))
    Show_tables.place(x=400,y=30)

    Player_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/Cricket_Player.png")
    my_picture = io.BytesIO(Player_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_players = ImageTk.PhotoImage(pil_img)
    PLAYERS_butt=tk.Button(front_page, text='PLAYERS',image = tk_players ,bg='white',fg='white', command=AllPlayersPage)
    PLAYERS_butt.place(x=300,y=100)
    CreateToolTip(PLAYERS_butt, text = 'Show all Players')

    Team_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/Cricket_Team.jpg")
    my_picture = io.BytesIO(Team_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_team = ImageTk.PhotoImage(pil_img)
    TEAM_butt=tk.Button(front_page, text='TEAMS',image = tk_team ,bg='white',fg='white', command=TeamStatsPage)
    TEAM_butt.place(x=600,y=100)
    CreateToolTip(TEAM_butt, text = 'Show all Teams')

    Record_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/Cricket_Record.png")
    my_picture = io.BytesIO(Record_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_record = ImageTk.PhotoImage(pil_img)
    RECORDS_butt=tk.Button(front_page, text='RECORDS',image = tk_record ,bg='white',fg='white', command=PlayerRecordsPage)
    RECORDS_butt.place(x=900,y=100)
    CreateToolTip(RECORDS_butt, text = 'Show all Records')

    Show_teams = tk.Label(front_page, text="Show by Team (Online Database)",width=30,font=("Times New Roman", 25,"bold"))
    Show_teams.place(x=x_start_logo_pos+100,y=y_start_logo_pos-60)
    csk_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_CSK_LOGO.png")
    my_picture = io.BytesIO(csk_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_csk = ImageTk.PhotoImage(pil_img)
    CSK_butt=tk.Button(front_page, text='CSK',image = tk_csk ,bg='yellow',fg='white', command=partial(AllPlayersPage, "CSK"))
    CSK_butt.place(x=x_start_logo_pos,y=y_start_logo_pos)
    CreateToolTip(CSK_butt, text = 'Chennai Super Kings')

    dc_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_DC_LOGO.png")
    my_picture = io.BytesIO(dc_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_dc = ImageTk.PhotoImage(pil_img)
    DC_butt=tk.Button(front_page, text='DC',image = tk_dc ,bg='light blue',fg='white', command=partial(AllPlayersPage, "DC"))
    DC_butt.place(x=x_start_logo_pos+200,y=y_start_logo_pos)
    CreateToolTip(DC_butt, text = 'Delhi Capitals')

    kkr_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_KKR_LOGO.png")
    my_picture = io.BytesIO(kkr_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_kkr = ImageTk.PhotoImage(pil_img)
    KKR_butt=tk.Button(front_page, text='KKR',image = tk_kkr ,bg='purple',fg='white', command=partial(AllPlayersPage, "KKR"))
    KKR_butt.place(x=x_start_logo_pos+400,y=y_start_logo_pos)
    CreateToolTip(KKR_butt, text = 'Kolkata Knight Riders')

    mi_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_MI_LOGO.png")
    my_picture = io.BytesIO(mi_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_mi = ImageTk.PhotoImage(pil_img)
    MI_butt=tk.Button(front_page, text='MI',image = tk_mi ,bg='blue',fg='white', command=partial(AllPlayersPage, "MI"))
    MI_butt.place(x=x_start_logo_pos+600,y=y_start_logo_pos)
    CreateToolTip(MI_butt, text = 'Mumbai Indians')

    pk_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_PK_LOGO.png")
    my_picture = io.BytesIO(pk_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_pk = ImageTk.PhotoImage(pil_img)
    PK_butt=tk.Button(front_page, text='PK',image = tk_pk ,bg='red',fg='white', command=partial(AllPlayersPage, "PK"))
    PK_butt.place(x=x_start_logo_pos,y=y_start_logo_pos+200)
    CreateToolTip(PK_butt, text = 'Punjab Kings')

    rr_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_RR_LOGO.png")
    my_picture = io.BytesIO(rr_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_rr = ImageTk.PhotoImage(pil_img)
    RR_butt=tk.Button(front_page, text='RR',image = tk_rr ,bg='blue',fg='white', command=partial(AllPlayersPage, "RR"))
    RR_butt.place(x=x_start_logo_pos+200,y=y_start_logo_pos+200)
    CreateToolTip(RR_butt, text = 'Rajasthan Royals')

    rcb_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_RCB_LOGO.png")
    my_picture = io.BytesIO(rcb_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_rcb = ImageTk.PhotoImage(pil_img)
    RCB_butt=tk.Button(front_page, text='RCB',image = tk_rcb ,bg='red',fg='white', command=partial(AllPlayersPage, "RCB"))
    RCB_butt.place(x=x_start_logo_pos+400,y=y_start_logo_pos+200)
    CreateToolTip(RCB_butt, text = 'Royal Challengers Bangalore')

    srh_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_SRH_LOGO.png")
    my_picture = io.BytesIO(srh_logo.content)
    pil_img = Image.open(my_picture).resize((150,150))
    tk_srh = ImageTk.PhotoImage(pil_img)
    SRH_butt=tk.Button(front_page, text='SRH',image = tk_srh ,bg='orange',fg='white', command=partial(AllPlayersPage, "SRH"))
    SRH_butt.place(x=x_start_logo_pos+600,y=y_start_logo_pos+200)
    CreateToolTip(SRH_butt, text = 'Sunrisers Hyderabad')

    Online_Reset=tk.Button(front_page, text='Retreieve Data from Online Source',width=30,bg='black',fg='white', command=O_Reset)
    Online_Reset.place(x=1100,y=680)
    CreateToolTip(Online_Reset, text = 'Be warned.\nThis will overwrite your current database!')
    front_page.mainloop()

def AllPlayersPage(team="none"):

    global all_player_page , front_page, update_player_page, delete_player_page,add_player_page
    try:
        front_page.destroy()
    except:
        pass
    try:
        add_player_page.destroy()
    except:
        pass
    try:
        delete_player_page.destroy()
    except:
        pass
    try:
        update_player_page.destroy()
    except:
        pass
    all_player_page = tk.Toplevel()

    width=all_player_page.winfo_screenwidth()               
    height=all_player_page.winfo_screenheight()               
    
    all_player_page.geometry("%dx%d" % (width, height))
    all_player_page.state('zoomed')
    all_player_page.title("All Players")
    heading=tk.Label(all_player_page, text="All Players",width=30,font=("Times New Roman", 20,"bold"))
    heading.grid(row=0,column=0)


    

    columns = ('TeamName', 'PlayerName', 'ShirtNumber', 'Economy' , 'BattingAvg' , 'Role', 'HighestScore' , 'MostWickets', 'Debut' )
    if(team=="none"):
        player_tree = ttk.Treeview(all_player_page, height=22,columns=columns, show='headings')
    else:
        player_tree = ttk.Treeview(all_player_page, height=11,columns=columns, show='headings')
    player_tree.grid(row=2, column=0, sticky='nsew',padx=50,pady=50)

    player_tree.heading('TeamName', text='Team')
    player_tree.column("TeamName", minwidth=0, width=200)

    player_tree.heading('PlayerName', text='Player')
    player_tree.column("PlayerName", minwidth=0, width=200)

    player_tree.heading('ShirtNumber', text='Shirt No.')
    player_tree.column("ShirtNumber", minwidth=0, width=100)

    player_tree.heading('Economy', text='Economy')
    player_tree.column("Economy", minwidth=0, width=100)

    player_tree.heading('BattingAvg', text='Batting Average')
    player_tree.column("BattingAvg", minwidth=0, width=100)

    player_tree.heading('Role', text='Role')
    player_tree.column("Role", minwidth=0, width=140)

    player_tree.heading('HighestScore', text='Highest Score')
    player_tree.column("HighestScore", minwidth=0, width=100)

    player_tree.heading('MostWickets', text='Most Wickets')
    player_tree.column("MostWickets", minwidth=0, width=100)

    player_tree.heading('Debut', text='Debut Date')
    player_tree.column("Debut", minwidth=0, width=140)

    if team=="none":
        for player in displayplayers():
            player_tree.insert("", 'end',iid=player[1], text=player[0],values =(player[0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8]))
    else:
        heading=tk.Label(all_player_page, text=teams[team],width=30,font=("Times New Roman", 20,"bold"))
        heading.grid(row=0,column=0)
        for player in findteam(teams[team])[0]:
            player_tree.insert("", 'end',iid=player[1], text=player[0],values=(player[0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8]))
        
        columns = ('TeamName', 'YearsPlayed', 'Wins', 'FinalsLost' , 'Captain' , 'Owner')
        team_tree = ttk.Treeview(all_player_page, height=1,columns=columns, show='headings')
        team_tree.grid(row=4, column=0, sticky='nsew',padx=50,pady=50)

        team_tree.heading('TeamName', text='Team')
        team_tree.column("TeamName", minwidth=0, width=200)

        team_tree.heading('YearsPlayed', text='Years Played')
        team_tree.column("YearsPlayed", minwidth=0, width=100)

        team_tree.heading('Wins', text='Wins')
        team_tree.column("Wins", minwidth=0, width=100)

        team_tree.heading('FinalsLost', text='Finals Lost')
        team_tree.column("FinalsLost", minwidth=0, width=100)

        team_tree.heading('Captain', text='Captain')
        team_tree.column("Captain", minwidth=0, width=200)

        team_tree.heading('Owner', text='Owner')
        team_tree.column("Owner", minwidth=0, width=140)


        for tea in displayteamstats(teams[team]):
            team_tree.insert("", 'end',iid=tea[0], text=tea[0],values =(tea[0],tea[1],tea[2],tea[3],tea[4],tea[5]))
        

        columns = ('TeamName', 'PlayerName', 'ShirtNumber', 'Salary' , 'Role' , 'Age','Record')
        record_tree = ttk.Treeview(all_player_page, height=5,columns=columns, show='headings')
        record_tree.grid(row=5, column=0, sticky='nsew',padx=50,pady=50)

        record_tree.heading('TeamName', text='Team')
        record_tree.column("TeamName", minwidth=0, width=200)

        record_tree.heading('PlayerName', text='Record Holder')
        record_tree.column("PlayerName", minwidth=0, width=200)

        record_tree.heading('ShirtNumber', text='Shirt No.')
        record_tree.column("ShirtNumber", minwidth=0, width=100)

        record_tree.heading('Salary', text='Salary (₹)')
        record_tree.column("Salary", minwidth=0, width=140)

        record_tree.heading('Role', text='Role')
        record_tree.column("Role", minwidth=0, width=140)

        record_tree.heading('Age', text='Age')
        record_tree.column("Age", minwidth=0, width=100)

        record_tree.heading('Record', text='Record Held')
        record_tree.column("Record", minwidth=0, width=200)


        for record in displayrecords(teams[team]):
            record_tree.insert("", 'end',iid=record[1], text=record[0],values =(record[0],record[1],record[2],record[3],record[4],record[5],record[6]))
    
    if team=="none":
        Search_var=tk.StringVar(all_player_page)

        search=tk.Entry(all_player_page,textvariable=Search_var,width=50)
        search.place(x=950,y=45)
        
        OPTIONS = [ "Choose Filter", "Team Name", "Player Name" , "Shirt Number","Economy","Batting Average","Role","Highest Score","Most Wickets","Debut Year"] 
        variable = StringVar(all_player_page) 
        variable.set(OPTIONS[0])
        w = OptionMenu(all_player_page, variable, *OPTIONS)
        w.grid(row=1,column=1)
        sea_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/search_icon.png")
        my_picture = io.BytesIO(sea_logo.content)
        pil_img = Image.open(my_picture).resize((30,30))
        tk_sea = ImageTk.PhotoImage(pil_img)
        Sea_butt=tk.Button(all_player_page, text='Search',image = tk_sea ,bg='white',fg='white',command=lambda: filter())
        Sea_butt.place(x=900,y=35)

        def filter():
            all_player_page.update()
            s=Search_var.get()
            o=variable.get()
            if s.isdigit() == False and "." not in s:
                s='"'+s+'"'
            if o=="Choose Filter":
                pass
            elif o=="Batting Average":
                o="BattingAvg"
            else:
                o=o.replace(" ","")
            for i in player_tree.get_children():
                player_tree.delete(i)
            for player in filterplayers(s,o):
                player_tree.insert("", 'end',iid=player[1], text=player[0],values=(player[0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8]))
            all_player_page.update()


    y_scrollbar = ttk.Scrollbar(all_player_page, orient=tk.VERTICAL, command=player_tree.yview)
    player_tree.configure(yscroll=y_scrollbar.set)
    y_scrollbar.grid(row=2, column=1, sticky='ns')

    x_scrollbar = ttk.Scrollbar(all_player_page, orient=tk.HORIZONTAL, command=player_tree.xview)
    player_tree.configure(xscroll=x_scrollbar.set)
    x_scrollbar.grid(row=3, column=0, sticky='ew')

    back = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/Arrow_back.png")
    my_picture = io.BytesIO(back.content)
    pil_img = Image.open(my_picture).resize((30,30))
    tk_pk = ImageTk.PhotoImage(pil_img)
    Back_butt=tk.Button(all_player_page, text='Back',image = tk_pk ,bg='white',fg='white', command=FrontPage)
    Back_butt.place(x=10,y=10)
    CreateToolTip(Back_butt, text = 'Go Back')

    if team=="none":
        Update_Player_butt=tk.Button(all_player_page, text='Update Player',width=30,bg='purple',fg='white', command=Update_Player_Name)
        Update_Player_butt.place(x=1000,y=680)
        CreateToolTip(Update_Player_butt, text = 'Update a Player using their Name')
    
        Add_Player_butt=tk.Button(all_player_page, text='Add Player',width=30,bg='blue',fg='white', command=Add_Player)
        Add_Player_butt.place(x=100,y=680)
        CreateToolTip(Add_Player_butt, text = 'Add a Player')

        Delete_Player_butt=tk.Button(all_player_page, text='Delete Player',width=30,bg='red',fg='white', command=Delete_Player_Name)
        Delete_Player_butt.place(x=550,y=680)
        CreateToolTip(Delete_Player_butt, text = 'Delete a Player using their Name')

    all_player_page.mainloop()


def Delete_Player_Name():
    global delete_player_name_page,all_player_page
    delete_player_name_page = tk.Toplevel()              
    
    delete_player_name_page.geometry("305x200")
    delete_player_name_page.title("Delete Player - Name")

    Show_tables = tk.Label(delete_player_name_page, text="Enter Player Name to Delete",width=30)
    Show_tables.grid(row=0,column=0,pady=25)
    e2_str_PlayerName=tk.StringVar(delete_player_name_page)
    e2=tk.Entry(delete_player_name_page,textvariable=e2_str_PlayerName,width=50)
    e2.grid(row=1,column=0,pady=25)
    Delete_Player_butt=tk.Button(delete_player_name_page, text='Delete Player',width=30,bg='red',fg='white', command=lambda: my_update())
    Delete_Player_butt.grid(row=2,column=0,pady=25)
    def my_update():
        Delete_Player(deleteplayer(e2_str_PlayerName.get()))
    delete_player_name_page.mainloop()

def Delete_Player(record):
    global delete_player_page,all_player_page,delete_player_name_page
    
    delete_player_page = tk.Toplevel()              
    delete_player_name_page.destroy()
    delete_player_page.geometry("200x200")
    delete_player_page.title("Delete Player")
    
    if record is not None:
        Show_tables = tk.Label(delete_player_page, text="Deleting the Player will also",width=30)
        Show_tables.grid(row=0,column=0)
        Show_tables = tk.Label(delete_player_page, text="delete the Records they hold",width=30)
        Show_tables.grid(row=1,column=0)
        e2=tk.Label(delete_player_page, text="Selected Player: "+record[1],width=30)
        e2.grid(row=2,column=0,pady=25)
        Delete_Player_butt=tk.Button(delete_player_page, text='Confirm Delete',width=30,bg='red',fg='white', command=lambda: my_update())
        Delete_Player_butt.grid(row=3,column=0,pady=50)
        def my_update():
            deleteplayer(record[1],"yes")
            all_player_page.destroy()
            AllPlayersPage()
    else:
        Show_tables = tk.Label(delete_player_page, text="Player does not exist",width=30)
        Show_tables.grid(row=0,column=0,pady=50)
        Exit_butt=tk.Button(delete_player_page, text='Exit',width=30,bg='red',fg='white', command=lambda: my_update())
        Exit_butt.grid(row=1,column=0,pady=50)
        def my_update():
            delete_player_page.destroy()
    

def Update_Player_Name():
    global update_player_name_page
    update_player_name_page = tk.Toplevel()              
    
    update_player_name_page.geometry("305x200")
    update_player_name_page.title("Update Player - Name")
    Show_tables = tk.Label(update_player_name_page, text="Enter Player Name to Update",width=30)
    Show_tables.grid(row=0,column=0,pady=25)
    e2_str_PlayerName=tk.StringVar(update_player_name_page)
    e2=tk.Entry(update_player_name_page,textvariable=e2_str_PlayerName,width=50)
    e2.grid(row=1,column=0,pady=25)
    Update_Player_butt=tk.Button(update_player_name_page, text='Update Player',width=30,bg='purple',fg='white', command=lambda: my_update())
    Update_Player_butt.grid(row=2,column=0,pady=25)
    def my_update():
        Update_Player(findplayer(e2_str_PlayerName.get()))
    update_player_name_page.mainloop()

def Add_Player(f=1):
    global add_player_page, all_player_page, add_team_page,t
    
    try:
        add_team_page.destroy()
    except:
        pass
    add_player_page = tk.Toplevel()              
    height=add_player_page.winfo_screenheight()               
    add_player_page.geometry("%dx%d" % (500, height))
    add_player_page.title("Add Player")
    
    


    e1_str_TeamName=tk.StringVar(add_player_page) 
    e2_str_PlayerName=tk.StringVar(add_player_page) 
    e3_str_ShirtNumber=tk.StringVar(add_player_page)
    e4_str_Economy=tk.StringVar(add_player_page)
    e5_str_BattingAvg=tk.StringVar(add_player_page)
    e6_str_Role=tk.StringVar(add_player_page)
    e7_str_Runs=tk.StringVar(add_player_page)
    e8_str_Wickets=tk.StringVar(add_player_page)
    e9_str_Debut=tk.StringVar(add_player_page)


    heading=tk.Label(add_player_page, text="Add Player",width=30,font=("Times New Roman", 20,"bold"))
    heading.grid(row=0,column=0,columnspan=2)

    r1 = tk.Label(add_player_page, text="Team Name:",width=20)
    r1.grid(row=1,column=0,padx=25,pady=25)
    r2 = tk.Label(add_player_page, text="Player Name:",width=20)
    r2.grid(row=2,column=0,padx=25,pady=25)
    r3 = tk.Label(add_player_page, text="Shirt Number:",width=20)
    r3.grid(row=3,column=0,padx=25,pady=25)
    r4 = tk.Label(add_player_page, text="Economy",width=20)
    r4.grid(row=4,column=0,padx=25,pady=25)
    r5 = tk.Label(add_player_page, text="Batting Average:",width=20)
    r5.grid(row=5,column=0,padx=25,pady=25)
    r6 = tk.Label(add_player_page, text="Role:",width=20)
    r6.grid(row=6,column=0,padx=25,pady=25)
    r7 = tk.Label(add_player_page, text="Maximum Runs:",width=20)
    r7.grid(row=7,column=0,padx=25,pady=25)
    r8 = tk.Label(add_player_page, text="Most Wickets:",width=20)
    r8.grid(row=8,column=0,padx=25,pady=25)
    r9 = tk.Label(add_player_page, text="Debut Date:",width=20)
    r9.grid(row=9,column=0,padx=25,pady=25)

    e1=tk.Entry(add_player_page,textvariable=e1_str_TeamName,width=20)
    e1.grid(row=1,column=1,pady=25)
    e2=tk.Entry(add_player_page,textvariable=e2_str_PlayerName,width=20)
    e2.grid(row=2,column=1,pady=25)
    e3=tk.Entry(add_player_page,textvariable=e3_str_ShirtNumber,width=20)
    e3.grid(row=3,column=1,pady=25)
    e4=tk.Entry(add_player_page,textvariable=e4_str_Economy,width=20)
    e4.grid(row=4,column=1,pady=25)
    e5=tk.Entry(add_player_page,textvariable=e5_str_BattingAvg,width=20)
    e5.grid(row=5,column=1,pady=25)
    e6=tk.Entry(add_player_page,textvariable=e6_str_Role,width=20)
    e6.grid(row=6,column=1,pady=25)
    e7=tk.Entry(add_player_page,textvariable=e7_str_Runs,width=20)
    e7.grid(row=7,column=1,pady=25)
    e8=tk.Entry(add_player_page,textvariable=e8_str_Wickets,width=20)
    e8.grid(row=8,column=1,pady=25)
    e9=tk.Entry(add_player_page,textvariable=e9_str_Debut,width=20)
    e9.grid(row=9,column=1,pady=25)
    b2 = tk.Button(add_player_page,text='Add',command=lambda: my_update(),bg="blue",fg="white")  
    b2.grid(row=10, column=1,pady=25) 
    def my_update(): # update record 
        global t
        data=(e1_str_TeamName.get(),e2_str_PlayerName.get(),e3_str_ShirtNumber.get(),e4_str_Economy.get(),e5_str_BattingAvg.get(),e6_str_Role.get(),e7_str_Runs.get(),e8_str_Wickets.get(),e9_str_Debut.get())
        try:
            addplayer(data)
        except Exception as error:
            error_string = str(error)
            print(error_string)
            if "a foreign key constraint fails" in error_string:
                e=tk.Label(add_player_page,text="Player does not Exist in Database",width=40,fg="red")
                e.grid(row=11,column=1,pady=25)
            elif "You have an error in your SQL syntax" in error_string:
                e=tk.Label(add_player_page,text="Please fill in all the details",width=40,fg="red")
                e.grid(row=11,column=1,pady=25,padx=50)
            elif "Unknown column" in error_string:
                e=tk.Label(add_player_page,text="You are using the wrong datatype",width=40,fg="red")
                e.grid(row=11,column=1,pady=25)
            elif "Out of range value" in error_string:
                e=tk.Label(add_player_page,text="A data field is out of range",width=40,fg="red")
                e.grid(row=11,column=1,pady=25)
            elif "Duplicate entry" in error_string:
                e=tk.Label(add_player_page,text="Duplicate Entry",width=40,fg="red")
                e.grid(row=11,column=1,pady=25)

        if t==f and f!=1:
            add_player_page.destroy()
            t=1
            all_team_page.destroy()
            TeamStatsPage()
        else:
            
            if f==1:
                all_player_page.destroy()
                AllPlayersPage()
            else:
                t=t+1
                e2_str_PlayerName.set("")
                e3_str_ShirtNumber.set("") 
                e4_str_Economy.set("") 
                e5_str_BattingAvg.set("")  
                e6_str_Role.set("")
                e7_str_Runs.set("")
                e8_str_Wickets.set("")
                e9_str_Debut.set("")

    add_player_page.mainloop()
            
    



def Update_Player(record):
    global update_player_name_page,update_player_page, all_player_page
    update_player_name_page.destroy()
    update_player_page = tk.Toplevel()

    if record is not None:               
        height=update_player_page.winfo_screenheight()               
        update_player_page.geometry("%dx%d" % (500, height))
        update_player_page.title("Update Player")
    
        s=record
    


        e1_str_TeamName=tk.StringVar(update_player_page) 
        e3_str_ShirtNumber=tk.StringVar(update_player_page)
        e4_str_Economy=tk.StringVar(update_player_page)
        e5_str_BattingAvg=tk.StringVar(update_player_page)
        e6_str_Role=tk.StringVar(update_player_page)
        e7_str_Runs=tk.StringVar(update_player_page)
        e8_str_Wickets=tk.StringVar(update_player_page)
        e9_str_Debut=tk.StringVar(update_player_page)

        e1_str_TeamName.set(s[0]) 
        e2_str_PlayerName=s[1]
        e3_str_ShirtNumber.set(s[2]) 
        e4_str_Economy.set(s[3]) 
        e5_str_BattingAvg.set(s[4])  
        e6_str_Role.set(s[5])
        e7_str_Runs.set(s[6])
        e8_str_Wickets.set(s[7])
        e9_str_Debut.set(s[8])

        heading=tk.Label(update_player_page, text="Update Player",width=30,font=("Times New Roman", 20,"bold"))
        heading.grid(row=0,column=0,columnspan=2)

        r1 = tk.Label(update_player_page, text="Team Name:",width=20)
        r1.grid(row=1,column=0,padx=25,pady=25)
        r2 = tk.Label(update_player_page, text="Player Name:",width=20)
        r2.grid(row=2,column=0,padx=25,pady=25)
        r3 = tk.Label(update_player_page, text="Shirt Number:",width=20)
        r3.grid(row=3,column=0,padx=25,pady=25)
        r4 = tk.Label(update_player_page, text="Economy",width=20)
        r4.grid(row=4,column=0,padx=25,pady=25)
        r5 = tk.Label(update_player_page, text="Batting Average:",width=20)
        r5.grid(row=5,column=0,padx=25,pady=25)
        r6 = tk.Label(update_player_page, text="Role:",width=20)
        r6.grid(row=6,column=0,padx=25,pady=25)
        r7 = tk.Label(update_player_page, text="Maximum Runs:",width=20)
        r7.grid(row=7,column=0,padx=25,pady=25)
        r8 = tk.Label(update_player_page, text="Most Wickets:",width=20)
        r8.grid(row=8,column=0,padx=25,pady=25)
        r9 = tk.Label(update_player_page, text="Debut Date:",width=20)
        r9.grid(row=9,column=0,padx=25,pady=25)

        e1=tk.Entry(update_player_page,textvariable=e1_str_TeamName,width=20)
        e1.grid(row=1,column=1,pady=25)
        e2=tk.Label(update_player_page,text=e2_str_PlayerName,width=20)
        e2.grid(row=2,column=1,pady=25)
        e3=tk.Entry(update_player_page,textvariable=e3_str_ShirtNumber,width=20)
        e3.grid(row=3,column=1,pady=25)
        e4=tk.Entry(update_player_page,textvariable=e4_str_Economy,width=20)
        e4.grid(row=4,column=1,pady=25)
        e5=tk.Entry(update_player_page,textvariable=e5_str_BattingAvg,width=20)
        e5.grid(row=5,column=1,pady=25)
        e6=tk.Entry(update_player_page,textvariable=e6_str_Role,width=20)
        e6.grid(row=6,column=1,pady=25)
        e7=tk.Entry(update_player_page,textvariable=e7_str_Runs,width=20)
        e7.grid(row=7,column=1,pady=25)
        e8=tk.Entry(update_player_page,textvariable=e8_str_Wickets,width=20)
        e8.grid(row=8,column=1,pady=25)
        e9=tk.Entry(update_player_page,textvariable=e9_str_Debut,width=20)
        e9.grid(row=9,column=1,pady=25)
        b2 = tk.Button(update_player_page,text='Update',command=lambda: my_update(),bg="purple",fg="white")  
        b2.grid(row=10, column=1,pady=25) 
        e=tk.Label(update_player_page,text="",width=40,fg="red")
        e.grid(row=11,column=1,pady=25)
        def my_update(): # update record 
            data=(e1_str_TeamName.get(),e2_str_PlayerName,e3_str_ShirtNumber.get(),e4_str_Economy.get(),e5_str_BattingAvg.get(),e6_str_Role.get(),e7_str_Runs.get(),e8_str_Wickets.get(),e9_str_Debut.get())
            try:
                updateplayer(data,s[1])
            except Exception as error:
                error_string = str(error)
                print(error_string)
                if "a foreign key constraint fails" in error_string:
                    e=tk.Label(update_player_page,text="Player does not Exist in Database",width=40,fg="red")
                    e.grid(row=11,column=1,pady=25)
                elif "You have an error in your SQL syntax" in error_string:
                    e=tk.Label(update_player_page,text="Please fill in all the details",width=40,fg="red")
                    e.grid(row=11,column=1,pady=25,padx=50)
                elif "Unknown column" in error_string:
                    e=tk.Label(update_player_page,text="You are using the wrong datatype",width=40,fg="red")
                    e.grid(row=11,column=1,pady=25)
                elif "Out of range value" in error_string:
                    e=tk.Label(update_player_page,text="A data field is out of range",width=40,fg="red")
                    e.grid(row=11,column=1,pady=25)
                elif "Duplicate entry" in error_string:
                    e=tk.Label(update_player_page,text="Duplicate Entry",width=40,fg="red")
                    e.grid(row=11,column=1,pady=25)

            all_player_page.destroy()
            AllPlayersPage()
    else:
        Show_tables = tk.Label(update_player_page, text="Player does not exist",width=30)
        Show_tables.grid(row=0,column=0,pady=50)
        Exit_butt=tk.Button(update_player_page, text='Exit',width=30,bg='purple',fg='white', command=lambda: my_update())
        Exit_butt.grid(row=1,column=0,pady=50)
        def my_update():
            update_player_page.destroy()
    update_player_page.mainloop()
            


 

def TeamStatsPage():

    global all_team_page , front_page, update_team_page, delete_team_page,add_team_page
    try:
        front_page.destroy()
    except:
        pass
    try:
        add_team_page.destroy()
    except:
        pass
    try:
        delete_team_page.destroy()
    except:
        pass
    try:
        update_team_page.destroy()
    except:
        pass
    all_team_page = tk.Toplevel()

    width=all_team_page.winfo_screenwidth()               
    height=all_team_page.winfo_screenheight()               
    
    all_team_page.geometry("%dx%d" % (width, height))
    all_team_page.state('zoomed')
    all_team_page.title("All Teams")
    heading=tk.Label(all_team_page, text="All Teams",width=30,font=("Times New Roman", 20,"bold"))
    heading.grid(row=0,column=0)
    columns = ('TeamName', 'YearsPlayed', 'Wins', 'FinalsLost' , 'Captain' , 'Owner')
    team_tree = ttk.Treeview(all_team_page, height=11,columns=columns, show='headings')
    team_tree.grid(row=1, column=0, sticky='nsew',padx=50,pady=50)

    team_tree.heading('TeamName', text='Team')
    team_tree.column("TeamName", minwidth=0, width=200)

    team_tree.heading('YearsPlayed', text='Years Played')
    team_tree.column("YearsPlayed", minwidth=0, width=100)

    team_tree.heading('Wins', text='Wins')
    team_tree.column("Wins", minwidth=0, width=100)

    team_tree.heading('FinalsLost', text='Finals Lost')
    team_tree.column("FinalsLost", minwidth=0, width=100)

    team_tree.heading('Captain', text='Captain')
    team_tree.column("Captain", minwidth=0, width=200)

    team_tree.heading('Owner', text='Owner')
    team_tree.column("Owner", minwidth=0, width=140)


    for team in displayteamstats():
        team_tree.insert("", 'end',iid=team[0], text=team[0],values =(team[0],team[1],team[2],team[3],team[4],team[5]))

    y_scrollbar = ttk.Scrollbar(all_team_page, orient=tk.VERTICAL, command=team_tree.yview)
    team_tree.configure(yscroll=y_scrollbar.set)
    y_scrollbar.grid(row=1, column=1, sticky='ns')

    x_scrollbar = ttk.Scrollbar(all_team_page, orient=tk.HORIZONTAL, command=team_tree.xview)
    team_tree.configure(xscroll=x_scrollbar.set)
    x_scrollbar.grid(row=2, column=0, sticky='ew')

    back = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/Arrow_back.png")
    my_picture = io.BytesIO(back.content)
    pil_img = Image.open(my_picture).resize((30,30))
    tk_pk = ImageTk.PhotoImage(pil_img)
    Back_butt=tk.Button(all_team_page, text='Back',image = tk_pk ,bg='white',fg='white', command=FrontPage)
    Back_butt.place(x=10,y=10)
    CreateToolTip(Back_butt, text = 'Go Back')

    Update_Team_butt=tk.Button(all_team_page, text='Update Team',width=30,bg='purple',fg='white', command=Update_Team_Name)
    Update_Team_butt.place(x=1000,y=680)
    CreateToolTip(Update_Team_butt, text = 'Update a Team using their Name')
    
    Add_Team_butt=tk.Button(all_team_page, text='Add Team',width=30,bg='blue',fg='white', command=Add_Team)
    Add_Team_butt.place(x=100,y=680)
    CreateToolTip(Add_Team_butt, text = 'Add a Team')

    Delete_Team_butt=tk.Button(all_team_page, text='Delete Team',width=30,bg='red',fg='white', command=Delete_Team_Name)
    Delete_Team_butt.place(x=550,y=680)
    CreateToolTip(Delete_Team_butt, text = 'Delete a Team using their Name')

    all_team_page.mainloop()


def Delete_Team_Name():
    global delete_team_name_page,all_team_page
    delete_team_name_page = tk.Toplevel()              
    
    delete_team_name_page.geometry("305x200")
    delete_team_name_page.title("Delete Team - Name")

    Show_tables = tk.Label(delete_team_name_page, text="Enter Team Name to Delete",width=30)
    Show_tables.grid(row=0,column=0,pady=25)
    e2_str_TeamName=tk.StringVar(delete_team_name_page)
    e2=tk.Entry(delete_team_name_page,textvariable=e2_str_TeamName,width=50)
    e2.grid(row=1,column=0,pady=25)
    Delete_Team_butt=tk.Button(delete_team_name_page, text='Delete Team',width=30,bg='red',fg='white', command=lambda: my_update())
    Delete_Team_butt.grid(row=2,column=0,pady=25)
    def my_update():
        Delete_Team(deleteteam(e2_str_TeamName.get()))
    delete_team_name_page.mainloop()

def Delete_Team(record):
    global delete_team_page,all_team_page,delete_team_name_page
    
    delete_team_page = tk.Toplevel()              
    delete_team_name_page.destroy()
    delete_team_page.geometry("200x200")
    delete_team_page.title("Delete Team")
    
    if record is not None:
        Show_tables = tk.Label(delete_team_page, text="Deleting the Team will also",width=30)
        Show_tables.grid(row=0,column=0)
        Show_tables = tk.Label(delete_team_page, text="delete the Players in them",width=30)
        Show_tables.grid(row=1,column=0)
        e2=tk.Label(delete_team_page, text="Selected Team: "+record[0],width=30)
        e2.grid(row=2,column=0,pady=25)
        Delete_Team_butt=tk.Button(delete_team_page, text='Confirm Delete',width=30,bg='red',fg='white', command=lambda: my_update())
        Delete_Team_butt.grid(row=3,column=0,pady=50)
        def my_update():
            deleteteam(record[0],"yes")
            all_team_page.destroy()
            TeamStatsPage()
    else:
        Show_tables = tk.Label(delete_team_page, text="Team does not exist",width=30)
        Show_tables.grid(row=0,column=0,pady=50)
        Exit_butt=tk.Button(delete_team_page, text='Exit',width=30,bg='red',fg='white', command=lambda: my_update())
        Exit_butt.grid(row=1,column=0,pady=50)
        def my_update():
            delete_team_page.destroy()
    

def Update_Team_Name():
    global update_team_name_page
    update_team_name_page = tk.Toplevel()              
    
    update_team_name_page.geometry("305x200")
    update_team_name_page.title("Update Team - Name")
    Show_tables = tk.Label(update_team_name_page, text="Enter Team Name to Update",width=30)
    Show_tables.grid(row=0,column=0,pady=25)
    e2_str_TeamName=tk.StringVar(update_team_name_page)
    e2=tk.Entry(update_team_name_page,textvariable=e2_str_TeamName,width=50)
    e2.grid(row=1,column=0,pady=25)
    Update_Team_butt=tk.Button(update_team_name_page, text='Update Team',width=30,bg='purple',fg='white', command=lambda: my_update())
    Update_Team_butt.grid(row=2,column=0,pady=25)
    def my_update():
        Update_Team(findteam(e2_str_TeamName.get()))
    update_team_name_page.mainloop()

def Add_Team():
    global add_team_page, all_team_page
    add_team_page = tk.Toplevel()           
    height=add_team_page.winfo_screenheight()               
    add_team_page.geometry("%dx%d" % (500, height))
    add_team_page.title("Add Team")
    

    e1_str_TeamName=tk.StringVar(add_team_page) 
    e2_str_YearsPlayed=tk.StringVar(add_team_page) 
    e3_str_Wins=tk.StringVar(add_team_page)
    e4_str_FinalsLost=tk.StringVar(add_team_page)
    e5_str_Captain=tk.StringVar(add_team_page)
    e6_str_Owner=tk.StringVar(add_team_page)

    heading=tk.Label(add_team_page, text="Add Team",width=30,font=("Times New Roman", 20,"bold"))
    heading.grid(row=0,column=0,columnspan=2)
    r1 = tk.Label(add_team_page, text="Team Name:",width=20)
    r1.grid(row=1,column=0,padx=25,pady=25)
    r2 = tk.Label(add_team_page, text="No. of Years Played:",width=20)
    r2.grid(row=2,column=0,padx=25,pady=25)
    r3 = tk.Label(add_team_page, text="Wins:",width=20)
    r3.grid(row=3,column=0,padx=25,pady=25)
    r4 = tk.Label(add_team_page, text="Finals lost:",width=20)
    r4.grid(row=4,column=0,padx=25,pady=25)
    r5 = tk.Label(add_team_page, text="Captain:",width=20)
    r5.grid(row=5,column=0,padx=25,pady=25)
    r6 = tk.Label(add_team_page, text="Owner:",width=20)
    r6.grid(row=6,column=0,padx=25,pady=25)
  

    e1=tk.Entry(add_team_page,textvariable=e1_str_TeamName,width=20)
    e1.grid(row=1,column=1,pady=25)
    e2=tk.Entry(add_team_page,textvariable=e2_str_YearsPlayed,width=20)
    e2.grid(row=2,column=1,pady=25)
    e3=tk.Entry(add_team_page,textvariable=e3_str_Wins,width=20)
    e3.grid(row=3,column=1,pady=25)
    e4=tk.Entry(add_team_page,textvariable=e4_str_FinalsLost,width=20)
    e4.grid(row=4,column=1,pady=25)
    e5=tk.Entry(add_team_page,textvariable=e5_str_Captain,width=20)
    e5.grid(row=5,column=1,pady=25)
    e6=tk.Entry(add_team_page,textvariable=e6_str_Owner,width=20)
    e6.grid(row=6,column=1,pady=25)

    b2 = tk.Button(add_team_page,text='Add',command=lambda: my_update(),bg="blue",fg="white")  
    b2.grid(row=7, column=1,pady=25) 

    e=tk.Label(add_team_page,text="",width=40,fg="red")
    e.grid(row=8,column=1,pady=25)
    def my_update(): # update record 
        data=(e1_str_TeamName.get(),e2_str_YearsPlayed.get(),e3_str_Wins.get(),e4_str_FinalsLost.get(),e5_str_Captain.get(),e6_str_Owner.get())
        try:
            addteam(data)
        except Exception as error:
            error_string = str(error)
            print(error_string)
            if "a foreign key constraint fails" in error_string:
                e=tk.Label(add_team_page,text="Player does not Exist in Database",width=40,fg="red")
                e.grid(row=8,column=1,pady=25)
            elif "You have an error in your SQL syntax" in error_string:
                e=tk.Label(add_team_page,text="Please fill in all the details",width=40,fg="red")
                e.grid(row=8,column=1,pady=25,padx=50)
            elif "Unknown column" in error_string:
                e=tk.Label(add_team_page,text="You are using the wrong datatype",width=40,fg="red")
                e.grid(row=8,column=1,pady=25)
            elif "Out of range value" in error_string:
                e=tk.Label(add_team_page,text="A data field is out of range",width=40,fg="red")
                e.grid(row=8,column=1,pady=25)
            elif "Duplicate entry" in error_string:
                e=tk.Label(add_team_page,text="Duplicate Entry",width=40,fg="red")
                e.grid(row=8,column=1,pady=25)

        Add_Player(2)

    add_team_page.mainloop()



def Update_Team(record):
    global update_team_name_page,update_team_page, all_team_page
    update_team_name_page.destroy()
    update_team_page = tk.Toplevel()
    record=record[1]
    if record is not None:             
        height=update_team_page.winfo_screenheight()               
        update_team_page.geometry("%dx%d" % (500, height))
        update_team_page.title("Update Team")
    
        s=record
    


        e1_str_TeamName=tk.StringVar(update_team_page) 
        e2_str_YearsPlayed=tk.StringVar(update_team_page) 
        e3_str_Wins=tk.StringVar(update_team_page)
        e4_str_FinalsLost=tk.StringVar(update_team_page)
        e5_str_Captain=tk.StringVar(update_team_page)
        e6_str_Owner=tk.StringVar(update_team_page)

        e1_str_TeamName.set(s[0]) 
        e2_str_YearsPlayed.set(s[1])
        e3_str_Wins.set(s[2]) 
        e4_str_FinalsLost.set(s[3]) 
        e5_str_Captain.set(s[4])  
        e6_str_Owner.set(s[5])
        
        heading=tk.Label(update_team_page, text="Update Team",width=30,font=("Times New Roman", 20,"bold"))
        heading.grid(row=0,column=0,columnspan=2)
        r1 = tk.Label(update_team_page, text="Team Name:",width=20)
        r1.grid(row=1,column=0,padx=25,pady=25)
        r2 = tk.Label(update_team_page, text="No. of Years Played:",width=20)
        r2.grid(row=2,column=0,padx=25,pady=25)
        r3 = tk.Label(update_team_page, text="Wins:",width=20)
        r3.grid(row=3,column=0,padx=25,pady=25)
        r4 = tk.Label(update_team_page, text="Finals lost:",width=20)
        r4.grid(row=4,column=0,padx=25,pady=25)
        r5 = tk.Label(update_team_page, text="Captain:",width=20)
        r5.grid(row=5,column=0,padx=25,pady=25)
        r6 = tk.Label(update_team_page, text="Owner:",width=20)
        r6.grid(row=6,column=0,padx=25,pady=25)

        e1=tk.Entry(update_team_page,textvariable=e1_str_TeamName,width=20)
        e1.grid(row=1,column=1,pady=25)
        e2=tk.Entry(update_team_page,textvariable=e2_str_YearsPlayed,width=20)
        e2.grid(row=2,column=1,pady=25)
        e3=tk.Entry(update_team_page,textvariable=e3_str_Wins,width=20)
        e3.grid(row=3,column=1,pady=25)
        e4=tk.Entry(update_team_page,textvariable=e4_str_FinalsLost,width=20)
        e4.grid(row=4,column=1,pady=25)
        e5=tk.Entry(update_team_page,textvariable=e5_str_Captain,width=20)
        e5.grid(row=5,column=1,pady=25)
        e6=tk.Entry(update_team_page,textvariable=e6_str_Owner,width=20)
        e6.grid(row=6,column=1,pady=25)
        b2 = tk.Button(update_team_page,text='Update',command=lambda: my_update(),bg="purple",fg="white")  
        b2.grid(row=7, column=1,pady=25)
        e=tk.Label(update_team_page,text="",width=40,fg="red")
        e.grid(row=8,column=1,pady=25) 
        def my_update(): # update record 
            team = [k for k, v in teams.items() if v == s[0]]
            if len(team)==1:
                teams[team[0]]=e1_str_TeamName.get()
            data=(e1_str_TeamName.get(),e2_str_YearsPlayed.get(),e3_str_Wins.get(),e4_str_FinalsLost.get(),e5_str_Captain.get(),e6_str_Owner.get())
            try:
                updateteam(data,s[0])
                all_team_page.destroy()
                TeamStatsPage()
            except Exception as error:
                error_string = str(error)
                print(error_string)
                if "a foreign key constraint fails" in error_string:
                    e=tk.Label(update_team_page,text="Player does not Exist in Database",width=40,fg="red")
                    e.grid(row=8,column=1,pady=25)
                elif "You have an error in your SQL syntax" in error_string:
                    e=tk.Label(update_team_page,text="Please fill in all the details",width=40,fg="red")
                    e.grid(row=8,column=1,pady=25,padx=50)
                elif "Unknown column" in error_string:
                    e=tk.Label(update_team_page,text="You are using the wrong datatype",width=40,fg="red")
                    e.grid(row=8,column=1,pady=25)
                elif "Out of range value" in error_string:
                    e=tk.Label(update_team_page,text="A data field is out of range",width=40,fg="red")
                    e.grid(row=8,column=1,pady=25)
                elif "Duplicate entry" in error_string:
                    e=tk.Label(update_team_page,text="Duplicate Entry",width=40,fg="red")
                    e.grid(row=8,column=1,pady=25)
            
    else:
        Show_tables = tk.Label(update_team_page, text="Team does not exist",width=30)
        Show_tables.grid(row=0,column=0,pady=50)
        Exit_butt=tk.Button(update_team_page, text='Exit',width=30,bg='purple',fg='white', command=lambda: my_update())
        Exit_butt.grid(row=1,column=0,pady=50)
        def my_update():
            update_team_page.destroy()
    update_team_page.mainloop()


def PlayerRecordsPage():

    global all_record_page , front_page, update_record_page, delete_record_page,add_record_page
    try:
        front_page.destroy()
    except:
        pass
    try:
        add_record_page.destroy()
    except:
        pass
    try:
        delete_record_page.destroy()
    except:
        pass
    try:
        update_record_page.destroy()
    except:
        pass
    all_record_page = tk.Toplevel()

    width=all_record_page.winfo_screenwidth()               
    height=all_record_page.winfo_screenheight()               
    
    all_record_page.geometry("%dx%d" % (width, height))
    all_record_page.state('zoomed')
    all_record_page.title("All Records")
    heading=tk.Label(all_record_page, text="All records",width=30,font=("Times New Roman", 20,"bold"))
    heading.grid(row=0,column=0)
    columns = ('TeamName', 'PlayerName', 'ShirtNumber', 'Salary' , 'Role' , 'Age','Record')
    record_tree = ttk.Treeview(all_record_page, height=11,columns=columns, show='headings')
    record_tree.grid(row=0, column=0, sticky='nsew',padx=50,pady=50)

    record_tree.heading('TeamName', text='Team')
    record_tree.column("TeamName", minwidth=0, width=200)

    record_tree.heading('PlayerName', text='Record Holder')
    record_tree.column("PlayerName", minwidth=0, width=200)

    record_tree.heading('ShirtNumber', text='Shirt No.')
    record_tree.column("ShirtNumber", minwidth=0, width=100)

    record_tree.heading('Salary', text='Salary (₹)')
    record_tree.column("Salary", minwidth=0, width=140)

    record_tree.heading('Role', text='Role')
    record_tree.column("Role", minwidth=0, width=140)

    record_tree.heading('Age', text='Age')
    record_tree.column("Age", minwidth=0, width=100)

    record_tree.heading('Record', text='Record Held')
    record_tree.column("Record", minwidth=0, width=200)


    for record in displayrecords():
        record_tree.insert("", 'end',iid=record[1], text=record[0],values =(record[0],record[1],record[2],record[3],record[4],record[5],record[6]))

    y_scrollbar = ttk.Scrollbar(all_record_page, orient=tk.VERTICAL, command=record_tree.yview)
    record_tree.configure(yscroll=y_scrollbar.set)
    y_scrollbar.grid(row=0, column=1, sticky='ns')

    x_scrollbar = ttk.Scrollbar(all_record_page, orient=tk.HORIZONTAL, command=record_tree.xview)
    record_tree.configure(xscroll=x_scrollbar.set)
    x_scrollbar.grid(row=1, column=0, sticky='ew')

    back = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/Arrow_back.png")
    my_picture = io.BytesIO(back.content)
    pil_img = Image.open(my_picture).resize((30,30))
    tk_pk = ImageTk.PhotoImage(pil_img)
    Back_butt=tk.Button(all_record_page, text='Back',image = tk_pk ,bg='white',fg='white', command=FrontPage)
    Back_butt.place(x=10,y=10)
    CreateToolTip(Back_butt, text = 'Go Back')

    Update_Record_butt=tk.Button(all_record_page, text='Update Record Holder',width=30,bg='purple',fg='white', command=Update_Record_Name)
    Update_Record_butt.place(x=1000,y=680)
    CreateToolTip(Update_Record_butt, text = 'Update a Record Holder using their Name')
    
    Add_Record_butt=tk.Button(all_record_page, text='Add Record Holder',width=30,bg='blue',fg='white', command=Add_Record)
    Add_Record_butt.place(x=100,y=680)
    CreateToolTip(Add_Record_butt, text = 'Add a Record and Holder')

    Delete_Record_butt=tk.Button(all_record_page, text='Delete Record Holder',width=30,bg='red',fg='white', command=Delete_Record_Name)
    Delete_Record_butt.place(x=550,y=680)
    CreateToolTip(Delete_Record_butt, text = 'Delete a Record Holder using their Name')

    all_record_page.mainloop()


def Delete_Record_Name():
    global delete_record_name_page,all_record_page
    delete_record_name_page = tk.Toplevel()              
    
    delete_record_name_page.geometry("305x200")
    delete_record_name_page.title("Delete Record - Name")

    Show_tables = tk.Label(delete_record_name_page, text="Enter Record Holder Name to Delete",width=30)
    Show_tables.grid(row=0,column=0,pady=25)
    e2_str_PlayerName=tk.StringVar(delete_record_name_page)
    e2=tk.Entry(delete_record_name_page,textvariable=e2_str_PlayerName,width=50)
    e2.grid(row=1,column=0,pady=25)
    Delete_Record_butt=tk.Button(delete_record_name_page, text='Delete Record',width=30,bg='red',fg='white', command=lambda: my_update())
    Delete_Record_butt.grid(row=2,column=0,pady=25)
    def my_update():
        Delete_Record(deleterecord(e2_str_PlayerName.get()))
    delete_record_name_page.mainloop()

def Delete_Record(record):
    global delete_record_page,all_record_page,delete_record_name_page
    
    delete_record_page = tk.Toplevel()              
    delete_record_name_page.destroy()
    delete_record_page.geometry("200x200")
    delete_record_page.title("Delete Record")
    
    if record is not None:
        Show_tables = tk.Label(delete_record_page, text="Deleting the Record",width=30)
        e2=tk.Label(delete_record_page, text="Selected Record: "+record[1],width=30,justify="left")
        e2.grid(row=2,column=0,pady=25)
        Delete_Record_butt=tk.Button(delete_record_page, text='Confirm Delete',width=30,bg='red',fg='white', command=lambda: my_update())
        Delete_Record_butt.grid(row=3,column=0,pady=50)
        def my_update():
            deleterecord(record[1],"yes")
            all_record_page.destroy()
            PlayerRecordsPage()
    else:
        Show_tables = tk.Label(delete_record_page, text="Record does not exist",width=30)
        Show_tables.grid(row=0,column=0,pady=50)
        Exit_butt=tk.Button(delete_record_page, text='Exit',width=30,bg='red',fg='white', command=lambda: my_update())
        Exit_butt.grid(row=1,column=0,pady=50)
        def my_update():
            delete_record_page.destroy()
    

def Update_Record_Name():
    global update_record_name_page
    update_record_name_page = tk.Toplevel()              
    
    update_record_name_page.geometry("305x200")
    update_record_name_page.title("Update Record - Name")
    Show_tables = tk.Label(update_record_name_page, text="Enter Record Holder Name to Update",width=30)
    Show_tables.grid(row=0,column=0,pady=25)
    e2_str_PlayerName=tk.StringVar(update_record_name_page)
    e2=tk.Entry(update_record_name_page,textvariable=e2_str_PlayerName,width=50)
    e2.grid(row=1,column=0,pady=25)
    Update_Record_butt=tk.Button(update_record_name_page, text='Update Record',width=30,bg='purple',fg='white', command=lambda: my_update())
    Update_Record_butt.grid(row=2,column=0,pady=25)
    def my_update():
        Update_Record(findrecord(e2_str_PlayerName.get()))
    update_record_name_page.mainloop()

def Add_Record():
    global add_record_page, all_record_page
    add_record_page = tk.Toplevel()             
    height=add_record_page.winfo_screenheight()               
    add_record_page.geometry("%dx%d" % (500, height))
    add_record_page.title("Add Record")
    
    e1_str_TeamName=tk.StringVar(add_record_page)
    e2_str_PlayerName=tk.StringVar(add_record_page) 
    e3_str_ShirtNumber=tk.StringVar(add_record_page) 
    e4_str_Salary=tk.StringVar(add_record_page)
    e5_str_Role=tk.StringVar(add_record_page)
    e6_str_Age=tk.StringVar(add_record_page)
    e7_str_Record=tk.StringVar(add_record_page)
    

    heading=tk.Label(add_record_page, text="Add Record",width=30,font=("Times New Roman", 20,"bold"))
    heading.grid(row=0,column=0,columnspan=2)
    r1 = tk.Label(add_record_page, text="Team Name:",width=20)
    r1.grid(row=1,column=0,padx=25,pady=25)
    r2 = tk.Label(add_record_page, text="Record Holder Name:",width=20)
    r2.grid(row=2,column=0,padx=25,pady=25)
    r3 = tk.Label(add_record_page, text="Shirt Number:",width=20)
    r3.grid(row=3,column=0,padx=25,pady=25)
    r4 = tk.Label(add_record_page, text="Salary (₹):",width=20)
    r4.grid(row=4,column=0,padx=25,pady=25)
    r5 = tk.Label(add_record_page, text="Role:",width=20)
    r5.grid(row=5,column=0,padx=25,pady=25)
    r6 = tk.Label(add_record_page, text="Age:",width=20)
    r6.grid(row=6,column=0,padx=25,pady=25)
    r7 = tk.Label(add_record_page, text="Record:",width=20)
    r7.grid(row=7,column=0,padx=25,pady=25)
  

    e1=tk.Entry(add_record_page,textvariable=e1_str_TeamName,width=20)
    e1.grid(row=1,column=1,pady=25)
    e2=tk.Entry(add_record_page,textvariable=e2_str_PlayerName,width=20)
    e2.grid(row=2,column=1,pady=25)
    e3=tk.Entry(add_record_page,textvariable=e3_str_ShirtNumber,width=20)
    e3.grid(row=3,column=1,pady=25)
    e4=tk.Entry(add_record_page,textvariable=e4_str_Salary,width=20)
    e4.grid(row=4,column=1,pady=25)
    e5=tk.Entry(add_record_page,textvariable=e5_str_Role,width=20)
    e5.grid(row=5,column=1,pady=25)
    e6=tk.Entry(add_record_page,textvariable=e6_str_Age,width=20)
    e6.grid(row=6,column=1,pady=25)
    e7=tk.Entry(add_record_page,textvariable=e7_str_Record,width=20)
    e7.grid(row=7,column=1,pady=25)

    b2 = tk.Button(add_record_page,text='Add',command=lambda: my_update(),bg="blue",fg="white")  
    b2.grid(row=8, column=1,pady=25) 
    e=tk.Label(add_record_page,text="",width=40,fg="red")
    e.grid(row=9,column=1,pady=25)
    def my_update(): # update record 
        data=(e1_str_TeamName.get(),e2_str_PlayerName.get(),e3_str_ShirtNumber.get(),e4_str_Salary.get(),e5_str_Role.get(),e6_str_Age.get(),e7_str_Record.get())
        try:
            addrecord(data)
            all_record_page.destroy()
            PlayerRecordsPage()
        except Exception as error:
            error_string = str(error)
            print(error_string)
            if "a foreign key constraint fails" in error_string:
                e=tk.Label(add_record_page,text="Player does not Exist in Database",width=40,fg="red")
                e.grid(row=9,column=1,pady=25)
            elif "You have an error in your SQL syntax" in error_string:
                e=tk.Label(add_record_page,text="Please fill in all the details",width=40,fg="red")
                e.grid(row=9,column=1,pady=25,padx=50)
            elif "Unknown column" in error_string:
                e=tk.Label(add_record_page,text="You are using the wrong datatype",width=40,fg="red")
                e.grid(row=9,column=1,pady=25)
            elif "Out of range value" in error_string:
                e=tk.Label(add_record_page,text="A data field is out of range",width=40,fg="red")
                e.grid(row=9,column=1,pady=25)
            elif "Duplicate entry" in error_string:
                e=tk.Label(add_record_page,text="Duplicate Entry",width=40,fg="red")
                e.grid(row=9,column=1,pady=25)

    add_record_page.mainloop()



def Update_Record(record):
    global update_record_name_page,update_record_page, all_record_page
    update_record_name_page.destroy()
    update_record_page = tk.Toplevel()
    if record is not None:             
        height=update_record_page.winfo_screenheight()               
        update_record_page.geometry("%dx%d" % (500, height))
        update_record_page.title("Update Record")
    
        s=record
    
    
        e1_str_TeamName=tk.StringVar(update_record_page)
        e2_str_PlayerName=tk.StringVar(update_record_page) 
        e3_str_ShirtNumber=tk.StringVar(update_record_page) 
        e4_str_Salary=tk.StringVar(update_record_page)
        e5_str_Role=tk.StringVar(update_record_page)
        e6_str_Age=tk.StringVar(update_record_page)
        e7_str_Record=tk.StringVar(update_record_page)

        e1_str_TeamName.set(s[0]) 
        e2_str_PlayerName.set(s[1])
        e3_str_ShirtNumber.set(s[2]) 
        e4_str_Salary.set(s[3]) 
        e5_str_Role.set(s[4])  
        e7_str_Record.set(s[5])


        heading=tk.Label(update_record_page, text="Update Record",width=30,font=("Times New Roman", 20,"bold"))
        heading.grid(row=0,column=0,columnspan=2)
        r1 = tk.Label(update_record_page, text="Team Name:",width=20)
        r1.grid(row=1,column=0,padx=25,pady=25)
        r2 = tk.Label(update_record_page, text="Record Holder Name:",width=20)
        r2.grid(row=2,column=0,padx=25,pady=25)
        r3 = tk.Label(update_record_page, text="Shirt Number:",width=20)
        r3.grid(row=3,column=0,padx=25,pady=25)
        r4 = tk.Label(update_record_page, text="Salary (₹):",width=20)
        r4.grid(row=4,column=0,padx=25,pady=25)
        r5 = tk.Label(update_record_page, text="Role:",width=20)
        r5.grid(row=5,column=0,padx=25,pady=25)
        r6 = tk.Label(update_record_page, text="Age:",width=20)
        r6.grid(row=6,column=0,padx=25,pady=25)
        r7 = tk.Label(update_record_page, text="Record:",width=20)
        r7.grid(row=7,column=0,padx=25,pady=25)
  

        e1=tk.Entry(update_record_page,textvariable=e1_str_TeamName,width=20)
        e1.grid(row=1,column=1,pady=25)
        e2=tk.Entry(update_record_page,textvariable=e2_str_PlayerName,width=20)
        e2.grid(row=2,column=1,pady=25)
        e3=tk.Entry(update_record_page,textvariable=e3_str_ShirtNumber,width=20)
        e3.grid(row=3,column=1,pady=25)
        e4=tk.Entry(update_record_page,textvariable=e4_str_Salary,width=20)
        e4.grid(row=4,column=1,pady=25)
        e5=tk.Entry(update_record_page,textvariable=e5_str_Role,width=20)
        e5.grid(row=5,column=1,pady=25)
        e6=tk.Entry(update_record_page,textvariable=e6_str_Age,width=20)
        e6.grid(row=6,column=1,pady=25)
        e7=tk.Entry(update_record_page,textvariable=e7_str_Record,width=20)
        e7.grid(row=7,column=1,pady=25)
        b2 = tk.Button(update_record_page,text='Update',command=lambda: my_update(),bg="purple",fg="white")  
        b2.grid(row=8, column=1,pady=25) 
        e=tk.Label(update_record_page,text="",width=40,fg="red")
        e.grid(row=9,column=1,pady=25)
        def my_update(): # update record 
            data=(e1_str_TeamName.get(),e2_str_PlayerName.get(),e3_str_ShirtNumber.get(),e4_str_Salary.get(),e5_str_Role.get(),e6_str_Age.get(),e7_str_Record.get())
            try:
                updaterecord(data,s[0])
                all_record_page.destroy()
                PlayerRecordsPage()
            except Exception as error:
                error_string = str(error)
                print(error_string)
                if "a foreign key constraint fails" in error_string:
                    e=tk.Label(update_record_page,text="Player does not Exist in Database",width=40,fg="red")
                    e.grid(row=9,column=1,pady=25)
                elif "You have an error in your SQL syntax" in error_string:
                    e=tk.Label(update_record_page,text="Please fill in all the details",width=40,fg="red")
                    e.grid(row=9,column=1,pady=25,padx=50)
                elif "Unknown column" in error_string:
                    e=tk.Label(update_record_page,text="You are using the wrong datatype",width=40,fg="red")
                    e.grid(row=9,column=1,pady=25)
                elif "Out of range value" in error_string:
                    e=tk.Label(update_record_page,text="A data field is out of range",width=40,fg="red")
                    e.grid(row=9,column=1,pady=25)
                elif "Duplicate entry" in error_string:
                    e=tk.Label(update_record_page,text="Duplicate Entry",width=40,fg="red")
                    e.grid(row=9,column=1,pady=25)
               
            
    else:
        Show_tables = tk.Label(delete_record_page, text="Team does not exist",width=30)
        Show_tables.grid(row=0,column=0,pady=50)
        Exit_butt=tk.Button(update_record_page, text='Exit',width=30,bg='red',fg='white', command=lambda: my_update())
        Exit_butt.grid(row=1,column=0,pady=50)
        def my_update():
            update_record_page.destroy()
    update_record_page.mainloop()


def StartPage():

    global start_page
    start_page = tk.Toplevel()    
    start_page.configure(background='white')         
    start_page.geometry("300x300")
    start_page.title("Welcome")
    ipl_logo = requests.get("https://raw.githubusercontent.com/mvdmCricNews/REPO/main/Data/logo/IPL_MAIN_LOGO.png")
    # create an image file object
    my_picture = io.BytesIO(ipl_logo.content)
    # use PIL to open image formats like .jpg  .png  .gif  etc.
    pil_img = Image.open(my_picture)
    # convert to an image Tkinter can use
    tk_img = ImageTk.PhotoImage(pil_img)
    Start_butt=tk.Button(start_page, text='Start',image = tk_img ,bg='blue',fg='white', command=FrontPage)
    Start_butt.place(x=40,y=40)
    CreateToolTip(Start_butt, text = 'Click me to start the program')
    start_page.mainloop()

StartPage() 