from ckan.plugins import (
    toolkit,
    implements,
    IConfigurer,
    IPackageController,
    IResourceController,
    SingletonPlugin
)
from ckantoolkit import config
from ckanext.fluent.validators import fluent_text_output
from ckanext.scheming.helpers import scheming_language_text


class BostonSchema(SingletonPlugin):
    implements(IConfigurer)
    implements(IPackageController, inherit=True)
    implements(IResourceController, inherit=True)

    # IConfigurer
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

    # IPackageController
    def after_create(self, context, pkg_dict):
        if 'title_translated' in pkg_dict:
            title_translated = fluent_text_output(pkg_dict.get('title_translated'))
            if title_translated.get('en'):
                title = title_translated.get('en')
            else:
                title = scheming_language_text(title_translated, config.get('ckan.locale_default', 'en'))
            if title:
                pkg_dict['title'] = title

        if 'notes_translated' in pkg_dict:
            notes_translated = fluent_text_output(pkg_dict.get('notes_translated'))
            if notes_translated.get('en'):
                notes = notes_translated.get('en')
            else:
                notes = scheming_language_text(notes_translated, config.get('ckan.locale_default', 'en'))
            if notes:
                pkg_dict['notes'] = notes
        return pkg_dict

    def after_update(self, context, pkg_dict):
        if 'title_translated' in pkg_dict:
            title_translated = fluent_text_output(pkg_dict.get('title_translated'))
            if title_translated.get('en'):
                # Default to en if available
                title = title_translated.get('en')
            else:
                # Get local language version if available
                title = scheming_language_text(title_translated, config.get('ckan.locale_default', 'en'))
            if title:
                pkg_dict['title'] = title

        if 'notes_translated' in pkg_dict:
            notes_translated = fluent_text_output(pkg_dict.get('notes_translated'))
            if notes_translated.get('en'):
                notes = notes_translated.get('en')
            else:
                notes = scheming_language_text(notes_translated, config.get('ckan.locale_default', 'en'))
            if notes:
                pkg_dict['notes'] = notes
        return pkg_dict

    # IResourceController
    def before_create(self, context, resource):
        if 'name_translated' in resource:
            name_translated = fluent_text_output(resource.get('name_translated'))
            if name_translated.get('en'):
                name = name_translated.get('en')
            else:
                name = scheming_language_text(name_translated, config.get('ckan.locale_default', 'en'))
            if name:
                resource['name'] = name
        if 'description_translated' in resource:
            description_translated = fluent_text_output(resource.get('description_translated'))
            if description_translated.get('en'):
                description = description_translated.get('en')
            else:
                description = scheming_language_text(description_translated, config.get('ckan.locale_default', 'en'))
            if description:
                resource['description'] = description
        return resource

    def before_update(self, context, current, resource):
        if 'name_translated' in resource:
            name_translated = fluent_text_output(resource.get('name_translated'))
            if name_translated.get('en'):
                name = name_translated.get('en')
            else:
                name = scheming_language_text(name_translated, config.get('ckan.locale_default', 'en'))
            if name:
                resource['name'] = name
        if 'description_translated' in resource:
            description_translated = fluent_text_output(resource.get('description_translated'))
            if description_translated.get('en'):
                description = description_translated.get('en')
            else:
                description = scheming_language_text(description_translated, config.get('ckan.locale_default', 'en'))
            if description:
                resource['description'] = description
        return resource
