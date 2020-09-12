from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.enums import CheckCategories


class EBSTest2Encryption(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure this test is new so we can diff [TESTING ONLY - NOT FOR PROD]"
        id = "CKV_AWS_3001"
        supported_resources = ['aws_ebs_volume']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return "encrypted"


check = EBSTest2Encryption()
