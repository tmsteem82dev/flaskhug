import hug

api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api,max_age=10))

@hug.post("/upload")
def uploadForm(body):
    return {"success": True}



