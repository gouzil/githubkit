"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0068 import RunnerLabel


class Runner(GitHubModel):
    """Self hosted runners

    A self hosted runner
    """

    id: int = Field(description="The id of the runner.")
    runner_group_id: Missing[int] = Field(
        default=UNSET, description="The id of the runner group."
    )
    name: str = Field(description="The name of the runner.")
    os: str = Field(description="The Operating System of the runner.")
    status: str = Field(description="The status of the runner.")
    busy: bool = Field()
    labels: List[RunnerLabel] = Field()


model_rebuild(Runner)

__all__ = ("Runner",)
