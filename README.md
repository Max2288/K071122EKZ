## Запуск

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

docker-compose up -d

python migrations.py

uvicorn main:app --reload
```

## Тестирование приложения и коллекция запросов

> /api/v1/students
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/students' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string"
}'
```

> api/v1/hobbies
```

curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/hobbies' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string"
}'
```

> api/v1/students/{student_id}/hobbies/{hobby_id}

```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/students/1/hobbies/1' \
  -H 'accept: application/json' \
  -d ''
```

> api/v1/students/{student_id}/hobbies

```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/students/3/hobbies' \
  -H 'accept: application/json'
```

> api/v1/students/{student_id}

```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/api/v1/students/3' \
  -H 'accept: application/json'
```

## Документация 

> Сваггер находится по урлу http://127.0.0.1:8000/docs
