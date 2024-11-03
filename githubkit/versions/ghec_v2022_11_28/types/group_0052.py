"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date
from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class CopilotUsageMetricsDayType(TypedDict):
    """Copilot Usage Metrics

    Copilot usage metrics for a given day.
    """

    date: date
    total_active_users: NotRequired[int]
    total_engaged_users: NotRequired[int]
    copilot_ide_code_completions: NotRequired[
        Union[CopilotIdeCodeCompletionsType, None]
    ]
    copilot_ide_chat: NotRequired[Union[CopilotIdeChatType, None]]
    copilot_dotcom_chat: NotRequired[Union[CopilotDotcomChatType, None]]
    copilot_dotcom_pull_requests: NotRequired[
        Union[CopilotDotcomPullRequestsType, None]
    ]


class CopilotDotcomChatType(TypedDict):
    """CopilotDotcomChat

    Usage metrics for Copilot Chat in github.com
    """

    total_engaged_users: NotRequired[int]
    models: NotRequired[List[CopilotDotcomChatPropModelsItemsType]]


class CopilotDotcomChatPropModelsItemsType(TypedDict):
    """CopilotDotcomChatPropModelsItems"""

    name: NotRequired[str]
    is_custom_model: NotRequired[bool]
    custom_model_training_date: NotRequired[Union[str, None]]
    total_engaged_users: NotRequired[int]
    total_chats: NotRequired[int]


class CopilotIdeChatType(TypedDict):
    """CopilotIdeChat

    Usage metrics for Copilot Chat in the IDE.
    """

    total_engaged_users: NotRequired[int]
    editors: NotRequired[List[CopilotIdeChatPropEditorsItemsType]]


class CopilotIdeChatPropEditorsItemsType(TypedDict):
    """CopilotIdeChatPropEditorsItems

    Copilot Chat metrics, for active editors.
    """

    name: NotRequired[str]
    total_engaged_users: NotRequired[int]
    models: NotRequired[List[CopilotIdeChatPropEditorsItemsPropModelsItemsType]]


class CopilotIdeChatPropEditorsItemsPropModelsItemsType(TypedDict):
    """CopilotIdeChatPropEditorsItemsPropModelsItems"""

    name: NotRequired[str]
    is_custom_model: NotRequired[bool]
    custom_model_training_date: NotRequired[Union[str, None]]
    total_engaged_users: NotRequired[int]
    total_chats: NotRequired[int]
    total_chat_insertion_events: NotRequired[int]
    total_chat_copy_events: NotRequired[int]


class CopilotDotcomPullRequestsType(TypedDict):
    """CopilotDotcomPullRequests

    Usage metrics for Copilot for pull requests.
    """

    total_engaged_users: NotRequired[int]
    repositories: NotRequired[List[CopilotDotcomPullRequestsPropRepositoriesItemsType]]


class CopilotDotcomPullRequestsPropRepositoriesItemsType(TypedDict):
    """CopilotDotcomPullRequestsPropRepositoriesItems"""

    name: NotRequired[str]
    total_engaged_users: NotRequired[int]
    models: NotRequired[
        List[CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItemsType]
    ]


class CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItemsType(TypedDict):
    """CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItems"""

    name: NotRequired[str]
    is_custom_model: NotRequired[bool]
    custom_model_training_date: NotRequired[Union[str, None]]
    total_pr_summaries_created: NotRequired[int]
    total_engaged_users: NotRequired[int]


class CopilotIdeCodeCompletionsType(TypedDict):
    """CopilotIdeCodeCompletions

    Usage metrics for Copilot editor code completions in the IDE.
    """

    total_engaged_users: NotRequired[int]
    languages: NotRequired[List[CopilotIdeCodeCompletionsPropLanguagesItemsType]]
    editors: NotRequired[List[CopilotIdeCodeCompletionsPropEditorsItemsType]]


class CopilotIdeCodeCompletionsPropLanguagesItemsType(TypedDict):
    """CopilotIdeCodeCompletionsPropLanguagesItems

    Usage metrics for a given language for the given editor for Copilot code
    completions.
    """

    name: NotRequired[str]
    total_engaged_users: NotRequired[int]


class CopilotIdeCodeCompletionsPropEditorsItemsType(TypedDict):
    """CopilotIdeCodeCompletionsPropEditorsItems

    Copilot code completion metrics for active editors.
    """

    name: NotRequired[str]
    total_engaged_users: NotRequired[int]
    models: NotRequired[
        List[CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsType]
    ]


class CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsType(TypedDict):
    """CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItems"""

    name: NotRequired[str]
    is_custom_model: NotRequired[bool]
    custom_model_training_date: NotRequired[Union[str, None]]
    total_engaged_users: NotRequired[int]
    languages: NotRequired[
        List[
            CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItemsType
        ]
    ]


class CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItemsType(
    TypedDict
):
    """CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItems

    Usage metrics for a given language for the given editor for Copilot code
    completions.
    """

    name: NotRequired[str]
    total_engaged_users: NotRequired[int]
    total_code_suggestions: NotRequired[int]
    total_code_acceptances: NotRequired[int]
    total_code_lines_suggested: NotRequired[int]
    total_code_lines_accepted: NotRequired[int]


__all__ = (
    "CopilotUsageMetricsDayType",
    "CopilotDotcomChatType",
    "CopilotDotcomChatPropModelsItemsType",
    "CopilotIdeChatType",
    "CopilotIdeChatPropEditorsItemsType",
    "CopilotIdeChatPropEditorsItemsPropModelsItemsType",
    "CopilotDotcomPullRequestsType",
    "CopilotDotcomPullRequestsPropRepositoriesItemsType",
    "CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItemsType",
    "CopilotIdeCodeCompletionsType",
    "CopilotIdeCodeCompletionsPropLanguagesItemsType",
    "CopilotIdeCodeCompletionsPropEditorsItemsType",
    "CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsType",
    "CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItemsType",
)
