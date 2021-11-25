def response(res: dict, data=None):
    result = {
        "code": res.get("code"),
        "message": res.get("message"),
        "data": data
    }
    return result
