from . import APP_NAME, PROJECT_NAME, APP_BASE


def application_routes(config):
    config.add_route(APP_NAME + '.home', '/')
    config.add_route(APP_NAME + '.log', '/log/{b_name}')
    config.add_route(APP_NAME + '.branch', '/branch')
    config.add_route(APP_NAME + '.cbranch', '/cbranch')
    config.add_static_view('static', 'static', cache_max_age=3600)

