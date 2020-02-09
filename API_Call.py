import requests





def get_branches():

    base_url = "http://api.leapos.ca/obp/v4.0.0/banks/15fa44fc932d4b4cae9d2f28ec7b5cf/branches"
    API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.De81eP_3gmHmmxJmRA92knXWiVqTGls2RLHc6Swh4Ic"
    headers = {
        'Authorization': 'DirectLogin token=%s' % (API_KEY)
    }
    r =  requests.get(base_url, headers=headers)
    print("CONTENT \n", type(r.json()))
    print("HEADER \n", r.headers)
    print("STATUS \n", r.status_code)

    return "'One is at 801 Stewart Green SW Calgary'"