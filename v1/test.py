import os

import openai

openai.api_type = "azure"

openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")

openai.api_version = "2022-12-01"

openai.api_key = os.getenv("AZURE_OPENAI_KEY")

 

response = openai.Completion.create(

  engine="turbo35",

  prompt="""Could you give me a ten sentence summary of the following:

 

This earthquake has brought back the painful memories of the magnitude 7.6 earthquake that struck the same region in October 2005 and left more than 75,000 people dead and hundreds of thousands homeless. #AzadKashmir #earthquake

An #earthquake of magnitude 5.8 jolted different parts of the Pakistan at 4:01 pm. The tremors were felt in #Islamabad, #Rawalpindi, #Lahore, #Peshawar, #Sialkot, #Charsadda, #Gujrat, #Malakand for 10 seconds as people ran out on to the roads from their houses and offices.

#BREAKING: A powerful 5.8-magnitude #earthquake has struck #Pakistan’s capital #Islamabad and other cities in the eastern #Punjab province. People gathered outside their office buildings, in panic, after the earthquake

RT @Ruptly: At least 20 dead after #earthquake hits #Pakistan-administered #Kashmir

Death Toll From Yesterday #earthquake Has Rose to 37 With More than 500 People InJured So Far In AJK ὡ3 Prayers Are With the Affected People.

RT @jazengr: So the death toll has risen to 19 and injured are over 300 with large-scale destruction near Mirpur AJK. #earthquake

Earlier today deadly and scariest#earthquake of 5.8 magnitude took place in my local city Jatlan and its surrounded areas. Almost about 20-25 people have lost their lives including one my uncle &amp; niece of my friend &amp; more than 300 been injured and shifted to nearest hospitals .

#EarthQuake catastrophic disaster in Mirpur Azad Kashmir Massive injured being rushed to hospital Roads and infrastructure Damaged very badly. casualties are expected.

#earthquake #AJK #Mirpur #Kashmir Over 25 Death, 370 injured &amp; some 220 houses/shops/mosques are either partially or completely damaged

25 died and 452 injured have been reported till 10 pm as per report presented to CS AJK out of which 160 critically injured while 292 are minor injured. #earthquake #AJK #Kashmir

Five killed, others injured in Iran train accident -  #Pakistan

Dozens of people have been killed and over 400 are injured due to yesterday’s earthquake in #Pakistan. The injured &amp; wounded need your help. #MuslimAid is on the ground, your generosity could save lives! Donate NOW: £75 could provide urgently needed medical supplies &amp; treatment.

Earthquake .. #azadkashmir #Pakistan

As #earthquakes with 5.8 magnitude jolts parts of #Pakistan, a building collapsed in #Mirpur #azadkashmir, leaving 50 persons so far wounded.

Death toll in #Mirpur #earthquake has risen to 19, according to officials. Nine bodies in Div HQ Hospital and 10 deaths in a village in the jurisdiction of #Jatlan

More Then 10 Casualities &amp; 100+ are injured Heavy damages in Mirpur, Bhimbar and other areas of AJK due to earthquake Ὁ4 #EarthQuake

The #earthquake epicenter was #Jhelum. Emergency has been declared in #Mirpur #Kashmir hospitals. Large cracks have appeared in roads.

19 killed and 300 + injured in Mirpur AK #earthquake

 

""",

  temperature=0,

  max_tokens=3000,

  top_p=0.5,

  frequency_penalty=0,

  presence_penalty=0,

  #best_of=1,

  stop=None)

 

print(response)