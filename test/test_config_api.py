# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.340
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import controlm_py
from controlm_py.api.config_api import ConfigApi  # noqa: E501
from controlm_py.rest import ApiException


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_agent(self):
        """Test case for add_agent

        add agent to Server  # noqa: E501
        """
        pass

    def test_add_agentless_host(self):
        """Test case for add_agentless_host

        add agentless host to Server  # noqa: E501
        """
        pass

    def test_add_archive_rule(self):
        """Test case for add_archive_rule

        Add Workload Archiving rule  # noqa: E501
        """
        pass

    def test_add_external_user(self):
        """Test case for add_external_user

        Add and external user  # noqa: E501
        """
        pass

    def test_add_external_user_for_site(self):
        """Test case for add_external_user_for_site

        Add and external user for site  # noqa: E501
        """
        pass

    def test_add_external_user_or_user_group_to_mft_folder(self):
        """Test case for add_external_user_or_user_group_to_mft_folder

        Add external user or user groups to virtual folder external users list.  # noqa: E501
        """
        pass

    def test_add_external_user_or_user_group_to_mft_folder_for_site(self):
        """Test case for add_external_user_or_user_group_to_mft_folder_for_site

        Add external user or user groups to virtual folder external users list for site.  # noqa: E501
        """
        pass

    def test_add_external_user_to_mft_user_group_for_site(self):
        """Test case for add_external_user_to_mft_user_group_for_site

        Add external user to user groups for site.  # noqa: E501
        """
        pass

    def test_add_gateway(self):
        """Test case for add_gateway

        add gateway.  # noqa: E501
        """
        pass

    def test_add_gateway_for_site(self):
        """Test case for add_gateway_for_site

        add gateway for site.  # noqa: E501
        """
        pass

    def test_add_host_restriction(self):
        """Test case for add_host_restriction

        Add new Host Restriction.  # noqa: E501
        """
        pass

    def test_add_host_to_hostgroup(self):
        """Test case for add_host_to_hostgroup

        add agent to hostgroup  # noqa: E501
        """
        pass

    def test_add_hub_to_cluster(self):
        """Test case for add_hub_to_cluster

        add hub to cluster.  # noqa: E501
        """
        pass

    def test_add_hub_to_cluster_for_site(self):
        """Test case for add_hub_to_cluster_for_site

        add hub to cluster for site.  # noqa: E501
        """
        pass

    def test_add_ldap_group_to_mft_user_group_for_site(self):
        """Test case for add_ldap_group_to_mft_user_group_for_site

        Add LDAP group to group for site.  # noqa: E501
        """
        pass

    def test_add_mft_folder(self):
        """Test case for add_mft_folder

        Add virtual folder  # noqa: E501
        """
        pass

    def test_add_mft_folder_for_site(self):
        """Test case for add_mft_folder_for_site

        Add virtual folder for site  # noqa: E501
        """
        pass

    def test_add_mft_processing_rule_for_site(self):
        """Test case for add_mft_processing_rule_for_site

        Add MFTE processing rule for site  # noqa: E501
        """
        pass

    def test_add_mft_user_group(self):
        """Test case for add_mft_user_group

        Add user group.  # noqa: E501
        """
        pass

    def test_add_mft_user_group_for_site(self):
        """Test case for add_mft_user_group_for_site

        Add user group for site.  # noqa: E501
        """
        pass

    def test_add_pgp_template(self):
        """Test case for add_pgp_template

        Add PGP Template  # noqa: E501
        """
        pass

    def test_add_remote_host(self):
        """Test case for add_remote_host

        add remote host to Server  # noqa: E501
        """
        pass

    def test_add_role(self):
        """Test case for add_role

        Add Authorization Role  # noqa: E501
        """
        pass

    def test_add_role_to_ldap_group(self):
        """Test case for add_role_to_ldap_group

        Add a role to LDAP group  # noqa: E501
        """
        pass

    def test_add_role_to_user(self):
        """Test case for add_role_to_user

        Add a role to user  # noqa: E501
        """
        pass

    def test_add_secret(self):
        """Test case for add_secret

        Add a new secret  # noqa: E501
        """
        pass

    def test_add_server(self):
        """Test case for add_server

        Discover and add server to the system  # noqa: E501
        """
        pass

    def test_add_ssh_key(self):
        """Test case for add_ssh_key

        Add an SSH key to the control-m server.  # noqa: E501
        """
        pass

    def test_add_user(self):
        """Test case for add_user

        Add user  # noqa: E501
        """
        pass

    def test_add_wda_gateway(self):
        """Test case for add_wda_gateway

        add DataAssurance gateway.  # noqa: E501
        """
        pass

    def test_add_zos_template(self):
        """Test case for add_zos_template

        Add z/OS Template  # noqa: E501
        """
        pass

    def test_authorize_mft_ssh_cluster(self):
        """Test case for authorize_mft_ssh_cluster

        Authorize SSH Cluster  # noqa: E501
        """
        pass

    def test_authorize_mft_ssh_host(self):
        """Test case for authorize_mft_ssh_host

        Authorize SSH Host  # noqa: E501
        """
        pass

    def test_authorize_ssh_known_agentlesshost(self):
        """Test case for authorize_ssh_known_agentlesshost

        Authorize  # noqa: E501
        """
        pass

    def test_authorize_ssh_known_remotehost(self):
        """Test case for authorize_ssh_known_remotehost

        Authorize  # noqa: E501
        """
        pass

    def test_change_user_password(self):
        """Test case for change_user_password

        Change user password  # noqa: E501
        """
        pass

    def test_create_agent_certificate_signing_request(self):
        """Test case for create_agent_certificate_signing_request

        Create certificate signing request (CSR).  # noqa: E501
        """
        pass

    def test_create_gateway(self):
        """Test case for create_gateway

        Add gateway for server.  # noqa: E501
        """
        pass

    def test_create_run_as_user(self):
        """Test case for create_run_as_user

        Add a new Run-as user  # noqa: E501
        """
        pass

    def test_ctm_pause(self):
        """Test case for ctm_pause

        Pause the CTM server.  # noqa: E501
        """
        pass

    def test_ctm_server_rename(self):
        """Test case for ctm_server_rename

        CTM Server Rename.  # noqa: E501
        """
        pass

    def test_ctm_server_rename_preview(self):
        """Test case for ctm_server_rename_preview

        CTM Server Rename Preview.  # noqa: E501
        """
        pass

    def test_database_to_sync_mode(self):
        """Test case for database_to_sync_mode

        Perform Control-M/Server Trigger DB sync mode  # noqa: E501
        """
        pass

    def test_define_server(self):
        """Test case for define_server

        add server definition to the system  # noqa: E501
        """
        pass

    def test_delete_agent(self):
        """Test case for delete_agent

        delete an agent from Server  # noqa: E501
        """
        pass

    def test_delete_agentless_host(self):
        """Test case for delete_agentless_host

        delete an agentless host from Server  # noqa: E501
        """
        pass

    def test_delete_archive_rule(self):
        """Test case for delete_archive_rule

        Delete Workload Archiving rule  # noqa: E501
        """
        pass

    def test_delete_authorization_role(self):
        """Test case for delete_authorization_role

        Delete Authorization Role  # noqa: E501
        """
        pass

    def test_delete_external_user(self):
        """Test case for delete_external_user

        Delete an external user  # noqa: E501
        """
        pass

    def test_delete_external_user_for_site(self):
        """Test case for delete_external_user_for_site

        Delete an external user from site  # noqa: E501
        """
        pass

    def test_delete_external_user_from_mft_user_group_for_site(self):
        """Test case for delete_external_user_from_mft_user_group_for_site

        Remove an external user from group in MFT for site.  # noqa: E501
        """
        pass

    def test_delete_external_user_or_user_group_from_mft_folder(self):
        """Test case for delete_external_user_or_user_group_from_mft_folder

        Remove an external user or user group from an existing virtual folder in MFT.  # noqa: E501
        """
        pass

    def test_delete_external_user_or_user_group_from_mft_folder_for_site(self):
        """Test case for delete_external_user_or_user_group_from_mft_folder_for_site

        Remove an external user or user group from an existing virtual folder in MFT for site.  # noqa: E501
        """
        pass

    def test_delete_host_from_group(self):
        """Test case for delete_host_from_group

        delete an agent from a hostgroup  # noqa: E501
        """
        pass

    def test_delete_host_group(self):
        """Test case for delete_host_group

        delete host group  # noqa: E501
        """
        pass

    def test_delete_host_restrictions(self):
        """Test case for delete_host_restrictions

        Delete Host Restrictions.  # noqa: E501
        """
        pass

    def test_delete_ldap_group_from_mft_user_group_for_site(self):
        """Test case for delete_ldap_group_from_mft_user_group_for_site

        Remove an LDAP group from group in MFT for site.  # noqa: E501
        """
        pass

    def test_delete_mft_folder(self):
        """Test case for delete_mft_folder

        Delete a virtual folder.  # noqa: E501
        """
        pass

    def test_delete_mft_folder_for_site(self):
        """Test case for delete_mft_folder_for_site

        Delete a virtual folder for site.  # noqa: E501
        """
        pass

    def test_delete_mft_processing_rule_for_site(self):
        """Test case for delete_mft_processing_rule_for_site

        Delete MFTE processing rule for site.  # noqa: E501
        """
        pass

    def test_delete_mft_user_group(self):
        """Test case for delete_mft_user_group

        Delete user group.  # noqa: E501
        """
        pass

    def test_delete_mft_user_group_for_site(self):
        """Test case for delete_mft_user_group_for_site

        Delete user group for site.  # noqa: E501
        """
        pass

    def test_delete_pgp_template(self):
        """Test case for delete_pgp_template

        Delete PGP Template  # noqa: E501
        """
        pass

    def test_delete_remote_host(self):
        """Test case for delete_remote_host

        delete a remote host from Server  # noqa: E501
        """
        pass

    def test_delete_role_from_ldap_group(self):
        """Test case for delete_role_from_ldap_group

        Delete a role from LDAP group  # noqa: E501
        """
        pass

    def test_delete_run_as_user(self):
        """Test case for delete_run_as_user

        delete Run-as user  # noqa: E501
        """
        pass

    def test_delete_secret(self):
        """Test case for delete_secret

        Delete an existing secret  # noqa: E501
        """
        pass

    def test_delete_ssh_key(self):
        """Test case for delete_ssh_key

        delete an SSH key from the control-m server.  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete user  # noqa: E501
        """
        pass

    def test_delete_zos_template(self):
        """Test case for delete_zos_template

        Delete z/OS Template  # noqa: E501
        """
        pass

    def test_deploy_agent_certificate(self):
        """Test case for deploy_agent_certificate

        Deploy certificate (CRT).  # noqa: E501
        """
        pass

    def test_disable_agent(self):
        """Test case for disable_agent

        disable agent from the Server  # noqa: E501
        """
        pass

    def test_disable_agentless_host(self):
        """Test case for disable_agentless_host

        disable agentless host from the Server  # noqa: E501
        """
        pass

    def test_disable_ctm_server(self):
        """Test case for disable_ctm_server

        Set server to disabled state.  # noqa: E501
        """
        pass

    def test_disable_mft_processing_rule_for_site(self):
        """Test case for disable_mft_processing_rule_for_site

        Disable MFTE processing rule for site  # noqa: E501
        """
        pass

    def test_enable_agent(self):
        """Test case for enable_agent

        enable agent from the Server  # noqa: E501
        """
        pass

    def test_enable_agentless_host(self):
        """Test case for enable_agentless_host

        enable agentless host from the Server  # noqa: E501
        """
        pass

    def test_enable_ctm_server(self):
        """Test case for enable_ctm_server

        Set server to enabled state.  # noqa: E501
        """
        pass

    def test_enable_mft_processing_rule_for_site(self):
        """Test case for enable_mft_processing_rule_for_site

        Enable MFTE processing rule for site  # noqa: E501
        """
        pass

    def test_failover(self):
        """Test case for failover

        Perform Control-M/Server failover to the secondary Control-M/Server server.  # noqa: E501
        """
        pass

    def test_fallback(self):
        """Test case for fallback

        Perform Control-M/Server fallback to the primary Control-M/Server server.  # noqa: E501
        """
        pass

    def test_generate_mft_rsa_ssh_key(self):
        """Test case for generate_mft_rsa_ssh_key

        Generate RSA SSH Key  # noqa: E501
        """
        pass

    def test_get_agent_certificate_expiration_date(self):
        """Test case for get_agent_certificate_expiration_date

        Get certificate expiration date.  # noqa: E501
        """
        pass

    def test_get_agent_parameters(self):
        """Test case for get_agent_parameters

        get agent parameters  # noqa: E501
        """
        pass

    def test_get_agentless_host_properties(self):
        """Test case for get_agentless_host_properties

        get an agentless host configuration from Server  # noqa: E501
        """
        pass

    def test_get_agentless_hosts(self):
        """Test case for get_agentless_hosts

        get Server agentless hosts  # noqa: E501
        """
        pass

    def test_get_agents(self):
        """Test case for get_agents

        get Server agents  # noqa: E501
        """
        pass

    def test_get_all_archive_rules(self):
        """Test case for get_all_archive_rules

        Get all Workload Archiving rules  # noqa: E501
        """
        pass

    def test_get_all_authorization_roles(self):
        """Test case for get_all_authorization_roles

        Get Authorization Roles  # noqa: E501
        """
        pass

    def test_get_all_organization_groups(self):
        """Test case for get_all_organization_groups

        Get All organization groups  # noqa: E501
        """
        pass

    def test_get_all_organization_users(self):
        """Test case for get_all_organization_users

        Get All organization users  # noqa: E501
        """
        pass

    def test_get_all_roles_associated_with_organization_group(self):
        """Test case for get_all_roles_associated_with_organization_group

        Get Authorization Roles associated with an organization group  # noqa: E501
        """
        pass

    def test_get_all_roles_associated_with_organization_user(self):
        """Test case for get_all_roles_associated_with_organization_user

        Get Authorization Roles associated with an Organization user  # noqa: E501
        """
        pass

    def test_get_all_users(self):
        """Test case for get_all_users

        Get users  # noqa: E501
        """
        pass

    def test_get_archive_statistics(self):
        """Test case for get_archive_statistics

        Get Workload Archiving statistics  # noqa: E501
        """
        pass

    def test_get_communication_analysis_report_for_agent(self):
        """Test case for get_communication_analysis_report_for_agent

        analyze communication between an Agent and its Server  # noqa: E501
        """
        pass

    def test_get_ctm_gate_ways(self):
        """Test case for get_ctm_gate_ways

        Get details of specific gateway component in the system.  # noqa: E501
        """
        pass

    def test_get_ctm_high_availability_status(self):
        """Test case for get_ctm_high_availability_status

        Get Control-M/Server High Availability status  # noqa: E501
        """
        pass

    def test_get_em_high_availability_status(self):
        """Test case for get_em_high_availability_status

        Get EM High Availability status  # noqa: E501
        """
        pass

    def test_get_external_user_authorized_folders(self):
        """Test case for get_external_user_authorized_folders

        Get MFT external user authorized folders  # noqa: E501
        """
        pass

    def test_get_external_user_authorized_folders_for_site(self):
        """Test case for get_external_user_authorized_folders_for_site

        Get MFT external user authorized folders for site  # noqa: E501
        """
        pass

    def test_get_external_users(self):
        """Test case for get_external_users

        Get MFT external users that match the search criteria.  # noqa: E501
        """
        pass

    def test_get_external_users_for_site(self):
        """Test case for get_external_users_for_site

        Get MFT external users for site that match the search criteria.  # noqa: E501
        """
        pass

    def test_get_fts_settings(self):
        """Test case for get_fts_settings

        Get File Transfer Server (FTS) configuration data.  # noqa: E501
        """
        pass

    def test_get_host_restriction_list(self):
        """Test case for get_host_restriction_list

        Get all host restrictions.  # noqa: E501
        """
        pass

    def test_get_hostgroups(self):
        """Test case for get_hostgroups

        get Server hostgroups  # noqa: E501
        """
        pass

    def test_get_hostgroups_and_agents_with_tag(self):
        """Test case for get_hostgroups_and_agents_with_tag

        get Server host groups with their agents  # noqa: E501
        """
        pass

    def test_get_hosts_in_group(self):
        """Test case for get_hosts_in_group

        get hostgroup agents  # noqa: E501
        """
        pass

    def test_get_hub_status_details(self):
        """Test case for get_hub_status_details

        Get hub status.  # noqa: E501
        """
        pass

    def test_get_hub_status_details_for_site(self):
        """Test case for get_hub_status_details_for_site

        Get hub status in site.  # noqa: E501
        """
        pass

    def test_get_identity_provider_metadata(self):
        """Test case for get_identity_provider_metadata

        Get identity Provider Metadata file  # noqa: E501
        """
        pass

    def test_get_load_balancer_properties(self):
        """Test case for get_load_balancer_properties

        Get loadBalancer parameters  # noqa: E501
        """
        pass

    def test_get_locked_external_users(self):
        """Test case for get_locked_external_users

        Get MFT locked external users.  # noqa: E501
        """
        pass

    def test_get_locked_external_users_for_site(self):
        """Test case for get_locked_external_users_for_site

        Get MFT locked external users for site.  # noqa: E501
        """
        pass

    def test_get_mft_configuration(self):
        """Test case for get_mft_configuration

        Get MFT Configuration  # noqa: E501
        """
        pass

    def test_get_mft_folders(self):
        """Test case for get_mft_folders

        Get MFT virtual folders that match the search criteria.  # noqa: E501
        """
        pass

    def test_get_mft_folders_for_site(self):
        """Test case for get_mft_folders_for_site

        Get MFT virtual folders that match the search criteria for site.  # noqa: E501
        """
        pass

    def test_get_mft_gateways(self):
        """Test case for get_mft_gateways

        Get MFT gateways  # noqa: E501
        """
        pass

    def test_get_mft_gateways_for_site(self):
        """Test case for get_mft_gateways_for_site

        Get MFT gateways for site  # noqa: E501
        """
        pass

    def test_get_mft_processing_rules_for_site(self):
        """Test case for get_mft_processing_rules_for_site

        Get MFTE processing rules that match the search criteria for site.  # noqa: E501
        """
        pass

    def test_get_mft_user_groups(self):
        """Test case for get_mft_user_groups

        Get all user groups that match the search criteria.  # noqa: E501
        """
        pass

    def test_get_mft_user_groups_for_site(self):
        """Test case for get_mft_user_groups_for_site

        Get all user groups that match the search criteria for site.  # noqa: E501
        """
        pass

    def test_get_organization_group_user_simulation(self):
        """Test case for get_organization_group_user_simulation

        Get organization group user with authorization sumulation  # noqa: E501
        """
        pass

    def test_get_pgp_templates(self):
        """Test case for get_pgp_templates

        Get PGP Templates  # noqa: E501
        """
        pass

    def test_get_remote_host_properties(self):
        """Test case for get_remote_host_properties

        get a remote host configuration from Server  # noqa: E501
        """
        pass

    def test_get_remote_hosts(self):
        """Test case for get_remote_hosts

        get Server remote hosts  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get Authorization Role  # noqa: E501
        """
        pass

    def test_get_role_associates(self):
        """Test case for get_role_associates

        Get all authorization entities associated with role  # noqa: E501
        """
        pass

    def test_get_run_as_user(self):
        """Test case for get_run_as_user

        Get Run-as user  # noqa: E501
        """
        pass

    def test_get_run_as_users_list(self):
        """Test case for get_run_as_users_list

        Get Run-as user list that match the requested search criteria.  # noqa: E501
        """
        pass

    def test_get_server_definition(self):
        """Test case for get_server_definition

        Get Control-M/Server definition.  # noqa: E501
        """
        pass

    def test_get_server_system_setting(self):
        """Test case for get_server_system_setting

        Get the Control-M server system settings  # noqa: E501
        """
        pass

    def test_get_servers(self):
        """Test case for get_servers

        get all the Servers name and hostname in the system  # noqa: E501
        """
        pass

    def test_get_ssh_key(self):
        """Test case for get_ssh_key

        Get public SSH key from the control-m server.  # noqa: E501
        """
        pass

    def test_get_ssh_keys_list(self):
        """Test case for get_ssh_keys_list

        Get all will return full ssh data for all objects.  # noqa: E501
        """
        pass

    def test_get_system_setting(self):
        """Test case for get_system_setting

        Get system setting for Control-M environment  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user  # noqa: E501
        """
        pass

    def test_get_user_effective_rights(self):
        """Test case for get_user_effective_rights

        Get user real effective authorizations  # noqa: E501
        """
        pass

    def test_get_user_simulation(self):
        """Test case for get_user_simulation

        Get user with authorization sumulation  # noqa: E501
        """
        pass

    def test_get_wda_datasets(self):
        """Test case for get_wda_datasets

        Get datasets for specific connection profile.  # noqa: E501
        """
        pass

    def test_get_wda_gateways(self):
        """Test case for get_wda_gateways

        Get DataAssurance gateways  # noqa: E501
        """
        pass

    def test_get_workflow_insights_data_export_status(self):
        """Test case for get_workflow_insights_data_export_status

        Get workflow data export status.  # noqa: E501
        """
        pass

    def test_get_workflow_insights_data_export_system_params(self):
        """Test case for get_workflow_insights_data_export_system_params

        Get workflow data export system parameters.  # noqa: E501
        """
        pass

    def test_get_workflow_insights_status(self):
        """Test case for get_workflow_insights_status

        get Workflow Insights status  # noqa: E501
        """
        pass

    def test_get_zos_templates(self):
        """Test case for get_zos_templates

        Get z/OS Templates  # noqa: E501
        """
        pass

    def test_list_secrets(self):
        """Test case for list_secrets

        Get list of secret names  # noqa: E501
        """
        pass

    def test_lock_external_user(self):
        """Test case for lock_external_user

        Lock external user  # noqa: E501
        """
        pass

    def test_lock_external_user_for_site(self):
        """Test case for lock_external_user_for_site

        Lock external user for site  # noqa: E501
        """
        pass

    def test_managed_ctm_server(self):
        """Test case for managed_ctm_server

        Set server to managed state.  # noqa: E501
        """
        pass

    def test_perform_em_failover(self):
        """Test case for perform_em_failover

        Perform EM failover to the secondary EM server  # noqa: E501
        """
        pass

    def test_perform_em_fallback(self):
        """Test case for perform_em_fallback

        Perform EM fallback to the primary EM server  # noqa: E501
        """
        pass

    def test_ping_agent(self):
        """Test case for ping_agent

        ping to the agent in the Server  # noqa: E501
        """
        pass

    def test_ping_agentless_host(self):
        """Test case for ping_agentless_host

        ping to the agentless host in the Server  # noqa: E501
        """
        pass

    def test_poll_add_ssh_key_request_by_polling_id(self):
        """Test case for poll_add_ssh_key_request_by_polling_id

        Polling request for async Add an SSH key to the control-m server.  # noqa: E501
        """
        pass

    def test_recycle_item(self):
        """Test case for recycle_item

        recycle item  # noqa: E501
        """
        pass

    def test_refresh_server_system_settings(self):
        """Test case for refresh_server_system_settings

        Refresh the Control-M server system settings  # noqa: E501
        """
        pass

    def test_remove_controlm_server(self):
        """Test case for remove_controlm_server

        Delete Server  # noqa: E501
        """
        pass

    def test_remove_ctm_gateway(self):
        """Test case for remove_ctm_gateway

        Delete gateway  # noqa: E501
        """
        pass

    def test_remove_gateway(self):
        """Test case for remove_gateway

        remove gateway.  # noqa: E501
        """
        pass

    def test_remove_gateway_for_site(self):
        """Test case for remove_gateway_for_site

        remove gateway for site.  # noqa: E501
        """
        pass

    def test_remove_hub_from_cluster(self):
        """Test case for remove_hub_from_cluster

        remove hub from cluster.  # noqa: E501
        """
        pass

    def test_remove_hub_from_cluster_for_site(self):
        """Test case for remove_hub_from_cluster_for_site

        remove hub from cluster for site.  # noqa: E501
        """
        pass

    def test_remove_role_from_user(self):
        """Test case for remove_role_from_user

        Remove a role from a user  # noqa: E501
        """
        pass

    def test_remove_wda_gateway(self):
        """Test case for remove_wda_gateway

        remove DataAssurance gateway.  # noqa: E501
        """
        pass

    def test_rename_role(self):
        """Test case for rename_role

        Rename Authorization Role  # noqa: E501
        """
        pass

    def test_replicate_database(self):
        """Test case for replicate_database

        Trigger DB replication For CTM High Availability  # noqa: E501
        """
        pass

    def test_resume_ctm(self):
        """Test case for resume_ctm

        Resume the CTM server.  # noqa: E501
        """
        pass

    def test_send_archive_cleanup_request(self):
        """Test case for send_archive_cleanup_request

        Deletes data (jobs including outputs and logs) from the Workload Archiving database.  # noqa: E501
        """
        pass

    def test_set_active_shout_destination_list(self):
        """Test case for set_active_shout_destination_list

        Activates the notification destinations list.  # noqa: E501
        """
        pass

    def test_set_agent_parameter(self):
        """Test case for set_agent_parameter

        set agent parameter  # noqa: E501
        """
        pass

    def test_set_ctm_desired_state(self):
        """Test case for set_ctm_desired_state

        Set server to desired state.  # noqa: E501
        """
        pass

    def test_set_em_as_primary(self):
        """Test case for set_em_as_primary

        Set the secondary EM server as Primary  # noqa: E501
        """
        pass

    def test_set_server_system_setting(self):
        """Test case for set_server_system_setting

        Set a system setting for Control-M server  # noqa: E501
        """
        pass

    def test_set_system_param(self):
        """Test case for set_system_param

        set value of a an em system parameter  # noqa: E501
        """
        pass

    def test_set_system_setting(self):
        """Test case for set_system_setting

        Set system setting for Control-M environment  # noqa: E501
        """
        pass

    def test_set_user_preferences(self):
        """Test case for set_user_preferences

        Set user preferences by user name  # noqa: E501
        """
        pass

    def test_set_workflow_insights_data_export_system_params(self):
        """Test case for set_workflow_insights_data_export_system_params

        set workflow data export system parameters.  # noqa: E501
        """
        pass

    def test_setasprimary(self):
        """Test case for setasprimary

        Set secondary server as Primary on a specified Server  # noqa: E501
        """
        pass

    def test_test_agent(self):
        """Test case for test_agent

        Test the Agent connectivity to the server.  # noqa: E501
        """
        pass

    def test_test_agentless_host(self):
        """Test case for test_agentless_host

        test Agentless Host in the Server  # noqa: E501
        """
        pass

    def test_test_run_as_user(self):
        """Test case for test_run_as_user

        Test existed Run-as user  # noqa: E501
        """
        pass

    def test_unlock_external_user(self):
        """Test case for unlock_external_user

        Unlock an external user  # noqa: E501
        """
        pass

    def test_unlock_external_user_for_site(self):
        """Test case for unlock_external_user_for_site

        Unlock an external user for site  # noqa: E501
        """
        pass

    def test_unlock_external_users(self):
        """Test case for unlock_external_users

        Unlock all external users  # noqa: E501
        """
        pass

    def test_unlock_external_users_for_site(self):
        """Test case for unlock_external_users_for_site

        Unlock all external users for site  # noqa: E501
        """
        pass

    def test_unmanaged_ctm_server(self):
        """Test case for unmanaged_ctm_server

        Set server to unmanaged state.  # noqa: E501
        """
        pass

    def test_update_agent_parameter(self):
        """Test case for update_agent_parameter

        Update agent parameter  # noqa: E501
        """
        pass

    def test_update_agentless_host(self):
        """Test case for update_agentless_host

        Update agentless host  # noqa: E501
        """
        pass

    def test_update_archive_rule(self):
        """Test case for update_archive_rule

        Edit Workload Archiving rule  # noqa: E501
        """
        pass

    def test_update_ctm_gateway(self):
        """Test case for update_ctm_gateway

        Update gateway.  # noqa: E501
        """
        pass

    def test_update_external_user(self):
        """Test case for update_external_user

        Update an external user  # noqa: E501
        """
        pass

    def test_update_external_user_for_site(self):
        """Test case for update_external_user_for_site

        Update an external user for site  # noqa: E501
        """
        pass

    def test_update_fts_settings(self):
        """Test case for update_fts_settings

        Update File Transfer Server (FTS) configuration data.  # noqa: E501
        """
        pass

    def test_update_host_restriction(self):
        """Test case for update_host_restriction

        Update an Host Restriction in the control-m server.  # noqa: E501
        """
        pass

    def test_update_hosts_in_hostgroup(self):
        """Test case for update_hosts_in_hostgroup

        update agents in hostgroup.  # noqa: E501
        """
        pass

    def test_update_load_balancer(self):
        """Test case for update_load_balancer

        update loadBalancer  # noqa: E501
        """
        pass

    def test_update_mft_configuration(self):
        """Test case for update_mft_configuration

        Update MFT Configuration  # noqa: E501
        """
        pass

    def test_update_mft_folder(self):
        """Test case for update_mft_folder

        Update an existing virtual folder in MFT.  # noqa: E501
        """
        pass

    def test_update_mft_folder_for_site(self):
        """Test case for update_mft_folder_for_site

        Update an existing virtual folder in MFT for site.  # noqa: E501
        """
        pass

    def test_update_mft_processing_rule_for_site(self):
        """Test case for update_mft_processing_rule_for_site

        Update MFTE processing rule for site  # noqa: E501
        """
        pass

    def test_update_mft_user_group(self):
        """Test case for update_mft_user_group

        Update user group.  # noqa: E501
        """
        pass

    def test_update_mft_user_group_for_site(self):
        """Test case for update_mft_user_group_for_site

        Update user group for site.  # noqa: E501
        """
        pass

    def test_update_pgp_template(self):
        """Test case for update_pgp_template

        Update PGP Template  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update Authorization Role  # noqa: E501
        """
        pass

    def test_update_run_as_user(self):
        """Test case for update_run_as_user

        Update Run-as user  # noqa: E501
        """
        pass

    def test_update_secret(self):
        """Test case for update_secret

        Update an existing secret  # noqa: E501
        """
        pass

    def test_update_server(self):
        """Test case for update_server

        Update Server  # noqa: E501
        """
        pass

    def test_update_ssh_key(self):
        """Test case for update_ssh_key

        Update an SSH key in the control-m server.  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user  # noqa: E501
        """
        pass

    def test_update_zos_template(self):
        """Test case for update_zos_template

        Update z/OS Template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
