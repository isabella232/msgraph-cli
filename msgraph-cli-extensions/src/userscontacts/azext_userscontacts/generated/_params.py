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

from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_userscontacts.action import (
    AddSingleValueExtendedProperties,
    AddMultiValueExtendedProperties
)


def load_arguments(self, _):

    with self.argument_context('userscontacts update') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('parent_folder_id', help='The ID of the folder\'s parent folder.')
        c.argument('display_name', help='The folder\'s display name.')
        c.argument('well_known_name', help='')
        c.argument('single_value_extended_properties', action=AddSingleValueExtendedProperties, nargs='*', help='The '
                   'collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.')
        c.argument('multi_value_extended_properties', action=AddMultiValueExtendedProperties, nargs='*', help='The '
                   'collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.')
        c.argument('contacts', type=validate_file_or_dict, help='The contacts in the folder. Navigation property. '
                   'Read-only. Nullable. Expected value: json-string/@json-file.')
        c.argument('child_folders', type=validate_file_or_dict, help='The collection of child folders in the folder. '
                   'Navigation property. Read-only. Nullable. Expected value: json-string/@json-file.')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('body', type=validate_file_or_dict, help='New navigation property values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('userscontacts create-contact') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('body', type=validate_file_or_dict, help='New navigation property Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('userscontacts create-contact-folder') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('parent_folder_id', help='The ID of the folder\'s parent folder.')
        c.argument('display_name', help='The folder\'s display name.')
        c.argument('well_known_name', help='')
        c.argument('single_value_extended_properties', action=AddSingleValueExtendedProperties, nargs='*', help='The '
                   'collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.')
        c.argument('multi_value_extended_properties', action=AddMultiValueExtendedProperties, nargs='*', help='The '
                   'collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.')
        c.argument('contacts', type=validate_file_or_dict, help='The contacts in the folder. Navigation property. '
                   'Read-only. Nullable. Expected value: json-string/@json-file.')
        c.argument('child_folders', type=validate_file_or_dict, help='The collection of child folders in the folder. '
                   'Navigation property. Read-only. Nullable. Expected value: json-string/@json-file.')

    with self.argument_context('userscontacts get-contact') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-contact-folder') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-contact') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-contact-folder') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts update') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_folder_id1', help='key: contactFolder-id of contactFolder')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('parent_folder_id', help='The ID of the folder\'s parent folder.')
        c.argument('display_name', help='The folder\'s display name.')
        c.argument('well_known_name', help='')
        c.argument('single_value_extended_properties', action=AddSingleValueExtendedProperties, nargs='*', help='The '
                   'collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.')
        c.argument('multi_value_extended_properties', action=AddMultiValueExtendedProperties, nargs='*', help='The '
                   'collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.')
        c.argument('contacts', type=validate_file_or_dict, help='The contacts in the folder. Navigation property. '
                   'Read-only. Nullable. Expected value: json-string/@json-file.')
        c.argument('child_folders', type=validate_file_or_dict, help='The collection of child folders in the folder. '
                   'Navigation property. Read-only. Nullable. Expected value: json-string/@json-file.')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('body', type=validate_file_or_dict, help='New navigation property values Expected value: '
                   'json-string/@json-file.')
        c.argument('multi_value_legacy_extended_property_id', help='key: multiValueLegacyExtendedProperty-id of '
                   'multiValueLegacyExtendedProperty')
        c.argument('value', nargs='*', help='A collection of property values.')
        c.argument('single_value_legacy_extended_property_id', help='key: singleValueLegacyExtendedProperty-id of '
                   'singleValueLegacyExtendedProperty')

    with self.argument_context('userscontacts create-child-folder') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('parent_folder_id', help='The ID of the folder\'s parent folder.')
        c.argument('display_name', help='The folder\'s display name.')
        c.argument('well_known_name', help='')
        c.argument('single_value_extended_properties', action=AddSingleValueExtendedProperties, nargs='*', help='The '
                   'collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.')
        c.argument('multi_value_extended_properties', action=AddMultiValueExtendedProperties, nargs='*', help='The '
                   'collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.')
        c.argument('contacts', type=validate_file_or_dict, help='The contacts in the folder. Navigation property. '
                   'Read-only. Nullable. Expected value: json-string/@json-file.')
        c.argument('child_folders', type=validate_file_or_dict, help='The collection of child folders in the folder. '
                   'Navigation property. Read-only. Nullable. Expected value: json-string/@json-file.')

    with self.argument_context('userscontacts create-contact') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('body', type=validate_file_or_dict, help='New navigation property Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('userscontacts create-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('value', nargs='*', help='A collection of property values.')

    with self.argument_context('userscontacts create-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('value', help='A property value.')

    with self.argument_context('userscontacts get-child-folder') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_folder_id1', help='key: contactFolder-id of contactFolder')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-contact') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('multi_value_legacy_extended_property_id', help='key: multiValueLegacyExtendedProperty-id of '
                   'multiValueLegacyExtendedProperty')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('single_value_legacy_extended_property_id', help='key: singleValueLegacyExtendedProperty-id of '
                   'singleValueLegacyExtendedProperty')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-child-folder') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-contact') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts update') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('extension_id', help='key: extension-id of extension')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('multi_value_legacy_extended_property_id', help='key: multiValueLegacyExtendedProperty-id of '
                   'multiValueLegacyExtendedProperty')
        c.argument('value', nargs='*', help='A collection of property values.')
        c.argument('single_value_legacy_extended_property_id', help='key: singleValueLegacyExtendedProperty-id of '
                   'singleValueLegacyExtendedProperty')
        c.argument('height', help='The height of the photo. Read-only.')
        c.argument('width', help='The width of the photo. Read-only.')

    with self.argument_context('userscontacts create-extension') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('id_', options_list=['--id'], help='Read-only.')

    with self.argument_context('userscontacts create-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('value', nargs='*', help='A collection of property values.')

    with self.argument_context('userscontacts create-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('value', help='A property value.')

    with self.argument_context('userscontacts get-extension') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('extension_id', help='key: extension-id of extension')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('multi_value_legacy_extended_property_id', help='key: multiValueLegacyExtendedProperty-id of '
                   'multiValueLegacyExtendedProperty')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-photo') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('single_value_legacy_extended_property_id', help='key: singleValueLegacyExtendedProperty-id of '
                   'singleValueLegacyExtendedProperty')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-extension') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_folder_id', help='key: contactFolder-id of contactFolder')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts update') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('extension_id', help='key: extension-id of extension')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('multi_value_legacy_extended_property_id', help='key: multiValueLegacyExtendedProperty-id of '
                   'multiValueLegacyExtendedProperty')
        c.argument('value', nargs='*', help='A collection of property values.')
        c.argument('single_value_legacy_extended_property_id', help='key: singleValueLegacyExtendedProperty-id of '
                   'singleValueLegacyExtendedProperty')
        c.argument('height', help='The height of the photo. Read-only.')
        c.argument('width', help='The width of the photo. Read-only.')

    with self.argument_context('userscontacts create-extension') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('id_', options_list=['--id'], help='Read-only.')

    with self.argument_context('userscontacts create-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('value', nargs='*', help='A collection of property values.')

    with self.argument_context('userscontacts create-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('value', help='A property value.')

    with self.argument_context('userscontacts get-extension') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('extension_id', help='key: extension-id of extension')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('multi_value_legacy_extended_property_id', help='key: multiValueLegacyExtendedProperty-id of '
                   'multiValueLegacyExtendedProperty')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-photo') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts get-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('single_value_legacy_extended_property_id', help='key: singleValueLegacyExtendedProperty-id of '
                   'singleValueLegacyExtendedProperty')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-extension') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-multi-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('userscontacts list-single-value-extended-property') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('contact_id', help='key: contact-id of contact')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')
