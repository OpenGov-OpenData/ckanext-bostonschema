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
