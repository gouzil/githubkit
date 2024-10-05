"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0141 import RepositoryRuleUpdate
from .group_0167 import RepositoryRuleOneof18
from .group_0163 import RepositoryRuleWorkflows
from .group_0144 import RepositoryRuleMergeQueue
from .group_0148 import RepositoryRulePullRequest
from .group_0165 import RepositoryRuleCodeScanning
from .group_0160 import RepositoryRuleTagNamePattern
from .group_0158 import RepositoryRuleBranchNamePattern
from .group_0146 import RepositoryRuleRequiredDeployments
from .group_0150 import RepositoryRuleRequiredStatusChecks
from .group_0152 import RepositoryRuleCommitMessagePattern
from .group_0156 import RepositoryRuleCommitterEmailPattern
from .group_0154 import RepositoryRuleCommitAuthorEmailPattern
from .group_0143 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0140 import (
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems"""

    rule: Missing[
        Union[
            RepositoryRuleCreation,
            RepositoryRuleUpdate,
            RepositoryRuleDeletion,
            RepositoryRuleRequiredLinearHistory,
            RepositoryRuleMergeQueue,
            RepositoryRuleRequiredDeployments,
            RepositoryRuleRequiredSignatures,
            RepositoryRulePullRequest,
            RepositoryRuleRequiredStatusChecks,
            RepositoryRuleNonFastForward,
            RepositoryRuleCommitMessagePattern,
            RepositoryRuleCommitAuthorEmailPattern,
            RepositoryRuleCommitterEmailPattern,
            RepositoryRuleBranchNamePattern,
            RepositoryRuleTagNamePattern,
            RepositoryRuleOneof15,
            RepositoryRuleOneof16,
            RepositoryRuleOneof17,
            RepositoryRuleOneof18,
            RepositoryRuleWorkflows,
            RepositoryRuleCodeScanning,
        ]
    ] = Field(default=UNSET, title="Repository Rule", description="A repository rule.")
    changes: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges
    ] = Field(default=UNSET)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges"""

    configuration: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration
    ] = Field(default=UNSET)
    rule_type: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType
    ] = Field(default=UNSET)
    pattern: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern
    ] = Field(default=UNSET)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pConfiguration
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pRuleType
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pPattern
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern
)

__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern",
)
