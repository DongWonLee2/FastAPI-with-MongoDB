from pymongo import MongoClient

# MongoClient를 사용하여 MongoDB 클러스터에 연결. 연결 문자열에는 사용자명, 비밀번호, 클러스터 URL 등이 포함. 
client = MongoClient("mongodb+srv://{username}:{password}@{cluster-url}&{appName}")

# todo_db 데이터베이스 선택
db = client.todo_db

# todo_db에 todo_collection을 선택
collection_name = db["todo_collection"]