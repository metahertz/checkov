from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class NeptuneEnforceAuditEnabled(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Neptune's parameter group isn't disableing the audit log"
        id = "CKV_AWS_MATT_TESTING"
        supported_resource = ['aws_neptune_cluster_parameter_group']
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resource)

    def scan_resource_conf(self, conf):
        """
            Looks for description at security group  rules :
            https://www.terraform.io/docs/providers/aws/r/security_group.html
        :param conf: aws_security_group configuration
        :return: <CheckResult>
        """
        if 'parameter' in conf.keys():
            item = next((item for item in conf['parameter'] if item["name"][0] == 'neptune_enable_audit_log'), None)
            if item == None:
                # Item is none, default without neptune_enable_audit_log set is disabled, fail.
                return CheckResult.FAILED
            if item["value"][0] == 1:
                # neptune_enable_audit_log set to enabled. Pass.
                return CheckResult.PASSED
            else:
                # neptune_enable_audit_log exists in parameters but is not 1, fail.
                return CheckResult.FAILED

check = NeptuneEnforceAuditEnabled()
