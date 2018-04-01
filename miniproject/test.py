#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://kamil-kasprzak.com/istqb-quizzes/')

    def test_Test(self):
        driver = self.driver
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='http://getistqb.com/']"))).click()
        quiz = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='vc_gitem-zone vc_gitem-zone-a uk-card uk-card-default vc_gitem-is-link']/a[@title='Purpurowy']")))
        #quiz.location_once_scrolled_into_view
        ActionChains(driver).move_to_element(quiz).perform()
        driver.execute_script("arguments[0].click()", quiz);
        #quiz.click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='startQuiz']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Testowanie jest używaniem oprogramowania w celu znajdowania defektów']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Analizy i projektowania testów']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[2]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Raportowanie rozbieżności jako incydentów']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[3]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='B, C i D']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[4]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Testowanie pokrycia instrukcji i decyzji']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[5]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Zstępujące testy integracyjne']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[6]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Testy wykonywane przez potencjalnych klientów w ich własnych środowiskach']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[7]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Testowanie atrybutów jakościowych systemu takich jak wydajność i użyteczność']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[8]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Skalowalność']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[9]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Jak wiele kodu zostało pokryte testami']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[10]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Moderator']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[11]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Jest to tani sposób na uzyskanie pewnych korzyści']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[12]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Może być trudno stwierdzić, czy test przeszedł czy nie']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[13]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='0, 1, 99, 100']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[14]/div[5]/div/input[@name='next']"))).click()
        sleep(2)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Wtedy, kiedy skończy się czas przewidziany na testy']"))).click()
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//li[15]/div[5]/div/input[@name='next']"))).click()
        result = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//p[@class='qzk_s_results_answers-result']")))
        self.assertEqual(u'UDZIELONO POPRAWNEJ ODPOWIEDZI NA 15 Z 15 PYTAŃ', result.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
