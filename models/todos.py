'''
ODM(Object-Document Mapping) 이란?
ODM은 객체와 문서 지향 데이터베이스 간의 매핑을 담당합니다. 문서 지향 데이터베이스는 데이터 구조를 문서 형식(JSON, BSON 등)으로 저장하며, 관계형 데이터베이스와 달리 테이블이 아닌 컬렉션을 사용합니다. ODM은 이러한 문서 지향 데이터베이스와 객체 간의 변환을 관리합니다.
ODM도 ORM과 근본적으로 하는 역할은 동일하다. 다만 데이터 매퍼가 사용되는 데이터베이스의 유형에서 갈린다.
정리하자면 ORM은 SQL을 위해서, ODM은 NoSQL을 위해서 존재한다.

ODM 작동 핵심
Pydantic 모델 (Todo): MongoDB 문서와 Python 객체 간의 매핑을 담당합니다. 이는 데이터 검증 및 직렬화/역직렬화를 통해 이루어집니다.
dict(todo): Pydantic 모델을 딕셔너리로 변환하여 MongoDB에 삽입하거나 업데이트할 때 사용됩니다.
직렬화 함수 (individual_serial, list_serial): MongoDB에서 가져온 문서를 Python 딕셔너리로 변환합니다.
'''
from pydantic import BaseModel

# 데이터 모델을 생성. ODM의 역할을 수행
class Todo(BaseModel):
    name: str
    description: str
    complete: bool
