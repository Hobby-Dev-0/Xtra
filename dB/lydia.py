from database import db_x

lydia = db_x["LYDIA"]


def add_chat(chat_id, session_id):
    stark = lydia.find_one({"chat_id": chat_id, "session_id": session_id})
    if stark:
        return False
    else:
        lydia.insert_one({"chat_id": chat_id, "session_id": session_id})
        return True


def remove_chat(chat_id):
    stark = lydia.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        lydia.delete_one({"chat_id": chat_id})
        return True

def get_all_chats():
    r = list(lydia.find())
    if r:
        return r
    else:
        return False

