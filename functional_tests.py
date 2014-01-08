from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# bob checks out homepage
		self.browser.get('http://localhost:8000')

		# bob notices page title and header says "todo"
		self.assertIn('todo', self.browser.title)
		self.fail('finish the test')

		# bob is invited to enter a todo item.

		# bob types "buy tomatoes" into a text box.

		# when bob hits enter, the page updates, and now the page lists:
		# "1: buy tomatoes" as an item in the todo list.

		# there is still a text box inviting him to add another item.
		# he enters "call mom".

		# the page updates again, and now shows both items in his list.

		# bob wonders whether the site will remember his list. he sees that
		# the site has generated a unique url for him. there is also some
		# explanatory text.

		# bob visits the url and the todo list is there.

if __name__ == '__main__':
	unittest.main(warnings='ignore')
