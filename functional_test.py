from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import *
from interactiveApp.views import adventureData
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('http://127.0.0.1:8000')

    def tearDown(self):
        self.browser.quit()
    
    def testForHomePage(self):

        # Tests Interactive Story Title
        self.assertIn('Skelio Adventure', self.browser.title, 'Wrong Title')

        #Test the H1 to make sure it is the home page.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome To Skelio', header_text)

        #Test for CSS Background
        background = self.browser.find_element_by_id("css").value_of_css_property('--dark')
        self.assertIn('#303030', background)

        # Test the input box.
        inputbox = self.browser.find_element_by_id('inputBoxName')
        self.assertEqual(
            inputbox.get_attribute('name'),
            'adventureName'
        )

        # Inputs into the input box an exampleName.
        inputbox.send_keys('ExampleAdventureName')

        # Hits enter to submit data
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    def testForFirstPage(self):
        # Checks option 1
        inputbox = self.browser.find_element_by_id('inputBoxName')
        inputbox.send_keys('ExampleAdventureName')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element_by_id('firstButton').click()
        headerOption1 = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Hello ExampleAdventureName', headerOption1)
        self.browser.find_element_by_id('Hunter').click()
        self.browser.find_element_by_id('submitFirst').click()
        
    
    def testForSecondPage(self):
        # Checks option 2
        inputbox = self.browser.find_element_by_id('inputBoxName')
        inputbox.send_keys('ExampleAdventureName')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element_by_id('firstButton').click()
        time.sleep(1)
        self.browser.find_element_by_id('Hunter').click()
        self.browser.find_element_by_id('submitFirst').click()
        self.browser.find_element_by_id('toSecondInteractive').click()
        headerOption2 = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Hello ExampleAdventureName', headerOption2)
        self.browser.find_element_by_id('Undead').click()
        self.browser.find_element_by_id('submitRace').click()

    def testForThirdPage(self):
        # Sets up third page information correctly
        inputbox = self.browser.find_element_by_id('inputBoxName')
        inputbox.send_keys('ExampleAdventureName')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element_by_id('firstButton').click()
        time.sleep(1)
        self.browser.find_element_by_id('Hunter').click()
        self.browser.find_element_by_id('submitFirst').click()
        self.browser.find_element_by_id('toSecondInteractive').click()
        headerOption2 = self.browser.find_element_by_tag_name('h1').text
        self.browser.find_element_by_id('Undead').click()
        self.browser.find_element_by_id('submitRace').click()
        time.sleep(1)
        self.browser.find_element_by_id('toThirdInteractive').click()

        #Checks all button exists
        RedoBox = self.browser.find_element_by_id('Redo')
        self.assertEqual(
            RedoBox.get_attribute('name'),
            'RedoButton'
        )
        ContinueBox = self.browser.find_element_by_id('cont')
        self.assertEqual(
            ContinueBox.get_attribute('name'),
            'ContinueButton'
        )

        #Check information on this page a short story about your character will be shown including your name, race, and class.
        thirdText = self.browser.find_element_by_id('thirdText').text
        self.assertIn('Hello ExampleAdventureName, your talents as a Hunter have been noted and you have been picked for this job. Good luck Undead', thirdText)

        #Check Hunter IMG
        classIMG = self.browser.find_element_by_id('ClassIMG')
        self.assertEqual(
            classIMG.get_attribute('src'),
            'http://127.0.0.1:8000/static/images/UserClasses/Hunter.png'
        )

        #Checks Undead IMG
        RaceIMG = self.browser.find_element_by_id('RaceIMG')
        self.assertEqual(
            RaceIMG.get_attribute('src'),
            'http://127.0.0.1:8000/static/images/RaceClasses/Undead.jpg'
        )

        #Checks to see if redo button sends you back to home page
        RedoBoxSend = self.browser.find_element_by_id('home')
        RedoBoxSend.click()
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome To Skelio', header_text)

        #Checks to see if continue button works
        self.browser.get('http://127.0.0.1:8000/thirdInteractive/')
        ContinueBoxSend = self.browser.find_element_by_id('continue')
        ContinueBoxSend.click()
        h1Text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Choose where you will start:', h1Text)

    def testForFourthPage(self):
        #Correct Information
        inputbox = self.browser.find_element_by_id('inputBoxName')
        inputbox.send_keys('ExampleAdventureName')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element_by_id('firstButton').click()
        time.sleep(1)
        self.browser.find_element_by_id('Hunter').click()
        self.browser.find_element_by_id('submitFirst').click()
        self.browser.find_element_by_id('toSecondInteractive').click()
        headerOption2 = self.browser.find_element_by_tag_name('h1').text
        self.browser.find_element_by_id('Undead').click()
        self.browser.find_element_by_id('submitRace').click()
        time.sleep(1)
        self.browser.find_element_by_id('toThirdInteractive').click()
        self.browser.find_element_by_id('continue').click()
        #This was also tested in previous page but checks to make sure your on fourth page.
        h1Text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Choose where you will start:', h1Text)

        #Submits Town
        self.browser.find_element_by_id('Town').click()
        self.browser.find_element_by_id('submitLocation').click()

        #Checks for button
        RedoBox = self.browser.find_element_by_id('beg')
        self.assertEqual(
            RedoBox.get_attribute('name'),
            'beginButton'
        )

    def testForFifthPage(self):
        #Correct Information
        inputbox = self.browser.find_element_by_id('inputBoxName')
        inputbox.send_keys('ExampleAdventureName')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element_by_id('firstButton').click()
        time.sleep(1)
        self.browser.find_element_by_id('Hunter').click()
        self.browser.find_element_by_id('submitFirst').click()
        self.browser.find_element_by_id('toSecondInteractive').click()
        headerOption2 = self.browser.find_element_by_tag_name('h1').text
        self.browser.find_element_by_id('Undead').click()
        self.browser.find_element_by_id('submitRace').click()
        time.sleep(1)
        self.browser.find_element_by_id('toThirdInteractive').click()
        self.browser.find_element_by_id('continue').click()

        self.browser.find_element_by_id('Town').click()
        self.browser.find_element_by_id('submitLocation').click()
        self.browser.find_element_by_id('beg').click()

        #Check for Text In Town
        startLocationText = self.browser.find_element_by_id('startLocation').text
        self.assertIn('Your starting area is Town', startLocationText)

        #Check Hunter IMG
        userLocationIMG = self.browser.find_element_by_id('userLocationIMG')
        self.assertEqual(
            userLocationIMG.get_attribute('src'),
            'http://127.0.0.1:8000/static/images/UserLocations/Town.jpg'
        )
        




        

if __name__ == '__main__':
    unittest.main()