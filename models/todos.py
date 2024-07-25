from pydantic import BaseModel

# 데이터 모델을 생성
class Todo(BaseModel):
    name: str
    description: str
    complete: bool