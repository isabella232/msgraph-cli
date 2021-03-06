# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_teams.generated._client_factory import cf_chat_chat
    teams_chat_chat = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._chat_chat_operations#ChatChatOperations.{}',
        client_factory=cf_chat_chat)
    with self.command_group('teams', teams_chat_chat, client_factory=cf_chat_chat) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-chat', 'teams_create_chat')
        g.custom_command('get-chat', 'teams_get_chat')
        g.custom_command('list-chat', 'teams_list_chat')
        g.custom_command('update-chat', 'teams_update_chat')

    from azext_teams.generated._client_factory import cf_chat
    teams_chat = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._chat_operations#ChatOperations.{}',
        client_factory=cf_chat)
    with self.command_group('teams', teams_chat, client_factory=cf_chat) as g:
        g.custom_command('get-all-message', 'teams_get_all_message')

    from azext_teams.generated._client_factory import cf_group
    teams_group = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._group_operations#GroupOperations.{}',
        client_factory=cf_group)
    with self.command_group('teams', teams_group, client_factory=cf_group) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('get-team', 'teams_get_team')
        g.custom_command('update-team', 'teams_update_team')

    from azext_teams.generated._client_factory import cf_team_team
    teams_team_team = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_team_operations#TeamTeamOperations.{}',
        client_factory=cf_team_team)
    with self.command_group('teams', teams_team_team, client_factory=cf_team_team) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-team', 'teams_create_team')
        g.custom_command('get-team', 'teams_get_team')
        g.custom_command('list-team', 'teams_list_team')
        g.custom_command('update-team', 'teams_update_team')

    from azext_teams.generated._client_factory import cf_team
    teams_team = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_operations#TeamOperations.{}',
        client_factory=cf_team)
    with self.command_group('teams', teams_team, client_factory=cf_team) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('archive', 'teams_archive')
        g.custom_command('clone', 'teams_clone')
        g.custom_command('create-channel', 'teams_create_channel')
        g.custom_command('create-installed-app', 'teams_create_installed_app')
        g.custom_command('create-member', 'teams_create_member')
        g.custom_command('create-operation', 'teams_create_operation')
        g.custom_command('get-all-message', 'teams_get_all_message')
        g.custom_command('get-channel', 'teams_get_channel')
        g.custom_command('get-group', 'teams_get_group')
        g.custom_command('get-installed-app', 'teams_get_installed_app')
        g.custom_command('get-member', 'teams_get_member')
        g.custom_command('get-operation', 'teams_get_operation')
        g.custom_command('get-primary-channel', 'teams_get_primary_channel')
        g.custom_command('get-ref-group', 'teams_get_ref_group')
        g.custom_command('get-ref-template', 'teams_get_ref_template')
        g.custom_command('get-schedule', 'teams_get_schedule')
        g.custom_command('get-template', 'teams_get_template')
        g.custom_command('list-channel', 'teams_list_channel')
        g.custom_command('list-installed-app', 'teams_list_installed_app')
        g.custom_command('list-member', 'teams_list_member')
        g.custom_command('list-operation', 'teams_list_operation')
        g.custom_command('set-ref-group', 'teams_set_ref_group')
        g.custom_command('set-ref-template', 'teams_set_ref_template')
        g.custom_command('unarchive', 'teams_unarchive')
        g.custom_command('update-channel', 'teams_update_channel')
        g.custom_command('update-installed-app', 'teams_update_installed_app')
        g.custom_command('update-member', 'teams_update_member')
        g.custom_command('update-operation', 'teams_update_operation')
        g.custom_command('update-primary-channel', 'teams_update_primary_channel')
        g.custom_command('update-schedule', 'teams_update_schedule')

    from azext_teams.generated._client_factory import cf_team_channel
    teams_team_channel = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_channel_operations#TeamChannelOperations.{}',
        client_factory=cf_team_channel)
    with self.command_group('teams', teams_team_channel, client_factory=cf_team_channel) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-member', 'teams_create_member')
        g.custom_command('create-message', 'teams_create_message')
        g.custom_command('create-tab', 'teams_create_tab')
        g.custom_command('get-file-folder', 'teams_get_file_folder')
        g.custom_command('get-member', 'teams_get_member')
        g.custom_command('get-message', 'teams_get_message')
        g.custom_command('get-tab', 'teams_get_tab')
        g.custom_command('list-member', 'teams_list_member')
        g.custom_command('list-message', 'teams_list_message')
        g.custom_command('list-tab', 'teams_list_tab')
        g.custom_command('update-file-folder', 'teams_update_file_folder')
        g.custom_command('update-member', 'teams_update_member')
        g.custom_command('update-message', 'teams_update_message')
        g.custom_command('update-tab', 'teams_update_tab')

    from azext_teams.generated._client_factory import cf_team_channel_message
    teams_team_channel_message = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_channel_message_operations#TeamChannelMessage'
        'Operations.{}',
        client_factory=cf_team_channel_message)
    with self.command_group('teams', teams_team_channel_message, client_factory=cf_team_channel_message) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-hosted-content', 'teams_create_hosted_content')
        g.custom_command('create-reply', 'teams_create_reply')
        g.custom_command('get-hosted-content', 'teams_get_hosted_content')
        g.custom_command('get-reply', 'teams_get_reply')
        g.custom_command('list-hosted-content', 'teams_list_hosted_content')
        g.custom_command('list-reply', 'teams_list_reply')
        g.custom_command('update-hosted-content', 'teams_update_hosted_content')
        g.custom_command('update-reply', 'teams_update_reply')

    from azext_teams.generated._client_factory import cf_team_channel_tab
    teams_team_channel_tab = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_channel_tab_operations#TeamChannelTabOperatio'
        'ns.{}',
        client_factory=cf_team_channel_tab)
    with self.command_group('teams', teams_team_channel_tab, client_factory=cf_team_channel_tab) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('get-ref-team-app', 'teams_get_ref_team_app')
        g.custom_command('get-team-app', 'teams_get_team_app')
        g.custom_command('set-ref-team-app', 'teams_set_ref_team_app')

    from azext_teams.generated._client_factory import cf_team_installed_app
    teams_team_installed_app = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_installed_app_operations#TeamInstalledAppOper'
        'ations.{}',
        client_factory=cf_team_installed_app)
    with self.command_group('teams', teams_team_installed_app, client_factory=cf_team_installed_app) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('get-ref-team-app', 'teams_get_ref_team_app')
        g.custom_command('get-ref-team-app-definition', 'teams_get_ref_team_app_definition')
        g.custom_command('get-team-app', 'teams_get_team_app')
        g.custom_command('get-team-app-definition', 'teams_get_team_app_definition')
        g.custom_command('set-ref-team-app', 'teams_set_ref_team_app')
        g.custom_command('set-ref-team-app-definition', 'teams_set_ref_team_app_definition')
        g.custom_command('upgrade', 'teams_upgrade')

    from azext_teams.generated._client_factory import cf_team_primary_channel
    teams_team_primary_channel = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_primary_channel_operations#TeamPrimaryChannel'
        'Operations.{}',
        client_factory=cf_team_primary_channel)
    with self.command_group('teams', teams_team_primary_channel, client_factory=cf_team_primary_channel) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-member', 'teams_create_member')
        g.custom_command('create-message', 'teams_create_message')
        g.custom_command('create-tab', 'teams_create_tab')
        g.custom_command('get-file-folder', 'teams_get_file_folder')
        g.custom_command('get-member', 'teams_get_member')
        g.custom_command('get-message', 'teams_get_message')
        g.custom_command('get-tab', 'teams_get_tab')
        g.custom_command('list-member', 'teams_list_member')
        g.custom_command('list-message', 'teams_list_message')
        g.custom_command('list-tab', 'teams_list_tab')
        g.custom_command('update-file-folder', 'teams_update_file_folder')
        g.custom_command('update-member', 'teams_update_member')
        g.custom_command('update-message', 'teams_update_message')
        g.custom_command('update-tab', 'teams_update_tab')

    from azext_teams.generated._client_factory import cf_team_primary_channel_message
    teams_team_primary_channel_message = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_primary_channel_message_operations#TeamPrimar'
        'yChannelMessageOperations.{}',
        client_factory=cf_team_primary_channel_message)
    with self.command_group('teams', teams_team_primary_channel_message,
                            client_factory=cf_team_primary_channel_message) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-hosted-content', 'teams_create_hosted_content')
        g.custom_command('create-reply', 'teams_create_reply')
        g.custom_command('get-hosted-content', 'teams_get_hosted_content')
        g.custom_command('get-reply', 'teams_get_reply')
        g.custom_command('list-hosted-content', 'teams_list_hosted_content')
        g.custom_command('list-reply', 'teams_list_reply')
        g.custom_command('update-hosted-content', 'teams_update_hosted_content')
        g.custom_command('update-reply', 'teams_update_reply')

    from azext_teams.generated._client_factory import cf_team_primary_channel_tab
    teams_team_primary_channel_tab = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_primary_channel_tab_operations#TeamPrimaryCha'
        'nnelTabOperations.{}',
        client_factory=cf_team_primary_channel_tab)
    with self.command_group('teams', teams_team_primary_channel_tab, client_factory=cf_team_primary_channel_tab) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('get-ref-team-app', 'teams_get_ref_team_app')
        g.custom_command('get-team-app', 'teams_get_team_app')
        g.custom_command('set-ref-team-app', 'teams_set_ref_team_app')

    from azext_teams.generated._client_factory import cf_team_schedule
    teams_team_schedule = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._team_schedule_operations#TeamScheduleOperations.{}'
        '',
        client_factory=cf_team_schedule)
    with self.command_group('teams', teams_team_schedule, client_factory=cf_team_schedule) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-offer-shift-request', 'teams_create_offer_shift_request')
        g.custom_command('create-open-shift', 'teams_create_open_shift')
        g.custom_command('create-open-shift-change-request', 'teams_create_open_shift_change_request')
        g.custom_command('create-scheduling-group', 'teams_create_scheduling_group')
        g.custom_command('create-shift', 'teams_create_shift')
        g.custom_command('create-swap-shift-change-request', 'teams_create_swap_shift_change_request')
        g.custom_command('create-time-off', 'teams_create_time_off')
        g.custom_command('create-time-off-reason', 'teams_create_time_off_reason')
        g.custom_command('create-time-off-request', 'teams_create_time_off_request')
        g.custom_command('get-offer-shift-request', 'teams_get_offer_shift_request')
        g.custom_command('get-open-shift', 'teams_get_open_shift')
        g.custom_command('get-open-shift-change-request', 'teams_get_open_shift_change_request')
        g.custom_command('get-scheduling-group', 'teams_get_scheduling_group')
        g.custom_command('get-shift', 'teams_get_shift')
        g.custom_command('get-swap-shift-change-request', 'teams_get_swap_shift_change_request')
        g.custom_command('get-time-off', 'teams_get_time_off')
        g.custom_command('get-time-off-reason', 'teams_get_time_off_reason')
        g.custom_command('get-time-off-request', 'teams_get_time_off_request')
        g.custom_command('list-offer-shift-request', 'teams_list_offer_shift_request')
        g.custom_command('list-open-shift', 'teams_list_open_shift')
        g.custom_command('list-open-shift-change-request', 'teams_list_open_shift_change_request')
        g.custom_command('list-scheduling-group', 'teams_list_scheduling_group')
        g.custom_command('list-shift', 'teams_list_shift')
        g.custom_command('list-swap-shift-change-request', 'teams_list_swap_shift_change_request')
        g.custom_command('list-time-off', 'teams_list_time_off')
        g.custom_command('list-time-off-reason', 'teams_list_time_off_reason')
        g.custom_command('list-time-off-request', 'teams_list_time_off_request')
        g.custom_command('share', 'teams_share')
        g.custom_command('update-offer-shift-request', 'teams_update_offer_shift_request')
        g.custom_command('update-open-shift', 'teams_update_open_shift')
        g.custom_command('update-open-shift-change-request', 'teams_update_open_shift_change_request')
        g.custom_command('update-scheduling-group', 'teams_update_scheduling_group')
        g.custom_command('update-shift', 'teams_update_shift')
        g.custom_command('update-swap-shift-change-request', 'teams_update_swap_shift_change_request')
        g.custom_command('update-time-off', 'teams_update_time_off')
        g.custom_command('update-time-off-reason', 'teams_update_time_off_reason')
        g.custom_command('update-time-off-request', 'teams_update_time_off_request')

    from azext_teams.generated._client_factory import cf_teamwork_teamwork
    teams_teamwork_teamwork = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._teamwork_teamwork_operations#TeamworkTeamworkOpera'
        'tions.{}',
        client_factory=cf_teamwork_teamwork)
    with self.command_group('teams', teams_teamwork_teamwork, client_factory=cf_teamwork_teamwork) as g:
        g.custom_command('get-teamwork', 'teams_get_teamwork')
        g.custom_command('update-teamwork', 'teams_update_teamwork')

    from azext_teams.generated._client_factory import cf_teamwork
    teams_teamwork = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._teamwork_operations#TeamworkOperations.{}',
        client_factory=cf_teamwork)
    with self.command_group('teams', teams_teamwork, client_factory=cf_teamwork) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-workforce-integration', 'teams_create_workforce_integration')
        g.custom_command('get-workforce-integration', 'teams_get_workforce_integration')
        g.custom_command('list-workforce-integration', 'teams_list_workforce_integration')
        g.custom_command('update-workforce-integration', 'teams_update_workforce_integration')

    from azext_teams.generated._client_factory import cf_user
    teams_user = CliCommandType(
        operations_tmpl='azext_teams.vendored_sdks.teams.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('teams', teams_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'teams_delete', confirmation=True)
        g.custom_command('create-joined-team', 'teams_create_joined_team')
        g.custom_command('get-joined-team', 'teams_get_joined_team')
        g.custom_command('list-joined-team', 'teams_list_joined_team')
        g.custom_command('update-joined-team', 'teams_update_joined_team')
