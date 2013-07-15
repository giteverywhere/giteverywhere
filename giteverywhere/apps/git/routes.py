from . import APP_NAME, PROJECT_NAME, APP_BASE


def application_routes(config):
    config.add_route(APP_NAME + '.home', '/')
    config.add_route(APP_NAME + '.log', '/log/{b_name}')
    config.add_route(APP_NAME + '.clog', '/clog/{repo}')
    
    config.add_route(APP_NAME + '.branch', '/branch')
    config.add_route(APP_NAME + '.cbranch', '/cbranch')
    config.add_route(APP_NAME + '.manage', '/manage/{repo}')
    config.add_route(APP_NAME + '.tag', '/tag')
    config.add_route(APP_NAME + '.showtag', '/showtag')
    config.add_route(APP_NAME + '.diff', '/diff')
    config.add_route(APP_NAME + '.files', '/files')
    config.add_route(APP_NAME + '.contents', '/contents/{f_name}')
 
    config.add_static_view('static', 'static', cache_max_age=3600)

