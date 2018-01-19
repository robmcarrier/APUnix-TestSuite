import unittest
import OldControl
import BSTestRunner

smoke_test = unittest.TestSuite([ unittest.defaultTestLoader.loadTestsFromTestCase(OldControl.logInScreen) , unittest.defaultTestLoader.loadTestsFromTestCase(OldControl.reportsScreen)])



fp = open("SummitQAresults.html", "wb")

runner = BSTestRunner.BSTestRunner(
            stream=fp,
            title='Summit Control Test',
            description='Demo of Automated Summit Control Regression Testing'
            )

runner.run(smoke_test)
