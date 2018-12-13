import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

config = {}

from ckanext.disablepwreset.logic.auth.get import request_reset, user_reset

class ConfigError(Exception):
    pass

class DisablePWResetPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IConfigurable)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'disablepwreset')

    # IAuthFunctions
    def get_auth_functions(self):
        return {
            'request_reset': request_reset,
            'user_reset': user_reset
        }

    # IConfigurable
    def configure(self, main_config):
        # Our own config schema, defines default values
        schema = {
            'ckanext.disablepwreset.permit_reset': {'default': False},
        }

        errors = []
        for i in schema:
            v = main_config.get(i, None)
            if v is not None:
                try:
                    config[i] = v
                except ConfigError as e:
                    errors.append(str(e))
            elif 'default' in schema[i]:
                config[i] = schema[i]['default']

        if len(errors):
            raise ConfigError("\n".join(errors))

        # make sure all strings are unicode formatted
        for key, value in config.iteritems():
            if isinstance(value, str):
                config[key] = unicode(value, encoding='utf-8')
