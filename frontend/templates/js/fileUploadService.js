var app = angular.module("testApp");

app.service("fileUploadService",function($http){
    var fileUpload = function(file,fdescript){
        var fd = new FormData();
        fd.append('description', fdescript)
        fd.append('file', file);

        console.log("uploading file: " + file);

        return $http.post("http://localhost:5000/uploader",fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        })
        .then(function(response){
            return response.data;
        });
    };

    return {
        fileUpload : fileUpload
    };
});