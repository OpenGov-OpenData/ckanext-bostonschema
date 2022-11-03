import pytest
from ckan.plugins import toolkit
from ckan.tests import factories, helpers


@pytest.mark.usefixtures("clean_db")
class TestBostonSchema():
    def test_create_dataset_with_title_translated(self, app):
        user = factories.Sysadmin()
        context = {'user': user['name']}

        dataset = helpers.call_action(
            'package_create',
            context=context,
            title_translated={'en': 'Test Dataset'},
            name='test-dataset',
            publisher='Department of Innovation and Technology',
            contact_point='Analytics Team',
            contact_point_email='analyticsteam@boston.gov'
        )
        assert dataset.get('title', '') == 'Test Dataset'

    def test_patch_dataset_with_title_translated(self, app):
        user = factories.Sysadmin()
        context = {'user': user['name']}

        dataset = helpers.call_action(
            'package_create',
            context=context,
            title_translated={'en': 'Test Dataset 2'},
            name='test-dataset-2',
            publisher='Department of Innovation and Technology',
            contact_point='Analytics Team',
            contact_point_email='analyticsteam@boston.gov'
        )
        assert dataset.get('title', '') == 'Test Dataset 2'

        new_dataset = helpers.call_action(
            'package_patch',
            context=context,
            id='test-dataset-2',
            title_translated={'en': 'Test Dataset 2 (Revised)'},
        )
        assert new_dataset.get('title', '') == 'Test Dataset 2 (Revised)'

    def test_create_dataset_with_notes_translated(self, app):
        user = factories.Sysadmin()
        context = {'user': user['name']}
        dataset = helpers.call_action(
            'package_create',
            context=context,
            title_translated={'en': 'Test Dataset 3'},
            notes_translated={'en': 'This is a test dataset.'},
            name='test-dataset-3',
            publisher='Department of Innovation and Technology',
            contact_point='Analytics Team',
            contact_point_email='analyticsteam@boston.gov'
        )
        assert dataset.get('title', '') == 'Test Dataset 3'
        assert dataset.get('notes', '') == 'This is a test dataset.'

    def test_patch_dataset_with_notes_translated(self, app):
        user = factories.Sysadmin()
        context = {'user': user['name']}
        dataset = helpers.call_action(
            'package_create',
            context=context,
            title_translated={'en': 'Test Dataset 4'},
            notes_translated={'en': 'This is a test dataset.'},
            name='test-dataset-4',
            publisher='Department of Innovation and Technology',
            contact_point='Analytics Team',
            contact_point_email='analyticsteam@boston.gov'
        )
        assert dataset.get('title', '') == 'Test Dataset 4'
        assert dataset.get('notes', '') == 'This is a test dataset.'

        new_dataset = helpers.call_action(
            'package_patch',
            context=context,
            id='test-dataset-4',
            notes_translated={'en': 'This is a test dataset that has been patched.'},
        )
        assert new_dataset.get('title', '') == 'Test Dataset 4'
        assert new_dataset.get('notes', '') == 'This is a test dataset that has been patched.'

    def test_create_resource_with_name_translated(self, app):
        user = factories.Sysadmin()
        context = {'user': user['name']}
        dataset = helpers.call_action(
            'package_create',
            context=context,
            title_translated={'en': 'Test Dataset 5'},
            name='test-dataset-5',
            publisher='Department of Innovation and Technology',
            contact_point='Analytics Team',
            contact_point_email='analyticsteam@boston.gov'
        )
        resource = helpers.call_action(
            'resource_create',
            context=context,
            package_id=dataset.get('id'),
            name_translated={'en': 'Test Resource'}
        )
        assert dataset.get('title', '') == 'Test Dataset 5'
        assert resource.get('name', '') == 'Test Resource'

    def test_patch_resource_with_name_translated(self, app):
        user = factories.Sysadmin()
        context = {'user': user['name']}
        dataset = helpers.call_action(
            'package_create',
            context=context,
            title_translated={'en': 'Test Dataset 6'},
            name='test-dataset-6',
            publisher='Department of Innovation and Technology',
            contact_point='Analytics Team',
            contact_point_email='analyticsteam@boston.gov'
        )
        resource = helpers.call_action(
            'resource_create',
            context=context,
            package_id=dataset.get('id'),
            name_translated={'en': 'Test Resource 2'}
        )
        assert dataset.get('title', '') == 'Test Dataset 6'
        assert resource.get('name', '') == 'Test Resource 2'

        new_resource = helpers.call_action(
            'resource_patch',
            context=context,
            id=resource.get('id'),
            name_translated={'en': 'Test Resource 2 (Revised)'},
        )
        assert dataset.get('title', '') == 'Test Dataset 6'
        assert new_resource.get('name', '') == 'Test Resource 2 (Revised)'

    def test_create_resource_with_description_translated(self, app):
        user = factories.Sysadmin()
        context = {'user': user['name']}
        dataset = helpers.call_action(
            'package_create',
            context=context,
            title_translated={'en': 'Test Dataset 7'},
            name='test-dataset-7',
            publisher='Department of Innovation and Technology',
            contact_point='Analytics Team',
            contact_point_email='analyticsteam@boston.gov'
        )
        resource = helpers.call_action(
            'resource_create',
            context=context,
            package_id=dataset.get('id'),
            description_translated={'en': 'This is a test resource'}
        )
        assert dataset.get('title', '') == 'Test Dataset 7'
        assert resource.get('description', '') == 'This is a test resource'

    def test_patch_resource_with_name_translated(self, app):
        user = factories.Sysadmin()
        context = {'user': user['name']}
        dataset = helpers.call_action(
            'package_create',
            context=context,
            title_translated={'en': 'Test Dataset 8'},
            name='test-dataset-8',
            publisher='Department of Innovation and Technology',
            contact_point='Analytics Team',
            contact_point_email='analyticsteam@boston.gov'
        )
        resource = helpers.call_action(
            'resource_create',
            context=context,
            package_id=dataset.get('id'),
            description_translated={'en': 'This is a test resource'}
        )
        assert dataset.get('title', '') == 'Test Dataset 8'
        assert resource.get('description', '') == 'This is a test resource'

        new_resource = helpers.call_action(
            'resource_patch',
            context=context,
            id=resource.get('id'),
            description_translated={'en': 'This is a test resource (Revised)'},
        )
        assert dataset.get('title', '') == 'Test Dataset 8'
        assert new_resource.get('description', '') == 'This is a test resource (Revised)'
