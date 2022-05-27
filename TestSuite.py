import unittest

import HtmlTestRunner

from Tests.Test_AddRemove import AddRemove
from Tests.Test_BasicAuth import BasicAuth
from Tests.Test_BrokenImg import BrokenImage


class TestSuite(unittest.TestCase):

    def test_suite_add_remove(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(AddRemove),
            unittest.defaultTestLoader.loadTestsFromTestCase(BasicAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(BrokenImage)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Results',
            report_name='Test results'
        )

        runner.run(smoke_test)
