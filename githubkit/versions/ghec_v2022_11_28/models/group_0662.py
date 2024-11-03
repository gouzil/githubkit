"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0420 import EnterpriseWebhooks
from .group_0421 import SimpleInstallation
from .group_0423 import RepositoryWebhooks
from .group_0453 import WebhooksProjectCard
from .group_0422 import OrganizationSimpleWebhooks


class WebhookProjectCardEdited(GitHubModel):
    """project_card edited event"""

    action: Literal["edited"] = Field()
    changes: WebhookProjectCardEditedPropChanges = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    project_card: WebhooksProjectCard = Field(title="Project Card")
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookProjectCardEditedPropChanges(GitHubModel):
    """WebhookProjectCardEditedPropChanges"""

    note: WebhookProjectCardEditedPropChangesPropNote = Field()


class WebhookProjectCardEditedPropChangesPropNote(GitHubModel):
    """WebhookProjectCardEditedPropChangesPropNote"""

    from_: Union[str, None] = Field(alias="from")


model_rebuild(WebhookProjectCardEdited)
model_rebuild(WebhookProjectCardEditedPropChanges)
model_rebuild(WebhookProjectCardEditedPropChangesPropNote)

__all__ = (
    "WebhookProjectCardEdited",
    "WebhookProjectCardEditedPropChanges",
    "WebhookProjectCardEditedPropChangesPropNote",
)
