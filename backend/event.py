class Event():

    def __init__(self, Dict: dict) -> None:
        if "eType" in Dict:
            self.etype = str(Dict["eType"])
        if "edetail" in Dict:
            self.edetail = dict(Dict["edetail"])

    def tojson(self) -> dict:
        """ 将获得GEvent类的dict形式"""
        js = {
            "eType": self.etype,
            "edetail": self.edetail,
        }
        return js
