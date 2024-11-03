"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgPatchBody(GitHubModel):
    """OrgsOrgPatchBody"""

    billing_email: Missing[str] = Field(
        default=UNSET,
        description="Billing email address. This address is not publicized.",
    )
    company: Missing[str] = Field(default=UNSET, description="The company name.")
    email: Missing[str] = Field(
        default=UNSET, description="The publicly visible email address."
    )
    twitter_username: Missing[str] = Field(
        default=UNSET, description="The Twitter username of the company."
    )
    location: Missing[str] = Field(default=UNSET, description="The location.")
    name: Missing[str] = Field(
        default=UNSET, description="The shorthand name of the company."
    )
    description: Missing[str] = Field(
        default=UNSET,
        description="The description of the company. The maximum size is 160 characters.",
    )
    has_organization_projects: Missing[bool] = Field(
        default=UNSET,
        description="Whether an organization can use organization projects.",
    )
    has_repository_projects: Missing[bool] = Field(
        default=UNSET,
        description="Whether repositories that belong to the organization can use repository projects.",
    )
    default_repository_permission: Missing[
        Literal["read", "write", "admin", "none"]
    ] = Field(
        default=UNSET,
        description="Default permission level members have for organization repositories.",
    )
    members_can_create_repositories: Missing[bool] = Field(
        default=UNSET,
        description="Whether of non-admin organization members can create repositories. **Note:** A parameter can override this parameter. See `members_allowed_repository_creation_type` in this table for details.",
    )
    members_can_create_internal_repositories: Missing[bool] = Field(
        default=UNSET,
        description='Whether organization members can create internal repositories, which are visible to all enterprise members. You can only allow members to create internal repositories if your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see "[Restricting repository creation in your organization](https://docs.github.com/enterprise-cloud@latest//github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)" in the GitHub Help documentation.',
    )
    members_can_create_private_repositories: Missing[bool] = Field(
        default=UNSET,
        description='Whether organization members can create private repositories, which are visible to organization members with permission. For more information, see "[Restricting repository creation in your organization](https://docs.github.com/enterprise-cloud@latest//github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)" in the GitHub Help documentation.',
    )
    members_can_create_public_repositories: Missing[bool] = Field(
        default=UNSET,
        description='Whether organization members can create public repositories, which are visible to anyone. For more information, see "[Restricting repository creation in your organization](https://docs.github.com/enterprise-cloud@latest//github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)" in the GitHub Help documentation.',
    )
    members_allowed_repository_creation_type: Missing[
        Literal["all", "private", "none"]
    ] = Field(
        default=UNSET,
        description="Specifies which types of repositories non-admin organization members can create. `private` is only available to repositories that are part of an organization on GitHub Enterprise Cloud. \n**Note:** This parameter is closing down and will be removed in the future. Its return value ignores internal repositories. Using this parameter overrides values set in `members_can_create_repositories`. See the parameter deprecation notice in the operation description for details.",
    )
    members_can_create_pages: Missing[bool] = Field(
        default=UNSET,
        description="Whether organization members can create GitHub Pages sites. Existing published sites will not be impacted.",
    )
    members_can_create_public_pages: Missing[bool] = Field(
        default=UNSET,
        description="Whether organization members can create public GitHub Pages sites. Existing published sites will not be impacted.",
    )
    members_can_create_private_pages: Missing[bool] = Field(
        default=UNSET,
        description="Whether organization members can create private GitHub Pages sites. Existing published sites will not be impacted.",
    )
    members_can_fork_private_repositories: Missing[bool] = Field(
        default=UNSET,
        description="Whether organization members can fork private organization repositories.",
    )
    web_commit_signoff_required: Missing[bool] = Field(
        default=UNSET,
        description="Whether contributors to organization repositories are required to sign off on commits they make through GitHub's web interface.",
    )
    blog: Missing[str] = Field(default=UNSET)
    advanced_security_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='**Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether GitHub Advanced Security is automatically enabled for new repositories and repositories transferred to this organization.\n\nTo use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-cloud@latest//organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."\n\nYou can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.',
    )
    dependabot_alerts_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='**Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether Dependabot alerts are automatically enabled for new repositories and repositories transferred to this organization.\n\nTo use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-cloud@latest//organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."\n\nYou can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.',
    )
    dependabot_security_updates_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='**Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether Dependabot security updates are automatically enabled for new repositories and repositories transferred to this organization.\n\nTo use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-cloud@latest//organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."\n\nYou can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.',
    )
    dependency_graph_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='**Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether dependency graph is automatically enabled for new repositories and repositories transferred to this organization.\n\nTo use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-cloud@latest//organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."\n\nYou can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.',
    )
    secret_scanning_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='**Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether secret scanning is automatically enabled for new repositories and repositories transferred to this organization.\n\nTo use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-cloud@latest//organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."\n\nYou can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.',
    )
    secret_scanning_push_protection_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='**Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether secret scanning push protection is automatically enabled for new repositories and repositories transferred to this organization.\n\nTo use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-cloud@latest//organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."\n\nYou can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.',
    )
    secret_scanning_push_protection_custom_link_enabled: Missing[bool] = Field(
        default=UNSET,
        description="Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection.",
    )
    secret_scanning_push_protection_custom_link: Missing[str] = Field(
        default=UNSET,
        description="If `secret_scanning_push_protection_custom_link_enabled` is true, the URL that will be displayed to contributors who are blocked from pushing a secret.",
    )
    secret_scanning_validity_checks_enabled: Missing[bool] = Field(
        default=UNSET,
        description="**Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether secret scanning automatic validity checks on supported partner tokens is enabled for all repositories under this organization.",
    )


model_rebuild(OrgsOrgPatchBody)

__all__ = ("OrgsOrgPatchBody",)
