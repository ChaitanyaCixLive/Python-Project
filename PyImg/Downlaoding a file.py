import urllib.request

csv_link = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"


def download_csb_file(url):
    response = urllib.request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    destination_url = 'file.csv'
    fx = open(destination_url,'w')

    for line in lines:
        fx.write(line + '\n')

    fx.close()

download_csb_file(csv_link)