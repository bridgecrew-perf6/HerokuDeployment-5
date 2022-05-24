# Heroku deployment Django 4 project

## Steps
1. Create new Django project in PyCharm with new empty venv named `HerokuDeployment` (or different)
2. Install dependencies:
```bash
pip install gunicorn
pip install django-heroku
pip install psycopg2-binary
```
3. Create `.gitignore` in project root as this: https://www.toptal.com/developers/gitignore/api/pycharm,django,python
4. Create `requirements.txt` file with command in project root
```bash
pip freeze > requirements.txt
```
5. Create application in Django
```bash
python manage.py startapp herokuapp
```
6. Add it to settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'herokuapp'
]
```
7. Create models:
```python
class Bottles(models.Model):
    name = models.CharField(max_length=50)
    volume = models.DecimalField()
    production_date = models.DateField()
```
8. And migrations:
```bash
python manage.py migrate
```

9. Create file named `Procfile` in project root (name after gunicorn must be the same as the project name created in step 1)
```python
web: gunicorn HerokuDeployment.wsgi --log-file -
```

10. Add in `settings.py` two lines at the bottom
```python
import django_heroku
django_heroku.settings(locals())
```
and add your app url to ALLOWED_HOSTS
```python
ALLOWED_HOSTS = ['django-deployment-demo.herokuapp.com', '127.0.0.1']
```


11. [Optional] Share project on github (might be private)

12. Now create heroku account and create new app with name and region
13. Install heroku-cli https://devcenter.heroku.com/articles/heroku-cli
14. Run `heroku login` command and login to heroku
15. Create repo on heroku `heroku git:remote -a django-deployment-demo`
16. Run `heroku config:set DISABLE_COLLECTSTATIC=1` or configure static files properly
17. Push your code to heroku to trigger deplyoment `git push heroku main`