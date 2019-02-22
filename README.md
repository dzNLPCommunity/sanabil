
# Sanabil
A platform to organize the work of charity in Algiers

## Built with

Sanabil was built with:

* [Django](https://www.djangoproject.com/)- Python-based free and open-source web framework
* [Semantic UI](https://semantic-ui.com/) - UI component framework for modern web apps

## Installation

Sanabil requires [Python](https://www.python.org/download/releases/3.7/) version 3+ to run.
### Packages
Install the required packages using pip:

```
pip install -r requirements.txt
```
### Database

For database and super-admin creation: 
```
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```
And then fill fixtures by running:
```
./manage.py loaddata */fixtures/*.json
```
### Collecting static files
Excute in terminal:
```
./manage.py collectstatic --noinput

```

### Running server:

To run server locally run in terminal :
`./manage.py runserver`

And open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to check the plateforme

## Get involved!
We are happy to receive bug reports, fixes,  or any other enhancements.
Please if you find any report bugs via the [github issue tracker](https://github.com/assem-ch/sanabil/issues).



