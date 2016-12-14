from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['POST']['/registration'] = 'Welcome#registration'
routes['POST']['/login'] = 'Welcome#login'
routes['/charts'] = 'Stock#charts'
routes['POST']['/stock'] = 'Stock#stock'
routes['/logoff'] = "Welcome#logoff"