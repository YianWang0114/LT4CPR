import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('wgeME3hMTipj-t2tIB03QpY-rnnS3LsajLR2K30YwNvk')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/0e358fc8-52c7-4b16-a92c-7ed72e947260')

language = language_translator.identify(
    'Language translator translates text from one language to another').get_result()
print(json.dumps(language, indent=2))


# import json
# from ibm_watson import LanguageTranslatorV3
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# authenticator = IAMAuthenticator('wgeME3hMTipj-t2tIB03QpY-rnnS3LsajLR2K30YwNvk')
# language_translator = LanguageTranslatorV3(
#     version='2018-05-01',
#     authenticator=authenticator
# )

# language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/0e358fc8-52c7-4b16-a92c-7ed72e947260')

# languages = language_translator.list_identifiable_languages().get_result()
# print(json.dumps(languages, indent=2))


