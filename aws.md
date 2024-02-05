
# conectar por ssh a un servidor de aws


ssh -i /path/key-pair-name.pem instance-user-name@instance-public-dns-name
chmod 400 ./.venv/LightsailDefaultKey-us-east-1.pem


source /home/ubuntu/django/.venv/bin/activate &&  gunicorn --bind unix:/tmp/django.sock --workers=1 --threads=25 --chdir /home/ubuntu/django config.wsgi:application
       
        {
        name: 'django',
        cmd: 'gunicorn',
        args: '--bind unix:/tmp/django.sock --workers=1 --threads=25 --chdir /home/ubuntu/django config.wsgi:application',
        watch: true,
        interpreter: '/home/ubuntu/django/.venv/bin/python'
        }