from fastapi import HTTPException

class ErrorHandler:
def ErrorHandler(e):
    raise HTTPException(status_code=400, detail=str(e))

def NotFoundHandler(e):
    raise HTTPException(status_code=404, detail=str(e))

def UnauthorizedHandler(e):
    raise HTTPException(status_code=401, detail=str(e))

def ForbiddenHandler(e):
    raise HTTPException(status_code=403, detail=str(e))

def ServerErrorHandler(e):
    raise HTTPException(status_code=500, detail=str(e))

def SuccessHandler(e):
    raise HTTPException(status_code=200, detail=str(e))