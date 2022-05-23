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
8. Create models:
```python
class Bottles(models.Model):
    name = models.CharField(max_length=50)
    volume = models.DecimalField()
    production_date = models.DateField()
```
9. And migrations:
```bash
python manage.py migrate
```

10. Create file named `Procfile` in project root (name after gunicorn must be the same as the project name created in step 1)
```python
web: gunicorn HerokuDeployment.wsgi --log-file -
```

11. Add in `settings.py` two lines at the bottom
```python
import django_heroku
django_heroku.settings(locals())
```

12. Comment out SECRET_KEY line in `settings.py` for safety:
```python
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-kbi3d)2p&5oxl!n2_z66%hgqg&%c4nytm-+7rn^z)(6jk=#%xq'
```

13. Share project on github