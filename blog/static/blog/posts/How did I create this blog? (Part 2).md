<img align="center" src="/static/markdownx/" alt="" width="1920"/>

Welcome to Part 2 of the "How did I create this blog?" series. It has been a while since my last post, been really busy at work and home. Finally found some time to crank out this post and it feels great to be back and continuing with this series.

Looking back, in [Part 1 ](https://ryanbutler.online/how-did-i-create-this-blog-part-1) we focused on getting the infrastructure up and running for the blog and created the Django Project, which was serving the default Django project page. Today, we will be creating our Blog App, create the models and setup a super user to draft and manage posts and categories through the Django admin view.

Please do reach out to me using the [contact](https://ryanbutler.online/contact/) page with your feedback about my blog or if you just want to talk about anything related to Python.

# Part 2

# Table of Contents
1. [Creating an App](#create-app)
2. [Creating Models](#django-models)
3. [Admin View](#django-admin)


<div id='create-app' markdown='1'></div>

## 1. Creating an App
After finishing [Part 1 ](https://ryanbutler.online/how-did-i-create-this-blog-part-1), you will have a Python virtual environment and a vanilla Django Project configured. Now we want to create our Blog App using the same virtual environment and Django Project. 

At this stage, you might be asking yourself, "What is the difference between a Django Project and a Django App?". Good question. According to the Django documentation:

- a *"Django Project"* is a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings. A project can contain multiple Apps.

- a *"Django App"* is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. An app can be in multiple projects.

Great, that is pretty clear. Let's move on.

When you installed Django, your system will not only have access to the [django-admin](https://docs.djangoProject.com/en/3.1/ref/django-admin/) commands, but you will also have a "admin.py" file in the root of the Django Project. We are going to use the "admin.py" file to create the Blog App. These are basically Django’s command-line utilities for administrative tasks of your Django Project.   

```bash
# Ensure your are current working directory is in the root of the Django Project and
# verify your virtual environment is activated
cd ~/myproject

tree -L 2
.
├── manage.py
├── myproject
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── venv
    ├── bin
    ├── include
    ├── lib
    └── pyvenv.cfg

source venv/bin/activate
(venv) 
```

Now create the Blog App.
```bash
(venv) python admin.py startapp blog
```

This should now be the contents of your Django Project directory excluding the venv directory.
```bash
(venv) tree -I venv -L 2
.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── myproject
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
```
The Project and Blog boilerplate is now ready to be changed.

<div id='django-models' markdown='1'></div>

## 2. Creating Models
In essence a [Django Model](https://docs.djangoproject.com/en/3.1/topics/db/models/) represents the structure of your database and is the only source of information which represents your data stored for your Django App. Models contain all the fields and behaviors for the App's data. In general, a model maps to a single database table.

See the below example which will create a table with 3 columns("id", "dog_name", "last_name"):
```python
from django.db import models

class Dog(models.Model):
    dog_name = models.CharField(max_length=30)
    dog_breed = models.CharField(max_length=30)
```
Note, the "id" field is implicitly created and automatically set as the Primary Key. This is one of my favorite features of working with Django. It abstracts all of the database semantics and nuances of writing your own SQL queries to create tables and instead lets you focus on modeling, creating and representing your data. Later when querying data, Django also exposes a [database API](https://docs.djangoproject.com/en/3.1/topics/db/queries/), which lets you easily create, retrieve, update and delete objects stored in the database.

Now that we know what models are and their purpose, lets create the model for our Blog App:
```python
# ~/myproject/blog/models.py

from django.db import models
from django.utils import timezone


STATUS = ((0, "Draft"), (1, "Publish"))


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        """Meta definition for Category."""

        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    publish_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    read_time = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        """Meta definition for Post."""

        ordering = ["-publish_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

```
Let's unpack the above. We created two tables: 
* Category; and 
* Post.

In the Post table, there are eight fields.
* title
* body
* created_on
* last_modified
* status
* publish_date
* categories (Many-to-Many relationship with the Category table)
* read_time

For the Category table we only have one field:
* name

Next, we will configure the Admin view, where we can manage our Posts and Categories for our Blog.

<div id='django-admin' markdown='1'></div>

## 3. Admin View
The Admin view is bundled by default in each Django project. In essence, the Admin view is used to manage your Apps from an administrator's point of view. 

For example in our Blog App, the administrator or author will draft new posts and publish them on the Blog using the Admin view. Viewers of the Blog are not allowed to draft and publish posts, they just get to browse your blog and read the posts. In order to access the Admin view, you need to create a superuser and authenticate with those credentials when prompted on the Admin view login page.

In order to create a superuser, we can use, yes you guessed it, the manage.py file and administrative commands. Run the below command and complete the relevant information in the prompts to create a superuser.

```bash
(venv) python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: admin@test.com
Password: ********
Password (again): ********
Superuser created successfully.
```

At this point you can run your Django project, with the below command:
```bash
(venv) python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 20, 2021 - 08:45:16
Django version 3.1.5, using settings 'my_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
You can now browse to http://127.0.0.1:8000/ to view the default Django project page and http://127.0.0.1:8000/admin to the Admin logon screen. Use the username and password you configured in the previous step to logon as your super user.

Once you have logged into the Admin view, you will notice that only the "AUTHENTICATION AND AUTHORIZATION" section with Users and Groups is available. This is because we have not registered our new models in the Admin view. In order to add your models to the Admin view to create and manage posts and categories you need add the below to your admin.py view file located in the blog directory:

```python
# ~/myproject/blog/admin.py

from django.db import models
from django.contrib import admin
from blog.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_on", "last_modified")
    list_filter = ("status",)
    search_fields = ["title", "body"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
```
Once you applied the above, run the Django server again and browse to the Admin view and login with your super user. You should see the "BLOG" section with both Post and Category models listed.

Now you can browse to each model to start creating categories and posts and they will be stored in your projects database.

![](/static/markdownx/2021/02/20/admin_view.png_55a504c8-b850-47c4-906f-8df147173102.png)

## Last words

This wraps up Part 2 of my multi-series posts where we will be deploying a blog similar to the one you are currently reading. In the next part we will be creating views, managing URL's and creating our blog's HTML templates. See you then!

*Best Regards*

*Ryan*