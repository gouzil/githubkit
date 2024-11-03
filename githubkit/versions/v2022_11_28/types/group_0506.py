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
from .group_0383 import EnterpriseWebhooksType
from .group_0386 import RepositoryWebhooksType
from .group_0399 import WebhooksRepositoriesItemsType
from .group_0385 import OrganizationSimpleWebhooksType


class WebhookInstallationNewPermissionsAcceptedType(TypedDict):
    """installation new_permissions_accepted event"""

    action: Literal["new_permissions_accepted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories: NotRequired[List[WebhooksRepositoriesItemsType]]
    repository: NotRequired[RepositoryWebhooksType]
    requester: NotRequired[None]
    sender: SimpleUserType


__all__ = ("WebhookInstallationNewPermissionsAcceptedType",)
