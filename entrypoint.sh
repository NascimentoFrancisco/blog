#!/bin/bash
# entrypoint.sh

# Espera até que o PostgreSQL esteja pronto
echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

python manage.py migrate

exec "$@"