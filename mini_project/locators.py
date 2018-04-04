# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class RedirectPageLocators(object):
    MAINURL             = (By.XPATH, "//a[@href='http://getistqb.com/']")

class MainPageLocatars(object):
    PURPLEQUIZ          = (By.XPATH,"//div[@class='vc_grid-item vc_clearfix app-grid-homepage-posts vc_col-sm-4 vc_visible-item fadeIn animated']")

class PurpleQuizStartPageLocators(object):
    STARTQUIZ           = (By.XPATH,"//input[@name='startQuiz']")

class PurpleQuizPageLocatars(object):
    QUESTION_1          = (By.XPATH,"//span[text()='Testowanie jest używaniem oprogramowania w celu znajdowania defektów']")
    NEXT_BUTTON_Q1      = (By.XPATH,"//input[@name='next']")
    QUESTION_2          = (By.XPATH,"//span[text()='Analizy i projektowania testów']")
    NEXT_BUTTON_Q2      = (By.XPATH,"//li[2]/div[5]/div/input[@name='next']")
    QUESTION_3          = (By.XPATH,"//span[text()='Raportowanie rozbieżności jako incydentów']")
    NEXT_BUTTON_Q3      = (By.XPATH,"//li[3]/div[5]/div/input[@name='next']")
    QUESTION_4          = (By.XPATH,"//span[text()='B, C i D']")
    NEXT_BUTTON_Q4      = (By.XPATH,"//li[4]/div[5]/div/input[@name='next']")
    QUESTION_5          = (By.XPATH,"//span[text()='Testowanie pokrycia instrukcji i decyzji']")
    NEXT_BUTTON_Q5      = (By.XPATH,"//li[5]/div[5]/div/input[@name='next']")
    QUESTION_6          = (By.XPATH,"//span[text()='Zstępujące testy integracyjne']")
    NEXT_BUTTON_Q6      = (By.XPATH,"//li[6]/div[5]/div/input[@name='next']")
    QUESTION_7          = (By.XPATH,"//span[text()='Testy wykonywane przez potencjalnych klientów w ich własnych środowiskach']")
    NEXT_BUTTON_Q7      = (By.XPATH,"//li[7]/div[5]/div/input[@name='next']")
    QUESTION_8          = (By.XPATH,"//span[text()='Testowanie atrybutów jakościowych systemu takich jak wydajność i użyteczność']")
    NEXT_BUTTON_Q8      = (By.XPATH,"//li[8]/div[5]/div/input[@name='next']")
    QUESTION_9          = (By.XPATH,"//span[text()='Skalowalność']")
    NEXT_BUTTON_Q9      = (By.XPATH,"//li[9]/div[5]/div/input[@name='next']")
    QUESTION_10         = (By.XPATH,"//span[text()='Jak wiele kodu zostało pokryte testami']")
    NEXT_BUTTON_Q10     = (By.XPATH,"//li[10]/div[5]/div/input[@name='next']")
    QUESTION_11         = (By.XPATH,"//span[text()='Moderator']")
    NEXT_BUTTON_Q11     = (By.XPATH,"//li[11]/div[5]/div/input[@name='next']")
    QUESTION_12         = (By.XPATH,"//span[text()='Jest to tani sposób na uzyskanie pewnych korzyści']")
    NEXT_BUTTON_Q12     = (By.XPATH,"//li[12]/div[5]/div/input[@name='next']")
    QUESTION_13         = (By.XPATH,"//span[text()='Może być trudno stwierdzić, czy test przeszedł czy nie']")
    NEXT_BUTTON_Q13     = (By.XPATH,"//li[13]/div[5]/div/input[@name='next']")
    QUESTION_14         = (By.XPATH,"//span[text()='0, 1, 99, 100']")
    NEXT_BUTTON_Q14     = (By.XPATH,"//li[14]/div[5]/div/input[@name='next']")
    QUESTION_15         = (By.XPATH,"//span[text()='Wtedy, kiedy skończy się czas przewidziany na testy']")
    FINISH_BUTTON_Q15   = (By.XPATH,"//li[15]/div[5]/div/input[@name='next']")
    PURPLE_QUIZ_RESULT  = (By.XPATH,"//p[@class='qzk_s_results_answers-result']")
