"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgCodeSecurityConfigurationsPostBodyType(TypedDict):
    """OrgsOrgCodeSecurityConfigurationsPostBody"""

    name: str
    description: str
    advanced_security: NotRequired[Literal["enabled", "disabled"]]
    dependency_graph: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependency_graph_autosubmit_action: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    dependency_graph_autosubmit_action_options: NotRequired[
        OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptionsType
    ]
    dependabot_alerts: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependabot_security_updates: NotRequired[Literal["enabled", "disabled", "not_set"]]
    code_scanning_default_setup: NotRequired[Literal["enabled", "disabled", "not_set"]]
    secret_scanning: NotRequired[Literal["enabled", "disabled", "not_set"]]
    secret_scanning_push_protection: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_delegated_bypass: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_delegated_bypass_options: NotRequired[
        OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsType
    ]
    secret_scanning_validity_checks: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_non_provider_patterns: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    private_vulnerability_reporting: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    enforcement: NotRequired[Literal["enforced", "unenforced"]]


class OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptionsType(
    TypedDict
):
    """OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOpti
    ons

    Feature options for Automatic dependency submission
    """

    labeled_runners: NotRequired[bool]


class OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsType(
    TypedDict
):
    """OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOption
    s

    Feature options for secret scanning delegated bypass
    """

    reviewers: NotRequired[
        List[
            OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItemsType
        ]
    ]


class OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItemsType(
    TypedDict
):
    """OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOption
    sPropReviewersItems
    """

    reviewer_id: int
    reviewer_type: Literal["TEAM", "ROLE"]


__all__ = (
    "OrgsOrgCodeSecurityConfigurationsPostBodyType",
    "OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptionsType",
    "OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsType",
    "OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItemsType",
)
