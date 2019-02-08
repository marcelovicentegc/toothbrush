# Toothbrush
A web-app that extracts the 20 most common words from .pdf, .doc and .txt files.

## Demo
<img src="https://github.com/marcelovicentegc/Toothbrush/blob/master/Toothbrush.gif" width="640" height="360" />

## Directions
1. Clone this repository:
2. Install dependencies: `cd Toothbrush/project/requirements; pip install -r base_win.txt; python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"` if on Windows, or `cd Toothbrush/project/requirements && pip install -r base.txt && python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"` if on Mac/Linux
4. Set a environment variable for `DJANGO_TOOTHBRUSH_SECRET_KEY`
5. Run migrations: `cd ../..; python manage.py makemigrations; python manage.py makemigrations toothpaste` if on Windows, or `cd ../.. && python manage.py makemigrations && python manage.py makemigrations toothpaste` if on Mac/Linux
6. Migrate database: `python manage.py migrate`
7. Run the application: `python manage.py runserver`