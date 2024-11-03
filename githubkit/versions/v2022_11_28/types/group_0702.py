"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0383 import EnterpriseWebhooksType
from .group_0384 import SimpleInstallationType
from .group_0386 import RepositoryWebhooksType
from .group_0385 import OrganizationSimpleWebhooksType


class WebhookRepositoryRenamedType(TypedDict):
    """repository renamed event"""

    action: Literal["renamed"]
    changes: WebhookRepositoryRenamedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookRepositoryRenamedPropChangesType(TypedDict):
    """WebhookRepositoryRenamedPropChanges"""

    repository: WebhookRepositoryRenamedPropChangesPropRepositoryType


class WebhookRepositoryRenamedPropChangesPropRepositoryType(TypedDict):
    """WebhookRepositoryRenamedPropChangesPropRepository"""

    name: WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType


class WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType(TypedDict):
    """WebhookRepositoryRenamedPropChangesPropRepositoryPropName"""

    from_: str


__all__ = (
    "WebhookRepositoryRenamedType",
    "WebhookRepositoryRenamedPropChangesType",
    "WebhookRepositoryRenamedPropChangesPropRepositoryType",
    "WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType",
)
