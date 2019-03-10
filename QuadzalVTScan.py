import os
try:
    import requests
except ImportError:
    os.system("pip3 install requests")
    os.system("cls")
    import requests
class QuadzalVTScan:
    def __init__(self, file = ""):
        self.file = file
        self.API_KEY = "f960e86374a177fa935f52c5063269a6710f5e9f0a1efcd5fb2853f2f3167865"
        self.params = {'apikey': self.API_KEY}
        self.headers = {"Accept-Encoding": "gzip, deflate","User-Agent" : "gzip,  My Python requests library example client or username"}

        self.DETECTED_TRUE = []
        self.DETECTED_FALSE = []

    def Scan(self):
        files = {'file':  open(self.file, 'rb')}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=self.params)
        json_response = response.json()
        resource = json_response.get("resource")
        return resource
    
    def Report(self):
        resource = self.Scan()
        self.params['resource'] = resource
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=self.params, headers=self.headers)
        if response.status_code != 200:
            raise Exception("Dont Connection with virustotal.com")
        json_response = response.json()
        malwareCompaines = json_response.get("scans")
        return malwareCompaines
    
    def MalwareDetect(self):
        malwareCompaines = self.Report()
        for company in malwareCompaines:
            reportDetail = malwareCompaines.get(company)
            if reportDetail.get("detected") == False:
                self.DETECTED_FALSE.append({"company":company, "detected":"No Malware"})
            else:
                self.DETECTED_TRUE.append({"company":company, "detected" : "Yes Malware"})
        return [self.DETECTED_TRUE, self.DETECTED_FALSE]

