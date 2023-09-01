from random import randrange
print("lol")
import telebot
import time
from telebot import types

bot = telebot.TeleBot('5159287717:AAHrmd3FBEvwoBw-b2Etr0Mr_xpanXpUFQU')

#mafia - 1; doctor - 2; comisar - 3; butterfly - 4; no one - 0; 5 - Dead one
#butterfly mute
class game():
    pass
class member():
    pass
class rule():
    pass

r = rule()
# define role set
r.mafia = 2
r.doctor = 1
r.comisar = 1
r.butterfly = 1


me = member()
g = game()

g.newgamerequire = 0
g.game = 0
g.rolemode = 0
g.groupmessage = 0
g.dn = 0
g.n = 0
g.day = 1
g.commode = 0
g.votemode = 0
g.voteattempt = 1
g.startgamemode = 0
g.deletemessageid = {}

g.deletemessageidb = {}
g.deleteuseridb = {}

g.deletemessageidm = {}
g.deleteuseridm = {}

g.deletemessageidc = {}
g.deleteuseridc = {}

g.deletemessageidd = {}
g.deleteuseridd = {}

me.doctattemt = 0
me.butterchoice = -1
me.endrole = {}
me.vote = {}
me.maffid = {}
me.docid = {}
me.imaf = {}
me.idoc = {}
me.mchoice = {}
me.dchoice = {}
me.bchoice = -1
me.id = {}
me.message = {}
me.name = {}
me.role = {}
try:
    @bot.message_handler(commands=['start'])
    def start(message):
        print("start")
        @bot.message_handler(commands=['m'])
        def m(message1):
            if message1.chat.type == "group":
                if g.rolemode == 0:
                    num = message1.text.replace("/m ","")
                    if num.isdigit() == True:
                        r.mafia = int(num)
                    else:
                        bot.send_message(message1.chat.id,"Number is not integer")
                else:
                    bot.send_message(message1.chat.id, "Game is already started")
            else:
                bot.send_message(message1.chat.id,"It is not group chat")

        @bot.message_handler(commands=['d'])
        def d(message1):
            if message1.chat.type == "group":
                if g.rolemode == 0:
                    num = message1.text.replace("/d ", "")
                    if num.isdigit() == True:
                        r.doctor = int(num)
                    else:
                        bot.send_message(message1.chat.id, "Number is not integer")
                else:
                    bot.send_message(message1.chat.id, "Game is already started")
            else:
                bot.send_message(message1.chat.id, "It is not group chat")


        @bot.message_handler(commands=['c'])
        def c(message1):
            if message1.chat.type == "group":
                if g.rolemode == 0:
                    num = message1.text.replace("/c ", "")
                    if num.isdigit() == True:
                        if int(num) > 1:
                            bot.send_message(message1.chat.id, "Number is bigger than 1")
                        else:
                            r.comisar = int(num)
                    else:
                        bot.send_message(message1.chat.id, "Number is not integer")
                else:
                    bot.send_message(message1.chat.id, "Game is already started")
            else:
                bot.send_message(message1.chat.id, "It is not group chat")

        @bot.message_handler(commands=['b'])
        def b(message1):
            if message1.chat.type == "group":
                if g.rolemode == 0:
                    num = message1.text.replace("/b ", "")
                    if num.isdigit() == True:
                        if int(num) > 1:
                            bot.send_message(message1.chat.id, "Number is bigger than 1")
                        else:
                            r.butterfly = int(num)
                    else:
                        bot.send_message(message1.chat.id, "Number is not integer")
                else:
                    bot.send_message(message1.chat.id, "Game is already started")
            else:
                bot.send_message(message1.chat.id, "It is not group chat")

        @bot.message_handler(commands=['gameinfo'])
        def gameinfo(message1):
            print('g.game = ' + str(g.game))
            print("\ng.rolemode = " + str(g.rolemode))
            print('\ng.groupmessage = ' + str(g.groupmessage))
            print('\ng.dn = ' + str(g.dn))
            print('\ng.n = ' + str(g.n))
            print('\ng.day = ' + str(g.day))
            print('\ng.commode =' + str(g.commode))
            print('\ng.votemode = ' + str(g.votemode))
            print('\ng.voteattempt = ' + str(g.voteattempt))
            print('\ng.startgamemode = ' + str(g.startgamemode))
            print("\ng.deletemessageid = " + str(g.deletemessageid))

            print('\n\nme.doctattemt = ' + str(me.doctattemt))
            print('\nme.butterchoice = ' + str(me.butterchoice))
            print('\nme.endrole = ' + str(me.endrole))
            print('\nme.vote = ' + str(me.vote))
            print('\nme.maffid = ' + str(me.maffid))
            print('\nme.docid = ' + str(me.docid))
            print('\nme.imaf = ' + str(me.imaf))
            print('\nme.idoc = ' + str(me.idoc))
            print('\nme.mchoice = ' + str(me.mchoice))
            print('\nme.dchoice = ' + str(me.dchoice))
            print('\nme.bchoice = ' + str(me.bchoice))
            print('\nme.id = ' + str(me.id))
            print('\nme.message = ' + str(me.message))
            print('\nme.name = ' + str(me.name))
            print('\nme.role = ' + str(me.role))

        @bot.message_handler(commands=['info'])
        def info(message1):
            print("n = " + str(g.n))
            print("me.id = " + str(me.id))
            print("me.role = " + str(me.role))
            print("me.message = " + str(me.message))
            print("me.name = " + str(me.name))
            print("\nRole of members")
            print("mafia: "+str(r.mafia))
            print("doctor: "+str(r.doctor))
            print("comisar: "+str(r.comisar))
            print("butterfly: "+str(r.butterfly))
            name = ""
            for i in me.name:
                name = name + "\n" + me.name[i]
            bot.send_message(message1.chat.id, "mafia: "+str(r.mafia)+"\ndoctor: "+str(r.doctor)+"\ncomisar: "+str(r.comisar)+"\nbutterfly: "+str(r.butterfly)+"\n\n"+"Members:"+name)

        @bot.message_handler(commands=['changename'])
        def changename(message1):
            newname = message1.text.replace("/changename ", "")
            for i in me.id:
                if me.id[i] == message1.from_user.id:
                    me.name[i] = newname
                    bot.send_message(message1.chat.id,"Name changed to "+newname)

        @bot.message_handler(commands=['break'])
        def Break(message1):
            if message1.chat.type == "group":
                if g.dn == 1:
                    bot.send_message(g.groupmessage,"Game will be stopped but you have to wait litle bit")
                    g.game = 0
                    g.n = 0
                    g.startgamemode = 0
                    g.rolemode = 0
                    g.dn = 0
                    g.votemode = 0
                    time.sleep(20)
                else:
                    g.game = 0
                    g.n = 0
                    g.rolemode = 0
                    g.dn = 0
                    g.startgamemode = 0
                    g.votemode = 0
                bot.send_message(g.groupmessage,"Game is stopped")

        @bot.message_handler(commands=['deleteid'])
        def deleteid(message1):
            if g.rolemode == 0:
                me.id = {}
                me.name = {}
                me.message = {}
                g.n = 0
                bot.send_message(g.groupmessage, "ID is deleted")
            else:
                bot.send_message(g.groupmessage,"You can use this comand only when role is not given")


        @bot.message_handler(commands=['get'])
        def get(message1):
            unic = 1
            if message1.chat.type == "private":
                if g.rolemode == 1:
                    bot.send_message(message1.chat.id,"Game is started\nYou are late")
                else:
                    for check in me.id:
                        if me.id[check] == message1.from_user.id:
                            unic = 0
                            break
                    if unic == 1:
                        me.id[g.n] = message1.from_user.id
                        me.message[g.n] = message1.chat.id
                        me.name[g.n] = message1.from_user.first_name
                        g.n = g.n + 1
                        bot.send_message(message1.chat.id, "Your id is saved. \nID: "+str(message1.from_user.id))
            else:
                bot.send_message(message1.chat.id, "It is not private chat")

        @bot.message_handler(commands=['myrole'])
        def myrole(message1):
            if message1.chat.type == 'private':
                for i in me.id:
                    if (me.id[i] == message1.from_user.id) and (g.rolemode == 1):
                        if me.role[i] == 0:
                            bot.send_message(message1.chat.id,"Citizen")
                        elif me.role[i] == 1:
                            bot.send_message(message1.chat.id, "Maffia")
                        elif me.role[i] == 2:
                            bot.send_message(message1.chat.id, "Docttor")
                        elif me.role[i] == 3:
                            bot.send_message(message1.chat.id, "Comissar")
                        elif me.role[i] == 4:
                            bot.send_message(message1.chat.id, "Butterfly")
                        elif me.role[i] == 5:
                            bot.send_message(message1.chat.id, "Dead one")
                        else:
                            bot.send_message(message1.chat.id, "Я хз хто ти такий.\nЯк ти сюда попав?!!?")
                    elif g.rolemode == 0:
                        bot.send_message(message1.chat.id,"You have no role yet")
                        break
            else:
                bot.send_message(message1.chat.id,"It is not private chat")

        @bot.message_handler(commands=['role'])
        def role(message1):
            g.groupmessage = message1.chat.id
            if g.rolemode == 0:
                if message1.chat.type == "group":
                    if len(me.id)<(r.mafia+r.doctor+r.comisar+r.butterfly):
                        bot.send_message(message1.chat.id, "Too few players")
                        g.rolemode = 0
                        g.newgamerequire = 1
                        g.startgamemode = 0
                    else:
                        if (r.mafia == 0) and (r.comisar == 0) and (r.doctor == 0) and (r.butterfly == 0):
                            bot.send_message(g.groupmessage,"You can not give role when m = 0 and d = 0 and c = 0 and b = 0")
                            g.newgamerequire = 1
                            g.startgamemode = 0
                        else:
                            g.rolemode = 1
                            #Присвоюєм 0
                            for i in range(len(me.id)):
                                me.role[i] = 0
                                me.endrole[i] = 0
                            #Визначаєм Мафію
                            if r.mafia != 0:
                                for i in (range(r.mafia)):
                                    rand = randrange(len(me.id))
                                    if me.role[rand] == 0:
                                        me.role[rand] = 1
                                        me.endrole[rand] = 1
                                        bot.send_message(me.message[rand], "Maffia")
                                    else:
                                        for j in range(len(me.id)):
                                            if rand < len(me.id)-1:
                                                rand = rand + 1
                                            else:
                                                rand = 0
                                            if me.role[rand] == 0:
                                                me.role[rand] = 1
                                                me.endrole[rand] = 1
                                                bot.send_message(me.message[rand],"Maffia")
                                                break
                            else:
                                print("Not mafia")

                            #Визначаєм доктор
                            if r.doctor != 0:
                                for i in (range(r.doctor)):
                                    rand = randrange(len(me.id))
                                    if me.role[rand] == 0:
                                        me.role[rand] = 2
                                        me.endrole[rand] = 2
                                        bot.send_message(me.message[rand], "Docttor")
                                    else:
                                        for j in range(len(me.id)):
                                            if rand < len(me.id)-1:
                                                rand = rand + 1
                                            else:
                                                rand = 0
                                            if me.role[rand] == 0:
                                                me.role[rand] = 2
                                                me.endrole[rand] = 2
                                                bot.send_message(me.message[rand],"Docttor")
                                                break
                            else:
                                print("Not doctor")

                            # Визначаєм комісар
                            if r.comisar != 0:
                                for i in (range(r.comisar)):
                                    rand = randrange(len(me.id))
                                    if me.role[rand] == 0:
                                        me.role[rand] = 3
                                        me.endrole[rand] = 3
                                        bot.send_message(me.message[rand], "Comisarr")
                                    else:
                                        for j in range(len(me.id)):
                                            if rand < len(me.id)-1:
                                                rand = rand + 1
                                            else:
                                                rand = 0
                                            if me.role[rand] == 0:
                                                me.role[rand] = 3
                                                me.endrole[rand] = 3
                                                bot.send_message(me.message[rand],"Comisarr")
                                                break
                            else:
                                print("Not comisar")

                            #Визнааєм бАбочку
                            if r.butterfly != 0:
                                for i in (range(r.butterfly)):
                                    rand = randrange(len(me.id))
                                    if me.role[rand] == 0:
                                        me.role[rand] = 4
                                        me.endrole[rand] = 4
                                        bot.send_message(me.message[rand], "Butterfly")
                                    else:
                                        for j in range(len(me.id)):
                                            if rand < len(me.id) - 1:
                                                rand = rand + 1
                                            else:
                                                rand = 0
                                            if me.role[rand] == 0:
                                                me.role[rand] = 4
                                                me.endrole[rand] = 4
                                                bot.send_message(me.message[rand], "Butterfly")
                                                break
                            else:
                                print("Not butterfly")

                            for i in me.role:
                                if me.role[i] == 0:
                                    bot.send_message(me.message[i],"Citizen")

                else:
                    bot.send_message(message1.chat.id, "It is not group chat")
            else:
                bot.send_message(message1.chat.id, "All roles is already given")


        @bot.message_handler(commands=['day'])
        def day(message1):
            if message1.chat.type == 'group':
                if g.rolemode == 0:
                    bot.send_message(message1.chat.id,"Role is not given")
                else:
                    if (g.commode == 0) and (g.game == 1):
                        bot.send_message(g.groupmessage,"Day " + str(g.day))

                        me.bchoice = -1
                        me.mchoice = {}
                        me.dchoice = {}
                        me.idoc = {}
                        me.imaf = {}

                        g.deletemessageidm = {}
                        g.deleteuseridm = {}
                        g.deletemessageidd = {}
                        g.deleteuseridd = {}

                        g.commode = 1
                        g.voteattempt = 0

                        countmaf = 0
                        countdoctor = 0
                        countdead = 0

                        for i in me.role:
                            if me.role[i] == 1:
                                me.imaf[countmaf] = i
                                countmaf = countmaf + 1
                            elif me.role[i] == 2:
                                me.idoc[countdoctor] = i
                                countdoctor = countdoctor + 1
                            elif me.role[i] == 5:
                                countdead = countdead + 1

                        if countmaf >= (len(me.id) - countdead - countmaf):
                            bot.send_message(g.groupmessage,"Game is over\nMaffia won")
                            me.role = {}
                            g.newgamerequire = 1
                            g.startgamemode = 0
                            g.rolemode = 0
                            g.day = 1
                            g.dn = 0
                            g.commode = 0
                            g.votemode = 0
                            g.voteattempt = 1
                            me.dchoice = {}
                            me.mchoice = {}
                            me.vote = {}
                            endmessage = "Roles of all players:\n"
                            for i in me.id:
                                if me.endrole[i] == 0:
                                    endmessage = endmessage + me.name[i] + " Citizen\n"
                                elif me.endrole[i] == 1:
                                    endmessage = endmessage + me.name[i] + " Maffia\n"
                                elif me.endrole[i] == 2:
                                    endmessage = endmessage + me.name[i] + " Docttor\n"
                                elif me.endrole[i] == 3:
                                    endmessage = endmessage + me.name[i] + " Comisar\n"
                                elif me.endrole[i] == 4:
                                    endmessage = endmessage + me.name[i] + " Butterfly\n"
                            bot.send_message(g.groupmessage,endmessage)
                        elif countmaf == 0:
                            bot.send_message(g.groupmessage,"Game is over\nMaffia is defeated")
                            me.role = {}
                            g.newgamerequire = 1
                            g.startgamemode = 0
                            g.rolemode = 0
                            g.day = 1
                            g.dn = 0
                            g.commode = 0
                            g.votemode = 0
                            g.voteattempt = 1
                            me.dchoice = {}
                            me.mchoice = {}
                            me.vote = {}
                            endmessage = "Roles of all players:\n"
                            for i in me.endrole:
                                if me.endrole[i] == 0:
                                    endmessage = endmessage + me.name[i] + " Citizen\n"
                                elif me.endrole[i] == 1:
                                    endmessage = endmessage + me.name[i] + " Maffia\n"
                                elif me.endrole[i] == 2:
                                    endmessage = endmessage + me.name[i] + " Docttor\n"
                                elif me.endrole[i] == 3:
                                    endmessage = endmessage + me.name[i] + " Comisar\n"
                                elif me.endrole[i] == 4:
                                    endmessage = endmessage + me.name[i] + " Butterfly\n"
                            bot.send_message(g.groupmessage, endmessage)
                        else:
                            nameofmaff = ""
                            nameofdoct = ""

                            for i in me.imaf:
                                num = me.imaf[i]
                                na = me.name[num]
                                nameofmaff = nameofmaff + "\n" + na
                            for i in me.idoc:
                                num = me.idoc[i]
                                na = me.name[num]
                                nameofdoct = nameofdoct + "\n" + na

                            bot.send_message(g.groupmessage, "Night\nSleep tight")

                            videosunset = open('venv/Video/night.gif', 'rb')
                            bot.send_animation(g.groupmessage, videosunset)
                            videosunset.close()

                            for i in me.id:
                                if me.role[i] == 3:
                                    icom = i
                                    break

                            for i in me.id:
                                if me.role[i] == 4:
                                    ibuu = i
                                    break

                            butteralive = 0
                            for i in me.id:
                                if me.role[i] == 4:
                                    butteralive =butteralive + 1
                            if butteralive != 0:
                                markupb = types.InlineKeyboardMarkup(row_width=4)
                                for j in me.id:
                                    if (me.role[j] != 4) and (me.role[j] != 5):
                                        item1 = types.InlineKeyboardButton(text=me.name[j], callback_data=me.id[j])
                                        markupb.add(item1)
                                buttermessage = bot.send_message(me.message[ibuu], "Choose your lucky victime", reply_markup=markupb)
                                deletebuttermessageid = buttermessage.message_id

                                #/////////////////////////////////////////////////////////////////////////////////////////////////////

                            markupc = types.InlineKeyboardMarkup(row_width=4)
                            comicaralive = 0
                            for i in me.id:
                                if me.role[i] == 3:
                                    comicaralive = comicaralive + 1
                            if (comicaralive != 0) and (g.day != 1):
                                for j in me.id:
                                    if (me.role[j] != 3) and (me.role[j] != 5):
                                        item1 = types.InlineKeyboardButton(text=me.name[j], callback_data=me.id[j])
                                        markupc.add(item1)
                                commessage = bot.send_message(me.message[icom], "Check someone",reply_markup=markupc)
                                deletecommessageid = commessage.message_id


                            for i in me.imaf:
                                bot.send_message(me.message[me.imaf[i]],"Your Maffiamate is:" + nameofmaff)
                                markup = types.InlineKeyboardMarkup(row_width=4)
                                for j in me.id:
                                    if (me.role[j] != 5) and (me.role[j] != 1):
                                        item1 = types.InlineKeyboardButton(text = me.name[j],callback_data = me.id[j])
                                        markup.add(item1)
                                mafmessage = bot.send_message(me.message[me.imaf[i]], "City sleeps but you are awake\nChoose your victim", reply_markup=markup)
                                g.deleteuseridm[len(g.deleteuseridm)] = me.message[me.imaf[i]]
                                g.deletemessageidm[len(g.deletemessageidm)] = mafmessage.message_id

                            for i in me.idoc:
                                bot.send_message(me.message[me.idoc[i]],"Your Docttormate is:" + nameofdoct)
                                markupd = types.InlineKeyboardMarkup(row_width=4)
                                for j in range(len(me.id)):
                                    if (me.role[j] != 5) and (me.role[j] != 2 or me.doctattemt != 1):
                                        item1 = types.InlineKeyboardButton(text = me.name[j],callback_data = me.id[j])
                                        markupd.add(item1)
                                docmessage = bot.send_message(me.message[me.idoc[i]], "It is a good time to save someone\nChoose the one you want to cure", reply_markup=markupd)
                                g.deleteuseridd[len(g.deleteuseridd)] = me.message[me.idoc[i]]
                                g.deletemessageidd[len(g.deletemessageidd)] = docmessage.message_id
                            # Початок ночі
                            g.dn = 1
                            for i in me.imaf:
                                me.maffid[i] = me.id[me.imaf[i]]
                            for i in me.idoc:
                                me.docid[i] = me.id[me.idoc[i]]
                            time.sleep(25)
                            # Кінець ночі
                            g.dn = 0
                            if g.game == 1:
                                g.commode = 0

                                for i in me.imaf:
                                    bot.send_message(me.message[me.imaf[i]], "Night is over\nWork is done")

                                bot.send_message(g.groupmessage, "Night is over")
                                #ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
                                try:
                                    bot.delete_message(me.message[ibuu],deletebuttermessageid)
                                except:
                                    print("Butterfly message is not found")
                                try:
                                    bot.delete_message(me.message[icom],deletecommessageid)
                                except:
                                    print("Comisarr message is not found")

                                for i in g.deleteuseridm:
                                    try:
                                        bot.delete_message(g.deleteuseridm[i],g.deletemessageidm[i])
                                    except:
                                        print("Maffia message is not found")

                                for i in g.deleteuseridd:
                                    try:
                                        bot.delete_message(g.deleteuseridd[i],g.deletemessageidd[i])
                                    except:
                                        print("Docttor message is not found")

                                videosunrise = open('venv/Video/day.gif', 'rb')
                                bot.send_animation(g.groupmessage, videosunrise)
                                videosunrise.close()

                                killed = -2
                                cured = -2
                                dnumofvotes = 0
                                mnumofvotes = 0
                                mvotes = {}
                                dvotes = {}
                                for j in me.id:
                                    for q in me.mchoice:
                                        if me.mchoice[q] == j:
                                            mnumofvotes = mnumofvotes + 1
                                            killed = j

                                    for q in me.dchoice:
                                        if me.dchoice[q] == j:
                                            dnumofvotes = dnumofvotes + 1
                                            cured = j

                                    mvotes[j] = mnumofvotes
                                    dvotes[j] = dnumofvotes
                                    mnumofvotes = 0
                                    dnumofvotes = 0
                                mmaxvote = 0
                                dmaxvote = 0

                                for j in mvotes:
                                    if mvotes[j] > mmaxvote:
                                        mmaxvote = mvotes[j]

                                for j in dvotes:
                                    if dvotes[j] > dmaxvote:
                                        dmaxvote = dvotes[j]

                                mnumofmax = 0
                                dnumofmax = 0
                                for j in mvotes:
                                    if mvotes[j] == mmaxvote:
                                        mnumofmax = mnumofmax + 1

                                for j in dvotes:
                                    if dvotes[j] == dmaxvote:
                                        dnumofmax = dnumofmax + 1

                                if cured != -2:
                                    if (me.role[cured] == 2) and (me.doctattemt == 0):
                                        me.doctattemt = 1
                                    elif (me.role[cured] == 2) and (me.doctattemt == 1):
                                        me.doctattemt = 2
                                    elif (me.role[cured] != 2) and (me.doctattemt == 1):
                                        me.doctattemt = 0
                                    elif me.doctattemt == 2:
                                        me.doctattemt = 0
                                else:
                                    if me.doctattemt == 1:
                                        me.doctattemt = 0
                                    elif me.doctattemt == 2:
                                        me.doctattemt = 0

                                if r.butterfly != 0:
                                    if me.bchoice == -1:
                                        bot.send_message(g.groupmessage,"Butterfly was quiet this night")
                                    else:
                                        bot.send_message(g.groupmessage,"Butterfly visited " + me.name[me.bchoice] + " this night")

                                if (killed == -1) or (killed == -2) or (mnumofmax > 1) or ((cured == killed) and (me.doctattemt != 2)):
                                    bot.send_message(g.groupmessage,"No one was killed")
                                else:
                                    bot.send_message(g.groupmessage,me.name[killed]+" is murdered")
                                    me.role[killed] = 5
                                g.day = g.day + 1
                    else:
                        bot.send_message(g.groupmessage,"You can not start new day at night")
            else:
                bot.send_message(message1.chat.id,"It is not group chat")

        @bot.message_handler(commands=['vote'])
        def vote(message1):
            if message1.chat.type == "group":
                if g.rolemode == 0:
                    bot.send_message(message1.chat.id,"Role is not given")
                else:
                    if g.dn == 1:
                        for i in me.id:
                            if me.id[i] == message1.from_user.id:
                                myi = i
                                break
                        if me.role[myi] == 5:
                            bot.send_message(message1.chat.id, "You are dead")
                        else:
                            bot.send_message(g.groupmessage,"You can not vote at night")
                    else:
                        if g.voteattempt == 0:
                            myi = -1
                            for i in me.id:
                                if me.id[i] == message1.from_user.id:
                                    myi = i
                                    break
                            if myi != -1:
                                if g.game == 1:
                                    g.deletemessageid = {}
                                    g.votemode = 1
                                    votemarkup = types.InlineKeyboardMarkup(row_width=4)
                                    for i in me.id:
                                        if me.role[i] != 5:
                                            item1 = types.InlineKeyboardButton(text=me.name[i], callback_data=me.id[i])
                                            votemarkup.add(item1)
                                    item1 = types.InlineKeyboardButton(text="Vote for no one", callback_data="nobody")
                                    votemarkup.add(item1)
                                    votemessage = bot.send_message(g.groupmessage,"Vote for the the one you want to vote out",reply_markup=votemarkup)
                                    g.deletemessageid[len(g.deletemessageid)] = votemessage.message_id

                                #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                for i in me.id:
                                    if me.role[i] == 5:
                                        me.vote[i] = None
                                    elif i == me.bchoice:
                                        me.vote[i] = None
                                    else:
                                        me.vote[i] = -1

                                endvote = 0
                                while endvote == 0:
                                    endvote = 1
                                    for i in me.vote:
                                        if me.vote[i] == -1:
                                            endvote = 0
                                    if g.game == 0:
                                        break

                                #//////////////////////////////////////////////////////////////////////
                                if g.game == 1:
                                    voteout = {}
                                    for i in me.id:
                                        voteout[i] = 0

                                    print("StartVoteout = " + str(voteout))
                                    #///////////////////////////////////////////////////////////////////////////////////////////////

                                    print("me.vote = " + str(me.vote))

                                    for i in me.vote:
                                        if me.vote[i] != None:
                                            print("me.vote = " + str(me.vote[i]))
                                            voteout[me.vote[i]] = voteout[me.vote[i]] + 1

                                    print("Voteout = " + str(voteout))

                                    vmax = 0
                                    imax = -1
                                    for i in voteout:
                                        if voteout[i] > vmax:
                                            vmax = voteout[i]
                                            imax = i

                                    numofmaxv = 0
                                    for i in voteout:
                                        if voteout[i] == vmax:
                                            numofmaxv = numofmaxv + 1
                                    if numofmaxv > 1:
                                        bot.send_message(g.groupmessage,"No one was voted out")
                                    elif imax != -1:
                                        bot.send_message(g.groupmessage,me.name[imax] + " is voted out")
                                        me.role[imax] = 5
                                    g.voteattempt = 1
                                    g.votemode = 0

                                    try:
                                        for i in g.deletemessageid:
                                            try:
                                                bot.delete_message(g.groupmessage, g.deletemessageid[i])
                                            except:
                                                print("Group message is not found")
                                    except:
                                        print("ERROR, unable to delete message")
                        else:
                            if g.day == 1:
                                bot.send_message(g.groupmessage,"You can not vote at first day")
                            else:
                                bot.send_message(g.groupmessage,"You can only vote once")
                        g.votemode = 0
            else:
                bot.send_message(message1.from_user.id,"It is not group chat")

        @bot.message_handler(commands=['startgame'])
        def startgame(message1):
            if message1.chat.type == "group":
                if g.dn == 0:
                    if g.votemode == 0:
                        if (g.startgamemode == 0):
                            g.startgamemode = 1
                            if (g.day == 1) and (g.game == 0):
                                g.game = 1
                                g.commode = 0
                                g.voteattempt = 1
                                me.doctattemt = 0
                                me.butterchoice = -1
                                me.endrole = {}
                                me.maffid = {}
                                me.docid = {}
                                me.imaf = {}
                                me.idoc = {}
                                me.mchoice = {}
                                me.dchoice = {}
                                me.bchoice = -1
                                me.role = {}
                            if g.game == 0:
                                g.day = 1
                                g.commode = 0
                                g.voteattempt = 1
                                me.doctattemt = 0
                                me.butterchoice = -1
                                me.endrole = {}
                                me.maffid = {}
                                me.docid = {}
                                me.imaf = {}
                                me.idoc = {}
                                me.mchoice = {}
                                me.dchoice = {}
                                me.bchoice = -1
                                me.role = {}
                            me.vote = {}
                            if (g.game == 1) and (g.day == 1):
                                role(message1)
                            if g.game == 1:
                                day(message1)
                            if g.newgamerequire == 1:
                                g.newgamerequire = 0
                                me.doctattemt = 0
                                print("Game is over")
                            else:
                                if g.game == 1:
                                    vote(message1)
                                if g.game == 1:
                                    g.startgamemode = 0
                                    startgame(message1)
                    else:
                        bot.send_message(g.groupmessage,"You can not start game when voting is on")
                else:
                    bot.send_message(g.groupmessage,"You can not start game at night")
            else:
                bot.send_message(message1.chat.id,"This is not group chat")

        @bot.callback_query_handler(func=lambda message: True)
        def q(call):
            if call.data == "nobody":
                ingamecheck = 0
                for i in me.id:
                    if me.id[i] == call.from_user.id:
                        ingamecheck = 1
                        break
                if ingamecheck == 1:
                    for i in me.id:
                        if me.id[i] == call.from_user.id:
                            myi = i
                            break
                    if me.bchoice == myi:
                        bot.send_message(g.groupmessage,me.name[myi] + " you are muted. You can not vote")
                    else:
                        if me.role[myi] == 5:
                            bot.send_message(g.groupmessage,"You are dead")
                        else:
                            if g.dn == 1:
                                if g.votemode != 1:
                                    if call.message.chat.type == "private":
                                        print("private")
                                    else:
                                        print("group")
                                else:
                                    bot.send_message(g.groupmessage,"You can vote only when voting is on")
                            else:
                                print("day")
                                if g.votemode == 1:
                                    votemessage2 = bot.send_message(g.groupmessage,me.name[myi] + " votes for no one")
                                    g.deletemessageid[len(g.deletemessageid)] = votemessage2.message_id
                                    me.vote[myi] = None
                                    print("voting")
                else:
                    bot.send_message(call.message.from_user.id,"You are not in game")
            else:
                ingamecheck = 0
                victemeingamecheck = 0
                for i in me.id:
                    if me.id[i] == call.from_user.id:
                        ingamecheck = 1
                        break

                for i in me.id:
                    if me.id[i] == int(call.data):
                        victemeingamecheck = 1
                        break
                if (ingamecheck == 1) and (victemeingamecheck == 1):
                    if g.dn == 1:
                        if g.votemode == 1:
                            pass
                        else:
                            if call.message.chat.type == "private":
                                for i in me.id:
                                    if me.id[i] == call.from_user.id:
                                        myi = i
                                        break
                                for i in me.id:
                                    if me.id[i] == int(call.data):
                                        victemi = i
                                        break
                                if me.role[myi] != 5:
                                    if me.role[myi] == 1:
                                        me.mchoice[myi] = victemi
                                        if me.role[victemi] == 5:
                                            bot.send_message(me.message[myi],"He/She is dead")
                                        if me.role[victemi] == 1:
                                            bot.send_message(me.message[myi], "He/She is Maffia")
                                        for i in me.imaf:
                                            bot.send_message(me.message[me.imaf[i]],str(me.name[myi]) + " chose to kill " + str(me.name[victemi]))
                                    elif me.role[myi] == 2:
                                        me.dchoice[myi] = victemi
                                        if me.role[victemi] == 5:
                                            bot.send_message(me.message[myi],"He/She is dead")
                                        #///////////////////////////////////////////////////////////////////////////////////
                                        if me.doctattemt != 2:
                                            for i in me.idoc:
                                                bot.send_message(me.message[me.idoc[i]],str(me.name[myi]) + " chose to cure " + str(me.name[victemi]))
                                        else:
                                            bot.send_message(me.message[myi],"You can not cure docttor twice in a row")

                                    elif me.role[myi] == 3:
                                        if (g.commode == 1) and (r.comisar != 0) and (g.day != 1):
                                            g.commode = 0
                                            nameofvictime = "???"
                                            if me.role[victemi] == 0:
                                                nameofvictime = "Citizen"
                                            elif me.role[victemi] == 1:
                                                nameofvictime = "Maffia"
                                            elif me.role[victemi] == 2:
                                                nameofvictime = "Doctor"
                                            elif me.role[victemi] == 3:
                                                nameofvictime = "dumbass \nYou chose yourself"
                                                g.commode = 1
                                            elif me.role[victemi] == 4:
                                                nameofvictime = "Butterfly"
                                            elif me.role[victemi] == 5:
                                                nameofvictime = "Dead"
                                            bot.send_message(me.message[myi],"Role of " + me.name[victemi] + " is " + nameofvictime)
                                    elif me.role[myi] == 4:
                                        me.bchoice = victemi
                                        bot.send_message(me.message[myi],"You want to visit " + me.name[victemi] + " this night")
                                else:
                                    bot.send_message(call.from_user.id,"You are dead")
                    else:
                        myi = -1
                        for i in me.id:
                            if me.id[i] == call.from_user.id:
                                myi = i
                                break
                        if myi < len(me.role):
                            print("That's could be the ERROR!!!!!!!")

                        if (myi != -1) and (myi < len(me.role)):
                            #//////////////////////////////////////////////////////ERROR
                            if me.role[myi] != 5:
                                for i in me.id:
                                    if me.id[i] == int(call.data):
                                        victemi = i
                                        break

                                if g.votemode == 1:
                                    if me.role[victemi] != 5:
                                        if me.role[myi] != 5:
                                            print("VOTING")
                                            if myi != me.bchoice:
                                                if call.message.chat.type == "group":
                                                    me.vote[myi] = victemi
                                                    votemessage = bot.send_message(g.groupmessage,me.name[myi] + " votes for " + me.name[victemi])
                                                    g.deletemessageid[len(g.deletemessageid)] = votemessage.message_id
                                                else:
                                                    bot.send_message(call.message.from_user.id,"Vote in the group chat")
                                            else:
                                                votemessage1 = bot.send_message(g.groupmessage,me.name[myi] + " you are muted. You can not vote")
                                                g.deletemessageid[len(g.deletemessageid)] = votemessage1.message_id
                                        else:
                                            bot.send_message(g.groupmessage,me.name[myi] + " you are dead. You can not vote")
                                else:
                                    if call.message.chat.type == "private":
                                        if g.rolemode == 0:
                                            bot.send_message(call.from_user.id, "You can vote only after role is given")
                                        else:
                                            bot.send_message(call.from_user.id,"You can vote only at night")
                                    else:
                                        if g.rolemode == 0:
                                            bot.send_message(g.groupmessage, "You can vote only after role is given")
                                        else:
                                            bot.send_message(g.groupmessage,"You can vote only when voting is on")
                            else:
                                print("lol")
                                bot.send_message(call.from_user.id,"You are dead")
                else:
                    if call.message.chat.type == "private":
                        if ingamecheck == 0:
                            bot.send_message(call.from_user.id,"You are not in game")
                        if victemeingamecheck == 0:
                            bot.send_message(call.from_user.id, "This player is not in game")
                    else:
                        bot.send_message(g.groupmessage, "You are not in game")
except:
    try:
        bot.send_message(g.groupmessage,"Game is brocken\nTry use /start to start again")
    except:
        pass
    r.mafia = 2
    r.doctor = 1
    r.comisar = 1
    r.butterfly = 1

    me = member()
    g = game()

    g.newgamerequire = 0
    g.game = 0
    g.rolemode = 0
    g.groupmessage = 0
    g.dn = 0
    g.n = 0
    g.day = 1
    g.commode = 0
    g.votemode = 0
    g.voteattempt = 1
    g.startgamemode = 0
    g.deletemessageid = {}

    g.deletemessageidb = {}
    g.deleteuseridb = {}

    g.deletemessageidm = {}
    g.deleteuseridm = {}

    g.deletemessageidc = {}
    g.deleteuseridc = {}

    g.deletemessageidd = {}
    g.deleteuseridd = {}

    me.doctattemt = 0
    me.butterchoice = -1
    me.endrole = {}
    me.vote = {}
    me.maffid = {}
    me.docid = {}
    me.imaf = {}
    me.idoc = {}
    me.mchoice = {}
    me.dchoice = {}
    me.bchoice = -1
    me.id = {}
    me.message = {}
    me.name = {}
    me.role = {}

bot.polling(none_stop=True)
