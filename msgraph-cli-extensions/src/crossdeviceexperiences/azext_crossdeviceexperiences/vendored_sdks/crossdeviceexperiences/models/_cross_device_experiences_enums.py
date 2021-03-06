# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Enum11(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATION_URL = "activationUrl"
    ACTIVITY_SOURCE_HOST = "activitySourceHost"
    APP_ACTIVITY_ID = "appActivityId"
    APP_DISPLAY_NAME = "appDisplayName"
    CONTENT_INFO = "contentInfo"
    CONTENT_URL = "contentUrl"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    FALLBACK_URL = "fallbackUrl"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    VISUAL_ELEMENTS = "visualElements"
    HISTORY_ITEMS = "historyItems"

class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORY_ITEMS = "historyItems"

class Enum6(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ACTIVE_DURATION_SECONDS = "activeDurationSeconds"
    ACTIVE_DURATION_SECONDS_DESC = "activeDurationSeconds desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    EXPIRATION_DATE_TIME_DESC = "expirationDateTime desc"
    LAST_ACTIVE_DATE_TIME = "lastActiveDateTime"
    LAST_ACTIVE_DATE_TIME_DESC = "lastActiveDateTime desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    STARTED_DATE_TIME = "startedDateTime"
    STARTED_DATE_TIME_DESC = "startedDateTime desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    USER_TIMEZONE = "userTimezone"
    USER_TIMEZONE_DESC = "userTimezone desc"

class Enum7(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVE_DURATION_SECONDS = "activeDurationSeconds"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    LAST_ACTIVE_DATE_TIME = "lastActiveDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STARTED_DATE_TIME = "startedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    ACTIVITY = "activity"

class Enum9(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVE_DURATION_SECONDS = "activeDurationSeconds"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    LAST_ACTIVE_DATE_TIME = "lastActiveDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STARTED_DATE_TIME = "startedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    ACTIVITY = "activity"

class Get2ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATION_URL = "activationUrl"
    ACTIVITY_SOURCE_HOST = "activitySourceHost"
    APP_ACTIVITY_ID = "appActivityId"
    APP_DISPLAY_NAME = "appDisplayName"
    CONTENT_INFO = "contentInfo"
    CONTENT_URL = "contentUrl"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    FALLBACK_URL = "fallbackUrl"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    VISUAL_ELEMENTS = "visualElements"
    HISTORY_ITEMS = "historyItems"

class Get3ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORY_ITEMS = "historyItems"

class Get4ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ACTIVITY = "activity"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ACTIVATION_URL = "activationUrl"
    ACTIVATION_URL_DESC = "activationUrl desc"
    ACTIVITY_SOURCE_HOST = "activitySourceHost"
    ACTIVITY_SOURCE_HOST_DESC = "activitySourceHost desc"
    APP_ACTIVITY_ID = "appActivityId"
    APP_ACTIVITY_ID_DESC = "appActivityId desc"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_DISPLAY_NAME_DESC = "appDisplayName desc"
    CONTENT_INFO = "contentInfo"
    CONTENT_INFO_DESC = "contentInfo desc"
    CONTENT_URL = "contentUrl"
    CONTENT_URL_DESC = "contentUrl desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    EXPIRATION_DATE_TIME_DESC = "expirationDateTime desc"
    FALLBACK_URL = "fallbackUrl"
    FALLBACK_URL_DESC = "fallbackUrl desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    USER_TIMEZONE = "userTimezone"
    USER_TIMEZONE_DESC = "userTimezone desc"
    VISUAL_ELEMENTS = "visualElements"
    VISUAL_ELEMENTS_DESC = "visualElements desc"

class Get7ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATION_URL = "activationUrl"
    ACTIVITY_SOURCE_HOST = "activitySourceHost"
    APP_ACTIVITY_ID = "appActivityId"
    APP_DISPLAY_NAME = "appDisplayName"
    CONTENT_INFO = "contentInfo"
    CONTENT_URL = "contentUrl"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    FALLBACK_URL = "fallbackUrl"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    VISUAL_ELEMENTS = "visualElements"
    HISTORY_ITEMS = "historyItems"

class Get8ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORY_ITEMS = "historyItems"

class Get9ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ACTIVITY = "activity"

class MicrosoftGraphStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ACTIVE = "active"
    UPDATED = "updated"
    DELETED = "deleted"
    IGNORED = "ignored"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"
