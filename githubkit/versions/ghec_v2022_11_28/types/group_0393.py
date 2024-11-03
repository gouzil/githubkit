"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0385 import MetaType
from .group_0391 import UserRoleItemsType
from .group_0390 import UserNameResponseType, UserEmailsResponseItemsType
from .group_0395 import ScimEnterpriseUserResponseAllof1PropGroupsItemsType


class ScimEnterpriseUserResponseType(TypedDict):
    """ScimEnterpriseUserResponse"""

    schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]]
    external_id: NotRequired[Union[str, None]]
    active: bool
    user_name: NotRequired[str]
    name: NotRequired[UserNameResponseType]
    display_name: NotRequired[Union[str, None]]
    emails: List[UserEmailsResponseItemsType]
    roles: NotRequired[List[UserRoleItemsType]]
    id: str
    groups: NotRequired[List[ScimEnterpriseUserResponseAllof1PropGroupsItemsType]]
    meta: MetaType


class ScimEnterpriseUserListType(TypedDict):
    """ScimEnterpriseUserList"""

    schemas: List[Literal["urn:ietf:params:scim:api:messages:2.0:ListResponse"]]
    total_results: int
    resources: List[ScimEnterpriseUserResponseType]
    start_index: int
    items_per_page: int


__all__ = (
    "ScimEnterpriseUserResponseType",
    "ScimEnterpriseUserListType",
)
