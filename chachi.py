from clarifai.client import ClarifaiApi
import os

#clarifai_api = ClarifaiApi()  # assumes environment variables are set.
#result = clarifai_api.tag_image_urls('http://goavitae.com/wp-content/themes/go-avitae-2014/images/Static/AVW-Lineup-05.png')
#print (result['results'][0]['result']['tag']['classes'][6])



def fune(object1,pic):
	clarifai_api = ClarifaiApi("gzPcmrpBHcjTmz2I4bu1_QQ9CNRuFAnyH6ZH7bJr", "U6hptJhZaowpSsu53yW4ETcWo4l1Wn7wUI9rt4fv")	
	result = clarifai_api.tag_image_urls(pic)
	result = (result['results'][0]['result']['tag']['classes'])
	if unicode(object1) in result:
		print('yes')
		return True 
	
	else:
		print ('false') 
		return False 


def Drink(Drink):
	print "i have a %s"	 % Drink

#Drink('drink')

def dog(i_dont_have_a_drink):
	print"i dont have a %s"  % i_dont_have_a_drink

 
#dog('drink')

fune("drink","https://upload.wikimedia.org/wikipedia/commons/b/b4/Havanese0315.jpg")
#fune("Dog","http://goavitae.com/wp-content/themes/go-avitae-2014/images/Static/AVW-Lineup-05.png")