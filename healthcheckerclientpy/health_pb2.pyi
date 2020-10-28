# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

class HealthCheckRequest(google___protobuf___message___Message):
    service = ...  # type: typing___Text
    def __init__(
        self,
        service: typing___Optional[typing___Text] = None,
    ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> HealthCheckRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(
            self, field_name: typing_extensions___Literal["service"]
        ) -> None: ...
    else:
        def ClearField(
            self, field_name: typing_extensions___Literal[b"service"]
        ) -> None: ...

class HealthCheckResponse(google___protobuf___message___Message):
    class ServingStatus(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> HealthCheckResponse.ServingStatus: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[HealthCheckResponse.ServingStatus]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[typing___Tuple[str, HealthCheckResponse.ServingStatus]]: ...
    UNKNOWN = typing___cast(ServingStatus, 0)
    SERVING = typing___cast(ServingStatus, 1)
    NOT_SERVING = typing___cast(ServingStatus, 2)

    status = ...  # type: HealthCheckResponse.ServingStatus
    def __init__(
        self,
        status: typing___Optional[HealthCheckResponse.ServingStatus] = None,
    ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> HealthCheckResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(
            self, field_name: typing_extensions___Literal["status"]
        ) -> None: ...
    else:
        def ClearField(
            self, field_name: typing_extensions___Literal[b"status"]
        ) -> None: ...
