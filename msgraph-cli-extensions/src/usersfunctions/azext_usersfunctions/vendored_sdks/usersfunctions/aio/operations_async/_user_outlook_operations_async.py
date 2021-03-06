# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserOutlookOperations:
    """UserOutlookOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_functions.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def supported_language(
        self,
        user_id: str,
        **kwargs
    ) -> List["models.MicrosoftGraphLocaleInfo"]:
        """Invoke function supportedLanguages.

        Invoke function supportedLanguages.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphLocaleInfo, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphLocaleInfo]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphLocaleInfo"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.supported_language.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphLocaleInfo]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    supported_language.metadata = {'url': '/users/{user-id}/outlook/microsoft.graph.supportedLanguages()'}  # type: ignore

    async def supported_time_zone_ee48(
        self,
        user_id: str,
        **kwargs
    ) -> List["models.MicrosoftGraphTimeZoneInformation"]:
        """Invoke function supportedTimeZones.

        Invoke function supportedTimeZones.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphTimeZoneInformation, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphTimeZoneInformation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphTimeZoneInformation"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.supported_time_zone_ee48.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphTimeZoneInformation]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    supported_time_zone_ee48.metadata = {'url': '/users/{user-id}/outlook/microsoft.graph.supportedTimeZones()'}  # type: ignore

    async def supported_time_zones51_c6(
        self,
        user_id: str,
        time_zone_standard: Union[str, "models.MicrosoftGraphTimeZoneStandard"],
        **kwargs
    ) -> List["models.MicrosoftGraphTimeZoneInformation"]:
        """Invoke function supportedTimeZones.

        Invoke function supportedTimeZones.

        :param user_id: key: id of user.
        :type user_id: str
        :param time_zone_standard:
        :type time_zone_standard: str or ~users_functions.models.MicrosoftGraphTimeZoneStandard
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphTimeZoneInformation, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphTimeZoneInformation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphTimeZoneInformation"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.supported_time_zones51_c6.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'TimeZoneStandard': self._serialize.url("time_zone_standard", time_zone_standard, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphTimeZoneInformation]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    supported_time_zones51_c6.metadata = {'url': '/users/{user-id}/outlook/microsoft.graph.supportedTimeZones(TimeZoneStandard={TimeZoneStandard})'}  # type: ignore
