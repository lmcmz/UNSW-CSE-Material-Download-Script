import requests, os
import filetype

def is_downloadable(url):
	h = requests.head(url, allow_redirects=True, verify=False)
	if not h.status_code == 200:
		return False
	header = h.headers
	content_type = header.get('content-type')
	if 'text' in content_type.lower():
		return False
	if 'html' in content_type.lower():
		return False
	return True

def download_file(url, path):
	if not is_downloadable(url):
		return False
	r = requests.Response()
	if not os.path.isfile(path):
		r = requests.get(url, verify=False)
		if r.status_code == 200:
			with open(path, 'wb') as f:
				f.write(r.content)
	kind = filetype.guess(path)
	path = path.replace("∑", ".").replace("§", "\"")
	if kind is not None:
		os.rename(path, path+"."+kind.extension)
#		print('File extension: %s' % kind.extension)
	return True