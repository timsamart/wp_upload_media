import requests
import json
import base64

user = 'restusr'
pythonapp = 'WWWW WWWW WWWW WWWW WWWW WWWW' # paste here your auth. token from Wordpress (plugin used: https://wordpress.org/plugins/application-passwords/)
url = 'http://www.nikosam-art.de/wp-json/wp/v2'
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8'))
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

media = {'file': open('picture.jpg','rb')}

image = requests.post(url + '/media', headers=headers, files=media)
link = json.loads(image.content.decode('utf-8'))['link']
postid =json.loads(image.content.decode('utf-8'))['id']
print('Your image is published on {} with ID {}'.format(link, postid))

post = {'caption': 'My great demo picture',
        'description': 'my great descrition'
        }
r = requests.post(url + '/media/'+str(postid), headers=headers, json=post)
print('Your image is updated on {} with ID {}'.format(link, postid))

# for publishing a simple post:
'''
post = {'date': '2017-06-19T20:00:35',
        'title': 'First REST API post',
        'slug': 'rest-api-1',
        'status': 'publish',
        'author': '1',
        'excerpt': 'Exceptional post!',
        'format': 'standard'
        }
r = requests.post(url + '/posts', headers=headers, json=post)
print('Your post is published on ' + json.loads(r.content)['link'])'''