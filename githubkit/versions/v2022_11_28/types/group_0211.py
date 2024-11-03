"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0074 import CodeScanningAnalysisToolType
from .group_0075 import CodeScanningAlertInstanceType


class CodeScanningAlertType(TypedDict):
    """CodeScanningAlert"""

    number: int
    created_at: datetime
    updated_at: NotRequired[datetime]
    url: str
    html_url: str
    instances_url: str
    state: Union[None, Literal["open", "dismissed", "fixed"]]
    fixed_at: NotRequired[Union[datetime, None]]
    dismissed_by: Union[None, SimpleUserType]
    dismissed_at: Union[datetime, None]
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ]
    dismissed_comment: NotRequired[Union[str, None]]
    rule: CodeScanningAlertRuleType
    tool: CodeScanningAnalysisToolType
    most_recent_instance: CodeScanningAlertInstanceType


class CodeScanningAlertRuleType(TypedDict):
    """CodeScanningAlertRule"""

    id: NotRequired[Union[str, None]]
    name: NotRequired[str]
    severity: NotRequired[Union[None, Literal["none", "note", "warning", "error"]]]
    security_severity_level: NotRequired[
        Union[None, Literal["low", "medium", "high", "critical"]]
    ]
    description: NotRequired[str]
    full_description: NotRequired[str]
    tags: NotRequired[Union[List[str], None]]
    help_: NotRequired[Union[str, None]]
    help_uri: NotRequired[Union[str, None]]


__all__ = (
    "CodeScanningAlertType",
    "CodeScanningAlertRuleType",
)
