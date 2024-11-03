"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0068 import RunnerLabel


class OrgsOrgActionsRunnersRunnerIdLabelsDeleteResponse200(GitHubModel):
    """OrgsOrgActionsRunnersRunnerIdLabelsDeleteResponse200"""

    total_count: int = Field()
    labels: List[RunnerLabel] = Field()


model_rebuild(OrgsOrgActionsRunnersRunnerIdLabelsDeleteResponse200)

__all__ = ("OrgsOrgActionsRunnersRunnerIdLabelsDeleteResponse200",)
