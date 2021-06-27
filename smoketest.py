#Here we run ours TestSuite
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from ordersAssertions import OrderAssertions
from menuAssertions import MenuAssertions
from newPlateAssertions import NewPlateAssertions

ordersAssertions_test = TestLoader().loadTestsFromTestCase(OrderAssertions)
menuAssertions_test = TestLoader().loadTestsFromTestCase(MenuAssertions)
newPlateAssertions_test = TestLoader().loadTestsFromTestCase(NewPlateAssertions)

smoke_test = TestSuite([ordersAssertions_test, menuAssertions_test, newPlateAssertions_test])

kwargs = {
    "output": "reports",
    "report_name": "final-report",
    "combine_reports": True,
    "add_timestamp": False
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)