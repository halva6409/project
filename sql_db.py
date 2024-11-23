import sqlite3
#import main
import config
con = sqlite3.connect(config.database)

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nine_monday(number, lesson , office, start_lesson, finish_lesson, change)")
cur.execute('''INSERT INTO nine_monday VALUES
                ( 1, '' , '' , '8:00'  , '8:45'  , '10min' ),
                ( 2, '' , '' , '8:55'  , '9:40'  , '20min' ),
                ( 3, '' , '' , '10:00' , '10;45' , '20min' ),
                ( 4, '' , '' , '11:05' , '11:50' , '10min' ),
                ( 5, '' , '' , '12:00' , '12:45' , '10min' ),
                ( 6, '' , '' , '12:55' , '13:40' , '10min' ),
                ( 7, '' , '' , '13:50' , '14:35' , '10min' ),
                ( 8, '' , '' , '14:45' , '15:30' , 'go home' )
            
            
            
        ''')
con.commit()


cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nine_tuesday(number, lesson , office, start_lesson, finish_lesson, change)")
cur.execute('''INSERT INTO nine_tuesday VALUES
                ( 1, '' , '' , '8:00'  , '8:45'  , '10min' ),
                ( 2, '' , '' , '8:55'  , '9:40'  , '20min' ),
                ( 3, '' , '' , '10:00' , '10;45' , '20min' ),
                ( 4, '' , '' , '11:05' , '11:50' , '10min' ),
                ( 5, '' , '' , '12:00' , '12:45' , '10min' ),
                ( 6, '' , '' , '12:55' , '13:40' , '10min' ),
                ( 7, '' , '' , '13:50' , '14:35' , '10min' ),
                ( 8, '' , '' , '14:45' , '15:30' , 'go home' )
            
            
            
        ''')
con.commit()

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nine_wednesday(number, lesson , office, start_lesson, finish_lesson, change)")
cur.execute('''INSERT INTO nine_wednesday VALUES
                ( 1, '' , '' , '8:00'  , '8:45'  , '10min' ),
                ( 2, '' , '' , '8:55'  , '9:40'  , '20min' ),
                ( 3, '' , '' , '10:00' , '10;45' , '20min' ),
                ( 4, '' , '' , '11:05' , '11:50' , '10min' ),
                ( 5, '' , '' , '12:00' , '12:45' , '10min' ),
                ( 6, '' , '' , '12:55' , '13:40' , '10min' ),
                ( 7, '' , '' , '13:50' , '14:35' , '10min' ),
                ( 8, '' , '' , '14:45' , '15:30' , 'go home' )
            
            
            
        ''')
con.commit()


cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nine_thursday(number, lesson , office, start_lesson, finish_lesson, change)")
cur.execute('''INSERT INTO nine_thursday VALUES
                ( 1, '' , '' , '8:00'  , '8:45'  , '10min' ),
                ( 2, '' , '' , '8:55'  , '9:40'  , '20min' ),
                ( 3, '' , '' , '10:00' , '10;45' , '20min' ),
                ( 4, '' , '' , '11:05' , '11:50' , '10min' ),
                ( 5, '' , '' , '12:00' , '12:45' , '10min' ),
                ( 6, '' , '' , '12:55' , '13:40' , '10min' ),
                ( 7, '' , '' , '13:50' , '14:35' , '10min' ),
                ( 8, '' , '' , '14:45' , '15:30' , 'go home' )
            
            
            
        ''')
con.commit()


cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nine_friday(number, lesson , office, start_lesson, finish_lesson, change)")
cur.execute('''INSERT INTO nine_friday VALUES
                ( 1, '' , '' , '8:00'  , '8:45'  , '10min' ),
                ( 2, '' , '' , '8:55'  , '9:40'  , '20min' ),
                ( 3, '' , '' , '10:00' , '10;45' , '20min' ),
                ( 4, '' , '' , '11:05' , '11:50' , '10min' ),
                ( 5, '' , '' , '12:00' , '12:45' , '10min' ),
                ( 6, '' , '' , '12:55' , '13:40' , '10min' ),
                ( 7, '' , '' , '13:50' , '14:35' , '10min' ),
                ( 8, '' , '' , '14:45' , '15:30' , 'go home' )
            
            
            
        ''')
con.commit()


#def plus_monday_one():
    #cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (main.one,1))

#def plus_monday_two():
    #cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (main.two,2))



#UPDATE nine_monday SET lesson = ? WHERE number = ?  






"""if main.one == 'Классный час':
    kab_1 = 208
elif main.two == 'Классный час':
    kab_2 = 208    
elif main.three == 'Классный час':
    kab_3 = 208
elif main.four == 'Классный час':
    kab_4 = 208
elif main.five == 'Классный час':
    kab_5 = 208
elif main.six == 'Классный час':
    kab_6 = 208
elif main.seven == 'Классный час':
    kab_7 = 208
elif main.eight == 'Классный час':
    kab_8 = 208

"""


"""( 1,  main.one   ,  kab_1  , '8:00'  , '8:45'  , '10min' ),
                    ( 2,  main.two   ,  kab_2  , '8:55'  , '9:40'  , '20min' ),
                    ( 3,  main.three ,  kab_3  , '10:00' , '10;45' , '20min' ),
                    ( 4,  main.four  ,  kab_4  , '11:05' , '11:50' , '10min' ),
                    ( 5,  main.five  ,  kab_5  , '12:00' , '12:45' , '10min' ),
                    ( 6,  main.six   ,  kab_6  , '12:55' , '13:40' , '10min' ),
                    ( 7,  main.seven ,  kab_7  , '13:50' , '14:35' , '10min' ),
                    ( 8,  'eight' ,  kab_8  , '14:45' , '15:30' , 'go home' )"""



























"""

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nine_monday(number, lesson , office, start_lesson, finish_lesson, change)")
cur.execute('''INSERT INTO nine_monday VALUES
                ( 1,  'Классный час'   ,   208  , '8:00' , '8:45' , '10min' ),
                ( 2,  'Информатика'    ,  '300?', '8:55' , '9:40' , '20min' ),
                ( 3,  'География'      ,  '500?', '10:00', '10;45', '20min' ),
                ( 4,  'История'        ,  '400?', '11:05', '11:50', '10min' ),
                ( 5,  'Русский язык'   ,  '500?', '12:00', '12:45', '10min' ),
                ( 6,  'Английский язык',  '???' , '12:55', '13:40', '10min' ),
                ( 7,  'Алгебра'        ,  '400?', '13:50', '14:35', '10min' ),
                ( 8,  'Нет урока'      ,    1   , '14:45', '15:30', 'go home' )
''')
con.commit()

cur.execute("CREATE TABLE IF NOT EXISTS nine_ (number, lesson , office, start_lesson, finish_lesson, change)")
cur.execute('''INSERT INTO nine_monday VALUES
                ( 1,  ''   ,   208  , '8:00' , '8:45' , '10min' ),
                ( 2,  ''    ,  '300?', '8:55' , '9:40' , '20min' ),
                ( 3,  ''      ,  '500?', '10:00', '10;45', '20min' ),
                ( 4,  ''        ,  '400?', '11:05', '11:50', '10min' ),
                ( 5,  ''   ,  '500?', '12:00', '12:45', '10min' ),
                ( 6,  '',  '???' , '12:55', '13:40', '10min' ),
                ( 7,  ''        ,  '400?', '13:50', '14:35', '10min' ),
                ( 8,  ''      ,    1   , '14:45', '15:30', 'go home' )
''')
con.commit()"""















