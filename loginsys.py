import pymysql

class User:
    def __init__(self, database):
        self.db = pymysql.connect(user='root',
                                  passwd='123456',
                                  database=database,
                                  charset='utf8')
        self.cur = self.db.cursor()

    def register(self,iden):
        sql = 'select * from loginsystem where id = %s;'
        self.cur.execute(sql,[iden])
        if not self.cur.fetchone():
            password = input('enter your password:')
            sql = 'insert into loginsystem values (%s,%s);'
            try:
                self.cur.execute(sql,[iden,password])
                self.db.commit()
            except Exception as e:
                self.db.rollback()
            print('register successfully')
        else:
            print('id is not avaliable, change and try it again.')
    
    def login(self,iden):
        sql = 'select * from loginsystem where id = %s;'
        self.cur.execute(sql,iden)
        if not self.cur.fetchone():
            print('id is does not exist, change and try it again.')  
        else:
            password = input('enter your password:')
            sql = 'select * from loginsystem where (id,password) = (%s,%s);'
            self.cur.execute(sql,[iden,password])
            if self.cur.fetchone():
                print('login successfully.')
            else:
                print('wrong password.')    


    

def main():
    user = User('login')
    sql = 'create table loginsystem (id varchar(32) primary key,\
password varchar(32))'
    user.cur.execute(sql)
    while True:
        option = input('register or login?')
        if option == '1':
            iden = input('create your account:')
            user.register(iden)
        elif option == '2':
            iden = input('enter your account:')
            user.login(iden)
        elif option == 'q':
            break


main()
