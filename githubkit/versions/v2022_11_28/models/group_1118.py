"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class UsersUsernameAttestationsSubjectDigestGetResponse200(GitHubModel):
    """UsersUsernameAttestationsSubjectDigestGetResponse200"""

    attestations: Missing[
        list[UsersUsernameAttestationsSubjectDigestGetResponse200PropAttestationsItems]
    ] = Field(default=UNSET)


class UsersUsernameAttestationsSubjectDigestGetResponse200PropAttestationsItems(
    GitHubModel
):
    """UsersUsernameAttestationsSubjectDigestGetResponse200PropAttestationsItems"""

    bundle: Missing[SigstoreBundle0] = Field(
        default=UNSET, title="Sigstore Bundle v0.1", description="Sigstore Bundle v0.1"
    )
    repository_id: Missing[int] = Field(default=UNSET)


class SigstoreBundle0(GitHubModel):
    """Sigstore Bundle v0.1

    Sigstore Bundle v0.1
    """

    media_type: Missing[str] = Field(default=UNSET, alias="mediaType")
    verification_material: Missing[SigstoreBundle0PropVerificationMaterial] = Field(
        default=UNSET, alias="verificationMaterial"
    )
    dsse_envelope: Missing[SigstoreBundle0PropDsseEnvelope] = Field(
        default=UNSET, alias="dsseEnvelope"
    )


class SigstoreBundle0PropDsseEnvelope(GitHubModel):
    """SigstoreBundle0PropDsseEnvelope"""

    payload: Missing[str] = Field(default=UNSET)
    payload_type: Missing[str] = Field(default=UNSET, alias="payloadType")
    signatures: Missing[list[SigstoreBundle0PropDsseEnvelopePropSignaturesItems]] = (
        Field(default=UNSET)
    )


class SigstoreBundle0PropDsseEnvelopePropSignaturesItems(GitHubModel):
    """SigstoreBundle0PropDsseEnvelopePropSignaturesItems"""

    sig: Missing[str] = Field(default=UNSET)
    keyid: Missing[str] = Field(default=UNSET)


class SigstoreBundle0PropVerificationMaterial(GitHubModel):
    """SigstoreBundle0PropVerificationMaterial"""

    x_509_certificate_chain: Missing[
        SigstoreBundle0PropVerificationMaterialPropX509CertificateChain
    ] = Field(default=UNSET, alias="x509CertificateChain")
    tlog_entries: Missing[
        list[SigstoreBundle0PropVerificationMaterialPropTlogEntriesItems]
    ] = Field(default=UNSET, alias="tlogEntries")
    timestamp_verification_data: Missing[Union[str, None]] = Field(
        default=UNSET, alias="timestampVerificationData"
    )


class SigstoreBundle0PropVerificationMaterialPropX509CertificateChain(GitHubModel):
    """SigstoreBundle0PropVerificationMaterialPropX509CertificateChain"""

    certificates: Missing[
        list[
            SigstoreBundle0PropVerificationMaterialPropX509CertificateChainPropCertificatesItems
        ]
    ] = Field(default=UNSET)


class SigstoreBundle0PropVerificationMaterialPropX509CertificateChainPropCertificatesItems(
    GitHubModel
):
    """SigstoreBundle0PropVerificationMaterialPropX509CertificateChainPropCertificatesI
    tems
    """

    raw_bytes: Missing[str] = Field(default=UNSET, alias="rawBytes")


class SigstoreBundle0PropVerificationMaterialPropTlogEntriesItems(GitHubModel):
    """SigstoreBundle0PropVerificationMaterialPropTlogEntriesItems"""

    log_index: Missing[str] = Field(default=UNSET, alias="logIndex")
    log_id: Missing[
        SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropLogId
    ] = Field(default=UNSET, alias="logId")
    kind_version: Missing[
        SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropKindVersion
    ] = Field(default=UNSET, alias="kindVersion")
    integrated_time: Missing[str] = Field(default=UNSET, alias="integratedTime")
    inclusion_promise: Missing[
        SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropInclusionPromise
    ] = Field(default=UNSET, alias="inclusionPromise")
    inclusion_proof: Missing[Union[str, None]] = Field(
        default=UNSET, alias="inclusionProof"
    )
    canonicalized_body: Missing[str] = Field(default=UNSET, alias="canonicalizedBody")


class SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropLogId(GitHubModel):
    """SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropLogId"""

    key_id: Missing[str] = Field(default=UNSET, alias="keyId")


class SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropKindVersion(
    GitHubModel
):
    """SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropKindVersion"""

    kind: Missing[str] = Field(default=UNSET)
    version: Missing[str] = Field(default=UNSET)


class SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropInclusionPromise(
    GitHubModel
):
    """SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropInclusionPromise"""

    signed_entry_timestamp: Missing[str] = Field(
        default=UNSET, alias="signedEntryTimestamp"
    )


model_rebuild(UsersUsernameAttestationsSubjectDigestGetResponse200)
model_rebuild(UsersUsernameAttestationsSubjectDigestGetResponse200PropAttestationsItems)
model_rebuild(SigstoreBundle0)
model_rebuild(SigstoreBundle0PropDsseEnvelope)
model_rebuild(SigstoreBundle0PropDsseEnvelopePropSignaturesItems)
model_rebuild(SigstoreBundle0PropVerificationMaterial)
model_rebuild(SigstoreBundle0PropVerificationMaterialPropX509CertificateChain)
model_rebuild(
    SigstoreBundle0PropVerificationMaterialPropX509CertificateChainPropCertificatesItems
)
model_rebuild(SigstoreBundle0PropVerificationMaterialPropTlogEntriesItems)
model_rebuild(SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropLogId)
model_rebuild(
    SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropKindVersion
)
model_rebuild(
    SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropInclusionPromise
)

__all__ = (
    "SigstoreBundle0",
    "SigstoreBundle0PropDsseEnvelope",
    "SigstoreBundle0PropDsseEnvelopePropSignaturesItems",
    "SigstoreBundle0PropVerificationMaterial",
    "SigstoreBundle0PropVerificationMaterialPropTlogEntriesItems",
    "SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropInclusionPromise",
    "SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropKindVersion",
    "SigstoreBundle0PropVerificationMaterialPropTlogEntriesItemsPropLogId",
    "SigstoreBundle0PropVerificationMaterialPropX509CertificateChain",
    "SigstoreBundle0PropVerificationMaterialPropX509CertificateChainPropCertificatesItems",
    "UsersUsernameAttestationsSubjectDigestGetResponse200",
    "UsersUsernameAttestationsSubjectDigestGetResponse200PropAttestationsItems",
)
