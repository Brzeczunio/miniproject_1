#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from pages import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://kamil-kasprzak.com/istqb-quizzes/')

    def test_Purple_Quiz(self):
        redirectPage = RedirectPage(self.driver)
        redirectPage.go_to_main_page()
        mainPage = MainPage(self.driver)
        mainPage.select_purple_quiz()
        purpleQuizStartPage = PurpleQuizStartPage(self.driver)
        purpleQuizStartPage.start_purple_quiz()
        purpleQuizPage = PurpleQuizPage(self.driver)
        purpleQuizPage.select_question_1()
        purpleQuizPage.click_next_button_q1()
        purpleQuizPage.select_question_2()
        purpleQuizPage.click_next_button_q2()
        purpleQuizPage.select_question_3()
        purpleQuizPage.click_next_button_q3()
        purpleQuizPage.select_question_4()
        purpleQuizPage.click_next_button_q4()
        purpleQuizPage.select_question_5()
        purpleQuizPage.click_next_button_q5()
        purpleQuizPage.select_question_6()
        purpleQuizPage.click_next_button_q6()
        purpleQuizPage.select_question_7()
        purpleQuizPage.click_next_button_q7()
        purpleQuizPage.select_question_8()
        purpleQuizPage.click_next_button_q8()
        purpleQuizPage.select_question_9()
        purpleQuizPage.click_next_button_q9()
        purpleQuizPage.select_question_10()
        purpleQuizPage.click_next_button_q10()
        purpleQuizPage.select_question_11()
        purpleQuizPage.click_next_button_q11()
        purpleQuizPage.select_question_12()
        purpleQuizPage.click_next_button_q12()
        purpleQuizPage.select_question_13()
        purpleQuizPage.click_next_button_q13()
        purpleQuizPage.select_question_14()
        purpleQuizPage.click_next_button_q14()
        purpleQuizPage.select_question_15()
        purpleQuizPage.click_next_button_q15()
        self.assertEqual(u'UDZIELONO POPRAWNEJ ODPOWIEDZI NA 15 Z 15 PYTAŃ', purpleQuizPage.purple_quiz_result())        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
