
def add_cache_headers(headers, path, url):
    if path.endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.css', '.js')):
        headers['Cache-Control'] = 'public, max-age=31536000'
