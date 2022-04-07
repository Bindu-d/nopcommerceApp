import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"

    log = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.log.info("******** Test_002_DDT_Login  *********")
        self.log.info("*********  Verifying Login Test  ***********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel: ", self.rows)
        lst_status = []     # Empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.log.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.expected == "Fail":
                    self.log.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.log.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.expected == "Fail":
                    self.log.info("*** Passed ***")
                    lst_status.append("Pass")
            print(lst_status)

        if "Fail" not in lst_status:
            self.log.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.log.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.log.info("******* End of Login DDT Test **********")
        self.log.info("**************** Completed  TC_LoginDDT_002 ************* ");




