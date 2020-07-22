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

from msgraph.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type
)
from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_bookings.action import (
    AddAddress,
    AddBusinessHours,
    AddSchedulingPolicy,
    AddCustomers,
    AddStart,
    AddReminders,
    AddServiceLocationCoordinates,
    AddDefaultReminders,
    AddWorkingHours
)


def load_arguments(self, _):

    with self.argument_context('bookings update') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('display_name', help='Display name of this entity.')
        c.argument('business_type', help='')
        c.argument('address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('phone', help='')
        c.argument('email', help='')
        c.argument('web_site_url', help='The URL of the business web site.')
        c.argument('default_currency_iso', help='')
        c.argument('business_hours', action=AddBusinessHours, nargs='*', help='')
        c.argument('scheduling_policy', action=AddSchedulingPolicy, nargs='*', help='bookingSchedulingPolicy')
        c.argument('is_published', arg_type=get_three_state_flag(), help='')
        c.argument('public_url', help='')
        c.argument('appointments', type=validate_file_or_dict, help='All appointments in this business. Expected '
                   'value: json-string/@json-file.')
        c.argument('calendar_view', type=validate_file_or_dict, help='A calendar view of appointments in this '
                   'business. Expected value: json-string/@json-file.')
        c.argument('customers', action=AddCustomers, nargs='*', help='All customers of this business.')
        c.argument('services', type=validate_file_or_dict, help='All services offered by this business. Expected '
                   'value: json-string/@json-file.')
        c.argument('staff_members', type=validate_file_or_dict, help='All staff members that provides services in this '
                   'business. Expected value: json-string/@json-file.')

    with self.argument_context('bookings delete') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('if_match', help='ETag')

    with self.argument_context('bookings create-booking-business') as c:
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('display_name', help='Display name of this entity.')
        c.argument('business_type', help='')
        c.argument('address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('phone', help='')
        c.argument('email', help='')
        c.argument('web_site_url', help='The URL of the business web site.')
        c.argument('default_currency_iso', help='')
        c.argument('business_hours', action=AddBusinessHours, nargs='*', help='')
        c.argument('scheduling_policy', action=AddSchedulingPolicy, nargs='*', help='bookingSchedulingPolicy')
        c.argument('is_published', arg_type=get_three_state_flag(), help='')
        c.argument('public_url', help='')
        c.argument('appointments', type=validate_file_or_dict, help='All appointments in this business. Expected '
                   'value: json-string/@json-file.')
        c.argument('calendar_view', type=validate_file_or_dict, help='A calendar view of appointments in this '
                   'business. Expected value: json-string/@json-file.')
        c.argument('customers', action=AddCustomers, nargs='*', help='All customers of this business.')
        c.argument('services', type=validate_file_or_dict, help='All services offered by this business. Expected '
                   'value: json-string/@json-file.')
        c.argument('staff_members', type=validate_file_or_dict, help='All staff members that provides services in this '
                   'business. Expected value: json-string/@json-file.')

    with self.argument_context('bookings get-booking-business') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings list-booking-business') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings update') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('booking_appointment_id', help='key: bookingAppointment-id of bookingAppointment')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('self_service_appointment_id', help='')
        c.argument('customer_id', help='The id of the booking customer associated with this appointment.')
        c.argument('customer_name', help='')
        c.argument('customer_email_address', help='')
        c.argument('customer_phone', help='')
        c.argument('customer_notes', help='Notes from the customer associated with this appointment.')
        c.argument('service_id', help='The id of the booking service associated with this appointment.')
        c.argument('service_name', help='The name of the booking service associated with this appointment.')
        c.argument('start', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('end', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('duration', help='')
        c.argument('pre_buffer', help='')
        c.argument('post_buffer', help='')
        c.argument('price_type', arg_type=get_enum_type(['undefined', 'fixedPrice', 'startingAt', 'hourly', 'free', ''
                   'priceVaries', 'callUs', 'notSet']), help='')
        c.argument('price', help='')
        c.argument('service_notes', help='')
        c.argument('reminders', action=AddReminders, nargs='*', help='')
        c.argument('opt_out_of_customer_email', arg_type=get_three_state_flag(), help='')
        c.argument('staff_member_ids', nargs='*', help='')
        c.argument('invoice_amount', help='')
        c.argument('invoice_date', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('invoice_id', help='')
        c.argument('invoice_status', arg_type=get_enum_type(['draft', 'reviewing', 'open', 'canceled', 'paid', ''
                   'corrective']), help='')
        c.argument('invoice_url', help='')
        c.argument('service_location_display_name', help='The name associated with the location.')
        c.argument('service_location_location_email_address', help='Optional email address of the location.')
        c.argument('service_location_address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('service_location_coordinates', action=AddServiceLocationCoordinates, nargs='*', help=''
                   'outlookGeoCoordinates')
        c.argument('service_location_location_uri', help='Optional URI representing the location.')
        c.argument('service_location_location_type', arg_type=get_enum_type(['default', 'conferenceRoom',
                   'homeAddress', 'businessAddress', 'geoCoordinates', 'streetAddress', 'hotel', 'restaurant', ''
                   'localBusiness', 'postalAddress']), help='')
        c.argument('service_location_unique_id', help='For internal use only.')
        c.argument('service_location_unique_id_type', arg_type=get_enum_type(['unknown', 'locationStore', 'directory',
                   'private', 'bing']), help='')
        c.argument('customer_location_display_name', help='The name associated with the location.')
        c.argument('customer_location_location_email_address', help='Optional email address of the location.')
        c.argument('customer_location_address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('customer_location_coordinates', action=AddServiceLocationCoordinates, nargs='*', help=''
                   'outlookGeoCoordinates')
        c.argument('customer_location_location_uri', help='Optional URI representing the location.')
        c.argument('customer_location_location_type', arg_type=get_enum_type(['default', 'conferenceRoom', ''
                   'homeAddress', 'businessAddress', 'geoCoordinates', 'streetAddress', 'hotel', 'restaurant', ''
                   'localBusiness', 'postalAddress']), help='')
        c.argument('customer_location_unique_id', help='For internal use only.')
        c.argument('customer_location_unique_id_type', arg_type=get_enum_type(['unknown', 'locationStore', 'directory',
                    'private', 'bing']), help='')
        c.argument('booking_customer_id', help='key: bookingCustomer-id of bookingCustomer')
        c.argument('display_name', help='Display name of this entity.')
        c.argument('email_address', help='The e-mail address of this person.')
        c.argument('booking_service_id', help='key: bookingService-id of bookingService')
        c.argument('default_duration', help='')
        c.argument('default_price', help='')
        c.argument('default_price_type', arg_type=get_enum_type(['undefined', 'fixedPrice', 'startingAt', 'hourly', ''
                   'free', 'priceVaries', 'callUs', 'notSet']), help='')
        c.argument('default_reminders', action=AddDefaultReminders, nargs='*', help='The default reminders set in an '
                   'appointment of this service.')
        c.argument('description', help='')
        c.argument('is_hidden_from_customers', arg_type=get_three_state_flag(), help='')
        c.argument('notes', help='')
        c.argument('scheduling_policy', action=AddSchedulingPolicy, nargs='*', help='bookingSchedulingPolicy')
        c.argument('default_location_display_name', help='The name associated with the location.')
        c.argument('default_location_location_email_address', help='Optional email address of the location.')
        c.argument('default_location_address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('default_location_coordinates', action=AddServiceLocationCoordinates, nargs='*', help=''
                   'outlookGeoCoordinates')
        c.argument('default_location_location_uri', help='Optional URI representing the location.')
        c.argument('default_location_location_type', arg_type=get_enum_type(['default', 'conferenceRoom',
                   'homeAddress', 'businessAddress', 'geoCoordinates', 'streetAddress', 'hotel', 'restaurant', ''
                   'localBusiness', 'postalAddress']), help='')
        c.argument('default_location_unique_id', help='For internal use only.')
        c.argument('default_location_unique_id_type', arg_type=get_enum_type(['unknown', 'locationStore', 'directory',
                   'private', 'bing']), help='')
        c.argument('booking_staff_member_id', help='key: bookingStaffMember-id of bookingStaffMember')
        c.argument('availability_is_affected_by_personal_calendar', arg_type=get_three_state_flag(), help='')
        c.argument('color_index', help='')
        c.argument('role', arg_type=get_enum_type(['guest', 'administrator', 'viewer', 'externalGuest']), help='')
        c.argument('use_business_hours', arg_type=get_three_state_flag(), help='')
        c.argument('working_hours', action=AddWorkingHours, nargs='*', help='')

    with self.argument_context('bookings create-appointment') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('self_service_appointment_id', help='')
        c.argument('customer_id', help='The id of the booking customer associated with this appointment.')
        c.argument('customer_name', help='')
        c.argument('customer_email_address', help='')
        c.argument('customer_phone', help='')
        c.argument('customer_notes', help='Notes from the customer associated with this appointment.')
        c.argument('service_id', help='The id of the booking service associated with this appointment.')
        c.argument('service_name', help='The name of the booking service associated with this appointment.')
        c.argument('start', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('end', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('duration', help='')
        c.argument('pre_buffer', help='')
        c.argument('post_buffer', help='')
        c.argument('price_type', arg_type=get_enum_type(['undefined', 'fixedPrice', 'startingAt', 'hourly', 'free', ''
                   'priceVaries', 'callUs', 'notSet']), help='')
        c.argument('price', help='')
        c.argument('service_notes', help='')
        c.argument('reminders', action=AddReminders, nargs='*', help='')
        c.argument('opt_out_of_customer_email', arg_type=get_three_state_flag(), help='')
        c.argument('staff_member_ids', nargs='*', help='')
        c.argument('invoice_amount', help='')
        c.argument('invoice_date', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('invoice_id', help='')
        c.argument('invoice_status', arg_type=get_enum_type(['draft', 'reviewing', 'open', 'canceled', 'paid', ''
                   'corrective']), help='')
        c.argument('invoice_url', help='')
        c.argument('service_location_display_name', help='The name associated with the location.')
        c.argument('service_location_location_email_address', help='Optional email address of the location.')
        c.argument('service_location_address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('service_location_coordinates', action=AddServiceLocationCoordinates, nargs='*', help=''
                   'outlookGeoCoordinates')
        c.argument('service_location_location_uri', help='Optional URI representing the location.')
        c.argument('service_location_location_type', arg_type=get_enum_type(['default', 'conferenceRoom',
                   'homeAddress', 'businessAddress', 'geoCoordinates', 'streetAddress', 'hotel', 'restaurant', ''
                   'localBusiness', 'postalAddress']), help='')
        c.argument('service_location_unique_id', help='For internal use only.')
        c.argument('service_location_unique_id_type', arg_type=get_enum_type(['unknown', 'locationStore', 'directory',
                   'private', 'bing']), help='')
        c.argument('customer_location_display_name', help='The name associated with the location.')
        c.argument('customer_location_location_email_address', help='Optional email address of the location.')
        c.argument('customer_location_address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('customer_location_coordinates', action=AddServiceLocationCoordinates, nargs='*', help=''
                   'outlookGeoCoordinates')
        c.argument('customer_location_location_uri', help='Optional URI representing the location.')
        c.argument('customer_location_location_type', arg_type=get_enum_type(['default', 'conferenceRoom', ''
                   'homeAddress', 'businessAddress', 'geoCoordinates', 'streetAddress', 'hotel', 'restaurant', ''
                   'localBusiness', 'postalAddress']), help='')
        c.argument('customer_location_unique_id', help='For internal use only.')
        c.argument('customer_location_unique_id_type', arg_type=get_enum_type(['unknown', 'locationStore', 'directory',
                    'private', 'bing']), help='')

    with self.argument_context('bookings create-calendar-view') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('self_service_appointment_id', help='')
        c.argument('customer_id', help='The id of the booking customer associated with this appointment.')
        c.argument('customer_name', help='')
        c.argument('customer_email_address', help='')
        c.argument('customer_phone', help='')
        c.argument('customer_notes', help='Notes from the customer associated with this appointment.')
        c.argument('service_id', help='The id of the booking service associated with this appointment.')
        c.argument('service_name', help='The name of the booking service associated with this appointment.')
        c.argument('start', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('end', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('duration', help='')
        c.argument('pre_buffer', help='')
        c.argument('post_buffer', help='')
        c.argument('price_type', arg_type=get_enum_type(['undefined', 'fixedPrice', 'startingAt', 'hourly', 'free', ''
                   'priceVaries', 'callUs', 'notSet']), help='')
        c.argument('price', help='')
        c.argument('service_notes', help='')
        c.argument('reminders', action=AddReminders, nargs='*', help='')
        c.argument('opt_out_of_customer_email', arg_type=get_three_state_flag(), help='')
        c.argument('staff_member_ids', nargs='*', help='')
        c.argument('invoice_amount', help='')
        c.argument('invoice_date', action=AddStart, nargs='*', help='dateTimeTimeZone')
        c.argument('invoice_id', help='')
        c.argument('invoice_status', arg_type=get_enum_type(['draft', 'reviewing', 'open', 'canceled', 'paid', ''
                   'corrective']), help='')
        c.argument('invoice_url', help='')
        c.argument('service_location_display_name', help='The name associated with the location.')
        c.argument('service_location_location_email_address', help='Optional email address of the location.')
        c.argument('service_location_address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('service_location_coordinates', action=AddServiceLocationCoordinates, nargs='*', help=''
                   'outlookGeoCoordinates')
        c.argument('service_location_location_uri', help='Optional URI representing the location.')
        c.argument('service_location_location_type', arg_type=get_enum_type(['default', 'conferenceRoom',
                   'homeAddress', 'businessAddress', 'geoCoordinates', 'streetAddress', 'hotel', 'restaurant', ''
                   'localBusiness', 'postalAddress']), help='')
        c.argument('service_location_unique_id', help='For internal use only.')
        c.argument('service_location_unique_id_type', arg_type=get_enum_type(['unknown', 'locationStore', 'directory',
                   'private', 'bing']), help='')
        c.argument('customer_location_display_name', help='The name associated with the location.')
        c.argument('customer_location_location_email_address', help='Optional email address of the location.')
        c.argument('customer_location_address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('customer_location_coordinates', action=AddServiceLocationCoordinates, nargs='*', help=''
                   'outlookGeoCoordinates')
        c.argument('customer_location_location_uri', help='Optional URI representing the location.')
        c.argument('customer_location_location_type', arg_type=get_enum_type(['default', 'conferenceRoom', ''
                   'homeAddress', 'businessAddress', 'geoCoordinates', 'streetAddress', 'hotel', 'restaurant', ''
                   'localBusiness', 'postalAddress']), help='')
        c.argument('customer_location_unique_id', help='For internal use only.')
        c.argument('customer_location_unique_id_type', arg_type=get_enum_type(['unknown', 'locationStore', 'directory',
                    'private', 'bing']), help='')

    with self.argument_context('bookings create-customer') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('display_name', help='Display name of this entity.')
        c.argument('email_address', help='The e-mail address of this person.')

    with self.argument_context('bookings create-service') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('display_name', help='Display name of this entity.')
        c.argument('default_duration', help='')
        c.argument('default_price', help='')
        c.argument('default_price_type', arg_type=get_enum_type(['undefined', 'fixedPrice', 'startingAt', 'hourly', ''
                   'free', 'priceVaries', 'callUs', 'notSet']), help='')
        c.argument('default_reminders', action=AddDefaultReminders, nargs='*', help='The default reminders set in an '
                   'appointment of this service.')
        c.argument('description', help='')
        c.argument('is_hidden_from_customers', arg_type=get_three_state_flag(), help='')
        c.argument('notes', help='')
        c.argument('pre_buffer', help='')
        c.argument('post_buffer', help='')
        c.argument('scheduling_policy', action=AddSchedulingPolicy, nargs='*', help='bookingSchedulingPolicy')
        c.argument('staff_member_ids', nargs='*', help='')
        c.argument('default_location_display_name', help='The name associated with the location.')
        c.argument('default_location_location_email_address', help='Optional email address of the location.')
        c.argument('default_location_address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('default_location_coordinates', action=AddServiceLocationCoordinates, nargs='*', help=''
                   'outlookGeoCoordinates')
        c.argument('default_location_location_uri', help='Optional URI representing the location.')
        c.argument('default_location_location_type', arg_type=get_enum_type(['default', 'conferenceRoom',
                   'homeAddress', 'businessAddress', 'geoCoordinates', 'streetAddress', 'hotel', 'restaurant', ''
                   'localBusiness', 'postalAddress']), help='')
        c.argument('default_location_unique_id', help='For internal use only.')
        c.argument('default_location_unique_id_type', arg_type=get_enum_type(['unknown', 'locationStore', 'directory',
                   'private', 'bing']), help='')

    with self.argument_context('bookings create-staff-member') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('display_name', help='Display name of this entity.')
        c.argument('email_address', help='The e-mail address of this person.')
        c.argument('availability_is_affected_by_personal_calendar', arg_type=get_three_state_flag(), help='')
        c.argument('color_index', help='')
        c.argument('role', arg_type=get_enum_type(['guest', 'administrator', 'viewer', 'externalGuest']), help='')
        c.argument('use_business_hours', arg_type=get_three_state_flag(), help='')
        c.argument('working_hours', action=AddWorkingHours, nargs='*', help='')

    with self.argument_context('bookings get-appointment') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('booking_appointment_id', help='key: bookingAppointment-id of bookingAppointment')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings get-calendar-view') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('booking_appointment_id', help='key: bookingAppointment-id of bookingAppointment')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings get-customer') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('booking_customer_id', help='key: bookingCustomer-id of bookingCustomer')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings get-service') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('booking_service_id', help='key: bookingService-id of bookingService')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings get-staff-member') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('booking_staff_member_id', help='key: bookingStaffMember-id of bookingStaffMember')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings list-appointment') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings list-calendar-view') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings list-customer') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings list-service') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings list-staff-member') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings publish') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')

    with self.argument_context('bookings unpublish') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')

    with self.argument_context('bookings cancel') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('booking_appointment_id', help='key: bookingAppointment-id of bookingAppointment')
        c.argument('cancellation_message', help='')

    with self.argument_context('bookings cancel') as c:
        c.argument('booking_business_id', help='key: bookingBusiness-id of bookingBusiness')
        c.argument('booking_appointment_id', help='key: bookingAppointment-id of bookingAppointment')
        c.argument('cancellation_message', help='')

    with self.argument_context('bookings update') as c:
        c.argument('booking_currency_id', help='key: bookingCurrency-id of bookingCurrency')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('symbol', help='')

    with self.argument_context('bookings delete') as c:
        c.argument('booking_currency_id', help='key: bookingCurrency-id of bookingCurrency')
        c.argument('if_match', help='ETag')

    with self.argument_context('bookings create-booking-currency') as c:
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('symbol', help='')

    with self.argument_context('bookings get-booking-currency') as c:
        c.argument('booking_currency_id', help='key: bookingCurrency-id of bookingCurrency')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('bookings list-booking-currency') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')
