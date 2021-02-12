# django-react-boilerplate

Boilerplate for integrating django with rest_framework, react and JWT

To start create a .env file in settings folder with these variables:

PYTHONDONTWRITEBYTECODE=1

DJANGO_SECRET_KEY='your_secret_code'

DJANGO_DEBUG=True

DJANGO_ALLOWED_HOSTS=127.0.0.1

Next run:  
`./manage.py makemigrations`
`./manage.py migrate`

Then go to frontend folder and run:
`npm install`

To start development:
`npm run start:dev`

Then run build:
`npm run build`

And Finaly:
`./manage.py runserver`
