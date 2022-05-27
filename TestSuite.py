import unittest

import HtmlTestRunner

from Tests.Test_AddRemove import AddRemove


class TestSuite(unittest.TestCase):

    def test_suite_add_remove(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(AddRemove)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Add Remove Page Results',
            report_name='Add/Remove tests'
        )

        runner.run(smoke_test)
