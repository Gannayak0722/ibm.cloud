#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_id
short_description: Manage C(iam_service_ids) for IAM Identity Services.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_service_id) resource for IAM Identity Services.
requirements:
  - "IamIdentityV1"
options:
  account_id:
    description: "ID of the account the service ID belongs to."
    type: str
  apikey:
    description: "Parameters for the API key in the Create service Id V1 REST request."
    type: dict
    suboptions:
      name:
        description: "Name of the API key. The name is not checked for uniqueness. Therefore multiple names
          with the same value can exist. Access is done via the UUID of the API key."
        type: str
      description:
        description: "The optional description of the API key. The 'description' property is only available
          if a description was provided during a create of an API key."
        type: str
      apikey:
        description: "You can optionally passthrough the API key value for this API key. If passed, a
          minimum length validation of 32 characters for that apiKey value is done, i.e. the
          value can contain any characters and can even be non-URL safe, but the minimum length
          requirement must be met. If omitted, the API key management will create an URL safe
          opaque API key value. The value of the API key is checked for uniqueness. Ensure
          enough variations when passing in this value."
        type: str
      store_value:
        description: "Send true or false to set whether the API key value is retrievable in the future by
          using the Get details of an API key request. If you create an API key for a user, you
          must specify C(false) or omit the value. We don't allow storing of API keys for users."
        type: bool
  name:
    description: "Name of the Service Id. The name is not checked for uniqueness. Therefore multiple
      names with the same value can exist. Access is done via the UUID of the Service Id."
    type: str
  unique_instance_crns:
    description: "Optional list of CRNs (string array) which point to the services connected to the
      service ID."
    type: list
    elements: str
  description:
    description: "The optional description of the Service Id. The 'description' property is only
      available if a description was provided during a create of a Service Id."
    type: str
  include_history:
    description: "Defines if the entity history is included in the response."
    type: bool
  if_match:
    description: "Version of the service ID to be updated. Specify the version that you retrieved as
      entity_tag (ETag header) when reading the service ID. This value helps identifying
      parallel usage of this API. Pass * to indicate to update any version available. This
      might result in stale updates."
    type: str
  entity_lock:
    description: "Indicates if the service ID is locked for further write operations. False by
      default."
    type: str
  id:
    description: "Unique ID of the service ID."
    type: str
  include_activity:
    description: "Defines if the entity's activity is included in the response. Retrieving activity
      data is an expensive operation, so only request this when needed."
    type: bool
  state:
    description:
      - Should the resource be present or absent.
    type: str
    default: present
    choices: [present, absent]
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
- name: Create ibm_iam_service_id
  vars:
    api_key_inside_create_service_id_request_model:
      name: 'testString'
      description: 'testString'
      apikey: 'testString'
      store_value: True
  ibm_iam_service_id:
    account_id: 'testString'
    name: 'testString'
    description: 'testString'
    unique_instance_crns: ['testString']
    apikey: '{{ api_key_inside_create_service_id_request_model }}'
    entity_lock: 'false'
    state: present

- name: Update ibm_iam_service_id
  ibm_iam_service_id:
    id: 'testString'
    if_match: 'testString'
    name: 'testString'
    description: 'testString'
    unique_instance_crns: ['testString']
    state: present

- name: Delete ibm_iam_service_id
  ibm_iam_service_id:
    id: 'testString'
    state: absent
'''

RETURN = r'''
context:
  description: "Context with key properties for problem determination."
  type: dict
  contains:
    transaction_id:
      description: "The transaction ID of the inbound REST request."
      type: str
    operation:
      description: "The operation of the inbound REST request."
      type: str
    user_agent:
      description: "The user agent of the inbound REST request."
      type: str
    url:
      description: "The URL of that cluster."
      type: str
    instance_id:
      description: "The instance ID of the server instance processing the request."
      type: str
    thread_id:
      description: "The thread ID of the server instance processing the request."
      type: str
    host:
      description: "The host of the server instance processing the request."
      type: str
    start_time:
      description: "The start time of the request."
      type: str
    end_time:
      description: "The finish time of the request."
      type: str
    elapsed_time:
      description: "The elapsed time in msec."
      type: str
    cluster_name:
      description: "The cluster name."
      type: str
  returned: on success for create, update operations
id:
  description: "Unique identifier of this Service Id."
  type: str
  returned: on success for create, update, delete operations
iam_id:
  description: "Cloud wide identifier for identities of this service ID."
  type: str
  returned: on success for create, update operations
entity_tag:
  description: "Version of the service ID details object. You need to specify this value when updating
    the service ID to avoid stale updates."
  type: str
  returned: on success for create, update operations
crn:
  description: "Cloud Resource Name of the item. Example Cloud Resource Name:
    'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::serviceid:1234-5678-9012'."
  type: str
  returned: on success for create, update operations
locked:
  description: "The service ID cannot be changed if set to true."
  type: bool
  returned: on success for create, update operations
created_at:
  description: "If set contains a date time string of the creation date in ISO format."
  type: str
  returned: on success for create, update operations
modified_at:
  description: "If set contains a date time string of the last modification date in ISO format."
  type: str
  returned: on success for create, update operations
account_id:
  description: "ID of the account the service ID belongs to."
  type: str
  returned: on success for create, update operations
name:
  description: "Name of the Service Id. The name is not checked for uniqueness. Therefore multiple
    names with the same value can exist. Access is done via the UUID of the Service Id."
  type: str
  returned: on success for create, update operations
description:
  description: "The optional description of the Service Id. The 'description' property is only
    available if a description was provided during a create of a Service Id."
  type: str
  returned: on success for create, update operations
unique_instance_crns:
  description: "Optional list of CRNs (string array) which point to the services connected to the
    service ID."
  type: list
  elements: str
  returned: on success for create, update operations
history:
  description: "History of the Service ID."
  type: list
  elements: 'dict'
  contains:
    timestamp:
      description: "Timestamp when the action was triggered."
      type: str
    iam_id:
      description: "IAM ID of the identity which triggered the action."
      type: str
    iam_id_account:
      description: "Account of the identity which triggered the action."
      type: str
    action:
      description: "Action of the history entry."
      type: str
    params:
      description: "Params of the history entry."
      type: list
      elements: str
    message_:
      description: "Message which summarizes the executed action."
      type: str
  returned: on success for create, update operations
apikey:
  description: "Response body format for API key V1 REST requests."
  type: dict
  contains:
    context:
      description: "Context with key properties for problem determination."
      type: dict
      contains:
        transaction_id:
          description: "The transaction ID of the inbound REST request."
          type: str
        operation:
          description: "The operation of the inbound REST request."
          type: str
        user_agent:
          description: "The user agent of the inbound REST request."
          type: str
        url:
          description: "The URL of that cluster."
          type: str
        instance_id:
          description: "The instance ID of the server instance processing the request."
          type: str
        thread_id:
          description: "The thread ID of the server instance processing the request."
          type: str
        host:
          description: "The host of the server instance processing the request."
          type: str
        start_time:
          description: "The start time of the request."
          type: str
        end_time:
          description: "The finish time of the request."
          type: str
        elapsed_time:
          description: "The elapsed time in msec."
          type: str
        cluster_name:
          description: "The cluster name."
          type: str
    id:
      description: "Unique identifier of this API Key."
      type: str
    entity_tag:
      description: "Version of the API Key details object. You need to specify this value when updating
        the API key to avoid stale updates."
      type: str
    crn:
      description: "Cloud Resource Name of the item. Example Cloud Resource Name:
        'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::apikey:1234-9012-5678'."
      type: str
    locked:
      description: "The API key cannot be changed if set to true."
      type: bool
    disabled:
      description: "Defines if API key is disabled, API key cannot be used if 'disabled' is set to true."
      type: bool
    created_at:
      description: "If set contains a date time string of the creation date in ISO format."
      type: str
    created_by:
      description: "IAM ID of the user or service which created the API key."
      type: str
    modified_at:
      description: "If set contains a date time string of the last modification date in ISO format."
      type: str
    name:
      description: "Name of the API key. The name is not checked for uniqueness. Therefore multiple names
        with the same value can exist. Access is done via the UUID of the API key."
      type: str
    support_sessions:
      description: "Defines if the API key supports sessions. Sessions are only supported for user
        apikeys."
      type: bool
    action_when_leaked:
      description: "Defines the action to take when API key is leaked, valid values are 'none', 'disable'
        and 'delete'."
      type: str
    description:
      description: "The optional description of the API key. The 'description' property is only available
        if a description was provided during a create of an API key."
      type: str
    iam_id:
      description: "The iam_id that this API key authenticates."
      type: str
    account_id:
      description: "ID of the account that this API key authenticates for."
      type: str
    apikey:
      description: "The API key value. This property only contains the API key value for the following
        cases: create an API key, update a service ID API key that stores the API key value as
        retrievable, or get a service ID API key that stores the API key value as retrievable.
        All other operations don't return the API key value, for example all user API key
        related operations, except for create, don't contain the API key value."
      type: str
    history:
      description: "History of the API key."
      type: list
      elements: 'dict'
      contains:
        timestamp:
          description: "Timestamp when the action was triggered."
          type: str
        iam_id:
          description: "IAM ID of the identity which triggered the action."
          type: str
        iam_id_account:
          description: "Account of the identity which triggered the action."
          type: str
        action:
          description: "Action of the history entry."
          type: str
        params:
          description: "Params of the history entry."
          type: list
          elements: str
        message_:
          description: "Message which summarizes the executed action."
          type: str
    activity:
      description: "No description has been provided."
      type: dict
      contains:
        last_authn:
          description: "Time when the entity was last authenticated."
          type: str
        authn_count:
          description: "Authentication count, number of times the entity was authenticated."
          type: int
  returned: on success for create, update operations
activity:
  description: "No description has been provided."
  type: dict
  contains:
    last_authn:
      description: "Time when the entity was last authenticated."
      type: str
    authn_count:
      description: "Authentication count, number of times the entity was authenticated."
      type: int
  returned: on success for create, update operations
status:
  description: The result status of the deletion
  type: str
  returned: on delete
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import IamIdentityV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        account_id=dict(
            type='str',
            required=False),
        # Represents the ApiKeyInsideCreateServiceIdRequest Python class
        apikey=dict(
            type='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
                apikey=dict(
                    type='str',
                    no_log=True,
                    required=False),
                store_value=dict(
                    type='bool',
                    required=False),
            ),
            no_log=True,
            required=False),
        name=dict(
            type='str',
            required=False),
        unique_instance_crns=dict(
            type='list',
            elements='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        include_history=dict(
            type='bool',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        entity_lock=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
        include_activity=dict(
            type='bool',
            required=False),
        state=dict(
            type='str',
            default='present',
            choices=['absent', 'present'],
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    account_id = module.params["account_id"]
    apikey = module.params["apikey"]
    name = module.params["name"]
    unique_instance_crns = module.params["unique_instance_crns"]
    description = module.params["description"]
    include_history = module.params["include_history"]
    if_match = module.params["if_match"]
    entity_lock = module.params["entity_lock"]
    id = module.params["id"]
    include_activity = module.params["include_activity"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='iam_identity')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamIdentityV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_identity')

    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_service_id(
                id=id,
                include_history=include_history,
                include_activity=include_activity,
            )
        except ApiException as ex:
            if ex.code == 404:
                resource_exists = False
            else:
                module.fail_json(msg=ex.message)
    else:
        # assume resource does not exist
        resource_exists = False

    # Delete path
    if state == "absent":
        if resource_exists:
            try:
                sdk.delete_service_id(
                    id=id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=id, status="deleted")
        else:
            module.exit_json(changed=False, id=id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_service_id(
                    account_id=account_id,
                    name=name,
                    description=description,
                    unique_instance_crns=unique_instance_crns,
                    apikey=apikey,
                    entity_lock=entity_lock,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_service_id(
                    id=id,
                    if_match=if_match,
                    name=name,
                    description=description,
                    unique_instance_crns=unique_instance_crns,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
