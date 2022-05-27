import unittest

import HtmlTestRunner

from Tests.Test_AddRemove import AddRemove
from Tests.Test_BasicAuth import BasicAuth
from Tests.Test_BrokenImg import BrokenImage
from Tests.Test_ContextMenu import ContextMenu


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(AddRemove),
            unittest.defaultTestLoader.loadTestsFromTestCase(BasicAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(BrokenImage),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Results',
            report_name='Test results'
        )

        runner.run(smoke_test)
