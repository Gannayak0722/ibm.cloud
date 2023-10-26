#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_template_info
short_description: Manage C(iam_access_group_template) for IAM Access Groups.
author: 
  - Gannayak Pabra (@Gannayak0722)
  - Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_access_group_template) for IAM Access Groups.
requirements:
  - "IamAccessGroupsV2"
options:
  account_id:
    description: "Enterprise account ID."
    type: str
  transaction_id:
    description: "An optional transaction id for the request."
    type: str
  limit:
    description: "Return up to this limit of results where limit is between 0 and 100."
    type: int
  verbose:
    description: "If C(verbose=true), IAM resource details are returned. If performance is a concern,
      leave the C(verbose) parameter off so that details are not retrieved."
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

- name: List ibm_iam_access_group_template
  ibm_iam_access_group_template_info:
    account_id: 'accountID-123'
    transaction_id: 'testString'
    limit: 50
    verbose: True
'''

RETURN = r'''
group_templates:
  description: "A list with all GroupTemplate instances."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "The ID of the access group template."
      type: str
    name:
      description: "The name of the access group template."
      type: str
    description:
      description: "The description of the access group template."
      type: str
    version:
      description: "The version of the access group template."
      type: str
    committed:
      description: "A boolean indicating whether the access group template is committed. You must commit a
        template before you can assign it to child accounts."
      type: bool
    group:
      description: "Access Group Component."
      type: dict
      contains:
        name:
          description: "Give the access group a unique name that doesn't conflict with other templates access
            group name in the given account. This is shown in child accounts."
          type: str
        description:
          description: "Access group description. This is shown in child accounts."
          type: str
        members:
          description: "Array of enterprise users to add to the template. All enterprise users that you add to
            the template must be invited to the child accounts where the template is assigned."
          type: dict
          contains:
            users:
              description: "Array of enterprise users to add to the template. All enterprise users that you add to
                the template must be invited to the child accounts where the template is assigned."
              type: list
              elements: str
            services:
              description: "Array of service IDs to add to the template."
              type: list
              elements: str
            action_controls:
              description: "Control whether or not access group administrators in child accounts can add and
                remove members from the enterprise-managed access group in their account."
              type: dict
              contains:
                add:
                  description: "Action control for adding child account members to an enterprise-managed access group.
                    If an access group administrator in a child account adds a member, they can always
                    remove them. Note that if conflicts arise between an update to this control in a new
                    version and members added by an administrator in the child account, you must resolve
                    those conflicts in the child account. This prevents breaking access in the child
                    account. For more information, see [Working with versions]
                    (https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-working-with-versions#new-version-scenarios)."
                  type: bool
                remove:
                  description: "Action control for removing enterprise-managed members from an enterprise-managed
                    access group. Note that if an enterprise member is removed from an enterprise-managed
                    access group in a child account and you reassign the template, the membership is
                    reinstated."
                  type: bool
        assertions:
          description: "Assertions Input Component."
          type: dict
          contains:
            rules:
              description: "Dynamic rules to automatically add federated users to access groups based on specific
                identity attributes."
              type: list
              elements: 'dict'
              contains:
                name:
                  description: "Dynamic rule name."
                  type: str
                expiration:
                  description: "Session duration in hours. Access group membership is revoked after this time period
                    expires. Users must log back in to refresh their access group membership."
                  type: int
                realm_name:
                  description: "The identity provider (IdP) URL."
                  type: str
                conditions:
                  description: "Conditions of membership. You can think of this as a key:value pair."
                  type: list
                  elements: 'dict'
                  contains:
                    claim:
                      description: "The key in the key:value pair."
                      type: str
                    operator:
                      description: "Compares the claim and the value."
                      type: str
                    value:
                      description: "The value in the key:value pair."
                      type: str
                action_controls:
                  description: "Control whether or not access group administrators in child accounts can update and
                    remove this dynamic rule in the enterprise-managed access group in their account.This
                    overrides outer level AssertionsActionControls."
                  type: dict
                  contains:
                    remove:
                      description: "Action control for removing this enterprise-managed dynamic rule."
                      type: bool
            action_controls:
              description: "Control whether or not access group administrators in child accounts can add, remove,
                and update dynamic rules for the enterprise-managed access group in their account. The
                inner level RuleActionControls override these C(remove) and C(update) action controls."
              type: dict
              contains:
                add:
                  description: "Action control for adding dynamic rules to an enterprise-managed access group. If an
                    access group administrator in a child account adds a dynamic rule, they can always
                    update or remove it. Note that if conflicts arise between an update to this control
                    and rules added or updated by an administrator in the child account, you must resolve
                    those conflicts in the child account. This prevents breaking access that the rules
                    might grant in the child account. For more information, see [Working with versions]."
                  type: bool
                remove:
                  description: "Action control for removing enterprise-managed dynamic rules in an enterprise-managed
                    access group. Note that if a rule is removed from an enterprise-managed access group
                    by an administrator in a child account and and you reassign the template, the rule is
                    reinstated."
                  type: bool
        action_controls:
          description: "Access group action controls component."
          type: dict
          contains:
            access:
              description: "Control whether or not access group administrators in child accounts can add access
                policies to the enterprise-managed access group in their account."
              type: dict
              contains:
                add:
                  description: "Action control for adding access policies to an enterprise-managed access group in a
                    child account. If an access group administrator in a child account adds a policy, they
                    can always update or remove it. Note that if conflicts arise between an update to this
                    control in a new version and polices added to the access group by an administrator in
                    a child account, you must resolve those conflicts in the child account. This prevents
                    breaking access in the child account. For more information, see [Working with
                    versions](https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-working-with-versions#new-version-scenarios)."
                  type: bool
    policy_template_references:
      description: "References to policy templates assigned to the access group template."
      type: list
      elements: 'dict'
      contains:
        id:
          description: "Policy template ID."
          type: str
        version:
          description: "Policy template version."
          type: str
    href:
      description: "The URL of the access group template resource."
      type: str
    created_at:
      description: "The date and time when the access group template was created."
      type: str
    created_by_id:
      description: "The ID of the user who created the access group template."
      type: str
    last_modified_at:
      description: "The date and time when the access group template was last modified."
      type: str
    last_modified_by_id:
      description: "The ID of the user who last modified the access group template."
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
    from ibm_platform_services.iam_access_groups_v2 import TemplatesPager
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        account_id=dict(
            type='str',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        limit=dict(
            type='int',
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

    account_id = module.params["account_id"]
    transaction_id = module.params["transaction_id"]
    limit = module.params["limit"]
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
        pager = TemplatesPager(
            client=sdk,
            account_id=account_id,
            transaction_id=transaction_id,
            limit=limit,
            verbose=verbose,
        )
        result = pager.get_all()
        module.exit_json(group_templates=result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
