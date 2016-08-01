'use strict';

var app = angular.module('django-crud', [ 'ui.router']);


app.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('zip', {
            url: '/',
            templateUrl: 'static/partial/zip.html',
            controller: 'ZipCtrl'
        });
}]);
