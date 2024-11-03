"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date
from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild


class CopilotUsageMetricsDay(ExtraGitHubModel):
    """Copilot Usage Metrics

    Copilot usage metrics for a given day.
    """

    date: date = Field(
        description="The date for which the usage metrics are aggregated, in `YYYY-MM-DD` format."
    )
    total_active_users: Missing[int] = Field(
        default=UNSET,
        description="The total number of Copilot users with activity belonging to any Copilot feature, globally, for the given day. Includes passive activity such as receiving a code suggestion, as well as engagement activity such as accepting a code suggestion or prompting chat. Does not include authentication events. Is not limited to the individual features detailed on the endpoint.",
    )
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="The total number of Copilot users who engaged with any Copilot feature, for the given day. Examples include but are not limited to accepting a code suggestion, prompting Copilot chat, or triggering a PR Summary. Does not include authentication events. Is not limited to the individual features detailed on the endpoint.",
    )
    copilot_ide_code_completions: Missing[Union[CopilotIdeCodeCompletions, None]] = (
        Field(
            default=UNSET,
            description="Usage metrics for Copilot editor code completions in the IDE.",
        )
    )
    copilot_ide_chat: Missing[Union[CopilotIdeChat, None]] = Field(
        default=UNSET, description="Usage metrics for Copilot Chat in the IDE."
    )
    copilot_dotcom_chat: Missing[Union[CopilotDotcomChat, None]] = Field(
        default=UNSET, description="Usage metrics for Copilot Chat in github.com"
    )
    copilot_dotcom_pull_requests: Missing[Union[CopilotDotcomPullRequests, None]] = (
        Field(default=UNSET, description="Usage metrics for Copilot for pull requests.")
    )


class CopilotDotcomChat(ExtraGitHubModel):
    """CopilotDotcomChat

    Usage metrics for Copilot Chat in github.com
    """

    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="Total number of users who prompted Copilot Chat on github.com at least once.",
    )
    models: Missing[List[CopilotDotcomChatPropModelsItems]] = Field(
        default=UNSET,
        description="List of model metrics for a custom models and the default model.",
    )


class CopilotDotcomChatPropModelsItems(GitHubModel):
    """CopilotDotcomChatPropModelsItems"""

    name: Missing[str] = Field(
        default=UNSET,
        description="Name of the language used for Copilot code completion suggestions, for the given editor.",
    )
    is_custom_model: Missing[bool] = Field(
        default=UNSET, description="Indicates whether a model is custom or default."
    )
    custom_model_training_date: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The training date for the custom model (if applicable).",
    )
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="Total number of users who prompted Copilot Chat on github.com at least once for each model.",
    )
    total_chats: Missing[int] = Field(
        default=UNSET,
        description="Total number of chats initiated by users on github.com.",
    )


class CopilotIdeChat(ExtraGitHubModel):
    """CopilotIdeChat

    Usage metrics for Copilot Chat in the IDE.
    """

    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="Total number of users who prompted Copilot Chat in the IDE.",
    )
    editors: Missing[List[CopilotIdeChatPropEditorsItems]] = Field(default=UNSET)


class CopilotIdeChatPropEditorsItems(GitHubModel):
    """CopilotIdeChatPropEditorsItems

    Copilot Chat metrics, for active editors.
    """

    name: Missing[str] = Field(default=UNSET, description="Name of the given editor.")
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="The number of users who prompted Copilot Chat in the specified editor.",
    )
    models: Missing[List[CopilotIdeChatPropEditorsItemsPropModelsItems]] = Field(
        default=UNSET,
        description="List of model metrics for custom models and the default model.",
    )


class CopilotIdeChatPropEditorsItemsPropModelsItems(GitHubModel):
    """CopilotIdeChatPropEditorsItemsPropModelsItems"""

    name: Missing[str] = Field(
        default=UNSET,
        description="Name of the language used for Copilot code completion suggestions, for the given editor.",
    )
    is_custom_model: Missing[bool] = Field(
        default=UNSET, description="Indicates whether a model is custom or default."
    )
    custom_model_training_date: Missing[Union[str, None]] = Field(
        default=UNSET, description="The training date for the custom model."
    )
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="The number of users who prompted Copilot Chat in the given editor and model.",
    )
    total_chats: Missing[int] = Field(
        default=UNSET,
        description="The total number of chats initiated by users in the given editor and model.",
    )
    total_chat_insertion_events: Missing[int] = Field(
        default=UNSET,
        description="The number of times users accepted a code suggestion from Copilot Chat using the 'Insert Code' UI element, for the given editor.",
    )
    total_chat_copy_events: Missing[int] = Field(
        default=UNSET,
        description="The number of times users copied a code suggestion from Copilot Chat using the keyboard, or the 'Copy' UI element, for the given editor.",
    )


class CopilotDotcomPullRequests(ExtraGitHubModel):
    """CopilotDotcomPullRequests

    Usage metrics for Copilot for pull requests.
    """

    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="The number of users who used Copilot for Pull Requests on github.com to generate a pull request summary at least once.",
    )
    repositories: Missing[List[CopilotDotcomPullRequestsPropRepositoriesItems]] = Field(
        default=UNSET,
        description="Repositories in which users used Copilot for Pull Requests to generate pull request summaries",
    )


class CopilotDotcomPullRequestsPropRepositoriesItems(GitHubModel):
    """CopilotDotcomPullRequestsPropRepositoriesItems"""

    name: Missing[str] = Field(default=UNSET, description="Repository name")
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="The number of users who generated pull request summaries using Copilot for Pull Requests in the given repository.",
    )
    models: Missing[
        List[CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItems]
    ] = Field(
        default=UNSET,
        description="List of model metrics for custom models and the default model.",
    )


class CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItems(GitHubModel):
    """CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItems"""

    name: Missing[str] = Field(
        default=UNSET,
        description="Name of the language used for Copilot code completion suggestions, for the given editor.",
    )
    is_custom_model: Missing[bool] = Field(
        default=UNSET, description="Indicates whether a model is custom or default."
    )
    custom_model_training_date: Missing[Union[str, None]] = Field(
        default=UNSET, description="The training date for the custom model."
    )
    total_pr_summaries_created: Missing[int] = Field(
        default=UNSET,
        description="The number of pull request summaries generated using Copilot for Pull Requests in the given repository.",
    )
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="The number of users who generated pull request summaries using Copilot for Pull Requests in the given repository and model.",
    )


class CopilotIdeCodeCompletions(ExtraGitHubModel):
    """CopilotIdeCodeCompletions

    Usage metrics for Copilot editor code completions in the IDE.
    """

    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="Number of users who accepted at least one Copilot code suggestion, across all active editors. Includes both full and partial acceptances.",
    )
    languages: Missing[List[CopilotIdeCodeCompletionsPropLanguagesItems]] = Field(
        default=UNSET, description="Code completion metrics for active languages."
    )
    editors: Missing[List[CopilotIdeCodeCompletionsPropEditorsItems]] = Field(
        default=UNSET
    )


class CopilotIdeCodeCompletionsPropLanguagesItems(GitHubModel):
    """CopilotIdeCodeCompletionsPropLanguagesItems

    Usage metrics for a given language for the given editor for Copilot code
    completions.
    """

    name: Missing[str] = Field(
        default=UNSET,
        description="Name of the language used for Copilot code completion suggestions.",
    )
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="Number of users who accepted at least one Copilot code completion suggestion for the given language. Includes both full and partial acceptances.",
    )


class CopilotIdeCodeCompletionsPropEditorsItems(ExtraGitHubModel):
    """CopilotIdeCodeCompletionsPropEditorsItems

    Copilot code completion metrics for active editors.
    """

    name: Missing[str] = Field(default=UNSET, description="Name of the given editor.")
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="Number of users who accepted at least one Copilot code completion suggestion for the given editor. Includes both full and partial acceptances.",
    )
    models: Missing[List[CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItems]] = (
        Field(
            default=UNSET,
            description="List of model metrics for custom models and the default model.",
        )
    )


class CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItems(GitHubModel):
    """CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItems"""

    name: Missing[str] = Field(
        default=UNSET,
        description="Name of the language used for Copilot code completion suggestions, for the given editor.",
    )
    is_custom_model: Missing[bool] = Field(
        default=UNSET, description="Indicates whether a model is custom or default."
    )
    custom_model_training_date: Missing[Union[str, None]] = Field(
        default=UNSET, description="The training date for the custom model."
    )
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="Number of users who accepted at least one Copilot code completion suggestion for the given editor, for the given language and model. Includes both full and partial acceptances.",
    )
    languages: Missing[
        List[CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItems]
    ] = Field(
        default=UNSET,
        description="Code completion metrics for active languages, for the given editor.",
    )


class CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItems(
    GitHubModel
):
    """CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItems

    Usage metrics for a given language for the given editor for Copilot code
    completions.
    """

    name: Missing[str] = Field(
        default=UNSET,
        description="Name of the language used for Copilot code completion suggestions, for the given editor.",
    )
    total_engaged_users: Missing[int] = Field(
        default=UNSET,
        description="Number of users who accepted at least one Copilot code completion suggestion for the given editor, for the given language. Includes both full and partial acceptances.",
    )
    total_code_suggestions: Missing[int] = Field(
        default=UNSET,
        description="The number of Copilot code suggestions generated for the given editor, for the given language.",
    )
    total_code_acceptances: Missing[int] = Field(
        default=UNSET,
        description="The number of Copilot code suggestions accepted for the given editor, for the given language. Includes both full and partial acceptances.",
    )
    total_code_lines_suggested: Missing[int] = Field(
        default=UNSET,
        description="The number of lines of code suggested by Copilot code completions for the given editor, for the given language.",
    )
    total_code_lines_accepted: Missing[int] = Field(
        default=UNSET,
        description="The number of lines of code accepted from Copilot code suggestions for the given editor, for the given language.",
    )


model_rebuild(CopilotUsageMetricsDay)
model_rebuild(CopilotDotcomChat)
model_rebuild(CopilotDotcomChatPropModelsItems)
model_rebuild(CopilotIdeChat)
model_rebuild(CopilotIdeChatPropEditorsItems)
model_rebuild(CopilotIdeChatPropEditorsItemsPropModelsItems)
model_rebuild(CopilotDotcomPullRequests)
model_rebuild(CopilotDotcomPullRequestsPropRepositoriesItems)
model_rebuild(CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItems)
model_rebuild(CopilotIdeCodeCompletions)
model_rebuild(CopilotIdeCodeCompletionsPropLanguagesItems)
model_rebuild(CopilotIdeCodeCompletionsPropEditorsItems)
model_rebuild(CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItems)
model_rebuild(
    CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItems
)

__all__ = (
    "CopilotUsageMetricsDay",
    "CopilotDotcomChat",
    "CopilotDotcomChatPropModelsItems",
    "CopilotIdeChat",
    "CopilotIdeChatPropEditorsItems",
    "CopilotIdeChatPropEditorsItemsPropModelsItems",
    "CopilotDotcomPullRequests",
    "CopilotDotcomPullRequestsPropRepositoriesItems",
    "CopilotDotcomPullRequestsPropRepositoriesItemsPropModelsItems",
    "CopilotIdeCodeCompletions",
    "CopilotIdeCodeCompletionsPropLanguagesItems",
    "CopilotIdeCodeCompletionsPropEditorsItems",
    "CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItems",
    "CopilotIdeCodeCompletionsPropEditorsItemsPropModelsItemsPropLanguagesItems",
)
