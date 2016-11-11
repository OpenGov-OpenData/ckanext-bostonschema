
from ckan.plugins import toolkit, IConfigurer, SingletonPlugin, implements

class BostonSchema(SingletonPlugin):
    implements(IConfigurer)

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

