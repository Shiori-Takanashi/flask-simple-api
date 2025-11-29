from datetime import datetime

def get_time():
    return {"msg": datetime.now().isoformat()}
