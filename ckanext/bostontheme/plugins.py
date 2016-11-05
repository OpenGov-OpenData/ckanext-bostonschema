
from ckan.plugins import toolkit, IConfigurer, SingletonPlugin, implements

class CustomTheme(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config):
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "static")

        config['scheming.presets'] = """
ckanext.scheming:presets.json
"""
        config['scheming.dataset_schemas'] = """
ckanext.bostontheme:schemas/dataset.yaml
"""

