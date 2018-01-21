var app = angular.module("testApp");

app.controller("TestController", function($scope, fileUploadService){
    $scope.uploadFile = function(){
        var file = $scope.myFile;
        var descript = $scope.filedescription;

        if(typeof descript == 'undefined')
        {
            descript = "";
        }
        console.log('file is ');
        console.dir(file);

        fileUploadService.fileUpload(file,descript);
    };

    $scope.resizeImage = function(){
        console.log("inside resize img");
        if($scope.imgfile){

            var img = new Image();
            img.onload = function(){
                console.log("loading image!");
                var canvas = document.createElement("canvas");
                canvas.width = 300
                canvas.height = canvas.width * (img.height / img.width);
                
                ctx = canvas.getContext("2d");

                ctx.drawImage(this,0,0,canvas.width,canvas.height);

                var dataUrl = canvas.toDataURL();

                console.log("dataurl: " + dataUrl);

                var fd = new FormData();

                // dataURL can be used to embedd image like this:
                var stringHtmlBody = "<div dir='ltr'>";
                stringHtmlBody += "This is the image I sent: <br>"                
                stringHtmlBody += '<img src=3d"cid:ii_test1" width="200" height="150">';
                stringHtmlBody += "</div>";

                fd.append("image_data", dataUrl);
                fd.append("img_id","ii_test1")
                fd.append("html_body", stringHtmlBody)
                //fileUploadService.resizedImageUpload(fd);
                fileUploadService.emailerSend(fd);
            };

            img.src=$scope.imgfile;
        }
    };
});