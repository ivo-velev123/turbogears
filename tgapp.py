from tg import expose, TGController, MinimalApplicationConfigurator
from tg.configurator.components.statics import StaticsConfigurationComponent
from wsgiref.simple_server import make_server
import webhelpers2
import webhelpers2.text

class RootController(TGController):
    @expose('index.xhtml')
    def index(self, person=None):
        return dict(person=person)
    
    @expose('hello.xhtml')
    def hello(self, person=None):
        return dict(person=person)
    
config = MinimalApplicationConfigurator()
config.update_blueprint({
    'server_static': True,
    'root_controller': RootController(),
    'renderers': ['kajiki'],
    'helpers': webhelpers2
})

config.register(StaticsConfigurationComponent)
config.update_blueprint({
    'serve_static': True,
    'paths': {
        'static_files': 'public'
    }
})
    
application = config.make_wsgi_app()

print("Serving on port 8080...")
httpd = make_server('', 8080, application)
print("serving on port 8080")
httpd.serve_forever()