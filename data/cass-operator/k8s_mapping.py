from known_schemas import K8sField, ResourceRequirementsSchema, PodTemplateSchema, TolerationsSchema
from known_schemas import ServiceAccountNameSchema, ImageSchema
from known_schemas.pod_schemas import NodeSelectorSchema
from known_schemas.resource_schemas import ComputeResourceRequirementsSchema, StorageResourceRequirementsSchema
from known_schemas.storage_schemas import PersistentVolumeClaimSpecSchema

WHITEBOX = [
    K8sField(['spec', 'serverImage'], ImageSchema),
    K8sField(['spec', 'configBuilderResources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'podTemplateSpec'], PodTemplateSchema),
    K8sField(['spec', 'resources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'systemLoggerResources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'configBuilderResources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'storageConfig', 'additionalVolumes', 'ITEM', 'pvcSpec'], PersistentVolumeClaimSpecSchema),
    K8sField(['spec', 'storageConfig', 'cassandraDataVolumeClaimSpec'], PersistentVolumeClaimSpecSchema),
    K8sField(['spec', 'configBuilderImage'], ImageSchema),
    K8sField(['spec', 'serviceAccount'], ServiceAccountNameSchema),
    K8sField(['spec', 'nodeSelector'], NodeSelectorSchema),
    K8sField(['spec', 'systemLoggerImage'], ImageSchema),
    K8sField(['spec', 'tolerations'], TolerationsSchema),
]

BLACKBOX = [
    K8sField(['spec', 'configBuilderResources'], ResourceRequirementsSchema),
    K8sField(['spec', 'podTemplateSpec'], PodTemplateSchema),
    K8sField(['spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'systemLoggerResources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'configBuilderResources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'storageConfig', 'additionalVolumes', 'ITEM', 'pvcSpec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'storageConfig', 'cassandraDataVolumeClaimSpec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'systemLoggerResources'], ResourceRequirementsSchema),
    K8sField(['spec', 'systemLoggerImage'], ImageSchema),
    K8sField(['spec', 'tolerations'], TolerationsSchema),
]