#!/usr/bin/env python
import sys

from tornado import web
from tornado.ioloop import IOLoop
from tornado.options import options, define

define('port', type=int, default=8000)
define('host', type=str, default='127.0.0.1')
options.parse_command_line()

APP_SETTINGS = {'static_path': 'static', 'template_path': 'html',
                'debug': True, 'gzip': True}


class LayoutHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, filename=None):
        if not filename:
            filename = 'index.html'
        self.render(filename)


application = web.Application([
    (r'/', LayoutHandler),
    (r'/(?P<filename>.*)', LayoutHandler)], **APP_SETTINGS)


def main():
    sys.stdout.write('Host: {0}\n'.format(options.host))
    sys.stdout.write('Port: {0}\n\n'.format(options.port))
    application.listen(options.port, options.host)
    try:
        IOLoop.instance().start()
    except KeyboardInterrupt:
        IOLoop.instance().stop()


if __name__ == '__main__':
    main()
