"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0168 import RepositoryRulesetType
from .group_0415 import EnterpriseWebhooksType
from .group_0416 import SimpleInstallationType
from .group_0418 import RepositoryWebhooksType
from .group_0417 import OrganizationSimpleWebhooksType
from .group_0745 import WebhookRepositoryRulesetEditedPropChangesType


class WebhookRepositoryRulesetEditedType(TypedDict):
    """repository ruleset edited event"""

    action: Literal["edited"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    repository_ruleset: RepositoryRulesetType
    changes: NotRequired[WebhookRepositoryRulesetEditedPropChangesType]
    sender: SimpleUserType


__all__ = ("WebhookRepositoryRulesetEditedType",)
