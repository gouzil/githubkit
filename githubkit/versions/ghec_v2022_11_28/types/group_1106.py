"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_1105 import ReposOwnerRepoPagesPostBodyPropSourceType


class ReposOwnerRepoPagesPostBodyAnyof0Type(TypedDict):
    """ReposOwnerRepoPagesPostBodyAnyof0"""

    build_type: NotRequired[Literal["legacy", "workflow"]]
    source: ReposOwnerRepoPagesPostBodyPropSourceType


__all__ = ("ReposOwnerRepoPagesPostBodyAnyof0Type",)
