'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def get_shakespearify(self, article):
        '''Generate a Shakespearified version of the given text'''
        prompt = "Rewrite the following article into iambic pentameter and early Modern English:" + article
        response = self.getResponse(prompt)
        return response

    def get_summarization(self, article):
        ''' Generate a summary of the given article '''
        prompt = "Summarize the following article with fewer words:" + article
        response = self.getResponse(prompt)
        return response


    def getSimplification(self, article):
        ''' Generate a simplified version of a text with grade school level vocabulary '''
        prompt = "Rewrite the following article with elementary school level vocabulary:" + article
        response = self.getResponse(prompt)
        return response
    
    def getPoem(self, article):
        ''' Generate a modified version of the article which replaces a poem that rhymes '''
        prompt = "Rewrite the following article as a poem that rhymes:" + article
        response = self.getResponse(prompt)
        return response
    
if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))
