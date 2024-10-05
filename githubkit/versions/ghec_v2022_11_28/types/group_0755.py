"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0415 import EnterpriseWebhooksType
from .group_0416 import SimpleInstallationType
from .group_0418 import RepositoryWebhooksType
from .group_0417 import OrganizationSimpleWebhooksType


class WebhookRepositoryVulnerabilityAlertResolveType(TypedDict):
    """repository_vulnerability_alert resolve event"""

    action: Literal["resolve"]
    alert: WebhookRepositoryVulnerabilityAlertResolvePropAlertType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookRepositoryVulnerabilityAlertResolvePropAlertType(TypedDict):
    """Repository Vulnerability Alert Alert

    The security alert of the vulnerable dependency.
    """

    affected_package_name: str
    affected_range: str
    created_at: str
    dismiss_reason: NotRequired[str]
    dismissed_at: NotRequired[str]
    dismisser: NotRequired[
        Union[
            WebhookRepositoryVulnerabilityAlertResolvePropAlertPropDismisserType, None
        ]
    ]
    external_identifier: str
    external_reference: Union[str, None]
    fix_reason: NotRequired[str]
    fixed_at: NotRequired[datetime]
    fixed_in: NotRequired[str]
    ghsa_id: str
    id: int
    node_id: str
    number: int
    severity: str
    state: Literal["fixed", "open"]


class WebhookRepositoryVulnerabilityAlertResolvePropAlertPropDismisserType(TypedDict):
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


__all__ = (
    "WebhookRepositoryVulnerabilityAlertResolveType",
    "WebhookRepositoryVulnerabilityAlertResolvePropAlertType",
    "WebhookRepositoryVulnerabilityAlertResolvePropAlertPropDismisserType",
)
