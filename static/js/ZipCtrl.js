'use strict';

app.controller('ZipCtrl', ['$scope','zipServices', function($scope,zipServices) {

    zipServices.getZip()
        .then(function(data) {
            $scope.zips = data;
            console.log($scope.zips);
        },
        function(data) {
           console.log('error', data);
        });

    $scope.zip = {'zipcode': '', 'city': '','state': '', 'country': ''};
    $scope.addZip = function() {

        console.log($scope.zip);
        zipServices.addZip($scope.zip)
            .then(function(data) {

                jQuery('#postEditZip').modal('hide');
                console.log(data);
                $scope.zips.unshift(data);

            }, function(data) {
               console.log('error', data);
            });
    };

    $scope.editShowZipData  = function(formData) {
        $scope.editButton=true;
        $scope.addButton=false;
        $scope.zip = angular.copy({
            id:formData.id,
            zipcode:formData.zipcode,
            state:formData.state.id,
            country:formData.country.id,
            city:formData.city.id
        });
        console.log($scope.zip);
    };
    $scope.buttonHandler=function(data){
        console.log(data)
        if(data==='add'){
            $scope.editButton=false;
            $scope.zip={};
        }
        if(data==='edit'){
            $scope.editButton=true;
        }
    }
    $scope.deleteZip = function(id) {

    zipServices.deleteZip(id)
        .then(function(response) {
               jQuery('#postEditZip').modal('hide');
               for(var i = 0; i < $scope.zips.length; i++) {
                    if($scope.zips[i].id == id) {
                        $scope.zips.splice(i, 1);
                    }
                }
        },
        function(data) {
           console.log('error', data);
        });

    }


    $scope.editZip=function (data) {
        console.log(data);
            zipServices.editZip(data)
        .then(function(response) {

               for(var i = 0; i < $scope.zips.length; i++) {
                    if($scope.zips[i].id == data.id) {
                        $scope.zips[i] = response;
                    }
                }
        },
        function(data) {
           console.log('error', data);
        });

    }
}]);


'use strict';

app.service('zipServices',[ '$q', '$http' , function($q, $http) {
    var service = {
        'request': function (args) {
            var API_URL = '/api';

            args = args || {};
            var deferred = $q.defer(),
                url = API_URL + args.url,
                method = args.method || "GET",
                params = args.params || {},
                data = args.data || {};

            $http({
                url: url,
                method: method.toUpperCase(),
                params: params,
                data: data
            })
            .success(angular.bind(this, function (data, status, headers, config) {
                    deferred.resolve(data, status);
            }))
            .error(angular.bind(this, function (data, status, headers, config) {
                console.log("error syncing with: " + url);
                // Set request status
                deferred.reject(data, status, headers, config);
            }));
            return deferred.promise;
        },

        'getZip': function() {
            return this.request({
                'method':"GET",
                'url':'/zip_list'
            })
        },

        'addZip': function(data) {
            return this.request({
                'method': "POST",
                'url': '/zip_create/',
                'data': data
            })
        },

        'editZip': function(data) {
            return this.request({
				'method': "PUT",
				'url': "/zip/"+data.id+"/",
                'data': data
			});
        },

        'deleteZip': function(id) {
            return this.request({
				'method': "DELETE",
				'url': "/zip/"+id+"/"
			});
        }
    };

    return service;
}]);