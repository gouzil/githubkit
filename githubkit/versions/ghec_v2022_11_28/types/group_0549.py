"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0017 import InstallationType
from .group_0420 import EnterpriseWebhooksType
from .group_0423 import RepositoryWebhooksType
from .group_0438 import WebhooksRepositoriesItemsType
from .group_0422 import OrganizationSimpleWebhooksType


class WebhookInstallationDeletedType(TypedDict):
    """installation deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories: NotRequired[List[WebhooksRepositoriesItemsType]]
    repository: NotRequired[RepositoryWebhooksType]
    requester: NotRequired[None]
    sender: SimpleUserType


__all__ = ("WebhookInstallationDeletedType",)
