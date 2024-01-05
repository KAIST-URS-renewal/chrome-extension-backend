# 가상 환경 활성화하기
source src/.venv/Scripts/activate

# fast api 서버 실행하기
python -m uvicorn main:app --reload

# DB Setup
docker compose -p newurs-backend -f .docker/docker-compose.yml --env-file .config/.env up -d
docker compose -p newurs-backend -f .docker/docker-compose.yml --env-file .config/.env down

