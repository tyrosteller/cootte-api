# Step 1: Python 3.12 이상의 가벼운 공식 이미지 사용 
FROM python:3.12

# Step 2: 작업 디렉토리 설정 
WORKDIR /app

# Step 3: Poetry 설치 
RUN pip install --no-cache-dir poetry

# Step 4: Poetry의 가상환경을 비활성화 (Docker 컨테이너 내에서 global하게 사용) 
RUN poetry config virtualenvs.create false

# Step 5: 의존성 설치를 위한 파일 복사 
COPY pyproject.toml poetry.lock ./

#Step 6: 의존성 설치
RUN poetry install --no-root --without dev 


# Step 7: 전체 소스 코드 복사 
COPY . .

# Step 8: FastAPI 애플리케이션 실행 (uvicorn) 
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]