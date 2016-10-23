
# Python-Basic

number = int(input("Enter the number: ")) <br>

<h2>import urllib</h2>
* Download a file from internet: <br>
    urllib.request.urlretrieve("url", "filename")  <br>


<h2>import requests</h2>
* Getting the source code of an url <br>
	request.get("url") <br>


<h2>import BeautifulSoup</h2>
* getting specific tag inside a source code string: <br>

		for link in soup.findall('a', {'class': 'item-name'}): <br>
	
				href = link.get('href')  //here link is the full line of tag and href string seperates the href tag only<br>
				title = link.string <br> // this is the plain text between the starting and ending tag
