# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._users_people_enums import *


class CollectionOfPerson(msrest.serialization.Model):
    """Collection of person.

    :param value:
    :type value: list[~users_people.models.MicrosoftGraphPerson]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPerson]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPerson"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPerson, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class MicrosoftGraphEntity(msrest.serialization.Model):
    """entity.

    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.id = id


class MicrosoftGraphLocation(msrest.serialization.Model):
    """location.

    :param display_name: The name associated with the location.
    :type display_name: str
    :param location_email_address: Optional email address of the location.
    :type location_email_address: str
    :param address: physicalAddress.
    :type address: ~users_people.models.MicrosoftGraphPhysicalAddress
    :param coordinates: outlookGeoCoordinates.
    :type coordinates: ~users_people.models.MicrosoftGraphOutlookGeoCoordinates
    :param location_uri: Optional URI representing the location.
    :type location_uri: str
    :param location_type:  Possible values include: "default", "conferenceRoom", "homeAddress",
     "businessAddress", "geoCoordinates", "streetAddress", "hotel", "restaurant", "localBusiness",
     "postalAddress".
    :type location_type: str or ~users_people.models.MicrosoftGraphLocationType
    :param unique_id: For internal use only.
    :type unique_id: str
    :param unique_id_type:  Possible values include: "unknown", "locationStore", "directory",
     "private", "bing".
    :type unique_id_type: str or ~users_people.models.MicrosoftGraphLocationUniqueIdType
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'location_email_address': {'key': 'locationEmailAddress', 'type': 'str'},
        'address': {'key': 'address', 'type': 'MicrosoftGraphPhysicalAddress'},
        'coordinates': {'key': 'coordinates', 'type': 'MicrosoftGraphOutlookGeoCoordinates'},
        'location_uri': {'key': 'locationUri', 'type': 'str'},
        'location_type': {'key': 'locationType', 'type': 'str'},
        'unique_id': {'key': 'uniqueId', 'type': 'str'},
        'unique_id_type': {'key': 'uniqueIdType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        display_name: Optional[str] = None,
        location_email_address: Optional[str] = None,
        address: Optional["MicrosoftGraphPhysicalAddress"] = None,
        coordinates: Optional["MicrosoftGraphOutlookGeoCoordinates"] = None,
        location_uri: Optional[str] = None,
        location_type: Optional[Union[str, "MicrosoftGraphLocationType"]] = None,
        unique_id: Optional[str] = None,
        unique_id_type: Optional[Union[str, "MicrosoftGraphLocationUniqueIdType"]] = None,
        **kwargs
    ):
        super(MicrosoftGraphLocation, self).__init__(**kwargs)
        self.display_name = display_name
        self.location_email_address = location_email_address
        self.address = address
        self.coordinates = coordinates
        self.location_uri = location_uri
        self.location_type = location_type
        self.unique_id = unique_id
        self.unique_id_type = unique_id_type


class MicrosoftGraphOutlookGeoCoordinates(msrest.serialization.Model):
    """outlookGeoCoordinates.

    :param altitude: The altitude of the location.
    :type altitude: float
    :param latitude: The latitude of the location.
    :type latitude: float
    :param longitude: The longitude of the location.
    :type longitude: float
    :param accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be
     measured in meters, such as the latitude and longitude are accurate to within 50 meters.
    :type accuracy: float
    :param altitude_accuracy: The accuracy of the altitude.
    :type altitude_accuracy: float
    """

    _attribute_map = {
        'altitude': {'key': 'altitude', 'type': 'float'},
        'latitude': {'key': 'latitude', 'type': 'float'},
        'longitude': {'key': 'longitude', 'type': 'float'},
        'accuracy': {'key': 'accuracy', 'type': 'float'},
        'altitude_accuracy': {'key': 'altitudeAccuracy', 'type': 'float'},
    }

    def __init__(
        self,
        *,
        altitude: Optional[float] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        accuracy: Optional[float] = None,
        altitude_accuracy: Optional[float] = None,
        **kwargs
    ):
        super(MicrosoftGraphOutlookGeoCoordinates, self).__init__(**kwargs)
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
        self.accuracy = accuracy
        self.altitude_accuracy = altitude_accuracy


class MicrosoftGraphPerson(MicrosoftGraphEntity):
    """person.

    :param id: Read-only.
    :type id: str
    :param display_name: The person's display name.
    :type display_name: str
    :param given_name: The person's given name.
    :type given_name: str
    :param surname: The person's surname.
    :type surname: str
    :param birthday: The person's birthday.
    :type birthday: str
    :param person_notes: Free-form notes that the user has taken about this person.
    :type person_notes: str
    :param is_favorite: true if the user has flagged this person as a favorite.
    :type is_favorite: bool
    :param email_addresses:
    :type email_addresses: list[~users_people.models.MicrosoftGraphRankedEmailAddress]
    :param phones: The person's phone numbers.
    :type phones: list[~users_people.models.MicrosoftGraphPhone]
    :param postal_addresses: The person's addresses.
    :type postal_addresses: list[~users_people.models.MicrosoftGraphLocation]
    :param websites: The person's websites.
    :type websites: list[~users_people.models.MicrosoftGraphWebsite]
    :param title:
    :type title: str
    :param company_name: The name of the person's company.
    :type company_name: str
    :param yomi_company: The phonetic Japanese name of the person's company.
    :type yomi_company: str
    :param department: The person's department.
    :type department: str
    :param office_location: The location of the person's office.
    :type office_location: str
    :param profession: The person's profession.
    :type profession: str
    :param sources:
    :type sources: list[~users_people.models.MicrosoftGraphPersonDataSource]
    :param mailbox_type:
    :type mailbox_type: str
    :param person_type: The type of person.
    :type person_type: str
    :param user_principal_name: The user principal name (UPN) of the person. The UPN is an
     Internet-style login name for the person based on the Internet standard RFC 822. By convention,
     this should map to the person's email name. The general format is alias@domain.
    :type user_principal_name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'given_name': {'key': 'givenName', 'type': 'str'},
        'surname': {'key': 'surname', 'type': 'str'},
        'birthday': {'key': 'birthday', 'type': 'str'},
        'person_notes': {'key': 'personNotes', 'type': 'str'},
        'is_favorite': {'key': 'isFavorite', 'type': 'bool'},
        'email_addresses': {'key': 'emailAddresses', 'type': '[MicrosoftGraphRankedEmailAddress]'},
        'phones': {'key': 'phones', 'type': '[MicrosoftGraphPhone]'},
        'postal_addresses': {'key': 'postalAddresses', 'type': '[MicrosoftGraphLocation]'},
        'websites': {'key': 'websites', 'type': '[MicrosoftGraphWebsite]'},
        'title': {'key': 'title', 'type': 'str'},
        'company_name': {'key': 'companyName', 'type': 'str'},
        'yomi_company': {'key': 'yomiCompany', 'type': 'str'},
        'department': {'key': 'department', 'type': 'str'},
        'office_location': {'key': 'officeLocation', 'type': 'str'},
        'profession': {'key': 'profession', 'type': 'str'},
        'sources': {'key': 'sources', 'type': '[MicrosoftGraphPersonDataSource]'},
        'mailbox_type': {'key': 'mailboxType', 'type': 'str'},
        'person_type': {'key': 'personType', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        display_name: Optional[str] = None,
        given_name: Optional[str] = None,
        surname: Optional[str] = None,
        birthday: Optional[str] = None,
        person_notes: Optional[str] = None,
        is_favorite: Optional[bool] = None,
        email_addresses: Optional[List["MicrosoftGraphRankedEmailAddress"]] = None,
        phones: Optional[List["MicrosoftGraphPhone"]] = None,
        postal_addresses: Optional[List["MicrosoftGraphLocation"]] = None,
        websites: Optional[List["MicrosoftGraphWebsite"]] = None,
        title: Optional[str] = None,
        company_name: Optional[str] = None,
        yomi_company: Optional[str] = None,
        department: Optional[str] = None,
        office_location: Optional[str] = None,
        profession: Optional[str] = None,
        sources: Optional[List["MicrosoftGraphPersonDataSource"]] = None,
        mailbox_type: Optional[str] = None,
        person_type: Optional[str] = None,
        user_principal_name: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPerson, self).__init__(id=id, **kwargs)
        self.display_name = display_name
        self.given_name = given_name
        self.surname = surname
        self.birthday = birthday
        self.person_notes = person_notes
        self.is_favorite = is_favorite
        self.email_addresses = email_addresses
        self.phones = phones
        self.postal_addresses = postal_addresses
        self.websites = websites
        self.title = title
        self.company_name = company_name
        self.yomi_company = yomi_company
        self.department = department
        self.office_location = office_location
        self.profession = profession
        self.sources = sources
        self.mailbox_type = mailbox_type
        self.person_type = person_type
        self.user_principal_name = user_principal_name


class MicrosoftGraphPersonDataSource(msrest.serialization.Model):
    """personDataSource.

    :param type:
    :type type: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPersonDataSource, self).__init__(**kwargs)
        self.type = type


class MicrosoftGraphPhone(msrest.serialization.Model):
    """phone.

    :param type:  Possible values include: "home", "business", "mobile", "other", "assistant",
     "homeFax", "businessFax", "otherFax", "pager", "radio".
    :type type: str or ~users_people.models.MicrosoftGraphPhoneType
    :param number: The phone number.
    :type number: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'number': {'key': 'number', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "MicrosoftGraphPhoneType"]] = None,
        number: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPhone, self).__init__(**kwargs)
        self.type = type
        self.number = number


class MicrosoftGraphPhysicalAddress(msrest.serialization.Model):
    """physicalAddress.

    :param type:  Possible values include: "unknown", "home", "business", "other".
    :type type: str or ~users_people.models.MicrosoftGraphPhysicalAddressType
    :param post_office_box:
    :type post_office_box: str
    :param street: The street.
    :type street: str
    :param city: The city.
    :type city: str
    :param state: The state.
    :type state: str
    :param country_or_region: The country or region. It's a free-format string value, for example,
     'United States'.
    :type country_or_region: str
    :param postal_code: The postal code.
    :type postal_code: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'post_office_box': {'key': 'postOfficeBox', 'type': 'str'},
        'street': {'key': 'street', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'country_or_region': {'key': 'countryOrRegion', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "MicrosoftGraphPhysicalAddressType"]] = None,
        post_office_box: Optional[str] = None,
        street: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        country_or_region: Optional[str] = None,
        postal_code: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPhysicalAddress, self).__init__(**kwargs)
        self.type = type
        self.post_office_box = post_office_box
        self.street = street
        self.city = city
        self.state = state
        self.country_or_region = country_or_region
        self.postal_code = postal_code


class MicrosoftGraphRankedEmailAddress(msrest.serialization.Model):
    """rankedEmailAddress.

    :param address:
    :type address: str
    :param rank:
    :type rank: float
    """

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'rank': {'key': 'rank', 'type': 'float'},
    }

    def __init__(
        self,
        *,
        address: Optional[str] = None,
        rank: Optional[float] = None,
        **kwargs
    ):
        super(MicrosoftGraphRankedEmailAddress, self).__init__(**kwargs)
        self.address = address
        self.rank = rank


class MicrosoftGraphWebsite(msrest.serialization.Model):
    """website.

    :param type:  Possible values include: "other", "home", "work", "blog", "profile".
    :type type: str or ~users_people.models.MicrosoftGraphWebsiteType
    :param address: The URL of the website.
    :type address: str
    :param display_name: The display name of the web site.
    :type display_name: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'address': {'key': 'address', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "MicrosoftGraphWebsiteType"]] = None,
        address: Optional[str] = None,
        display_name: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphWebsite, self).__init__(**kwargs)
        self.type = type
        self.address = address
        self.display_name = display_name


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~users_people.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        *,
        error: "OdataErrorMain",
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.error = error


class OdataErrorDetail(msrest.serialization.Model):
    """OdataErrorDetail.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


class OdataErrorMain(msrest.serialization.Model):
    """OdataErrorMain.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~users_people.models.OdataErrorDetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[OdataErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        details: Optional[List["OdataErrorDetail"]] = None,
        innererror: Optional[object] = None,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror
