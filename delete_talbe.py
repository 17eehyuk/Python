import sqlite3

#DB파일에연결   #없으면 생성됨
conn = sqlite3.connect('./db/animal.db') 

#커서생성   #커서에 명령을 해서 처리 수행
c = conn.cursor()

#업데이트
# SET : 바꿀 값
# WHERE : 바꾸고 싶은 값        # WHERE 지정 안하면 전부다 바뀜 매우 주의!!!!!
c.execute(
    '''
    DELETE FROM 포유류 WHERE 이름 = '개'
    '''
)



#닫기
conn.close()