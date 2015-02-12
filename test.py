def get_images(query="finland"):
    import requests
    payload = {'method':'cooperhewitt.objects.getRandom','access_token':   'f6aa02b8af1aea894e304c4ca0f62d62', 'has_image': 'YES'}
    r = requests.get("https://api.collection.cooperhewitt.org/rest/", params=payload)
    object_id = r.json()["object"]["id"]
    print object_id
    payload = {'method':'cooperhewitt.objects.getImages','access_token':   'f6aa02b8af1aea894e304c4ca0f62d62', 'object_id': object_id}
    r = requests.get("https://api.collection.cooperhewitt.org/rest/", params=payload)
    image_url = r.json()["images"][0]["b"]["url"]
    return image_url
print get_images()