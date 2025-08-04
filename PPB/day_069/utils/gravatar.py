from flask_gravatar import Gravatar

def init_gravatar(app):
    gravatar = Gravatar(app,
                      size=100,
                      rating='g',
                      default='retro',
                      force_default=False,
                      force_lower=False,
                      use_ssl=False,
                      base_url=None)
    return gravatar