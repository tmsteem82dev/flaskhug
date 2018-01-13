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
});