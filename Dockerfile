FROM node:18-alpine3.18 AS frontend-builder

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

ENV NODE_ENV=production
RUN npm run build

FROM python:3.10.12-alpine3.18

WORKDIR /app

COPY --from=frontend-builder /app /app

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input

# CMD uvicorn django_project.asgi:application --host 0.0.0.0 --port $PORT
CMD gunicorn django_project.wsgi