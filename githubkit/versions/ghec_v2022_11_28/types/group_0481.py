"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0426 import ExemptionRequestType
from .group_0425 import ExemptionResponseType
from .group_0420 import EnterpriseWebhooksType
from .group_0421 import SimpleInstallationType
from .group_0423 import RepositoryWebhooksType
from .group_0422 import OrganizationSimpleWebhooksType


class WebhookExemptionRequestResponseDismissedType(TypedDict):
    """Exemption response dismissed event"""

    action: Literal["response_dismissed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    exemption_request: ExemptionRequestType
    exemption_response: ExemptionResponseType
    sender: SimpleUserType


__all__ = ("WebhookExemptionRequestResponseDismissedType",)
