angular.module('services', ['ngResource']).
    factory('Category', function($resource) {
         return $resource('/talks/api/categories');
    }).
    factory('Talk', function($resource) {
         return $resource('/talks/api/categories/:categoryId/talks', {categoryId: 'categoryId'});
    });

angular.module('xconf', ['services']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}).filter('startFrom', function() {
    return function(input, start) {
        start = +start; //parse to int
        return input.slice(start);
    };
});

var XConfCtrl = ["$scope", "Category", "Talk", function($scope, Category, Talk){
    Category.get(function(data){
        data.results = _(data.results).map(function(category){
            category.hyphanizedTitle = hyphanize(category.title);
            return category;
        });
        $scope.categories = data;
        $scope.selectedCategory = data.results[0];
    });

    var hyphanize = function(string) {
        return string.replace(' ','-');
    };

    $scope.currentPage = 1;
    $scope.pageSize = 4;

    $scope.talks = {results: []};

    $scope.loadTalks = function(category){
        Talk.get({categoryId: category.id, page_size: $scope.pageSize, page: $scope.currentPage}, function(data){
            $scope.talks = data;
            $scope.nextAvailable = data.next;
            $scope.previousAvailable = data.previous;
        });
    };

    $scope.switchTalks = function(category) {
        $scope.currentPage = 1;
        $scope.loadTalks(category);        
    }

    $scope.nextPage = function(category){
        $scope.currentPage += 1;
        $scope.loadTalks(category);
    };

    $scope.previousPage = function(category) {
        $scope.currentPage -= 1;
        $scope.loadTalks(category);
    };
}];