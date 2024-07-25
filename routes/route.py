from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial 
from bson import ObjectId # MongoDB의 '_id' 필드를 처리하기 위해 임포트. MongoDB는 기본적으로 각 문서(레코드)에 '_id'라는 필드를 자동으로 생성하며, 이 필드의 데이터 타입이 'ObjectID'이다.

# 라우터 인스턴스 생성 / 라우터: mini fastapi application
router = APIRouter()

# Get Request Method
@router.get("/") # MongoDB 컬렉션에서 모든 문서를 가져와 반환.
async def get_todos():
    todos = list_serial(collection_name.find()) # 직렬화 후 리스트로 변환.
    return todos # 직렬화 된 리스트를 반환. FastAPI는 JSON 형식으로 클라이언트에게 응답.

# Post Request Method
@router.post("/")
async def post_todo(todo: Todo): # 새로운 할 일을 MongoDB 컬렉션에 추가.
    collection_name.insert_one(dict(todo)) # todo를 딕셔너리 형태로 변환 후 MongoDB 컬렉션에 삽입. insert_one: pymongo 라이브러리에서 제공하며, 단일 문서를 데이터베이스에 추가하는 기능을 수행. 삽입할 문서(일반적으로 딕셔너리 형태)를 인자로 받는다.

# Put Request Method
@router.put("/{id}") 
async def put_todo(id: str, todo: Todo): # 특정 ID의 할 일을 업데이트한다. ID는 '_id'필드 값을 말한다.
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)}) # ObjectID(id): 문자열 형태의 'id'를 MongoDB의 'objectID'타입으로 변환. / '$set' 연산자를 사용하여 특정 필드만 업데이트한다. find_one_and_update 메서드는 MongoDB에서 특정 조건에 맞는 단일 문서를 찾고, 그 문서를 업데이트 하는 기능을 제공. $set 연산자는 MongoDB에서 문서를 업데이트할 때 특정 필드의 값을 설정하는 데 사용된다. 기존 필드를 업데이트하거나 새로운 필드 추가 가능. 
    
# Delete Request Method
@router.delete("/{id}") 
async def delete_todo(id: str): # 특정 ID의 할 일을 삭제.
    collection_name.find_one_and_delete({"_id": ObjectId(id)}) # '_id'필드가 'ObjectId(id)'와 일치하는 문서를 찾아내 삭제한다.