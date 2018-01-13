import hug
from werkzeug.utils import secure_filename

api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api,max_age=10))

@hug.post("/upload")
def uploadForm(body):
    file = body['file']
    description = body['file_description']

    print(description)

    if file:
        print("writing file?")
        with open(body['file_name'],"wb") as open_file:
            open_file.write(file)

    return {"success": True}



