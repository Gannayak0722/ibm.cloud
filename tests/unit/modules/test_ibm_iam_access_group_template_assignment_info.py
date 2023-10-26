# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_iam_access_group_template_assignment_info

try:
    from .common import DetailedResponseMock
    from ibm_cloud_sdk_core import ApiException
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def mock_operations(func):
    def wrapper(self):
        # Make sure the imports are correct in both test and module packages.
        self.assertIsNone(MISSING_IMPORT_EXC)
        self.assertIsNone(ibm_iam_access_group_template_assignment_info.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.read_patcher = patch('plugins.modules.ibm_iam_access_group_template_assignment_info.IamAccessGroupsV2.get_assignment')
        self.read_mock = self.read_patcher.start()
        self.list_patcher = patch('plugins.modules.ibm_iam_access_group_template_assignment_info.IamAccessGroupsV2.list_assignments')
        self.list_mock = self.list_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.read_patcher.stop()
        self.list_patcher.stop()

    return wrapper


class TestListTemplateAssignmentResponseModuleInfo(ModuleTestCase):
    """
    Test class for ListTemplateAssignmentResponse module testing.
    """

    @mock_operations
    def test_read_ibm_iam_access_group_template_assignment_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'assignment_id': 'testString',
            'transaction_id': 'testString',
            'verbose': False,
        }

        headers = {
            'ETag': 'my-etag-value'
        }

        self.read_mock.return_value = DetailedResponseMock(datasource, headers)

        set_module_args({
            'assignment_id': 'testString',
            'transaction_id': 'testString',
            'verbose': False,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            ibm_iam_access_group_template_assignment_info.main()

        self.assertEqual(result.exception.args[0]['etag'], 'my-etag-value')
        for field, value in datasource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        self.read_mock.assert_called_once_with(
            assignment_id='testString',
            transaction_id='testString',
            verbose=False,
        )

    @mock_operations
    def test_read_ibm_iam_access_group_template_assignment_failed(self):
        """Test the "read" path - failed."""
        self.read_mock.side_effect = ApiException(400, message='Read ibm_iam_access_group_template_assignment error')

        set_module_args({
            'assignment_id': 'testString',
            'transaction_id': 'testString',
            'verbose': False,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            ibm_iam_access_group_template_assignment_info.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Read ibm_iam_access_group_template_assignment error')

        self.read_mock.assert_called_once_with(
            assignment_id='testString',
            transaction_id='testString',
            verbose=False,
        )

    @mock_operations
    def test_list_ibm_iam_access_group_template_assignment_success(self):
        """Test the "list" path - successful."""
        self.list_mock.return_value = DetailedResponseMock(dict(resources=[]))

        set_module_args({
            'account_id': 'accountID-123',
            'template_id': 'testString',
            'template_version': 'testString',
            'target': 'testString',
            'status': 'accepted',
            'transaction_id': 'testString',
            'limit': 50,
            'offset': 0,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            ibm_iam_access_group_template_assignment_info.main()

        self.assertEqual(result.exception.args[0].get("resources"), [])

        self.list_mock.assert_called_once()

    @mock_operations
    def test_list_ibm_iam_access_group_template_assignment_failed(self):
        """Test the "list" path - failed."""
        self.list_mock.side_effect = ApiException(400, message='List ibm_iam_access_group_template_assignment error')

        set_module_args({
            'account_id': 'accountID-123',
            'template_id': 'testString',
            'template_version': 'testString',
            'target': 'testString',
            'status': 'accepted',
            'transaction_id': 'testString',
            'limit': 50,
            'offset': 0,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            ibm_iam_access_group_template_assignment_info.main()

        self.assertEqual(result.exception.args[0]['msg'], 'List ibm_iam_access_group_template_assignment error')

        self.list_mock.assert_called_once()
