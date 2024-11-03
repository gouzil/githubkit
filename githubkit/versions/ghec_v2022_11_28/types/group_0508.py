"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0273 import DependabotAlertType
from .group_0420 import EnterpriseWebhooksType
from .group_0421 import SimpleInstallationType
from .group_0423 import RepositoryWebhooksType
from .group_0422 import OrganizationSimpleWebhooksType


class WebhookDependabotAlertAutoReopenedType(TypedDict):
    """Dependabot alert auto-reopened event"""

    action: Literal["auto_reopened"]
    alert: DependabotAlertType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookDependabotAlertAutoReopenedType",)
