# encoding: utf-8

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
        toolkit.add_template_directory(config_, u'templates')
        toolkit.add_public_directory(config_, u'public')
        toolkit.add_resource(u'fanstatic', u'disablepwreset')

    # IAuthFunctions
    def get_auth_functions(self):
        return {
            u'request_reset': request_reset,
            u'user_reset': user_reset
        }

    # IConfigurable
    def configure(self, main_config):
        # Our own config schema, defines default values
        schema = {
            u'ckanext.disablepwreset.permit_reset': {
                u'default': False,
                u'parse': toolkit.asbool
            },
        }

        errors = []
        for i in schema:
            v = main_config.get(i, None)
            if v is not None:
                if u'parse' in schema[i]:
                    v = (schema[i][u'parse'])(v)
                try:
                    config[i] = v
                except ConfigError as e:
                    errors.append(str(e))
            elif u'default' in schema[i]:
                config[i] = schema[i][u'default']

        if len(errors):
            raise ConfigError(u'\n'.join(errors))

        # make sure all strings are unicode formatted
        for key, value in config.iteritems():
            if isinstance(value, str):
                config[key] = unicode(value, encoding=u'utf-8')
