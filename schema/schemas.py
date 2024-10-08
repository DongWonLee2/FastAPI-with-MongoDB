def individual_serial(todo) -> dict: # MongoDB의 단일 문서를 직렬화하여 딕셔너리 형태로 반환한다. 문서 지향 데이터베이스의 데이터를 Python 객체로 변환.
    return{
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }

def list_serial(todos) -> list: # 리스트 형태로 변환
    return[individual_serial(todo) for todo in todos]
