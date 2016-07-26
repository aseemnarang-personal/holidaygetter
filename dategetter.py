class DateGetter:
    def parsejsonline(self, jsonstr):
        date = jsonstr[0]['date'].encode("utf-8")
        name = jsonstr[0]['name'].encode("utf-8")
        observed = jsonstr[0]['observed'].encode("utf-8")
        public = jsonstr[0]['public']
        return[date, name, observed, public]
    def main(self , country_code, years):
        import requests
        holidaymat=[]
        for year in years:
            url = 'https://holidayapi.com/v1/holidays?country='+country_code+'&year='+year+'&key=cc7b2479-e5a8-40e4-bb29-7281f739613c'
            response =  requests.get(url)
            if response.status_code != 200:
                print response.status_code
            else:
                holidays =  response.json()['holidays']
                for outerdate in holidays:
                    holidaymat.append(self.parsejsonline(holidays[outerdate]))
        return holidaymat