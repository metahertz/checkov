import unittest

import hcl2

from checkov.common.models.enums import CheckResult
from checkov.terraform.checks.resource.aws.NeptuneEnforceAuditEnabled import check


class TESTNeptuneEnforceAuditEnabled(unittest.TestCase):

    def test_failure(self):
        hcl_res = hcl2.loads("""
                                resource "aws_neptune_cluster_parameter_group" "example" {
                                  family      = "neptune1"
                                  name        = "example"
                                  description = "neptune cluster parameter group"

                                  parameter {
                                    name = "other_parameter"
                                    value = 0
                                  }
                                }
                """)
        resource_conf = hcl_res['resource'][0]['aws_neptune_cluster_parameter_group']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)


    def test_success(self):
        hcl_res = hcl2.loads("""
                                resource "aws_neptune_cluster_parameter_group" "example" {
                                  family      = "neptune1"
                                  name        = "example"
                                  description = "neptune cluster parameter group"

                                  parameter {
                                    name  = "neptune_enable_audit_log"
                                    value = 1
                                  }
                                }
                """)
        resource_conf = hcl_res['resource'][0]['aws_neptune_cluster_parameter_group']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)

if __name__ == '__main__':
    unittest.main()
