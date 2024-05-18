import sqlalchemy as db
import phonenumbers





engine=db.create_engine("sqlite:///table.db")
cur=engine.connect()
metadata=db.MetaData()

users=db.Table("users", metadata,
               db.Column("id", db.Integer, primary_key=True),
               db.Column("tg_id", db.Integer),
               db.Column("Name", db.Text, default="-"),
               db.Column("Sname", db.Text, default="-"),
               db.Column("teg_t", db.Text, default="-"),
               db.Column("phone_nomber", db.Text, default="-")
               )
metadata.create_all(engine)




def reg_id(id):
    if []==((cur.execute(users.select().where(users.columns.tg_id==id))).fetchall()):
        cur.execute(users.insert().values([{"tg_id":id}]))
        cur.commit()




def reg_name(name, id, teg):
    cur.execute(users.update().values({"Name":name}).where(users.columns.tg_id==id))
    cur.commit()
    cur.execute(users.update().values({"teg_t":teg}).where(users.columns.tg_id==id))
    cur.commit()
    
    
    
def reg_sname(sname, id):
    cur.execute(users.update().values({"Sname":sname}).where(users.columns.tg_id == id))
    cur.commit()
    
    
def correct(phone):
    if phone == "-":
        return True
    else:
        try:
            phonenumbers.is_possible_number(phonenumbers.parse(phone))
            return True
        except:
            return False       



def reg_phone(phone, id):
    if phone == "-":
        cur.execute(users.update().values({"phone_nomber":phone}).where(users.columns.tg_id == id))
        cur.commit()
    else:
        try: 
            phonenumbers.is_possible_number(phonenumbers.parse(phone))
            cur.execute(users.update().values({"phone_nomber":phone}).where(users.columns.tg_id == id))
            cur.commit()
        except:
            pass

def table_users():
    b=""
    a = ((cur.execute(users.select())).fetchall())
    for i in range (len(a)):
        for y in range (6):
            if y == 0:
                b+="\n id в базе: "+str(a[i][0])+", "
            if y == 1:
                b+="id чата в телеграмм: "+str(a[i][1])+", "
            if y == 2:
                b+="Имя: "+str(a[i][2])+", "
            if y ==3:
                b+="Фамилия: "+str(a[i][3])+", "
            if y  == 4:
                b+="тег в телегамме: "+str(a[i][4])+", "
            if y == 5:
                b+="номер телефона: "+str(a[i][5])+";\n"
    return b
                
                
def profile(tg_id):
    return (cur.execute(users.select().where(users.columns.tg_id==tg_id))).fetchall()


def up(tg_id, teg_t):
    if (cur.execute(users.select().where(users.columns.teg_t==teg_t))).fetchall()==[]:
        cur.execute(users.update().values({"teg_t":teg_t}).where(users.columns.tg_id==tg_id))
        cur.commit()


                


#print((cur.execute(users.select())).fetchall())


