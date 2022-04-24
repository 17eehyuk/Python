import sqlite3

#DB파일에연결   #없으면 생성됨
conn = sqlite3.connect('./db/animal.db')

#커서생성   #커서에 명령을 해서 처리 수행 
c = conn.cursor()

#테이블생성
c.execute(
    '''
    SELECT * FROM 포유류
    '''
)

#fetch 종류 1개, 여러개, 전부
#c.fetchone()           #('사자', 9)
#c.fetchmany(2)         #[('사자', 9), ('고양이', 12)]
#c.fetchall()           #[('사자', 9), ('고양이', 12), ('개', 12)]      #튜플형식


#응용 반복문 활용
names = c.fetchall()

for name in names:
    print(name[0])
'''
사자
고양이
개
'''


#응용 일부만 읽기       #rowid : 아이디출력
c.execute(
    '''
    SELECT rowid, * FROM 포유류 WHERE 평균수명 >= 11
    '''
)
print(c.fetchall())


#수업내용 : 일부포함 출력   => % dldyd
'''
WHERE last_name LIKE 'Br%'
'''


#닫기
conn.close()