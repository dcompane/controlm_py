# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.325
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import controlm_py
from controlm_py.api.provision_api import ProvisionApi  # noqa: E501
from controlm_py.rest import ApiException


class TestProvisionApi(unittest.TestCase):
    """ProvisionApi unit test stubs"""

    def setUp(self):
        self.api = ProvisionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_provision_repo(self):
        """Test case for add_provision_repo

        Add a configuration of a local repository.  # noqa: E501
        """
        pass

    def test_cancel_upgrade_activity(self):
        """Test case for cancel_upgrade_activity

        Cancel upgrade activity  # noqa: E501
        """
        pass

    def test_delete_provision_repo(self):
        """Test case for delete_provision_repo

        Delete configuration of a local repository  # noqa: E501
        """
        pass

    def test_delete_upgrade_activity(self):
        """Test case for delete_upgrade_activity

        Delete upgrade activity status for specific upgrade id.  # noqa: E501
        """
        pass

    def test_get_all_upgrade_activities_status(self):
        """Test case for get_all_upgrade_activities_status

        Get all upgrade activities status.  # noqa: E501
        """
        pass

    def test_get_deploy_versions(self):
        """Test case for get_deploy_versions

        Get available versions for upgrade.  # noqa: E501
        """
        pass

    def test_get_eligible_agents_for_upgrade(self):
        """Test case for get_eligible_agents_for_upgrade

        Get eligible agents for upgrade that match the requested search criteria.  # noqa: E501
        """
        pass

    def test_get_images(self):
        """Test case for get_images

        get list of available images for the requested OS  # noqa: E501
        """
        pass

    def test_get_provision_repo(self):
        """Test case for get_provision_repo

        Get the configuration of the local repo from EM  # noqa: E501
        """
        pass

    def test_get_upgrade_activity_log(self):
        """Test case for get_upgrade_activity_log

        Returns log of upgrade activity.  # noqa: E501
        """
        pass

    def test_get_upgrade_activity_status_per_upgrade_id(self):
        """Test case for get_upgrade_activity_status_per_upgrade_id

        Get upgrade activity status for specific upgrade id.  # noqa: E501
        """
        pass

    def test_list_provision_repos(self):
        """Test case for list_provision_repos

        Get the configuration of all the local repos from EM  # noqa: E501
        """
        pass

    def test_retry_upgrade_activity(self):
        """Test case for retry_upgrade_activity

        Retry upgrade activity  # noqa: E501
        """
        pass

    def test_transfer_and_install_product(self):
        """Test case for transfer_and_install_product

        Transfer and install a product on an agent  # noqa: E501
        """
        pass

    def test_uninstall_product(self):
        """Test case for uninstall_product

        Uninstall a product from an agent  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()