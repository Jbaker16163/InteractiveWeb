import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interactiveProject.settings")
import django
django.setup()

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
        fireFoxOptions.headless=False
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('http://127.0.0.1:8000')

    def tearDown(self):
        self.browser.quit()
    
    def testForHomePage(self):

        self.browser.find_element_by_id('login').click()
        time.sleep(2)
        loginBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[1]/div/input')
        loginBox.send_keys('Ghios16153')
        passwordBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[2]/div/input')
        passwordBox.send_keys('Testpassword65!')
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(3)

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
        self.browser.find_element_by_id('login').click()
        time.sleep(2)
        loginBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[1]/div/input')
        loginBox.send_keys('Ghios16153')
        passwordBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[2]/div/input')
        passwordBox.send_keys('Testpassword65!')
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(3)

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
        self.browser.find_element_by_id('login').click()
        loginBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[1]/div/input')
        loginBox.send_keys('Ghios16153')
        passwordBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[2]/div/input')
        passwordBox.send_keys('Testpassword65!')
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(3)

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
        self.browser.find_element_by_id('login').click()
        time.sleep(2)
        loginBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[1]/div/input')
        loginBox.send_keys('Ghios16153')
        passwordBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[2]/div/input')
        passwordBox.send_keys('Testpassword65!')
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(3)

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
            'https://jbaker16163.github.io/StyleForInteractive/style/images/UserClasses/Hunter.png'
        )

        #Checks Undead IMG
        RaceIMG = self.browser.find_element_by_id('RaceIMG')
        self.assertEqual(
            RaceIMG.get_attribute('src'),
            'https://jbaker16163.github.io/StyleForInteractive/style/images/RaceClasses/Undead.jpg'
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
        self.browser.find_element_by_id('login').click()
        time.sleep(2)
        loginBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[1]/div/input')
        loginBox.send_keys('Ghios16153')
        passwordBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[2]/div/input')
        passwordBox.send_keys('Testpassword65!')
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(3)

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
        self.browser.find_element_by_id('login').click()
        time.sleep(2)
        loginBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[1]/div/input')
        loginBox.send_keys('Ghios16153')
        passwordBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[2]/div/input')
        passwordBox.send_keys('Testpassword65!')
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(3)

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
            'https://jbaker16163.github.io/StyleForInteractive/style/images/UserLocations/Town.jpg'
        )

    def testForSixthPage(self):
        self.browser.find_element_by_id('login').click()
        time.sleep(2)
        loginBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[1]/div/input')
        loginBox.send_keys('Ghios16153')
        passwordBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[2]/div/input')
        passwordBox.send_keys('Testpassword65!')
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(3)

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
        time.sleep(1)
        self.browser.find_element_by_id('toSixth').click()

        #Check for Correct Text
        hunterText = self.browser.find_element_by_id('hunterEnd').text
        self.assertIn('You are unable to do much when it comes to a horde of goblins! You were able to pick off a few but they swarm you and take over the town. You die.', hunterText)

class LiveTest(unittest.TestCase):

    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('https://interactivewebapp.azurewebsites.net/')

    def tearDown(self):
        self.browser.quit()

    def LiveTest(self):
        self.browser.find_element_by_id('login').click()
        time.sleep(2)
        loginBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[1]/div/input')
        loginBox.send_keys('Ghios16153')
        passwordBox = self.browser.find_element_by_xpath('/html/body/div/main/div/div/div/form/div[2]/div/input')
        passwordBox.send_keys('Testpassword65!')
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(3)

        #Correct Information
        inputbox = self.browser.find_element_by_id('inputBoxName')
        inputbox.send_keys('ExampleAdventureName')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element_by_id('firstButton').click()
        time.sleep(1)
        self.browser.find_element_by_id('Rogue').click()
        self.browser.find_element_by_id('submitFirst').click()
        self.browser.find_element_by_id('toSecondInteractive').click()
        headerOption2 = self.browser.find_element_by_tag_name('h1').text
        self.browser.find_element_by_id('Undead').click()
        self.browser.find_element_by_id('submitRace').click()
        time.sleep(1)
        self.browser.find_element_by_id('toThirdInteractive').click()
        self.browser.find_element_by_id('continue').click()
        self.browser.find_element_by_id('City').click()
        self.browser.find_element_by_id('submitLocation').click()
        self.browser.find_element_by_id('beg').click()
        time.sleep(1)
        self.browser.find_element_by_id('toSixth').click()
        
        rogueEndText = self.browser.find_element_by_id('BadEndRogue').text
        self.assertIn('You are unable to do much when it comes to winged beasts flying above the city. Your best bet is to flee before they find you. You escape but the city has lost a great number of people.', rogueEndText)

if __name__ == '__main__':
    unittest.main()