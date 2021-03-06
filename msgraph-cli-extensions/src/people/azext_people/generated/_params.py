# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import get_three_state_flag
from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_people.action import (
    AddPersonType,
    AddPhones,
    AddScoredEmailAddresses,
    AddWebsites,
    AddResourceReference,
    AddResourceVisualization,
    AddLastSharedSharedBy,
    AddLastUsed
)


def load_arguments(self, _):

    with self.argument_context('people delete') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('person_id', type=str, help='key: id of person')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('people create-person') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('birthday', type=str, help='The person\'s birthday.')
        c.argument('company_name', type=str, help='The name of the person\'s company.')
        c.argument('department', type=str, help='The person\'s department.')
        c.argument('display_name', type=str, help='The person\'s display name.')
        c.argument('given_name', type=str, help='The person\'s given name.')
        c.argument('im_address', type=str, help='The instant message voice over IP (VOIP) session initiation protocol '
                   '(SIP) address for the user. Read-only.')
        c.argument('is_favorite', arg_type=get_three_state_flag(), help='true if the user has flagged this person as a '
                   'favorite.')
        c.argument('job_title', type=str, help='The person\'s job title.')
        c.argument('office_location', type=str, help='The location of the person\'s office.')
        c.argument('person_notes', type=str, help='Free-form notes that the user has taken about this person.')
        c.argument('person_type', action=AddPersonType, nargs='*', help='personType')
        c.argument('phones', action=AddPhones, nargs='*', help='The person\'s phone numbers.')
        c.argument('postal_addresses', type=validate_file_or_dict, help='The person\'s addresses. Expected value: '
                   'json-string/@json-file.')
        c.argument('profession', type=str, help='The person\'s profession.')
        c.argument('scored_email_addresses', action=AddScoredEmailAddresses, nargs='*', help='The person\'s email '
                   'addresses.')
        c.argument('surname', type=str, help='The person\'s surname.')
        c.argument('user_principal_name', type=str, help='The user principal name (UPN) of the person. The UPN is an '
                   'Internet-style login name for the person based on the Internet standard RFC 822. By convention, '
                   'this should map to the person\'s email name. The general format is alias@domain.')
        c.argument('websites', action=AddWebsites, nargs='*', help='The person\'s websites.')
        c.argument('yomi_company', type=str, help='The phonetic Japanese name of the person\'s company.')

    with self.argument_context('people get-insight') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people get-person') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('person_id', type=str, help='key: id of person')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people list-person') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people update-insight') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('shared', type=validate_file_or_dict, help='Calculated relationship identifying documents shared '
                   'with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive '
                   'for Business and SharePoint files found in Outlook messages and meetings. This also includes URLs '
                   'and reference attachments to Teams conversations. Ordered by recency of share. Expected value: '
                   'json-string/@json-file.')
        c.argument('trending', type=validate_file_or_dict, help='Calculated relationship identifying documents '
                   'trending around a user. Trending documents are calculated based on activity of the user\'s closest '
                   'network of people and include files stored in OneDrive for Business and SharePoint. Trending '
                   'insights help the user to discover potentially useful content that the user has access to, but has '
                   'never viewed before. Expected value: json-string/@json-file.')
        c.argument('used', type=validate_file_or_dict, help='Calculated relationship identifying the latest documents '
                   'viewed or modified by a user, including OneDrive for Business and SharePoint documents, ranked by '
                   'recency of use. Expected value: json-string/@json-file.')

    with self.argument_context('people update-person') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('person_id', type=str, help='key: id of person')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('birthday', type=str, help='The person\'s birthday.')
        c.argument('company_name', type=str, help='The name of the person\'s company.')
        c.argument('department', type=str, help='The person\'s department.')
        c.argument('display_name', type=str, help='The person\'s display name.')
        c.argument('given_name', type=str, help='The person\'s given name.')
        c.argument('im_address', type=str, help='The instant message voice over IP (VOIP) session initiation protocol '
                   '(SIP) address for the user. Read-only.')
        c.argument('is_favorite', arg_type=get_three_state_flag(), help='true if the user has flagged this person as a '
                   'favorite.')
        c.argument('job_title', type=str, help='The person\'s job title.')
        c.argument('office_location', type=str, help='The location of the person\'s office.')
        c.argument('person_notes', type=str, help='Free-form notes that the user has taken about this person.')
        c.argument('person_type', action=AddPersonType, nargs='*', help='personType')
        c.argument('phones', action=AddPhones, nargs='*', help='The person\'s phone numbers.')
        c.argument('postal_addresses', type=validate_file_or_dict, help='The person\'s addresses. Expected value: '
                   'json-string/@json-file.')
        c.argument('profession', type=str, help='The person\'s profession.')
        c.argument('scored_email_addresses', action=AddScoredEmailAddresses, nargs='*', help='The person\'s email '
                   'addresses.')
        c.argument('surname', type=str, help='The person\'s surname.')
        c.argument('user_principal_name', type=str, help='The user principal name (UPN) of the person. The UPN is an '
                   'Internet-style login name for the person based on the Internet standard RFC 822. By convention, '
                   'this should map to the person\'s email name. The general format is alias@domain.')
        c.argument('websites', action=AddWebsites, nargs='*', help='The person\'s websites.')
        c.argument('yomi_company', type=str, help='The phonetic Japanese name of the person\'s company.')

    with self.argument_context('people delete') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')
        c.argument('if_match', type=str, help='ETag')
        c.argument('trending_id', type=str, help='key: id of trending')
        c.argument('used_insight_id', type=str, help='key: id of usedInsight')

    with self.argument_context('people create-shared') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('resource_reference', action=AddResourceReference, nargs='*', help='resourceReference')
        c.argument('resource_visualization', action=AddResourceVisualization, nargs='*', help='resourceVisualization')
        c.argument('sharing_history', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('resource_id', type=str, help='Read-only.')
        c.argument('last_shared_method_id', type=str, help='Read-only.')
        c.argument('last_shared_shared_by', action=AddLastSharedSharedBy, nargs='*', help='insightIdentity')
        c.argument('last_shared_shared_date_time', help='The date and time the file was last shared. The timestamp '
                   'represents date and time information using ISO 8601 format and is always in UTC time. For example, '
                   'midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.')
        c.argument('last_shared_sharing_reference', action=AddResourceReference, nargs='*', help='resourceReference')
        c.argument('last_shared_sharing_subject', type=str, help='The subject with which the document was shared.')
        c.argument('last_shared_sharing_type', type=str, help='Determines the way the document was shared, can be by a '
                   '\'Link\', \'Attachment\', \'Group\', \'Site\'.')

    with self.argument_context('people create-trending') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('last_modified_date_time', help='')
        c.argument('resource_reference', action=AddResourceReference, nargs='*', help='resourceReference')
        c.argument('resource_visualization', action=AddResourceVisualization, nargs='*', help='resourceVisualization')
        c.argument('weight', type=float, help='Value indicating how much the document is currently trending. The '
                   'larger the number, the more the document is currently trending around the user (the more relevant '
                   'it is). Returned documents are sorted by this value.')
        c.argument('resource_id', type=str, help='Read-only.')

    with self.argument_context('people create-used') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('last_used', action=AddLastUsed, nargs='*', help='usageDetails')
        c.argument('resource_reference', action=AddResourceReference, nargs='*', help='resourceReference')
        c.argument('resource_visualization', action=AddResourceVisualization, nargs='*', help='resourceVisualization')
        c.argument('resource_id', type=str, help='Read-only.')

    with self.argument_context('people get-shared') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people get-trending') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('trending_id', type=str, help='key: id of trending')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people get-used') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('used_insight_id', type=str, help='key: id of usedInsight')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people list-shared') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people list-trending') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people list-used') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people update-shared') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('resource_reference', action=AddResourceReference, nargs='*', help='resourceReference')
        c.argument('resource_visualization', action=AddResourceVisualization, nargs='*', help='resourceVisualization')
        c.argument('sharing_history', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('resource_id', type=str, help='Read-only.')
        c.argument('last_shared_method_id', type=str, help='Read-only.')
        c.argument('last_shared_shared_by', action=AddLastSharedSharedBy, nargs='*', help='insightIdentity')
        c.argument('last_shared_shared_date_time', help='The date and time the file was last shared. The timestamp '
                   'represents date and time information using ISO 8601 format and is always in UTC time. For example, '
                   'midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.')
        c.argument('last_shared_sharing_reference', action=AddResourceReference, nargs='*', help='resourceReference')
        c.argument('last_shared_sharing_subject', type=str, help='The subject with which the document was shared.')
        c.argument('last_shared_sharing_type', type=str, help='Determines the way the document was shared, can be by a '
                   '\'Link\', \'Attachment\', \'Group\', \'Site\'.')

    with self.argument_context('people update-trending') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('trending_id', type=str, help='key: id of trending')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('last_modified_date_time', help='')
        c.argument('resource_reference', action=AddResourceReference, nargs='*', help='resourceReference')
        c.argument('resource_visualization', action=AddResourceVisualization, nargs='*', help='resourceVisualization')
        c.argument('weight', type=float, help='Value indicating how much the document is currently trending. The '
                   'larger the number, the more the document is currently trending around the user (the more relevant '
                   'it is). Returned documents are sorted by this value.')
        c.argument('resource_id', type=str, help='Read-only.')

    with self.argument_context('people update-used') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('used_insight_id', type=str, help='key: id of usedInsight')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('last_used', action=AddLastUsed, nargs='*', help='usageDetails')
        c.argument('resource_reference', action=AddResourceReference, nargs='*', help='resourceReference')
        c.argument('resource_visualization', action=AddResourceVisualization, nargs='*', help='resourceVisualization')
        c.argument('resource_id', type=str, help='Read-only.')

    with self.argument_context('people delete') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('people get-last-shared-method') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people get-ref-last-shared-method') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')

    with self.argument_context('people get-ref-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')

    with self.argument_context('people get-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people set-ref-last-shared-method') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('people set-ref-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('shared_insight_id', type=str, help='key: id of sharedInsight')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('people delete') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('trending_id', type=str, help='key: id of trending')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('people get-ref-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('trending_id', type=str, help='key: id of trending')

    with self.argument_context('people get-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('trending_id', type=str, help='key: id of trending')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people set-ref-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('trending_id', type=str, help='key: id of trending')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('people delete') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('used_insight_id', type=str, help='key: id of usedInsight')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('people get-ref-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('used_insight_id', type=str, help='key: id of usedInsight')

    with self.argument_context('people get-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('used_insight_id', type=str, help='key: id of usedInsight')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('people set-ref-resource') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('used_insight_id', type=str, help='key: id of usedInsight')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')
