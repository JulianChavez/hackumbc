
from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()  # assumes environment variables are set.
result = clarifai_api.tag_image_urls(['http://goavitae.com/wp-content/themes/go-avitae-2014/images/Static/AVW-Lineup-05.png','http://goavitae.com/wp-content/uploads/2015/02/AVW-Flavor-Bottles_web2.jpg'])
print (result['results'][0]['result']['tag']['classes'][6])

print "i do have a drink"