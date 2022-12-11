import sys
minn_enter = 'a'
try:
    import pyttsx3,webbrowser,smtplib,random,datetime,os
    import speech_recognition as sr
    import mysql.connector

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices)-1].id)

    def speak(audio):
        print('Tom : ' + audio)
        engine.say(audio)
        engine.runAndWait()

    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning!')

        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon!')

        if currentH >= 18 and currentH !=0:
            speak('Good Evening!')

    greetMe()

    def conn():
        conob=mysql.connector.connect(host='localhost',user='root',password='root',database='project')
        if conob.is_connected():
            speak('Database connection sucessful..')
            speak('I an ready and online!!!')
            cur=conob.cursor()
    conn()
            
    speak("Enter your username : ")
    username = str(input(">>>> "))
    speak("Enter your password : ")
    password = str(input(">>>>"))

    if username == '' or username == 'default':
        username ='your email'  #to send mail via this mail
    if password == '' or password == 'default':
        password ='your password' #email password



    speak('Hello sir, I am your digital assistant!!!!')
    speak('How may I help you ?')
    speak('I can be accessed in two ways : ')
    speak('1 -> Through voice command!')
    speak('2 -> Through typing')
    speak('To enable voice command say  : activate voice command')
    speak('To enable typing say  : activate typing')
    speak('Kindly note that i am a beta release')

    '''re = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        re.pause_threshold =  1
        audio = re.listen(source)
    try:
        queryte = re.recognize_google(audio, language='en-in')
        print('User: ' + queryte + '\n')
    except :
        speak('sorry sir! due to some error by default typing mode is activated ')
        queryte='text mode'
    if queryte =='1' or queryte == 'voice' or queryte == 'voice command' or queryte == 'activate voice command' or queryte == 'activate voice mode' :
        speak('sir you have chosen voice mode')
        def myCommand():
                r = sr.Recognizer()                                                                                   
                with sr.Microphone() as source:                                                                       
                    print("Listening...")
                    r.pause_threshold =  1
                    audio = r.listen(source)
                try:
                    query = r.recognize_google(audio, language='en-in')
                    print('User: ' + query + '\n')
                    return query
                except sr.UnknownValueError:
                    plzMsgs = ['Sorry sir! I didn\'t get that! Try typing the command!!','sorry sir i am unable to recognise your voice kindly try typing the command','sir plz type the command']
                    speak(random.choice(plzMsgs))
                    query = str(input('Command: '))
                    print('User: ' + query + '\n')
                    return query
                except  sr.RequestError:
                    onMsgs = ['sorry sir! i am not online now','sorry sir! i am unable to talk to the internet','sorry sir i and internet are\'t talking now',]
                    speak(random.choice(onMsgs))
                    sys.exit()
    else:
        speak('sir you have chosen text mode')
        def myCommand():
            query = str(input('Command: '))
            return query'''
    def myCommand():
        query = str(input('Command: '))
        return query

    def check():
        speak("ok connected")

    def disp_stu():
        q="select * from student;"
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def disp_lib():
        q="select * from library"
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def add_stu_det():
        speak("Enter student_name,student_id,class,roll_no : ")
        L=eval(input(">>> "))
        q="insert into student values('{}','{}','{}','{}')".\
        format(L[0],L[1],L[2],L[3])
        cur.execute(q)
        conob.commit()# to save the changes
    def search_in_stu_id():
        speak("Enter student_id : ")
        m=input(">>> ")
        q="select * from student where student_id='{}'".format(m)
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def search_in_stu_name():
        speak("Enter student name : ")
        m=input(">>> ")
        q="select * from student where student_name='{}'".format(m)
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def search_in_stu_class():
        speak("Enter class : ")
        m=input(">>> ")
        q="select * from student where class='{}'".format(m)
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def search_in_lib_id():
        speak('Enter Book_id : ')
        m=input(">>> ")
        q="select * from library where book_id='{}'".format(m)
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def search_in_lib_title():
        speak("Enter book_title : ")
        m=input(">>> ")
        q="select * from library where book_title='{}'".format(m)
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def search_in_lib_publisher():
        speak('Enter publiser : ')
        m=input(">>> ")
        q="select * from library where publiser='{}'".format(m)
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def search_in_lib_subj():
        speak("Enter subject : ")
        m=input(">>> ")
        q="select * from library where subject='{}'".format(m)
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            speak(i)
    def add_book():
        speak("Enter book_title,subject,book_id,publisher,price,edition : ")
        L=eval(input(">>> "))
        q="insert into library values('{}','{}','{}',{},{},'{}')".\
        format(L[0],L[1],L[2],L[3],L[4],L[5])
        cur.execute(q)
        conob.commit()# to save the changes
    def del_book():
        speak("enter book_id : ")
        RN=input(">>> ")
        q="DELETE FROM library WHERE book_id='{}'".\
        format(RN)
        cur.execute(q)
        conob.commit()
    def del_stu():
        speak("enter student id : ")
        RN=input(">>> ")
        q="DELETE FROM STUDENT WHERE student_id='{}'".\
        format(RN)
        cur.execute(q)
        conob.commit()
    def giv_book():
        speak('Enter name,student_id,book_id,class,roll_no,status : ')
        L=eval(input(">>> "))
        L.append('taken')
        q="insert into library_student(student_name,student_id,book_id,class,roll_no,status) values('{}','{}','{}','{}','{}','{}')".\
        format(L[0],L[1],L[2],L[3],L[4],L[5])
        cur.execute(q)
        conob.commit()# to save the changes
    def sub_book():
        speak("Enter book_id : ")
        L=eval(input(">>> "))
        L.append("deposited")
        q="UPDATE library_student SET status='{}' where book_id='{}'".\
        format(L[1],L[0])
        cur.execute(q)
        conob.commit()# to save the changes
    def update_book():
        speak('Enter previous book_id : ')
        m=input(">>> ")
        speak('Enter new details - book_title,book_id,publisher,price,edition : ')
        L=eval(input(">>> "))
        q="update library set book_title='{}',book_id='{}',publisher='{}',price='{}',edition='{}', where book_id='{}' ".\
        format(L[0],L[1],L[2],L[3],L[4],m)
        cur.execute(q)
        conob.commit()
    def update_stu():
        speak("Enter previous student_id : ")
        m=input('>>> ')
        L=eval(input("Enter name,student_id,class,roll_no, : "))
        q="update student set name='{}',student_id='{}',class='{}',roll_no='{}' where student_id='{}' ".\
        format(L[0],L[1],L[2],L[3],m)
        cur.execute(q)
        conob.commit()

    def con_close():
        conob.close()
    def init_screen():
        speak("**************************************")
        speak("*****Library Management*********")
        speak("Made by : Santosh Prajapati")

    def menu():
    
        speak("1 or Connection status")
        speak("2 or display all students")
        speak("3 or display all books in library")
        speak("4 or add new student")
        speak("5 or search for student by id")
        speak("6 or search for student by name")
        speak("7 or search for student by class")
        speak("8 or search for book by id")
        speak("9 or search for book by book title")
        speak("10 or search for bok by publisher")
        speak("11 or search for book by subject")
        speak('12 or add a book to library')
        speak("13 or remove a book from library")
        speak("14 or remove a sudent")
        speak("15 or give book")
        speak("16 or submit book")
        speak("17 or update book details")
        speak('18 or update student details')
        speak("19 or for closing program")
        speak("20 or for info about developer")



    if __name__ == '__main__':

        while True:
        
            query = myCommand()
            query = query.lower()
            
            if query == '':
                stMsgs = ['try that again!!','kindly repeat that again !!!','try again sir!!!','i don\'t understand that!!!!','please repeat that again!!!!']
                speak(random.choice(stMsgs))
            
            elif query == '1' or query=='one' or query=='check connection':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','checking connection']
                speak(random.choice(stMsgs))
                check()

            elif query == '2' or query=='two' or query=='display all students':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','displayng all students']
                speak(random.choice(stMsgs))
                disp_stu()

            elif query == '3' or query=='three' or query=='display all books in library':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','showing books','showing all books']
                speak(random.choice(stMsgs))
                disp_lib()

            elif query == '4' or query=='four' or query=='add new student':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','adding new data']
                speak(random.choice(stMsgs))
                add_stu_det()

            elif query == '5' or query=='five' or query=='search for student by id':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','searching student']
                speak(random.choice(stMsgs))
                search_in_stu_id()

            elif query == '6' or query=='six' or query=='search for student by name':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','searching for student']
                speak(random.choice(stMsgs))
                search_in_stu_name()

            elif query == '7' or query=='seven' or query=='searh for student by class':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','searching for student']
                speak(random.choice(stMsgs))
                search_in_stu_class()

            elif query == '8' or query=='eight' or query=='search for book by id':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','searching for book']
                speak(random.choice(stMsgs))
                search_in_lib_id()

            elif query == '9' or query=='nine' or query=='search for book by title':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','searching for book']
                speak(random.choice(stMsgs))
                search_in_lib_title()

            elif query == '10' or query=='ten' or query=='search for book by publisher':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','searchng for book']
                speak(random.choice(stMsgs))
                search_in_lib_publisher()
            
            elif query == '11' or query=='eleven' or query=='search for book by subject':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','searching for book']
                speak(random.choice(stMsgs))
                search_in_lib_subj()

            elif query == '12' or query=='twelve' or query=='add a book to library':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','adding book']
                speak(random.choice(stMsgs))
                add_book()

            elif query == '13' or query=='thirteen' or query=='remove a book from library':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','removing book']
                speak(random.choice(stMsgs))
                del_book()

            elif query == '14' or query=='fourteen' or query=='remove a student':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','removing a student']
                speak(random.choice(stMsgs))
                del_stu()

            elif query == '15' or query=='fifteen' or query=='give book':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','giving book']
                speak(random.choice(stMsgs))
                giv_book()

            elif query == '16' or query=='sixteen' or query=='submit book':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','submitting book']
                speak(random.choice(stMsgs))
                sub_book()

            elif query == '17' or query=='seventeen' or query=='update book details':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','update book details']
                speak(random.choice(stMsgs))
                update_book()

            elif query == '18' or query=='eighteen' or query=='update student details':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','updating details']
                speak(random.choice(stMsgs))
                update_stu()
            
            elif query == '19' or query=='nineteen' or query=='for closing program':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','closing program']
                speak(random.choice(stMsgs))
                con_close()
                sys.exit()

            elif query == '20' or query=='twenty' or query=='for info developer':
                stMsgs = ['ok processing ... your request ....','please wait... your request is being processed','ok','showing details']
                speak(random.choice(stMsgs))
                init_screen()

            elif query=='help' or query=='menu':
                stMsgs=['ok processing.....your request..... ',' please wait....your request is being processed','ok','showing details']
                speak(random.choice(stMsgs))
                menu()
                          
            
            elif query == 'hmm' or query == 'hm' or query == 'ouchh' :
                stMsgs = ['hmm','kindly elabrate!!','try that again!!']
                speak(random.choice(stMsgs))

            elif query == 'what is your name' or query == 'tell me your name' or query == 'your name please' :
                speak('my name is Tom sir')
                speak('i am your digital assistant')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))
            
            elif query == 'tell me about yourself' or query=='what can you do' or query == 'give me your intro' or query == 'tell me something about you' or query == 'who made you' or query == 'who is your creator' or query == 'who is your god':
                speak('my name is Tom sir')
                speak('i am your digital assistant')
                speak('i am under development by the Santosh Prajapti')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))

            elif query == 'Tom' or query == 'Tom are you online' or query == 'are you active now' or query == 'Tom are you ready' or query == 'Tom i need your help' or query == 'Tom can you help me':
                speak('yes sir')
                speak('i am ready and online now')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))

            elif query == 'where is your home' or query == 'where do you live' or query == 'your address please' or query == 'tell me your address' or query == 'tell me your address please': 
                stMsgs = ['thank you for asking such an intro','thank you sir for such question','i am glad to know that you want to know about me']
                speak(random.choice(stMsgs))
                speak('thank you for asking such a intro')
                speak('i am your digital assistant')
                speak('i am under development by the Santosh Prajapti')
                speak('currently i don\'n have any home')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))

            elif query == "what\'s up" or query == 'how are you' or query == 'what about you':
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy' , 'i am feeling chilled what about you sir']
                speak(random.choice(stMsgs))

            elif query == 'thanks' or query == 'thank you Tom' or query == 'thank you' or query == 'thank you for help' or query == 'thank you for doing my things' or query == 'thanks for help' :
                stMsgs = ['welcome sir','same to you sir','welcome to you sir']
                speak(random.choice(stMsgs))
                stMsgs = ['Just doing my things!','just doing my jobs sir', 'no need to say thanks sir', 'same to you sir', 'thank you sir i am nice and full of energy' , 'i am feeling chilled now sir what about you sir']
                speak(random.choice(stMsgs))
                
            elif query == 'thanks for help ' or query  == 'thanks you so much' or query == 'thank for all Tom' or query == 'thanks Tom' :
                stMsgs = ['welcome sir','same to you sir','welcome to you sir']
                speak(random.choice(stMsgs))
                stMsgs = ['Just doing my things!','just doing my jobs sir', 'no need to say thanks sir', 'same to you sir', 'thank you sir i am nice and full of energy' , 'i am feeling chilled now sir what about you sir']
                speak(random.choice(stMsgs))

            elif query == 'email' or query == 'send email' or query == 'send mail' :
                speak('Who is the recipient? ')
                recipient = myCommand()

                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)
                    server.sendmail(username, recipient+'@gmail.com', content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry sir! I am unable to send your message at this moment!')


            elif query =='nothing' or query == 'exit' or query == 'abort' or query == 'stop' or query == 'go away' or query == 'quit' or query == 'goodbye' :
                speak('okay')
                speak('Bye sir, have a good day.')
                sys.exit()
            

            elif query  == 'what is the time now' or query == 'tell me the time' or query == 'tell me system time' or query == 'time now':
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"sir, the time is {strTime}")
                
            
            elif query == 'hello' or query == 'hi' or query == 'hii' or query == 'hy' or query == 'hyy' :
                hiMsgs = ['hello','hii','hi','hy','hello sir']
                speak(random.choice(hiMsgs))

            elif 'bye' in query or 'byy' in query or query == 'by' :
                speak('Bye sir, have a good day.')
                sys.exit()

            elif query == 'contact your boss' or query == 'contact your developer' or query == 'contact your creator':
                speak('Ok processing ...... ')
                recipient = 'santosh52628'

                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)
                    server.sendmail(username, recipient+'@gmail.com', content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry sir! I am unable to send your message at this moment!')
            
            elif query == 'restart' or query == 'restart my PC' or query == 'please restart my PC' or query == 'please restart' or query == 'reboot' or query == 'reboot my PC ' or query == 'restart my computer' or query == 'reboot my computer':
                speak('Rebooting .....')
                os.system("shutdown -t 10 -r -f") 
                sys.exit()

            elif query == 'shutdown' or query == 'shutdown my PC' or query == 'please shutdown my PC' or query == 'please shutdown' or query == 'shutdown my computer' or query == 'shutdown my computer':
                speak('Shutting down ....')
                os.system("shutdown -t 10 -s -f")
                sys.exit()

            elif 'search for on google' in query or 'search on google for' in query :
                stMsgs = ['opening google','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                if 'search for on google ' in query :
                    query=query.replace("search for on google",'')
                elif 'search on google for' in query :
                    query = query.replace('search on google for','')
                webbrowser.open('https://www.google.com/search?q='+query)

            elif 'search for on youtube' in query :
                stMsgs = ['opening youtube','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                if 'search for on youtube ' in query :
                    query=query.replace("search for on youtube",'')
                elif 'search on youtube for' in query :
                    query = query.replace('search on youtube for','')
                    webbrowser.open('https://www.youtube.com/results?search_query='+query)
        

            else:
                query = query
                speak('Searching...')
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
            
                except:
                    webbrowser.open('https://www.google.com/search?q='+query)
            
            speak('Next Command! sir!')
            minn_enter = 'b'
except:
    if minn_enter == 'b':
        sys.exit()
    else:
        print('An error occurred kindly restart the program') 
        sy=input("Hit Enter to exit ")
        sys.exit()
