from event import Event
import method

def EventDistributer(Event: Event) -> Event:
    """
        根据Event.eType将需求分发给对应函数
        返回对象包含所求信息
    """
    if Event.etype == "GetWord":
        return GetWordHandler(Event)
    if Event.etype == "GetUser":
        return GetUserHandler(Event)
    if Event.etype == "FindMemo":
        return FindMemoHandler(Event)
    if Event.etype == "InsertMemo":
        return InsertMemoHandler(Event)
    if Event.etype == "DeleteMemo":
        return DeleteMemoHandler(Event)
    if Event.etype == "GetMemo":
        return GetMemoHandler(Event)
    if Event.etype == "GetMemoWord":
        return GetMemoWordHandler(Event)
    if Event.etype == "GetID":
        return GetIDHandler(Event)


def GetWordHandler(Event: Event) -> Event:
    if "word" in Event.edetail:
        # print(Event.edetail)
        Event.edetail["word_translation"] = method.getword(Event.edetail["word"])
    return Event


def GetUserHandler(Event: Event) -> Event:
    Event.edetail["result"] = method.getuser(Event.edetail["openid"], Event.edetail["session_key"])
    return Event


def FindMemoHandler(Event: Event) -> Event:
    Event.edetail["result"] = method.findmemo(Event.edetail["openid"], Event.edetail["word"])
    return Event


def InsertMemoHandler(Event: Event) -> Event:
    Event.edetail["result"] = method.insertmemo(Event.edetail["openid"], Event.edetail["word"], Event.edetail["level"])
    return Event


def DeleteMemoHandler(Event: Event) -> Event:
    Event.edetail["result"] = method.deletememo(Event.edetail["openid"], Event.edetail["word"], Event.edetail["level"])
    return Event


def GetMemoHandler(Event: Event) -> Event:
    Event.edetail["word_translation"] = method.getmemo(Event.edetail["openid"], Event.edetail["level"])
    return Event


def GetMemoWordHandler(Event: Event) -> Event:
    Event.edetail["word_translation"] = method.getmemoword(Event.edetail["openid"], Event.edetail["word"],
                                                           Event.edetail["level"])
    return Event

def GetIDHandler(Event: Event) -> Event:
    Event.edetail["openid"], Event.edetail["session_key"] = method.getid(Event.edetail["js_code"])
    return Event
