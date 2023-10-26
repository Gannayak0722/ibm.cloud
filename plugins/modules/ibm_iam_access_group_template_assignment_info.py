#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_template_assignment_info
short_description: Manage C(iam_access_group_template_assignment) for IAM Access Groups.
author: 
  - Gannayak Pabra (@Gannayak0722)
  - Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_access_group_template_assignment) for IAM Access Groups.
requirements:
  - "IamAccessGroupsV2"
options:
  assignment_id:
    description: "Assignment ID."
    type: str
  account_id:
    description: "Enterprise account ID."
    type: str
  template_version:
    description: "Filter results by Template Version."
    type: str
  offset:
    description: "The offset of the first result item to be returned."
    type: int
  transaction_id:
    description: "An optional transaction id for the request."
    type: str
  limit:
    description: "Return up to this limit of results where limit is between 0 and 100."
    type: int
  template_id:
    description: "Filter results by Template Id."
    type: str
  target:
    description: "Filter results by the assignment target."
    type: str
  status:
    description: "Filter results by the assignment status."
    type: str
    choices:
      - "accepted"
      - "in_progress"
      - "succeeded"
      - "failed"
  verbose:
    description: "Returns resources access group template assigned, possible values C(true) or
      C(false)."
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
- name: Read ibm_iam_access_group_template_assignment
  ibm_iam_access_group_template_assignment_info:
    assignment_id: 'testString'
    transaction_id: 'testString'
    verbose: False

- name: List ibm_iam_access_group_template_assignment
  ibm_iam_access_group_template_assignment_info:
    account_id: 'accountID-123'
    template_id: 'testString'
    template_version: 'testString'
    target: 'testString'
    status: 'accepted'
    transaction_id: 'testString'
    limit: 50
    offset: 0
'''

RETURN = r'''
id:
  description: "The ID of the assignment."
  type: str
  returned: on success for read operation
account_id:
  description: "The ID of the account that the assignment belongs to."
  type: str
  returned: on success for read operation
template_id:
  description: "The ID of the template that the assignment is based on."
  type: str
  returned: on success for read operation
template_version:
  description: "The version of the template that the assignment is based on."
  type: str
  returned: on success for read operation
target_type:
  description: "The type of the entity that the assignment applies to."
  type: str
  returned: on success for read operation
target:
  description: "The ID of the entity that the assignment applies to."
  type: str
  returned: on success for read operation
operation:
  description: "The operation that the assignment applies to (e.g. 'create', 'update', 'delete')."
  type: str
  returned: on success for read operation
status:
  description: "The status of the assignment (e.g. 'pending', 'success', 'failure')."
  type: str
  returned: on success for read operation
resources:
  description: "List of resources for the assignment."
  type: list
  elements: 'dict'
  contains:
    target:
      description: "The ID of the entity that the resource list applies to."
      type: str
    group:
      description: "Assignment Resource Access Group."
      type: dict
      contains:
        group:
          description: "Assignment resource entry."
          type: dict
          contains:
            id:
              description: "Assignment Resource Entry Id."
              type: str
            name:
              description: "Optional name of the resource."
              type: str
            version:
              description: "Optional version of the resource."
              type: str
            resource:
              description: "Resource in assignment resource entry."
              type: str
            error:
              description: "Error in assignment resource entry."
              type: str
            operation:
              description: "Optional operation on the resource."
              type: str
            status:
              description: "Status of assignment resource entry."
              type: str
        members:
          description: "List of member resources of the group."
          type: list
          elements: 'dict'
          contains:
            id:
              description: "Assignment Resource Entry Id."
              type: str
            name:
              description: "Optional name of the resource."
              type: str
            version:
              description: "Optional version of the resource."
              type: str
            resource:
              description: "Resource in assignment resource entry."
              type: str
            error:
              description: "Error in assignment resource entry."
              type: str
            operation:
              description: "Optional operation on the resource."
              type: str
            status:
              description: "Status of assignment resource entry."
              type: str
        rules:
          description: "List of rules associated with the group."
          type: list
          elements: 'dict'
          contains:
            id:
              description: "Assignment Resource Entry Id."
              type: str
            name:
              description: "Optional name of the resource."
              type: str
            version:
              description: "Optional version of the resource."
              type: str
            resource:
              description: "Resource in assignment resource entry."
              type: str
            error:
              description: "Error in assignment resource entry."
              type: str
            operation:
              description: "Optional operation on the resource."
              type: str
            status:
              description: "Status of assignment resource entry."
              type: str
    policy_template_references:
      description: "List of policy template references for the resource list."
      type: list
      elements: 'dict'
      contains:
        id:
          description: "Assignment Resource Entry Id."
          type: str
        name:
          description: "Optional name of the resource."
          type: str
        version:
          description: "Optional version of the resource."
          type: str
        resource:
          description: "Resource in assignment resource entry."
          type: str
        error:
          description: "Error in assignment resource entry."
          type: str
        operation:
          description: "Optional operation on the resource."
          type: str
        status:
          description: "Status of assignment resource entry."
          type: str
  returned: on success for read operation
href:
  description: "The URL of the assignment resource."
  type: str
  returned: on success for read operation
created_at:
  description: "The date and time when the assignment was created."
  type: str
  returned: on success for read operation
created_by_id:
  description: "The user or system that created the assignment."
  type: str
  returned: on success for read operation
last_modified_at:
  description: "The date and time when the assignment was last updated."
  type: str
  returned: on success for read operation
last_modified_by_id:
  description: "The user or system that last updated the assignment."
  type: str
  returned: on success for read operation
limit:
  description: "Maximum number of items returned in the response."
  type: int
  returned: on success for list operation
offset:
  description: "Index of the first item returned in the response."
  type: int
  returned: on success for list operation
total_count:
  description: "Total number of items matching the query."
  type: int
  returned: on success for list operation
first:
  description: "A link object."
  type: dict
  contains:
    href:
      description: "A string containing the link's URL."
      type: str
  returned: on success for list operation
last:
  description: "A link object."
  type: dict
  contains:
    href:
      description: "A string containing the link's URL."
      type: str
  returned: on success for list operation
assignments:
  description: "List of template assignments."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "The ID of the assignment."
      type: str
    account_id:
      description: "The ID of the account that the assignment belongs to."
      type: str
    template_id:
      description: "The ID of the template that the assignment is based on."
      type: str
    template_version:
      description: "The version of the template that the assignment is based on."
      type: str
    target_type:
      description: "The type of the entity that the assignment applies to."
      type: str
      choices:
        - 'Account'
        - 'AccountGroup'
    target:
      description: "The ID of the entity that the assignment applies to."
      type: str
    operation:
      description: "The operation that the assignment applies to (e.g. 'assign', 'update', 'remove')."
      type: str
      choices:
        - 'assign'
        - 'update'
        - 'remove'
    status:
      description: "The status of the assignment (e.g. 'accepted', 'in_progress', 'succeeded', 'failed',
        'superseded')."
      type: str
      choices:
        - 'accepted'
        - 'in_progress'
        - 'succeeded'
        - 'failed'
        - 'superseded'
    href:
      description: "The URL of the assignment resource."
      type: str
    created_at:
      description: "The date and time when the assignment was created."
      type: str
    created_by_id:
      description: "The user or system that created the assignment."
      type: str
    last_modified_at:
      description: "The date and time when the assignment was last updated."
      type: str
    last_modified_by_id:
      description: "The user or system that last updated the assignment."
      type: str
  returned: on success for list operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
etag:
  description: The ETag value associated with the C(TemplateAssignmentVerboseResponse)
  returned: on read
  type: str
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import IamAccessGroupsV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        assignment_id=dict(
            type='str',
            required=False),
        account_id=dict(
            type='str',
            required=False),
        template_version=dict(
            type='str',
            required=False),
        offset=dict(
            type='int',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        limit=dict(
            type='int',
            required=False),
        template_id=dict(
            type='str',
            required=False),
        target=dict(
            type='str',
            required=False),
        status=dict(
            type='str',
            choices=[
                'accepted',
                'in_progress',
                'succeeded',
                'failed',
            ],
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

    assignment_id = module.params["assignment_id"]
    account_id = module.params["account_id"]
    template_version = module.params["template_version"]
    offset = module.params["offset"]
    transaction_id = module.params["transaction_id"]
    limit = module.params["limit"]
    template_id = module.params["template_id"]
    target = module.params["target"]
    status = module.params["status"]
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

    if assignment_id:
        # read
        try:
            response = sdk.get_assignment(
                assignment_id=assignment_id,
                transaction_id=transaction_id,
                verbose=verbose,
            )

            result = response.get_result()
            etag = response.get_headers().get('ETag')

            module.exit_json(etag=etag, **result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)

    # list
    try:
        response = sdk.list_assignments(
            account_id=account_id,
            template_id=template_id,
            template_version=template_version,
            target=target,
            status=status,
            transaction_id=transaction_id,
            limit=limit,
            offset=offset,
        )

        result = response.get_result()

        module.exit_json(**result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
