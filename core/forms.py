from django import forms
from django.conf import settings
import requests
from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets ={'name': TextInput(attrs={'class' : 'input', 'placeholder': 'Enter a City Name'})}

class RobohashForm(forms.Form):
    user_text = forms.CharField(max_length= 250)

    def hashit(self):
        result = {}
        user_text = self.cleaned_data
        iframe = 'img src="https://robohash.org/?{text}.png"'
        url = endpoint.format()

        print(url)

        return result

class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=25)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        endpoint = 'https://od-api.oxforddictionaries.com/api/v1/entries/{source_lang}/{word_id}'
        url = endpoint.format(source_lang='en', word_id=word)
        headers = {'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
        return result



class SynonymsForm(forms.Form):
    word = forms.CharField(max_length=25)

    def search(self):
         result = {}
         word = self.cleaned_data['word']
         endpoint = 'https://od-api.oxforddictionaries.com/api/v1/entries/{source_lang}/{word_id}/synonyms;antonyms'
         url = endpoint.format(source_lang='en', word_id=word)
         headers= { 'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
         response = requests.get(url, headers=headers)
         if response.status_code == 200:  # SUCCESS
             result = response.json()
             result['success'] = True
         else:
             result['success'] = False
             if response.status_code == 404:  # NOT FOUND
                 result['message'] = 'No entry found for "%s"' % word
             else:
                 result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
         return result


class AntonymsForm(forms.Form):
    word = forms.CharField(max_length=25)

    def search(self):
         result = {}
         word = self.cleaned_data['word']
         endpoint = 'https://od-api.oxforddictionaries.com/api/v1/entries/{source_lang}/{word_id}/synonyms;antonyms'
         url = endpoint.format(source_lang='en', word_id=word)
         headers= { 'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
         response = requests.get(url, headers=headers)
         if response.status_code == 200:  # SUCCESS
             result = response.json()
             result['success'] = True
         else:
             result['success'] = False
             if response.status_code == 404:  # NOT FOUND
                 result['message'] = 'No entry found for "%s"' % word
             else:
                 result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
         return result
