# aitecell

## ways to run locally
1. `rename .env.sample to .env in aitecell directory where settings.py is based`
2. `python3 -m venv env` - create virtual environment
3. `source env/bin/activate` - activate virtual environment
4. `pip install -r requirements.txt` - install dependencies
5. `python3 manage.py makemigrations` - create migrations (after every schema changes)
6. `python3 manage.py migrate` - apply migrations (after every schema changes)
7. `python3 manage.py runserver` - run server - make sure to use sqlite3 database & always keep your debug=True while development


## db.sqlite3 admin config
username: `admin`
password: `admin`

## Endpoints
`https://aitecell.herokuapp.com/api/`

## Todo
- [x] create tags model - newsletter, social media, events, meet, documents, images, 
- [x] add tag to each link (allow only one tag per link)
- [X] create a flag model // can create flags to turn feature on and off
- [X] rename category model to tag model
- [X] other info - motto, vision, mission, etc
- [X] latest updates new badge to be shown on only updates which are added in last 7 days and to 3 recent updates
- [X] is active internship logic
- [X] add a section for policy and rules

## Frontend link
https://ait-ecell.netlify.app