def github_downloader(self, self2):
  autor = self
  projekt = self2
  url = "https://github.com/" + autor + "/" + projekt + "/archive/master.zip"
  name = projekt + ".zip"
  urllib.request.urlretrieve(url, name)
