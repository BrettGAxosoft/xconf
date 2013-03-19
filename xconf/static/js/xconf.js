angular.module('services', ['ngResource']).
    factory('Category', function($resource) {
         return $resource('/talks/api/categories');
    }).
    factory('Talk', function($resource) {
         return $resource('/talks/api/categories/:categoryId/talks', {categoryId: 'categoryId'});
    }).
    factory('Vote', function($resource) {
         return $resource('/talks/api/votes');
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

var XConfCtrl = ["$scope", "Category", "Talk", "Vote", function($scope, Category, Talk, Vote){
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

    $scope.isCurrentPage = function(category) {
        console.log(window.location.hash);
        return ("#" + category.hyphanizedTitle == window.location.hash) ? "active" : "";
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

    $scope.vote = function(talk) {
      var vote = new Vote();
      vote.talk = talk.id;
      vote.csrfmiddlewaretoken = $('[name=csrfmiddlewaretoken]').val();
      vote.$save(function(){
        alert("Thankyou for voting");
      }, function() {
        alert("You have used all your votes. You can unvote a talk if you changed your mind");
      });
    }
}];
