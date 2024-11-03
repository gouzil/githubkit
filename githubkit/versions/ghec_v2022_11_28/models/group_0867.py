"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesPutBody(GitHubModel):
    """OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesPutBody"""

    selected_repository_ids: List[int] = Field(
        description="List of repository IDs that can access the runner group."
    )


model_rebuild(OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesPutBody)

__all__ = ("OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesPutBody",)
