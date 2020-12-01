# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class CommunicationCallRecordSessionOperations(object):
    """CommunicationCallRecordSessionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~cloud_communications.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_segment(
        self,
        call_record_id,  # type: str
        session_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum34"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum35"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.CollectionOfSegment"
        """Get segments from communications.

        Get segments from communications.

        :param call_record_id: key: callRecord-id of callRecord.
        :type call_record_id: str
        :param session_id: key: session-id of session.
        :type session_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~cloud_communications.models.Enum34]
        :param select: Select properties to be returned.
        :type select: list[str or ~cloud_communications.models.Enum35]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CollectionOfSegment, or the result of cls(response)
        :rtype: ~cloud_communications.models.CollectionOfSegment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfSegment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.list_segment.metadata['url']  # type: ignore
        path_format_arguments = {
            'callRecord-id': self._serialize.url("call_record_id", call_record_id, 'str'),
            'session-id': self._serialize.url("session_id", session_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if self._config.top is not None:
            query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
        if self._config.skip is not None:
            query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
        if self._config.search is not None:
            query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
        if self._config.filter is not None:
            query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
        if self._config.count is not None:
            query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CollectionOfSegment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_segment.metadata = {'url': '/communications/callRecords/{callRecord-id}/sessions/{session-id}/segments'}  # type: ignore

    def create_segment(
        self,
        call_record_id,  # type: str
        session_id,  # type: str
        id=None,  # type: Optional[str]
        start_date_time=None,  # type: Optional[datetime.datetime]
        end_date_time=None,  # type: Optional[datetime.datetime]
        failure_info=None,  # type: Optional["models.MicrosoftGraphCallRecordsFailureInfo"]
        media=None,  # type: Optional[List["models.MicrosoftGraphCallRecordsMedia"]]
        user_agent_parameter=None,  # type: Optional["models.MicrosoftGraphCallRecordsUserAgent"]
        microsoft_graph_call_records_user_agent=None,  # type: Optional["models.MicrosoftGraphCallRecordsUserAgent"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphCallRecordsSegment"
        """Create new navigation property to segments for communications.

        Create new navigation property to segments for communications.

        :param call_record_id: key: callRecord-id of callRecord.
        :type call_record_id: str
        :param session_id: key: session-id of session.
        :type session_id: str
        :param id: Read-only.
        :type id: str
        :param start_date_time:
        :type start_date_time: ~datetime.datetime
        :param end_date_time:
        :type end_date_time: ~datetime.datetime
        :param failure_info: failureInfo.
        :type failure_info: ~cloud_communications.models.MicrosoftGraphCallRecordsFailureInfo
        :param media:
        :type media: list[~cloud_communications.models.MicrosoftGraphCallRecordsMedia]
        :param user_agent_parameter: userAgent.
        :type user_agent_parameter: ~cloud_communications.models.MicrosoftGraphCallRecordsUserAgent
        :param microsoft_graph_call_records_user_agent: userAgent.
        :type microsoft_graph_call_records_user_agent: ~cloud_communications.models.MicrosoftGraphCallRecordsUserAgent
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphCallRecordsSegment, or the result of cls(response)
        :rtype: ~cloud_communications.models.MicrosoftGraphCallRecordsSegment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphCallRecordsSegment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphCallRecordsSegment(id=id, start_date_time=start_date_time, end_date_time=end_date_time, failure_info=failure_info, media=media, user_agent_callee_user_agent=user_agent_parameter, user_agent_caller_user_agent=microsoft_graph_call_records_user_agent)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_segment.metadata['url']  # type: ignore
        path_format_arguments = {
            'callRecord-id': self._serialize.url("call_record_id", call_record_id, 'str'),
            'session-id': self._serialize.url("session_id", session_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphCallRecordsSegment')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphCallRecordsSegment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_segment.metadata = {'url': '/communications/callRecords/{callRecord-id}/sessions/{session-id}/segments'}  # type: ignore

    def get_segment(
        self,
        call_record_id,  # type: str
        session_id,  # type: str
        segment_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum36"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphCallRecordsSegment"
        """Get segments from communications.

        Get segments from communications.

        :param call_record_id: key: callRecord-id of callRecord.
        :type call_record_id: str
        :param session_id: key: session-id of session.
        :type session_id: str
        :param segment_id: key: segment-id of segment.
        :type segment_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~cloud_communications.models.Enum36]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphCallRecordsSegment, or the result of cls(response)
        :rtype: ~cloud_communications.models.MicrosoftGraphCallRecordsSegment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphCallRecordsSegment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_segment.metadata['url']  # type: ignore
        path_format_arguments = {
            'callRecord-id': self._serialize.url("call_record_id", call_record_id, 'str'),
            'session-id': self._serialize.url("session_id", session_id, 'str'),
            'segment-id': self._serialize.url("segment_id", segment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphCallRecordsSegment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_segment.metadata = {'url': '/communications/callRecords/{callRecord-id}/sessions/{session-id}/segments/{segment-id}'}  # type: ignore

    def update_segment(
        self,
        call_record_id,  # type: str
        session_id,  # type: str
        segment_id,  # type: str
        id=None,  # type: Optional[str]
        start_date_time=None,  # type: Optional[datetime.datetime]
        end_date_time=None,  # type: Optional[datetime.datetime]
        failure_info=None,  # type: Optional["models.MicrosoftGraphCallRecordsFailureInfo"]
        media=None,  # type: Optional[List["models.MicrosoftGraphCallRecordsMedia"]]
        user_agent_parameter=None,  # type: Optional["models.MicrosoftGraphCallRecordsUserAgent"]
        microsoft_graph_call_records_user_agent=None,  # type: Optional["models.MicrosoftGraphCallRecordsUserAgent"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property segments in communications.

        Update the navigation property segments in communications.

        :param call_record_id: key: callRecord-id of callRecord.
        :type call_record_id: str
        :param session_id: key: session-id of session.
        :type session_id: str
        :param segment_id: key: segment-id of segment.
        :type segment_id: str
        :param id: Read-only.
        :type id: str
        :param start_date_time:
        :type start_date_time: ~datetime.datetime
        :param end_date_time:
        :type end_date_time: ~datetime.datetime
        :param failure_info: failureInfo.
        :type failure_info: ~cloud_communications.models.MicrosoftGraphCallRecordsFailureInfo
        :param media:
        :type media: list[~cloud_communications.models.MicrosoftGraphCallRecordsMedia]
        :param user_agent_parameter: userAgent.
        :type user_agent_parameter: ~cloud_communications.models.MicrosoftGraphCallRecordsUserAgent
        :param microsoft_graph_call_records_user_agent: userAgent.
        :type microsoft_graph_call_records_user_agent: ~cloud_communications.models.MicrosoftGraphCallRecordsUserAgent
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphCallRecordsSegment(id=id, start_date_time=start_date_time, end_date_time=end_date_time, failure_info=failure_info, media=media, user_agent_callee_user_agent=user_agent_parameter, user_agent_caller_user_agent=microsoft_graph_call_records_user_agent)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_segment.metadata['url']  # type: ignore
        path_format_arguments = {
            'callRecord-id': self._serialize.url("call_record_id", call_record_id, 'str'),
            'session-id': self._serialize.url("session_id", session_id, 'str'),
            'segment-id': self._serialize.url("segment_id", segment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphCallRecordsSegment')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_segment.metadata = {'url': '/communications/callRecords/{callRecord-id}/sessions/{session-id}/segments/{segment-id}'}  # type: ignore
