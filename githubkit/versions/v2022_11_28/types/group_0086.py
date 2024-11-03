"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType


class OrganizationInvitationType(TypedDict):
    """Organization Invitation

    Organization Invitation
    """

    id: int
    login: Union[str, None]
    email: Union[str, None]
    role: str
    created_at: str
    failed_at: NotRequired[Union[str, None]]
    failed_reason: NotRequired[Union[str, None]]
    inviter: SimpleUserType
    team_count: int
    node_id: str
    invitation_teams_url: str
    invitation_source: NotRequired[str]


__all__ = ("OrganizationInvitationType",)
