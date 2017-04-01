#!/usr/bin/env bash
USER="admin"
MAIL="sroy8091@gmail.com"
PASS="admin"

if [ -z "$VCAP_APP_PORT" ];
  then SERVER_PORT=5000;
  else SERVER_PORT="$VCAP_APP_PORT";
fi

echo [$0] port is------------------- $SERVER_PORT
python manage.py makemigrations
python manage.py migrate
echo "from account.models import user ; User.objects.create_superuser('${USER}', '${MAIL}', '${PASS}')" | python manage.py shell

echo [$0] Starting Django Server...
python manage.py runserver 0.0.0.0:$SERVER_PORT --noreload