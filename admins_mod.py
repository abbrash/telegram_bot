admin_dict = {'Arash': 107998330, 
              'Art': 1108290862, 
              'Akram': 567038670
              }

def is_admin(user_id: int) -> bool:
    return user_id in admin_dict.values()

def get_admin_name(admin_id: int) -> str:
    for name, id in admin_dict.items():
        if id == admin_id:
            return name
    return "ناشناس"     # "Unknown" in Persian