import sqlite3

#DB파일에연결   #없으면 생성됨
conn = sqlite3.connect('./db/animal.db')

#커서생성   #커서에 명령을 해서 처리 수행
c = conn.cursor()

#테이블생성 
c.execute(
    '''
    CREATE TABLE 포유류(이름 text, 평균수명 integer)
    '''
)

print('생성성공')

'''
테이블 타입은 5개 존재
NULL        존재유무
INTEGER     정수
REAL        실수
TEXT        글자
BLOB        모든것      #틀릴수도 있음...
'''

#커밋 : 변화를 기록하기
conn.commit()

#닫기
conn.close()