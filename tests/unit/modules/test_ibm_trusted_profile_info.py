# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_trusted_profile_info

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
        self.assertIsNone(ibm_trusted_profile_info.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.read_patcher = patch('plugins.modules.ibm_trusted_profile_info.IamIdentityV1.get_profile')
        self.read_mock = self.read_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.read_patcher.stop()

    return wrapper


class TestTrustedProfileModuleInfo(ModuleTestCase):
    """
    Test class for TrustedProfile module testing.
    """

    @mock_operations
    def test_read_ibm_trusted_profile_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'profile_id': 'testString',
            'include_activity': False,
        }

        self.read_mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'profile_id': 'testString',
            'include_activity': False,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_IDENTITY_AUTH_TYPE'] = 'noAuth'
            ibm_trusted_profile_info.main()

        for field, value in datasource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        self.read_mock.assert_called_once_with(
            profile_id='testString',
            include_activity=False,
        )

    @mock_operations
    def test_read_ibm_trusted_profile_failed(self):
        """Test the "read" path - failed."""
        self.read_mock.side_effect = ApiException(400, message='Read ibm_trusted_profile error')

        set_module_args({
            'profile_id': 'testString',
            'include_activity': False,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_IDENTITY_AUTH_TYPE'] = 'noAuth'
            ibm_trusted_profile_info.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Read ibm_trusted_profile error')

        self.read_mock.assert_called_once_with(
            profile_id='testString',
            include_activity=False,
        )
