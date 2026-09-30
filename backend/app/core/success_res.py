
def success_response(data, message:str):
    return {
        "success":True,
        "message":message,
        "data":data ,
    }