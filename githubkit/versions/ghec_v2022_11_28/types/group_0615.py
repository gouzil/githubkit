"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0415 import EnterpriseWebhooksType
from .group_0416 import SimpleInstallationType
from .group_0418 import RepositoryWebhooksType
from .group_0417 import OrganizationSimpleWebhooksType
from .group_0441 import WebhooksMarketplacePurchaseType


class WebhookMarketplacePurchaseChangedType(TypedDict):
    """marketplace_purchase changed event"""

    action: Literal["changed"]
    effective_date: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    marketplace_purchase: WebhooksMarketplacePurchaseType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    previous_marketplace_purchase: NotRequired[
        WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchaseType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


class WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchaseType(TypedDict):
    """Marketplace Purchase"""

    account: (
        WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccountType
    )
    billing_cycle: str
    free_trial_ends_on: Union[str, None]
    next_billing_date: NotRequired[Union[str, None]]
    on_free_trial: Union[bool, None]
    plan: WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlan"""

    bullets: List[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


__all__ = (
    "WebhookMarketplacePurchaseChangedType",
    "WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchaseType",
    "WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlanType",
)
