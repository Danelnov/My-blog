# My Personal Blog

The blog template was not created by me, if you want to download the original template click [here](https://startbootstrap.com/theme/clean-blog).

## **Setup**

### Configure development environment

You must first install poetry, if you still don't have it you can follow the installation guide [here](https://python-poetry.org/docs/#installation).

Then create a virtual environment with the following command:

```terminal
$ poetry shell
```

Once you have created the virtual environment, install the dependencies:

```terminal
$ poetry install
```

### Create the database

To create the database you just have to put these three commands in your terminal:

```terminal
$ manage migrate

$ manage makemigrations blog

$ manage migrate blog
```

> __*NOTE:*__ if the manage command doesn't work for you, you can try `python manage.py`

### Create superuser and start server

To be able to edit and publish post you need to create a user, for this you have to use the following command:

```terminal
$ manage cretesuperuser
```

Once you have created a user you can start the server.

```terminal
$ manage runserver
```
