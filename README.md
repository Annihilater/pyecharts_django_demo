# 在 Django 中使用 pyecharts

> 本指南介绍了如何在 Django 中使用 pyecharts。

## Django 模板渲染

### Step 0: 新建一个 Django 项目

```shell
$ django-admin startproject pyecharts_django_demo
```

创建一个应用程序

```shell
$ python manage.py startapp demo
```

在 `pyecharts_django_demo/settings.py` 中注册应用程序

```python
# pyecharts_django_demo/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demo'  # <---
]
```

编辑 `demo/urls.py` 文件

```python
# demo/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

在 `pyecharts_django_demo/urls.py` 中新增 `demo.urls`

```python
pyecharts_django_demo/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'demo/', include('demo.urls'))  # <---
]
```

### Step 1: 拷贝 pyecharts 模板

先在 `demo` 文件夹下新建 templates 文件夹

```shell
chenjiandongx@DESKTOP-E83NUHA:/mnt/d/Python/pyecharts-django-demo/pyecharts_django_demo/demo$ ls
__init__.py  __pycache__  admin.py  apps.py  migrations  models.py  templates  tests.py  urls.py  views.py
```

将 pyecharts 模板，位于 `pyecharts.render.templates` 拷贝至刚新建的 templates 文件夹

```shell
chenjiandongx@DESKTOP-E83NUHA:/mnt/d/Python/pyecharts-django-demo/pyecharts_django_demo/demo/templates$ tree
.
├── jupyter_lab.html
├── jupyter_notebook.html
├── macro
├── nteract.html
├── simple_chart.html
├── simple_page.html
└── table.html
```

### Step 2: 渲染图表

将下列代码保存到 `demo/views.py` 中。

```python
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./demo/templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar


def index(request):
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return HttpResponse(c.render_embed())
```

### Step 3: 运行项目

```shell
$ python manage.py runserver
```

使用浏览器打开 http://127.0.0.1:8000/demo 即可访问服务

![image-20200417182134663](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2020-04-17-102135.png)

