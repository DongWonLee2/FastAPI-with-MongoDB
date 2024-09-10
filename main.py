from fastapi import FastAPI
from routes.route import router

app = FastAPI()

# include_router: 다른 모듈에서 정의된 라우터를 메인 애플리케이션에 포함. 코드 구조를 모듈화하고 유지보수에 용이.
app.include_router(router)

#테스트
#테스트 branch
#테스트 commit
#테스트 commit txt