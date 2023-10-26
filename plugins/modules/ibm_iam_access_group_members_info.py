#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_members_info
short_description: Manage C(iam_access_group_members) for IAM Access Groups.
author: 
  - Gannayak Pabra (@Gannayak0722)
  - Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_access_group_members) for IAM Access Groups.
requirements:
  - "IamAccessGroupsV2"
options:
  access_group_id:
    description: "The access group identifier."
    type: str
  transaction_id:
    description: "An optional transaction ID can be passed to your request, which can be useful for
      tracking calls through multiple services by using one identifier. The header key
      must be set to Transaction-Id and the value is anything that you choose. If no
      transaction ID is passed in, then a random ID is generated."
    type: str
  limit:
    description: "Return up to this limit of results where limit is between 0 and 100."
    type: int
  sort:
    description: "If verbose is true, sort the results by id, name, or email."
    type: str
  type:
    description: "Filter the results by member type."
    type: str
  membership_type:
    description: "Filters members by membership type. Filter by C(static), C(dynamic) or C(all).
      C(static) lists the members explicitly added to the access group, and C(dynamic)
      lists the members that are part of the access group at that time via dynamic rules.
      C(all) lists both static and dynamic members."
    type: str
  verbose:
    description: "Return user's email and name for each user ID or the name for each service ID or
      trusted profile."
    type: bool
seealso:
  - name: IBM Cloud Schematics docs
    description: "Use Schematics to run your Ansible playbooks to provision, configure, and manage IBM Cloud resources."
    link: https://cloud.ibm.com/docs/schematics
notes:
  - "Authenticate this module by using an IBM Cloud API key. For more information about working with IBM Cloud API keys,
    see I(Managing API keys): U(https://cloud.ibm.com/docs/account?topic=account-manapikey)."
  - "To configure the authentication, set your IBM Cloud API key on the C(IC_API_KEY) environment variable.
    The API key will be used to authenticate all IBM Cloud modules that use this environment variable."
'''

EXAMPLES = r'''

- name: List ibm_iam_access_group_members
  ibm_iam_access_group_members_info:
    access_group_id: 'testString'
    transaction_id: 'testString'
    membership_type: 'static'
    limit: 50
    type: 'testString'
    verbose: False
    sort: 'testString'
'''

RETURN = r'''
members:
  description: "A list with all ListGroupMembersResponseMember instances."
  type: list
  elements: 'dict'
  contains:
    iam_id:
      description: "The IBMid or Service Id of the member."
      type: str
    type:
      description: "The member type - either C(user), C(service) or C(profile)."
      type: str
    membership_type:
      description: "The membership type - either C(static) or C(dynamic)."
      type: str
    name:
      description: "The user's or service id's name."
      type: str
    email:
      description: "If the member type is user, this is the user's email."
      type: str
    description:
      description: "If the member type is service, this is the service id's description."
      type: str
    href:
      description: "A url to the given member resource."
      type: str
    created_at:
      description: "The timestamp the membership was created at."
      type: str
    created_by_id:
      description: "The C(iam_id) of the entity that created the membership."
      type: str
  returned: on success for list operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import IamAccessGroupsV2
    from ibm_platform_services.iam_access_groups_v2 import AccessGroupMembersPager
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        access_group_id=dict(
            type='str',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        limit=dict(
            type='int',
            required=False),
        sort=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            required=False),
        membership_type=dict(
            type='str',
            required=False),
        verbose=dict(
            type='bool',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    access_group_id = module.params["access_group_id"]
    transaction_id = module.params["transaction_id"]
    limit = module.params["limit"]
    sort = module.params["sort"]
    type = module.params["type"]
    membership_type = module.params["membership_type"]
    verbose = module.params["verbose"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_access_groups')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamAccessGroupsV2(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_access_groups')

    # list
    try:
        pager = AccessGroupMembersPager(
            client=sdk,
            access_group_id=access_group_id,
            transaction_id=transaction_id,
            membership_type=membership_type,
            limit=limit,
            type=type,
            verbose=verbose,
            sort=sort,
        )
        result = pager.get_all()
        module.exit_json(members=result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
