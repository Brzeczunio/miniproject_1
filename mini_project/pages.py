from selenium import webdriver
from base import Page
from locators import *

class RedirectPage(Page):
    def go_to_main_page(self):
        self.find_element(RedirectPageLocators.MAINURL).click()

class MainPage(Page):
    def select_purple_quiz(self):
        self.scroll_to_elemet(MainPageLocatars.PURPLEQUIZ).click()

class PurpleQuizStartPage(Page):
    def start_purple_quiz(self):
        self.find_element(PurpleQuizStartPageLocators.STARTQUIZ).click()

class PurpleQuizPage(Page):
    def select_question_1(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_1).click()

    def click_next_button_q1(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q1).click()

    def select_question_2(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_2).click()

    def click_next_button_q2(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q2).click()

    def select_question_3(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_3).click()

    def click_next_button_q3(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q3).click()

    def select_question_4(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_4).click()

    def click_next_button_q4(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q4).click()

    def select_question_1(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_1).click()

    def click_next_button_q1(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q1).click()

    def select_question_2(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_2).click()

    def click_next_button_q2(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q2).click()

    def select_question_3(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_3).click()

    def click_next_button_q3(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q3).click()

    def select_question_4(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_4).click()

    def click_next_button_q4(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q4).click()

    def select_question_5(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_5).click()

    def click_next_button_q5(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q5).click()

    def select_question_6(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_6).click()

    def click_next_button_q6(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q6).click()

    def select_question_7(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_7).click()

    def click_next_button_q7(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q7).click()

    def select_question_8(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_8).click()

    def click_next_button_q8(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q8).click()

    def select_question_9(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_9).click()

    def click_next_button_q9(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q9).click()

    def select_question_10(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_10).click()

    def click_next_button_q10(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q10).click()

    def select_question_11(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_11).click()

    def click_next_button_q11(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q11).click()

    def select_question_12(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_12).click()

    def click_next_button_q12(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q12).click()

    def select_question_13(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_13).click()

    def click_next_button_q13(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q13).click()

    def select_question_14(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_14).click()

    def click_next_button_q14(self):
        self.find_element(PurpleQuizPageLocatars.NEXT_BUTTON_Q14).click()

    def select_question_15(self):
        self.find_element(PurpleQuizPageLocatars.QUESTION_15).click()

    def click_next_button_q15(self):
        self.find_element(PurpleQuizPageLocatars.FINISH_BUTTON_Q15).click()

    def purple_quiz_result(self):
        return self.find_element(PurpleQuizPageLocatars.PURPLE_QUIZ_RESULT).text
