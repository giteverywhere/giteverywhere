from . import APP_NAME, PROJECT_NAME, APP_BASE


def application_routes(config):
    config.add_route(APP_NAME + '.home', '/')
    config.add_route(APP_NAME + '.log', '/log/{repo}/{b_name}')
    config.add_route(APP_NAME + '.clog', '/clog/{repo}')
    
    config.add_route(APP_NAME + '.branch', '/branch/{repo}')
    config.add_route(APP_NAME + '.cbranch', '/cbranch')
    config.add_route(APP_NAME + '.branches', '/branches/{repo}')
    
    config.add_route(APP_NAME + '.manage', '/manage/{repo}')
    config.add_route(APP_NAME + '.tag', '/tag/{repo}')
    config.add_route(APP_NAME + '.showtag', '/showtag')
    config.add_route(APP_NAME + '.diff', '/diff/{repo}')
    config.add_route(APP_NAME + '.cdiff', '/cdiff/{repo}/{hash}')
    config.add_route(APP_NAME + '.files', '/files/{repo}')
    config.add_route(APP_NAME + '.contents', '/contents/{repo}/{f_name:.*}')
    config.add_route(APP_NAME + '.dir', '/dir/{repo}')
    config.add_route(APP_NAME + '.browse', '/browse/{repo}')
 
    config.add_static_view('static', 'static', cache_max_age=3600)

