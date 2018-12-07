import HTMLTestRunner
import unittest
import sys
import os

if __name__ == '__main__':
    # suite = unittest.defaultTestLoader.discover(start_dir=os.path.dirname(sys.argv[0]) + os.sep + "test_cases",
    #                                             pattern="test_*.py")
    # HTMLTestRunner.HTMLTestRunner(
    #     stream=open(os.path.dirname(sys.argv[0]) + os.sep + "reports" + os.sep + "report.html", "wb"),
    #     title="接口测试报告demo",
    #     description="接口测试",
    #     tester="fqivy").run(suite)

    suite = unittest.defaultTestLoader.discover(start_dir=os.path.dirname(sys.argv[0]) + os.sep + "test_client_cases",
                                                pattern="test_*.py")

    HTMLTestRunner.HTMLTestRunner(
        stream=open(os.path.dirname(sys.argv[0]) + os.sep + "reports" + os.sep + "client_report.html", "wb"),
        title="接口测试报告demo",
        description="接口测试",
        tester="fqivy").run(suite)
