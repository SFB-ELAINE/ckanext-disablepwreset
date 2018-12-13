# encoding: utf-8

from ckan.plugins import toolkit
from ckan.common import _

from ckanext.disablepwreset.plugin import config


@toolkit.chained_auth_function
@toolkit.auth_allow_anonymous_access
def user_reset(next_auth, context, data_dict=None):
    return _permit_reset(next_auth, context, data_dict)


@toolkit.chained_auth_function
@toolkit.auth_allow_anonymous_access
def request_reset(next_auth, context, data_dict=None):
    return _permit_reset(next_auth, context, data_dict)


def _permit_reset(next_auth, context, data_dict):
    permit_reset = config[u'ckanext.disablepwreset.permit_reset']

    if not permit_reset:
        return {
            u'success': False,
            u'msg': _(u'Not authorized to reset password')
        }
    return next_auth(context, data_dict)
