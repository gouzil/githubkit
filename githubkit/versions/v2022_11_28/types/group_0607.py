"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0383 import EnterpriseWebhooksType
from .group_0384 import SimpleInstallationType
from .group_0386 import RepositoryWebhooksType
from .group_0385 import OrganizationSimpleWebhooksType


class WebhookPageBuildType(TypedDict):
    """page_build event"""

    build: WebhookPageBuildPropBuildType
    enterprise: NotRequired[EnterpriseWebhooksType]
    id: int
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookPageBuildPropBuildType(TypedDict):
    """WebhookPageBuildPropBuild

    The [List GitHub Pages builds](https://docs.github.com/rest/pages/pages#list-
    github-pages-builds) itself.
    """

    commit: Union[str, None]
    created_at: str
    duration: int
    error: WebhookPageBuildPropBuildPropErrorType
    pusher: Union[WebhookPageBuildPropBuildPropPusherType, None]
    status: str
    updated_at: str
    url: str


class WebhookPageBuildPropBuildPropErrorType(TypedDict):
    """WebhookPageBuildPropBuildPropError"""

    message: Union[str, None]


class WebhookPageBuildPropBuildPropPusherType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = (
    "WebhookPageBuildType",
    "WebhookPageBuildPropBuildType",
    "WebhookPageBuildPropBuildPropErrorType",
    "WebhookPageBuildPropBuildPropPusherType",
)
