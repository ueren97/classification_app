from flickrapi import FlickrAPI
from urllib.request import urlretrieve
# from pprint import pprint
import os
import time
import sys


# information of api key

key = '**********'
secret = '**********'
wait_time = 1

# designate saved directory
imgname = sys.argv[1]
savedir = './' + imgname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=imgname,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, licence'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'

    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
