# library_site

# Запуск
```
git clone https://github.com/ema5353/library_site
```
```
cd library_site
```
``` 
virtualenv venv 
```

``` 
pip install -r requirements.txt
```

``` 
source venv/bin/activate 
```
``` 
python3 manage.py migrate
```
``` 
python3 manage.py createsuperuser
```
``` 
python3 manage.py runserver 
```
