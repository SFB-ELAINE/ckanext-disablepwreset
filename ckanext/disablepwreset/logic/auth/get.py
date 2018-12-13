# encoding: utf-8

import ckan.logic as logic
import ckan.authz as authz

from ckan.common import _

import ckanext.disablepwreset.plugin as p

def _permit_reset():
    permit_reset = p.config['ckanext.disablepwreset.permit_reset']

    if not permit_reset:
        return {'success': False, 'msg': _('Not authorized to '
            'reset password')}
    return {'success': True}

def user_reset(context, data_dict=None):
    return _permit_reset()

def request_reset(context, data_dict=None):
    return _permit_reset()