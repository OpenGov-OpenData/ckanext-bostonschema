from ckanapi import LocalCKAN

def nonsysadmin_user_choices(field):
    """
    Return the non-sysadmin users as a choice list
    """
    lc = LocalCKAN(username='')
    return [
        {'value': u['id'], 'label': u['display_name']}
        for u in lc.action.user_list() if not u['sysadmin']]
