"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0385 import WebhooksDeployKeyType
from .group_0378 import EnterpriseWebhooksType
from .group_0379 import SimpleInstallationType
from .group_0381 import RepositoryWebhooksType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookDeployKeyCreatedType(TypedDict):
    """deploy_key created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    key: WebhooksDeployKeyType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookDeployKeyCreatedType",)
