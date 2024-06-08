
admin_dict = {'Arash': 107998330
              }

def is_admin(chat_id):
    return chat_id in admin_dict.values()
