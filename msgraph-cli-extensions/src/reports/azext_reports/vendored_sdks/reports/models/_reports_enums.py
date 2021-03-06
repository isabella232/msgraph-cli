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


class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVITY_DATE_TIME = "activityDateTime"
    ACTIVITY_DISPLAY_NAME = "activityDisplayName"
    ADDITIONAL_DETAILS = "additionalDetails"
    CATEGORY = "category"
    CORRELATION_ID = "correlationId"
    INITIATED_BY = "initiatedBy"
    LOGGED_BY_SERVICE = "loggedByService"
    OPERATION_TYPE = "operationType"
    RESULT = "result"
    RESULT_REASON = "resultReason"
    TARGET_RESOURCES = "targetResources"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_DISPLAY_NAME_DESC = "appDisplayName desc"
    APP_ID = "appId"
    APP_ID_DESC = "appId desc"
    APPLIED_CONDITIONAL_ACCESS_POLICIES = "appliedConditionalAccessPolicies"
    APPLIED_CONDITIONAL_ACCESS_POLICIES_DESC = "appliedConditionalAccessPolicies desc"
    CLIENT_APP_USED = "clientAppUsed"
    CLIENT_APP_USED_DESC = "clientAppUsed desc"
    CONDITIONAL_ACCESS_STATUS = "conditionalAccessStatus"
    CONDITIONAL_ACCESS_STATUS_DESC = "conditionalAccessStatus desc"
    CORRELATION_ID = "correlationId"
    CORRELATION_ID_DESC = "correlationId desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    DEVICE_DETAIL = "deviceDetail"
    DEVICE_DETAIL_DESC = "deviceDetail desc"
    IP_ADDRESS = "ipAddress"
    IP_ADDRESS_DESC = "ipAddress desc"
    IS_INTERACTIVE = "isInteractive"
    IS_INTERACTIVE_DESC = "isInteractive desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_DISPLAY_NAME_DESC = "resourceDisplayName desc"
    RESOURCE_ID = "resourceId"
    RESOURCE_ID_DESC = "resourceId desc"
    RISK_DETAIL = "riskDetail"
    RISK_DETAIL_DESC = "riskDetail desc"
    RISK_EVENT_TYPES = "riskEventTypes"
    RISK_EVENT_TYPES_DESC = "riskEventTypes desc"
    RISK_EVENT_TYPES_V2 = "riskEventTypes_v2"
    RISK_EVENT_TYPES_V2_DESC = "riskEventTypes_v2 desc"
    RISK_LEVEL_AGGREGATED = "riskLevelAggregated"
    RISK_LEVEL_AGGREGATED_DESC = "riskLevelAggregated desc"
    RISK_LEVEL_DURING_SIGN_IN = "riskLevelDuringSignIn"
    RISK_LEVEL_DURING_SIGN_IN_DESC = "riskLevelDuringSignIn desc"
    RISK_STATE = "riskState"
    RISK_STATE_DESC = "riskState desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    USER_DISPLAY_NAME = "userDisplayName"
    USER_DISPLAY_NAME_DESC = "userDisplayName desc"
    USER_ID = "userId"
    USER_ID_DESC = "userId desc"
    USER_PRINCIPAL_NAME = "userPrincipalName"
    USER_PRINCIPAL_NAME_DESC = "userPrincipalName desc"
    TARGET_TENANT_ID = "targetTenantId"
    TARGET_TENANT_ID_DESC = "targetTenantId desc"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_ID = "appId"
    APPLIED_CONDITIONAL_ACCESS_POLICIES = "appliedConditionalAccessPolicies"
    CLIENT_APP_USED = "clientAppUsed"
    CONDITIONAL_ACCESS_STATUS = "conditionalAccessStatus"
    CORRELATION_ID = "correlationId"
    CREATED_DATE_TIME = "createdDateTime"
    DEVICE_DETAIL = "deviceDetail"
    IP_ADDRESS = "ipAddress"
    IS_INTERACTIVE = "isInteractive"
    LOCATION = "location"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"
    RISK_DETAIL = "riskDetail"
    RISK_EVENT_TYPES = "riskEventTypes"
    RISK_EVENT_TYPES_V2 = "riskEventTypes_v2"
    RISK_LEVEL_AGGREGATED = "riskLevelAggregated"
    RISK_LEVEL_DURING_SIGN_IN = "riskLevelDuringSignIn"
    RISK_STATE = "riskState"
    STATUS = "status"
    USER_DISPLAY_NAME = "userDisplayName"
    USER_ID = "userId"
    USER_PRINCIPAL_NAME = "userPrincipalName"
    TARGET_TENANT_ID = "targetTenantId"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_ID = "appId"
    APPLIED_CONDITIONAL_ACCESS_POLICIES = "appliedConditionalAccessPolicies"
    CLIENT_APP_USED = "clientAppUsed"
    CONDITIONAL_ACCESS_STATUS = "conditionalAccessStatus"
    CORRELATION_ID = "correlationId"
    CREATED_DATE_TIME = "createdDateTime"
    DEVICE_DETAIL = "deviceDetail"
    IP_ADDRESS = "ipAddress"
    IS_INTERACTIVE = "isInteractive"
    LOCATION = "location"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"
    RISK_DETAIL = "riskDetail"
    RISK_EVENT_TYPES = "riskEventTypes"
    RISK_EVENT_TYPES_V2 = "riskEventTypes_v2"
    RISK_LEVEL_AGGREGATED = "riskLevelAggregated"
    RISK_LEVEL_DURING_SIGN_IN = "riskLevelDuringSignIn"
    RISK_STATE = "riskState"
    STATUS = "status"
    USER_DISPLAY_NAME = "userDisplayName"
    USER_ID = "userId"
    USER_PRINCIPAL_NAME = "userPrincipalName"
    TARGET_TENANT_ID = "targetTenantId"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_DISPLAY_NAME_DESC = "appDisplayName desc"
    APP_ID = "appId"
    APP_ID_DESC = "appId desc"
    APPLIED_CONDITIONAL_ACCESS_POLICIES = "appliedConditionalAccessPolicies"
    APPLIED_CONDITIONAL_ACCESS_POLICIES_DESC = "appliedConditionalAccessPolicies desc"
    CLIENT_APP_USED = "clientAppUsed"
    CLIENT_APP_USED_DESC = "clientAppUsed desc"
    CONDITIONAL_ACCESS_STATUS = "conditionalAccessStatus"
    CONDITIONAL_ACCESS_STATUS_DESC = "conditionalAccessStatus desc"
    CORRELATION_ID = "correlationId"
    CORRELATION_ID_DESC = "correlationId desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    DEVICE_DETAIL = "deviceDetail"
    DEVICE_DETAIL_DESC = "deviceDetail desc"
    IP_ADDRESS = "ipAddress"
    IP_ADDRESS_DESC = "ipAddress desc"
    IS_INTERACTIVE = "isInteractive"
    IS_INTERACTIVE_DESC = "isInteractive desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_DISPLAY_NAME_DESC = "resourceDisplayName desc"
    RESOURCE_ID = "resourceId"
    RESOURCE_ID_DESC = "resourceId desc"
    RISK_DETAIL = "riskDetail"
    RISK_DETAIL_DESC = "riskDetail desc"
    RISK_EVENT_TYPES = "riskEventTypes"
    RISK_EVENT_TYPES_DESC = "riskEventTypes desc"
    RISK_EVENT_TYPES_V2 = "riskEventTypes_v2"
    RISK_EVENT_TYPES_V2_DESC = "riskEventTypes_v2 desc"
    RISK_LEVEL_AGGREGATED = "riskLevelAggregated"
    RISK_LEVEL_AGGREGATED_DESC = "riskLevelAggregated desc"
    RISK_LEVEL_DURING_SIGN_IN = "riskLevelDuringSignIn"
    RISK_LEVEL_DURING_SIGN_IN_DESC = "riskLevelDuringSignIn desc"
    RISK_STATE = "riskState"
    RISK_STATE_DESC = "riskState desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    USER_DISPLAY_NAME = "userDisplayName"
    USER_DISPLAY_NAME_DESC = "userDisplayName desc"
    USER_ID = "userId"
    USER_ID_DESC = "userId desc"
    USER_PRINCIPAL_NAME = "userPrincipalName"
    USER_PRINCIPAL_NAME_DESC = "userPrincipalName desc"

class Enum17(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_ID = "appId"
    APPLIED_CONDITIONAL_ACCESS_POLICIES = "appliedConditionalAccessPolicies"
    CLIENT_APP_USED = "clientAppUsed"
    CONDITIONAL_ACCESS_STATUS = "conditionalAccessStatus"
    CORRELATION_ID = "correlationId"
    CREATED_DATE_TIME = "createdDateTime"
    DEVICE_DETAIL = "deviceDetail"
    IP_ADDRESS = "ipAddress"
    IS_INTERACTIVE = "isInteractive"
    LOCATION = "location"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"
    RISK_DETAIL = "riskDetail"
    RISK_EVENT_TYPES = "riskEventTypes"
    RISK_EVENT_TYPES_V2 = "riskEventTypes_v2"
    RISK_LEVEL_AGGREGATED = "riskLevelAggregated"
    RISK_LEVEL_DURING_SIGN_IN = "riskLevelDuringSignIn"
    RISK_STATE = "riskState"
    STATUS = "status"
    USER_DISPLAY_NAME = "userDisplayName"
    USER_ID = "userId"
    USER_PRINCIPAL_NAME = "userPrincipalName"

class Enum18(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_ID = "appId"
    APPLIED_CONDITIONAL_ACCESS_POLICIES = "appliedConditionalAccessPolicies"
    CLIENT_APP_USED = "clientAppUsed"
    CONDITIONAL_ACCESS_STATUS = "conditionalAccessStatus"
    CORRELATION_ID = "correlationId"
    CREATED_DATE_TIME = "createdDateTime"
    DEVICE_DETAIL = "deviceDetail"
    IP_ADDRESS = "ipAddress"
    IS_INTERACTIVE = "isInteractive"
    LOCATION = "location"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"
    RISK_DETAIL = "riskDetail"
    RISK_EVENT_TYPES = "riskEventTypes"
    RISK_EVENT_TYPES_V2 = "riskEventTypes_v2"
    RISK_LEVEL_AGGREGATED = "riskLevelAggregated"
    RISK_LEVEL_DURING_SIGN_IN = "riskLevelDuringSignIn"
    RISK_STATE = "riskState"
    STATUS = "status"
    USER_DISPLAY_NAME = "userDisplayName"
    USER_ID = "userId"
    USER_PRINCIPAL_NAME = "userPrincipalName"

class Get0ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DIRECTORY_AUDITS = "directoryAudits"
    RESTRICTED_SIGN_INS = "restrictedSignIns"
    SIGN_INS = "signIns"

class Get1ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DIRECTORY_AUDITS = "directoryAudits"
    RESTRICTED_SIGN_INS = "restrictedSignIns"
    SIGN_INS = "signIns"

class Get5ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ACTIVITY_DATE_TIME = "activityDateTime"
    ACTIVITY_DATE_TIME_DESC = "activityDateTime desc"
    ACTIVITY_DISPLAY_NAME = "activityDisplayName"
    ACTIVITY_DISPLAY_NAME_DESC = "activityDisplayName desc"
    ADDITIONAL_DETAILS = "additionalDetails"
    ADDITIONAL_DETAILS_DESC = "additionalDetails desc"
    CATEGORY = "category"
    CATEGORY_DESC = "category desc"
    CORRELATION_ID = "correlationId"
    CORRELATION_ID_DESC = "correlationId desc"
    INITIATED_BY = "initiatedBy"
    INITIATED_BY_DESC = "initiatedBy desc"
    LOGGED_BY_SERVICE = "loggedByService"
    LOGGED_BY_SERVICE_DESC = "loggedByService desc"
    OPERATION_TYPE = "operationType"
    OPERATION_TYPE_DESC = "operationType desc"
    RESULT = "result"
    RESULT_DESC = "result desc"
    RESULT_REASON = "resultReason"
    RESULT_REASON_DESC = "resultReason desc"
    TARGET_RESOURCES = "targetResources"
    TARGET_RESOURCES_DESC = "targetResources desc"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVITY_DATE_TIME = "activityDateTime"
    ACTIVITY_DISPLAY_NAME = "activityDisplayName"
    ADDITIONAL_DETAILS = "additionalDetails"
    CATEGORY = "category"
    CORRELATION_ID = "correlationId"
    INITIATED_BY = "initiatedBy"
    LOGGED_BY_SERVICE = "loggedByService"
    OPERATION_TYPE = "operationType"
    RESULT = "result"
    RESULT_REASON = "resultReason"
    TARGET_RESOURCES = "targetResources"

class MicrosoftGraphAppliedConditionalAccessPolicyResult(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUCCESS = "success"
    FAILURE = "failure"
    NOT_APPLIED = "notApplied"
    NOT_ENABLED = "notEnabled"
    UNKNOWN = "unknown"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphConditionalAccessStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUCCESS = "success"
    FAILURE = "failure"
    NOT_APPLIED = "notApplied"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphGroupType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNIFIED_GROUPS = "unifiedGroups"
    AZURE_AD = "azureAD"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphOperationResult(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUCCESS = "success"
    FAILURE = "failure"
    TIMEOUT = "timeout"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphRiskDetail(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    ADMIN_GENERATED_TEMPORARY_PASSWORD = "adminGeneratedTemporaryPassword"
    USER_PERFORMED_SECURED_PASSWORD_CHANGE = "userPerformedSecuredPasswordChange"
    USER_PERFORMED_SECURED_PASSWORD_RESET = "userPerformedSecuredPasswordReset"
    ADMIN_CONFIRMED_SIGNIN_SAFE = "adminConfirmedSigninSafe"
    AI_CONFIRMED_SIGNIN_SAFE = "aiConfirmedSigninSafe"
    USER_PASSED_MFA_DRIVEN_BY_RISK_BASED_POLICY = "userPassedMFADrivenByRiskBasedPolicy"
    ADMIN_DISMISSED_ALL_RISK_FOR_USER = "adminDismissedAllRiskForUser"
    ADMIN_CONFIRMED_SIGNIN_COMPROMISED = "adminConfirmedSigninCompromised"
    HIDDEN = "hidden"
    ADMIN_CONFIRMED_USER_COMPROMISED = "adminConfirmedUserCompromised"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphRiskEventType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNLIKELY_TRAVEL = "unlikelyTravel"
    ANONYMIZED_IP_ADDRESS = "anonymizedIPAddress"
    MALICIOUS_IP_ADDRESS = "maliciousIPAddress"
    UNFAMILIAR_FEATURES = "unfamiliarFeatures"
    MALWARE_INFECTED_IP_ADDRESS = "malwareInfectedIPAddress"
    SUSPICIOUS_IP_ADDRESS = "suspiciousIPAddress"
    LEAKED_CREDENTIALS = "leakedCredentials"
    INVESTIGATIONS_THREAT_INTELLIGENCE = "investigationsThreatIntelligence"
    GENERIC = "generic"
    ADMIN_CONFIRMED_USER_COMPROMISED = "adminConfirmedUserCompromised"
    MCAS_IMPOSSIBLE_TRAVEL = "mcasImpossibleTravel"
    MCAS_SUSPICIOUS_INBOX_MANIPULATION_RULES = "mcasSuspiciousInboxManipulationRules"
    INVESTIGATIONS_THREAT_INTELLIGENCE_SIGNIN_LINKED = "investigationsThreatIntelligenceSigninLinked"
    MALICIOUS_IP_ADDRESS_VALID_CREDENTIALS_BLOCKED_IP = "maliciousIPAddressValidCredentialsBlockedIP"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphRiskLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    HIDDEN = "hidden"
    NONE = "none"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphRiskState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    CONFIRMED_SAFE = "confirmedSafe"
    REMEDIATED = "remediated"
    DISMISSED = "dismissed"
    AT_RISK = "atRisk"
    CONFIRMED_COMPROMISED = "confirmedCompromised"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"
