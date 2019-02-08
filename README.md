# Toothbrush
A web-app that extracts the 20 most common words from .pdf, .doc and .txt files.

## Demo
<img src="https://github.com/marcelovicentegc/Toothbrush/blob/master/Toothbrush.gif" width="640" height="360" />

## Directions
1. Clone this repository:
2. Install dependencies: `cd Toothbrush/project/requirements; pip install -r base.txt` if on Windows, or `cd Toothbrush/project/requirements && pip install -r base.txt` if on Mac/Linux
3. Run migrations: `cd ../..; python manage.py makemigrations; python manage.py makemigrations toothpaste` if on Windows, or `cd ../.. && python manage.py makemigrations && python manage.py makemigrations toothpaste` if on Mac/Linux
4. Migrate database: `python manage.py migrate`
5. Run the application: `python manage.py runserver`