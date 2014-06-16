Layout
======

Удобная верстка без повторения html-кода общих блоков

###Основные удобства


* наследование от базового шаблона
* переопределение общих блоков на отдельных страницах

###Зависимости

* Python 2.7+
* Git

###Примечания для пользователей windows

* Python [http://www.activestate.com/activepython/downloads](http://www.activestate.com/activepython/downloads)
* Git [http://git-scm.com/download/win](http://git-scm.com/download/win)
* можно сделать ярлык файла run.py на рабочий стол и запускать проект через него


###Установка и настройка

* переключиться в директорию с проектами
* выполнить `git clone https://github.com/pirsipy/layout.git project_name`, где `project_name` - название вашего будущего проекта
* переключиться в директорию проекта `project_name`
* установить зависимости для Python `pip install -r requirements.txt`
* выполнить команду `python run.py`
* открыть в браузере [http://localhost:8000](http://localhost:8000)

###Доступные настройки

* `--host` - адрес сервера для запуска приложения (по умолчанию: 127.0.0.1)
* `--port` - адрес сервера для запуска приложения (по умолчанию: 8000)

Пример: для доступа к просмотру вашего проекта по порту `8080` другим пользователям сети, нужно выполнить команду

    python run.py --host=0.0.0.0 --port=8080

Для остановки сервера в консоли нужно нажать `Ctrl+C`

###Работа со статикой:

В директории `static` должны располагаться css, js, jpg и т.п. файлы, доступ к которым можно получить по ссылке, к примеру:

* [http://localhost:8000/static/css/test.css](http://localhost:8000/static/css/test.css)
* [http://localhost:8000/static/js/jquery.js](http://localhost:8000/static/js/jquery.js)
* [http://localhost:8000/static/images/example.jpg](http://localhost:8000/static/images/example.jpg)

Взаимодействия с html-файлами можно изучить на примере имеющихся в проекте
