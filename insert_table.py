import sqlite3

#DB파일에연결   #없으면 생성됨
conn = sqlite3.connect('./db/animal.db')

#커서생성   #커서에 명령을 해서 처리 수행 
c = conn.cursor()

#테이블 삽입    #한번에 여러게 추가 불가능 1개만 가능
c.execute(
    '''
    INSERT INTO 포유류(이름, 평균수명) VALUES('사자', 9);
    '''
)

print('삽입성공')

#응용 한번에 여러개 넣기        #튜플형식
mammals = [
    ('고양이', 12),
    ('개', 12)
    ]

c.executemany(
    '''
    INSERT INTO 포유류(이름, 평균수명) VALUES(?, ?);
    ''', mammals
)

print('삽입성공')


#커밋 : 변화를 기록하기
conn.commit()

#닫기
conn.close()