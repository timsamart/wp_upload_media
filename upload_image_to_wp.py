# Copyright [2018] [Timotheos Samartzidis]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import requests
import json
import base64

user = 'theuserwiththeauthcode'
pythonapp = 'WWWW WWWW WWWW WWWW WWWW WWWW' # paste here your auth. token from Wordpress (plugin used: https://wordpress.org/plugins/application-passwords/)
url = 'http://www.mypage.com/wp-json/wp/v2'
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8'))
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

media = {'file': open('picture.jpg','rb')} # 'picture.jpg' path to the image

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