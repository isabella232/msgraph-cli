# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CollectionOfApplicationSignInDetailedSummary
    from ._models_py3 import CollectionOfCredentialUserRegistrationDetails
    from ._models_py3 import CollectionOfPrintUsageSummaryByPrinter
    from ._models_py3 import CollectionOfPrintUsageSummaryByPrinter0
    from ._models_py3 import CollectionOfPrintUsageSummaryByUser
    from ._models_py3 import CollectionOfPrintUsageSummaryByUser0
    from ._models_py3 import CollectionOfUserCredentialUsageDetails
    from ._models_py3 import MicrosoftGraphApplicationSignInDetailedSummary
    from ._models_py3 import MicrosoftGraphApplicationSignInSummary
    from ._models_py3 import MicrosoftGraphAzureAdFeatureUsage
    from ._models_py3 import MicrosoftGraphAzureAdLicenseUsage
    from ._models_py3 import MicrosoftGraphAzureAdUserFeatureUsage
    from ._models_py3 import MicrosoftGraphCredentialUsageSummary
    from ._models_py3 import MicrosoftGraphCredentialUserRegistrationCount
    from ._models_py3 import MicrosoftGraphCredentialUserRegistrationDetails
    from ._models_py3 import MicrosoftGraphEmailActivitySummary
    from ._models_py3 import MicrosoftGraphEmailActivityUserDetail
    from ._models_py3 import MicrosoftGraphEmailAppUsageAppsUserCounts
    from ._models_py3 import MicrosoftGraphEmailAppUsageUserCounts
    from ._models_py3 import MicrosoftGraphEmailAppUsageUserDetail
    from ._models_py3 import MicrosoftGraphEmailAppUsageVersionsUserCounts
    from ._models_py3 import MicrosoftGraphEntity
    from ._models_py3 import MicrosoftGraphFeatureUsageDetail
    from ._models_py3 import MicrosoftGraphKeyValuePair
    from ._models_py3 import MicrosoftGraphLicenseInfoDetail
    from ._models_py3 import MicrosoftGraphMailboxUsageDetail
    from ._models_py3 import MicrosoftGraphMailboxUsageMailboxCounts
    from ._models_py3 import MicrosoftGraphMailboxUsageQuotaStatusMailboxCounts
    from ._models_py3 import MicrosoftGraphMailboxUsageStorage
    from ._models_py3 import MicrosoftGraphOffice365ActivationCounts
    from ._models_py3 import MicrosoftGraphOffice365ActivationsUserCounts
    from ._models_py3 import MicrosoftGraphOffice365ActivationsUserDetail
    from ._models_py3 import MicrosoftGraphOffice365ActiveUserCounts
    from ._models_py3 import MicrosoftGraphOffice365ActiveUserDetail
    from ._models_py3 import MicrosoftGraphOffice365GroupsActivityCounts
    from ._models_py3 import MicrosoftGraphOffice365GroupsActivityDetail
    from ._models_py3 import MicrosoftGraphOffice365GroupsActivityFileCounts
    from ._models_py3 import MicrosoftGraphOffice365GroupsActivityGroupCounts
    from ._models_py3 import MicrosoftGraphOffice365GroupsActivityStorage
    from ._models_py3 import MicrosoftGraphOffice365ServicesUserCounts
    from ._models_py3 import MicrosoftGraphOneDriveActivityUserDetail
    from ._models_py3 import MicrosoftGraphOneDriveUsageAccountCounts
    from ._models_py3 import MicrosoftGraphOneDriveUsageAccountDetail
    from ._models_py3 import MicrosoftGraphOneDriveUsageFileCounts
    from ._models_py3 import MicrosoftGraphPrintUsageSummaryByPrinter
    from ._models_py3 import MicrosoftGraphPrintUsageSummaryByUser
    from ._models_py3 import MicrosoftGraphRelyingPartyDetailedSummary
    from ._models_py3 import MicrosoftGraphReport
    from ._models_py3 import MicrosoftGraphReportRoot
    from ._models_py3 import MicrosoftGraphSharePointActivityPages
    from ._models_py3 import MicrosoftGraphSharePointActivityUserCounts
    from ._models_py3 import MicrosoftGraphSharePointActivityUserDetail
    from ._models_py3 import MicrosoftGraphSharePointSiteUsageDetail
    from ._models_py3 import MicrosoftGraphSharePointSiteUsageFileCounts
    from ._models_py3 import MicrosoftGraphSharePointSiteUsagePages
    from ._models_py3 import MicrosoftGraphSharePointSiteUsageSiteCounts
    from ._models_py3 import MicrosoftGraphSiteActivitySummary
    from ._models_py3 import MicrosoftGraphSiteUsageStorage
    from ._models_py3 import MicrosoftGraphSkypeForBusinessActivityCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessActivityUserCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessActivityUserDetail
    from ._models_py3 import MicrosoftGraphSkypeForBusinessDeviceUsageDistributionUserCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessDeviceUsageUserCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessDeviceUsageUserDetail
    from ._models_py3 import MicrosoftGraphSkypeForBusinessOrganizerActivityCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessOrganizerActivityMinuteCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessOrganizerActivityUserCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessParticipantActivityCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessParticipantActivityMinuteCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessParticipantActivityUserCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessPeerToPeerActivityCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessPeerToPeerActivityMinuteCounts
    from ._models_py3 import MicrosoftGraphSkypeForBusinessPeerToPeerActivityUserCounts
    from ._models_py3 import MicrosoftGraphTeamsDeviceUsageDistributionUserCounts
    from ._models_py3 import MicrosoftGraphTeamsDeviceUsageUserCounts
    from ._models_py3 import MicrosoftGraphTeamsDeviceUsageUserDetail
    from ._models_py3 import MicrosoftGraphTeamsUserActivityCounts
    from ._models_py3 import MicrosoftGraphTeamsUserActivityUserCounts
    from ._models_py3 import MicrosoftGraphTeamsUserActivityUserDetail
    from ._models_py3 import MicrosoftGraphUserActivationCounts
    from ._models_py3 import MicrosoftGraphUserCredentialUsageDetails
    from ._models_py3 import MicrosoftGraphUserRegistrationCount
    from ._models_py3 import MicrosoftGraphYammerActivitySummary
    from ._models_py3 import MicrosoftGraphYammerActivityUserDetail
    from ._models_py3 import MicrosoftGraphYammerDeviceUsageDistributionUserCounts
    from ._models_py3 import MicrosoftGraphYammerDeviceUsageUserCounts
    from ._models_py3 import MicrosoftGraphYammerDeviceUsageUserDetail
    from ._models_py3 import MicrosoftGraphYammerGroupsActivityCounts
    from ._models_py3 import MicrosoftGraphYammerGroupsActivityDetail
    from ._models_py3 import MicrosoftGraphYammerGroupsActivityGroupCounts
    from ._models_py3 import OdataError
    from ._models_py3 import OdataErrorDetail
    from ._models_py3 import OdataErrorMain
except (SyntaxError, ImportError):
    from ._models import CollectionOfApplicationSignInDetailedSummary  # type: ignore
    from ._models import CollectionOfCredentialUserRegistrationDetails  # type: ignore
    from ._models import CollectionOfPrintUsageSummaryByPrinter  # type: ignore
    from ._models import CollectionOfPrintUsageSummaryByPrinter0  # type: ignore
    from ._models import CollectionOfPrintUsageSummaryByUser  # type: ignore
    from ._models import CollectionOfPrintUsageSummaryByUser0  # type: ignore
    from ._models import CollectionOfUserCredentialUsageDetails  # type: ignore
    from ._models import MicrosoftGraphApplicationSignInDetailedSummary  # type: ignore
    from ._models import MicrosoftGraphApplicationSignInSummary  # type: ignore
    from ._models import MicrosoftGraphAzureAdFeatureUsage  # type: ignore
    from ._models import MicrosoftGraphAzureAdLicenseUsage  # type: ignore
    from ._models import MicrosoftGraphAzureAdUserFeatureUsage  # type: ignore
    from ._models import MicrosoftGraphCredentialUsageSummary  # type: ignore
    from ._models import MicrosoftGraphCredentialUserRegistrationCount  # type: ignore
    from ._models import MicrosoftGraphCredentialUserRegistrationDetails  # type: ignore
    from ._models import MicrosoftGraphEmailActivitySummary  # type: ignore
    from ._models import MicrosoftGraphEmailActivityUserDetail  # type: ignore
    from ._models import MicrosoftGraphEmailAppUsageAppsUserCounts  # type: ignore
    from ._models import MicrosoftGraphEmailAppUsageUserCounts  # type: ignore
    from ._models import MicrosoftGraphEmailAppUsageUserDetail  # type: ignore
    from ._models import MicrosoftGraphEmailAppUsageVersionsUserCounts  # type: ignore
    from ._models import MicrosoftGraphEntity  # type: ignore
    from ._models import MicrosoftGraphFeatureUsageDetail  # type: ignore
    from ._models import MicrosoftGraphKeyValuePair  # type: ignore
    from ._models import MicrosoftGraphLicenseInfoDetail  # type: ignore
    from ._models import MicrosoftGraphMailboxUsageDetail  # type: ignore
    from ._models import MicrosoftGraphMailboxUsageMailboxCounts  # type: ignore
    from ._models import MicrosoftGraphMailboxUsageQuotaStatusMailboxCounts  # type: ignore
    from ._models import MicrosoftGraphMailboxUsageStorage  # type: ignore
    from ._models import MicrosoftGraphOffice365ActivationCounts  # type: ignore
    from ._models import MicrosoftGraphOffice365ActivationsUserCounts  # type: ignore
    from ._models import MicrosoftGraphOffice365ActivationsUserDetail  # type: ignore
    from ._models import MicrosoftGraphOffice365ActiveUserCounts  # type: ignore
    from ._models import MicrosoftGraphOffice365ActiveUserDetail  # type: ignore
    from ._models import MicrosoftGraphOffice365GroupsActivityCounts  # type: ignore
    from ._models import MicrosoftGraphOffice365GroupsActivityDetail  # type: ignore
    from ._models import MicrosoftGraphOffice365GroupsActivityFileCounts  # type: ignore
    from ._models import MicrosoftGraphOffice365GroupsActivityGroupCounts  # type: ignore
    from ._models import MicrosoftGraphOffice365GroupsActivityStorage  # type: ignore
    from ._models import MicrosoftGraphOffice365ServicesUserCounts  # type: ignore
    from ._models import MicrosoftGraphOneDriveActivityUserDetail  # type: ignore
    from ._models import MicrosoftGraphOneDriveUsageAccountCounts  # type: ignore
    from ._models import MicrosoftGraphOneDriveUsageAccountDetail  # type: ignore
    from ._models import MicrosoftGraphOneDriveUsageFileCounts  # type: ignore
    from ._models import MicrosoftGraphPrintUsageSummaryByPrinter  # type: ignore
    from ._models import MicrosoftGraphPrintUsageSummaryByUser  # type: ignore
    from ._models import MicrosoftGraphRelyingPartyDetailedSummary  # type: ignore
    from ._models import MicrosoftGraphReport  # type: ignore
    from ._models import MicrosoftGraphReportRoot  # type: ignore
    from ._models import MicrosoftGraphSharePointActivityPages  # type: ignore
    from ._models import MicrosoftGraphSharePointActivityUserCounts  # type: ignore
    from ._models import MicrosoftGraphSharePointActivityUserDetail  # type: ignore
    from ._models import MicrosoftGraphSharePointSiteUsageDetail  # type: ignore
    from ._models import MicrosoftGraphSharePointSiteUsageFileCounts  # type: ignore
    from ._models import MicrosoftGraphSharePointSiteUsagePages  # type: ignore
    from ._models import MicrosoftGraphSharePointSiteUsageSiteCounts  # type: ignore
    from ._models import MicrosoftGraphSiteActivitySummary  # type: ignore
    from ._models import MicrosoftGraphSiteUsageStorage  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessActivityCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessActivityUserCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessActivityUserDetail  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessDeviceUsageDistributionUserCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessDeviceUsageUserCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessDeviceUsageUserDetail  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessOrganizerActivityCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessOrganizerActivityMinuteCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessOrganizerActivityUserCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessParticipantActivityCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessParticipantActivityMinuteCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessParticipantActivityUserCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessPeerToPeerActivityCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessPeerToPeerActivityMinuteCounts  # type: ignore
    from ._models import MicrosoftGraphSkypeForBusinessPeerToPeerActivityUserCounts  # type: ignore
    from ._models import MicrosoftGraphTeamsDeviceUsageDistributionUserCounts  # type: ignore
    from ._models import MicrosoftGraphTeamsDeviceUsageUserCounts  # type: ignore
    from ._models import MicrosoftGraphTeamsDeviceUsageUserDetail  # type: ignore
    from ._models import MicrosoftGraphTeamsUserActivityCounts  # type: ignore
    from ._models import MicrosoftGraphTeamsUserActivityUserCounts  # type: ignore
    from ._models import MicrosoftGraphTeamsUserActivityUserDetail  # type: ignore
    from ._models import MicrosoftGraphUserActivationCounts  # type: ignore
    from ._models import MicrosoftGraphUserCredentialUsageDetails  # type: ignore
    from ._models import MicrosoftGraphUserRegistrationCount  # type: ignore
    from ._models import MicrosoftGraphYammerActivitySummary  # type: ignore
    from ._models import MicrosoftGraphYammerActivityUserDetail  # type: ignore
    from ._models import MicrosoftGraphYammerDeviceUsageDistributionUserCounts  # type: ignore
    from ._models import MicrosoftGraphYammerDeviceUsageUserCounts  # type: ignore
    from ._models import MicrosoftGraphYammerDeviceUsageUserDetail  # type: ignore
    from ._models import MicrosoftGraphYammerGroupsActivityCounts  # type: ignore
    from ._models import MicrosoftGraphYammerGroupsActivityDetail  # type: ignore
    from ._models import MicrosoftGraphYammerGroupsActivityGroupCounts  # type: ignore
    from ._models import OdataError  # type: ignore
    from ._models import OdataErrorDetail  # type: ignore
    from ._models import OdataErrorMain  # type: ignore

from ._reports_enums import (
    Enum10,
    Enum11,
    Enum12,
    Enum13,
    Enum14,
    Enum15,
    Enum16,
    Enum20,
    Enum21,
    Enum22,
    Enum23,
    Enum24,
    Enum25,
    Enum26,
    Enum27,
    Enum28,
    Enum7,
    Enum8,
    Enum9,
    Get0ItemsItem,
    Get1ItemsItem,
    Get5ItemsItem,
    Get6ItemsItem,
    MicrosoftGraphAzureAdLicenseType,
    MicrosoftGraphFeatureType,
    MicrosoftGraphMigrationStatus,
    MicrosoftGraphRegistrationAuthMethod,
    MicrosoftGraphRegistrationStatusType,
    MicrosoftGraphUsageAuthMethod,
)

__all__ = [
    'CollectionOfApplicationSignInDetailedSummary',
    'CollectionOfCredentialUserRegistrationDetails',
    'CollectionOfPrintUsageSummaryByPrinter',
    'CollectionOfPrintUsageSummaryByPrinter0',
    'CollectionOfPrintUsageSummaryByUser',
    'CollectionOfPrintUsageSummaryByUser0',
    'CollectionOfUserCredentialUsageDetails',
    'MicrosoftGraphApplicationSignInDetailedSummary',
    'MicrosoftGraphApplicationSignInSummary',
    'MicrosoftGraphAzureAdFeatureUsage',
    'MicrosoftGraphAzureAdLicenseUsage',
    'MicrosoftGraphAzureAdUserFeatureUsage',
    'MicrosoftGraphCredentialUsageSummary',
    'MicrosoftGraphCredentialUserRegistrationCount',
    'MicrosoftGraphCredentialUserRegistrationDetails',
    'MicrosoftGraphEmailActivitySummary',
    'MicrosoftGraphEmailActivityUserDetail',
    'MicrosoftGraphEmailAppUsageAppsUserCounts',
    'MicrosoftGraphEmailAppUsageUserCounts',
    'MicrosoftGraphEmailAppUsageUserDetail',
    'MicrosoftGraphEmailAppUsageVersionsUserCounts',
    'MicrosoftGraphEntity',
    'MicrosoftGraphFeatureUsageDetail',
    'MicrosoftGraphKeyValuePair',
    'MicrosoftGraphLicenseInfoDetail',
    'MicrosoftGraphMailboxUsageDetail',
    'MicrosoftGraphMailboxUsageMailboxCounts',
    'MicrosoftGraphMailboxUsageQuotaStatusMailboxCounts',
    'MicrosoftGraphMailboxUsageStorage',
    'MicrosoftGraphOffice365ActivationCounts',
    'MicrosoftGraphOffice365ActivationsUserCounts',
    'MicrosoftGraphOffice365ActivationsUserDetail',
    'MicrosoftGraphOffice365ActiveUserCounts',
    'MicrosoftGraphOffice365ActiveUserDetail',
    'MicrosoftGraphOffice365GroupsActivityCounts',
    'MicrosoftGraphOffice365GroupsActivityDetail',
    'MicrosoftGraphOffice365GroupsActivityFileCounts',
    'MicrosoftGraphOffice365GroupsActivityGroupCounts',
    'MicrosoftGraphOffice365GroupsActivityStorage',
    'MicrosoftGraphOffice365ServicesUserCounts',
    'MicrosoftGraphOneDriveActivityUserDetail',
    'MicrosoftGraphOneDriveUsageAccountCounts',
    'MicrosoftGraphOneDriveUsageAccountDetail',
    'MicrosoftGraphOneDriveUsageFileCounts',
    'MicrosoftGraphPrintUsageSummaryByPrinter',
    'MicrosoftGraphPrintUsageSummaryByUser',
    'MicrosoftGraphRelyingPartyDetailedSummary',
    'MicrosoftGraphReport',
    'MicrosoftGraphReportRoot',
    'MicrosoftGraphSharePointActivityPages',
    'MicrosoftGraphSharePointActivityUserCounts',
    'MicrosoftGraphSharePointActivityUserDetail',
    'MicrosoftGraphSharePointSiteUsageDetail',
    'MicrosoftGraphSharePointSiteUsageFileCounts',
    'MicrosoftGraphSharePointSiteUsagePages',
    'MicrosoftGraphSharePointSiteUsageSiteCounts',
    'MicrosoftGraphSiteActivitySummary',
    'MicrosoftGraphSiteUsageStorage',
    'MicrosoftGraphSkypeForBusinessActivityCounts',
    'MicrosoftGraphSkypeForBusinessActivityUserCounts',
    'MicrosoftGraphSkypeForBusinessActivityUserDetail',
    'MicrosoftGraphSkypeForBusinessDeviceUsageDistributionUserCounts',
    'MicrosoftGraphSkypeForBusinessDeviceUsageUserCounts',
    'MicrosoftGraphSkypeForBusinessDeviceUsageUserDetail',
    'MicrosoftGraphSkypeForBusinessOrganizerActivityCounts',
    'MicrosoftGraphSkypeForBusinessOrganizerActivityMinuteCounts',
    'MicrosoftGraphSkypeForBusinessOrganizerActivityUserCounts',
    'MicrosoftGraphSkypeForBusinessParticipantActivityCounts',
    'MicrosoftGraphSkypeForBusinessParticipantActivityMinuteCounts',
    'MicrosoftGraphSkypeForBusinessParticipantActivityUserCounts',
    'MicrosoftGraphSkypeForBusinessPeerToPeerActivityCounts',
    'MicrosoftGraphSkypeForBusinessPeerToPeerActivityMinuteCounts',
    'MicrosoftGraphSkypeForBusinessPeerToPeerActivityUserCounts',
    'MicrosoftGraphTeamsDeviceUsageDistributionUserCounts',
    'MicrosoftGraphTeamsDeviceUsageUserCounts',
    'MicrosoftGraphTeamsDeviceUsageUserDetail',
    'MicrosoftGraphTeamsUserActivityCounts',
    'MicrosoftGraphTeamsUserActivityUserCounts',
    'MicrosoftGraphTeamsUserActivityUserDetail',
    'MicrosoftGraphUserActivationCounts',
    'MicrosoftGraphUserCredentialUsageDetails',
    'MicrosoftGraphUserRegistrationCount',
    'MicrosoftGraphYammerActivitySummary',
    'MicrosoftGraphYammerActivityUserDetail',
    'MicrosoftGraphYammerDeviceUsageDistributionUserCounts',
    'MicrosoftGraphYammerDeviceUsageUserCounts',
    'MicrosoftGraphYammerDeviceUsageUserDetail',
    'MicrosoftGraphYammerGroupsActivityCounts',
    'MicrosoftGraphYammerGroupsActivityDetail',
    'MicrosoftGraphYammerGroupsActivityGroupCounts',
    'OdataError',
    'OdataErrorDetail',
    'OdataErrorMain',
    'Enum10',
    'Enum11',
    'Enum12',
    'Enum13',
    'Enum14',
    'Enum15',
    'Enum16',
    'Enum20',
    'Enum21',
    'Enum22',
    'Enum23',
    'Enum24',
    'Enum25',
    'Enum26',
    'Enum27',
    'Enum28',
    'Enum7',
    'Enum8',
    'Enum9',
    'Get0ItemsItem',
    'Get1ItemsItem',
    'Get5ItemsItem',
    'Get6ItemsItem',
    'MicrosoftGraphAzureAdLicenseType',
    'MicrosoftGraphFeatureType',
    'MicrosoftGraphMigrationStatus',
    'MicrosoftGraphRegistrationAuthMethod',
    'MicrosoftGraphRegistrationStatusType',
    'MicrosoftGraphUsageAuthMethod',
]