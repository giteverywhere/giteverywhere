from . import APP_NAME, PROJECT_NAME, APP_BASE


def application_routes(config):
    config.add_route(APP_NAME + '.home', '/')
    config.add_route(APP_NAME + '.view_repo_names', '/view_repo_names')
    config.add_route(APP_NAME + '.log', '/log/{repo}/{b_name}')
    config.add_route(APP_NAME + '.clog', '/clog/{repo}/{output}') 
   # config.add_route(APP_NAME + '.alog', '/alog/{repo}')
    config.add_route(APP_NAME + '.branch', '/branch/{repo}/{output}')
    config.add_route(APP_NAME + '.cbranch', '/cbranch/{repo}/{output}')   
    config.add_route(APP_NAME + '.tag', '/tag/{repo}')
    config.add_route(APP_NAME + '.showtag', '/showtag/{repo}')
    config.add_route(APP_NAME + '.diff', '/diff/{repo}')
    config.add_route(APP_NAME + '.cdiff', '/cdiff/{repo}/{hash}')
    config.add_route(APP_NAME + '.files', '/files/{repo}')
    config.add_route(APP_NAME + '.contents', '/contents/{repo}/{f_name:.*}')
    config.add_route(APP_NAME + '.branches', '/branches/{repo}')
    config.add_route(APP_NAME + '.manage', '/manage/{repo}')
    config.add_route(APP_NAME + '.zip', '/zip/{repo}')
    config.add_route(APP_NAME + '.tar', '/tar/{repo}')
    config.add_route(APP_NAME + '.tar_gz', '/tar_gz/{repo}')
    config.add_static_view('static', 'git:static/')
    config.add_static_view('statics', 'static', cache_max_age=3600)
    

