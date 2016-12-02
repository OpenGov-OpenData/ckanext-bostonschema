import json

from ckanext.bostonschema import helpers

from ckan.plugins import (toolkit, IConfigurer, SingletonPlugin, implements,
    ITemplateHelpers, IPermissionLabels)
from ckan.lib.plugins import DefaultPermissionLabels

class BostonSchema(SingletonPlugin, DefaultPermissionLabels):
    implements(IConfigurer)
    implements(ITemplateHelpers)
    implements(IPermissionLabels)

    def update_config(self, config):
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "static")

        config['scheming.presets'] = """
ckanext.scheming:presets.json
ckanext.fluent:presets.json
ckanext.bostonschema:schemas/presets.yaml
"""
        config['scheming.dataset_schemas'] = """
ckanext.bostonschema:schemas/dataset.yaml
"""

    def get_helpers(self):
        return {'nonsysadmin_user_choices': helpers.nonsysadmin_user_choices}

    def get_dataset_labels(self, dataset_obj):
        view_users = json.loads(dataset_obj.extras.get('view_users', '[]'))
        labels = super(BostonSchema, self).get_dataset_labels(dataset_obj)
        return labels + [u'view-%s' % u for u in view_users]

    def get_user_dataset_labels(self, user_obj):
        labels = super(BostonSchema, self).get_user_dataset_labels(user_obj)
        if user_obj:
            labels.append(u'view-%s' % user_obj.id)
        return labels
