# coding=utf8
""" Batch

The primary code for looping through a list, applying each element to a prompt \
template, and running that prompt
"""

__author__		= "Chris Nasr"
__copyright__	= "Ouroboros Coding Inc."
__version__		= "1.0.0"
__email__		= "chris@ouroboroscoding.com"
__created__		= "2023-12-29"

# Ouroboros modules
import undefined
from strings import strtr

# Python modules
from typing import List
from os import environ

# Pip modules
from openai import OpenAI

def batch(
	template: str,
	data: List[dict],
	delimiter: str = '%',
	temperature: float = 0.5,
	api_key: str = undefined
) -> List[str]:
	"""Batch

	Takes a list of variable data and uses it to fill the same template, using \
	each result as a prompt to get a response

	Arguments:
		template (str): The template which will be filled in for each element
		data (dict[]): A list of dictionaries of which each key will be \
			treated as a variable in the template
		delimiter (str): A character, or characters, that will differentiate \
			a template variable from the rest of the template. Defaults to '%' \
			as in %my_template_variable%
		temperature (float): The temperature to pass along to openai. Must be \
			between 0.0 and 1.0. Higher values result in more creative responses
		api_key (str): The API key used with openai, if not passed, expects \
			to find the key in a .env file as OPEN_AI_KEY

	Returns:
		The list of responses in the same order as the data passed
	"""

	# Init the response list
	lResponses = []

	# If the api key wasn't passed
	if api_key is undefined:

		# Try to load it from the env
		api_key = environ.get('OPEN_AI_KEY')

		# If it still doesn't exist, raise an error
		raise RuntimeError('api_key was not passed and can not be found in .env')

	# Create client
	oAI = OpenAI(api_key = api_key)

	# Loop through each element of the data
	for d in data:

		# Copy the template
		sPrompt = template

		# Create the template keys from each key in the data dict
		dTranslate = { '%s%s%s' % (
			delimiter, k, delimiter
		): d[k] for k in d }

		# Replace the variables in the template
		sPrompt = strtr(template, dTranslate)

		# Run the prompt
		oResponse = oAI.chat.completions.create(
			model = 'gpt-3.5-turbo',
			messages = [
				{'role': 'system', 'content': 'You are a helpful assistant.'},
				{'role': 'user', 'content': sPrompt}
			],
			temperature = temperature
		)

		# Append the response message to the list
		lResponses.append(oResponse.choices[0].message.content)

	# Return the responses
	return lResponses