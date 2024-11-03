"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class Topic(GitHubModel):
    """Topic

    A topic aggregates entities that are related to a subject.
    """

    names: List[str] = Field()


model_rebuild(Topic)

__all__ = ("Topic",)
