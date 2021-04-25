<img align="center" src="/static/markdownx/2021/04/20/views_code.png_1a277b54-5166-411a-ba26-04ed0c6fd190.png" alt="views_code"/>

This is Part 3 of this series of how I created this blog using Django. It has been a long time since my last post, been pretty busy at work and at home with the kids, but finally got some time to focus and draft this post. This is the last tutorial in this three part series. I will however include some features, tips and tricks in my future posts, which I did not touch on in this series.

In this post we will be looking at creating some views, managing the URL paths, creating some fancy HTML templates and finally adding some Markdown support.  Writing your posts in Markdown lets you focus on your content creation, without worrying about by adding HTML and CSS to your post.

As always, please reach out to [me](https://ryanbutler.online/contact/) if you have any comments, questions or just want to say hi!

Links to previous parts in the series:

- [Part 1](https://ryanbutler.online/how-did-i-create-this-blog-part-1)
- [Part 2](https://ryanbutler.online/how-did-i-create-this-blog-part-2)

# Part 3

# Table of Contents
1. [Creating Views](#django-views)
2. [Managing URLs](#django-urls)
3. [HTML Templates](#django-templates)
4. [Markdown Support](#markdown-support)


<div id='django-views' markdown='1'></div>

## 1. Creating Views

The Django Documentation does a great job explaining what a view is, and as a matter of fact any other areas of Django as well. I always refer back to their Documentation of I am stuck or looking for some better understanding on a Django topic.

"A view function, or view for short, is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really."

Ref: [Django Documentation - Views](https://docs.djangoproject.com/en/3.2/topics/http/views/)

The view functions can be stored anywhere in your project, but I prefer to keep them in the views.py file located in each app of my Django project, where possible.

```bash
(venv) tree blog -L 1
blog
├── __init__.py
├── admin.py
├── apps.py
├── migrations
├── models.py
├── tests.py
└── views.py
```

Let's take a look at a basic `views.py` file with a good mix of different types of views:

<script src="https://gist.github.com/ryanleonbutler/bcc02c3e89de5a2a3cb67c14585d28a4.js"></script>

Don't be intimidated by the above code snipped, it is actually pretty straight forward. Django comes with some awesome built-in generic views to assist in generating list and detail views of objects from your database. I used class-based views for the first two view functions and thereafter just my basic view functions to render the HTML. The class-based views are really simple to use. You only need an object(s)(which is a model or a list of objects from a query), pass in a context variable and reference an HTML template. The two functions, named `get_object` in each class-based view, is used to query the database and return an object(s). 

See reference to the Django documentation [here](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/), should you require more information on class-based views.

<div id='django-urls' markdown='1'></div>

## 2. Managing URLs

The routing logic of your Django app is contained in the `urls.py` file within your app. This is where pattern matching is performed in order to route your requests to the correct page. This routing logic is based on the path in the URL of your request.

Let's first breakdown a URL and each part of a URL to better understand which part is called the "path".

<img align="center" src="/static/markdownx/2021/04/20/url_breakdown.png_5b8e39a5-f496-436a-b274-b66ce6ccb100.png" alt="url_breakdown"/>

Now that we know what the path part is, lets look at my `urls.py` file below:

<script src="https://gist.github.com/ryanleonbutler/6de8bc241f3f00cc6ae95f7e964fe5b4.js"></script>

As you can see we can use two types of functions, `path` or `url`. You would use path to satisfy a specific path pattern for example `""`, which is the first path, and is a wild card which will catch all the URL paths that does not match any of the other patterns below it. You would use a URL if you know the specific path that you would want to route to, for example my `contact/` and `about/` pages will never change and has a static path.

After the path part, the next argument is the class or function that is imported from your `views.py` file. Then you also assign a `name` variable.

Again, see the Django documentation [here](https://docs.djangoproject.com/en/3.2/topics/http/urls/) for more detailed information on using the urls.py file to route requests.

<div id='django-templates' markdown='1'></div>

## 3. HTML Templates

Next, we look at the HTML templates which will have all of your HTML and CSS boilerplate. I cheated here, since I am not a very creative web designer and more a backend developer. I used a static site generator, like [Hugo](https://gohugo.io/) to generate my HTML, CSS and JS, which I just modified to suite my needs. The great thing about using a static site generator, it will have all the HTML semantics like meta-tags, which will not only increase your SEO rankings it will also have display preview images when sharing links to your blog on social media platforms.

I am not going to share any code examples here, however I will reference the Django documentation which will guide you to create some sample templates as well as a `base.html` template which you can reference in all of your templates to avoid duplication.

See Django documentation [here](https://docs.djangoproject.com/en/3.2/ref/templates/language/).

<div id='markdown-support' markdown='1'></div>

## 4. Markdown Support

Our last topic, is adding Markdown support. I cannot stress this feature enough, it has really changed my blogging experience it lets me write my posts with more freedom and with more focus on the content itself then managing the HTML and CSS behind it to make it look half decent on the page.

I used the Django plugin, [Markdownx](https://pypi.org/project/django-markdownx/). It suited my needs and was pretty easy to implement. You can see the implementation guide [here](https://neutronx.github.io/django-markdownx/installation/).

## Last words
And that is all folks. I hope this series of posts has not only inspired you to get started with Django and creating your own blog, but also guided you along the way. Please do share with me your blog if you used my series of posts as an inspiration to create your own blog using Django and Python. 

Thank you for your continued support and stay safe out there my fellow Pythonistas!