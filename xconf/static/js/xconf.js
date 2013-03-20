angular.module('services', ['ngResource']).
    factory('Category', function($resource) {
         return $resource('/talks/api/categories');
    }).
    factory('Talk', function($resource) {
         return $resource('/talks/api/categories/:categoryId/talks', {categoryId: 'categoryId'});
    }).
    factory('TalkDetail', function($resource) {
         return $resource('/talks/api/talks/:id/detail', {id: 'id'});
    }).
    factory('Vote', function($resource) {
         return $resource('/talks/api/votes/:id', {'id': '@id'});
    }).
    factory('VotedTalk', function($resource) {
         return $resource('/talks/api/categories/:categoryId/uservotes', {categoryId: 'categoryId'});
    });


angular.module('xconf', ['services']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}).filter('startFrom', function() {
    return function(input, start) {
        start = +start; //parse to int
        return input.slice(start);
    };
}).config(function($httpProvider) {
    $httpProvider.defaults.transformRequest.push(function(data, headersGetter) {
        var headers = headersGetter();
        headers['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
        return data;
    });
});

var XConfCtrl = ["$scope", "Category", "Talk", "Vote", "VotedTalk", "TalkDetail", function($scope, Category, Talk, Vote, VotedTalk, TalkDetail){
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
        return ("#" + category.hyphanizedTitle == window.location.hash) ? "active" : "";
    };

    $scope.currentPage = 1;
    $scope.pageSize = 8;

    $scope.talks = {results: []};
    $scope.userVotes = {results: []};


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
        $scope.loadVotedTalks(category);
    };

    $scope.loadVotedTalks = function(category) {
        VotedTalk.get({categoryId: category.id}, function(data){
          $scope.userVotes = data;
        });
    }

    $scope.nextPage = function(category){
        $scope.currentPage += 1;
        $scope.loadTalks(category);
    };

    $scope.previousPage = function(category) {
        $scope.currentPage -= 1;
        $scope.loadTalks(category);
    };

    $scope.showTalkDetails = function(talk, category) {
      TalkDetail.get({id: talk.id}, function(talkDetails){
        $scope.currentTalk = talkDetails;
        $scope.currentCategory = category;
        $('#talk-details').modal();
      });
    }

    $scope.hasVoted = function(talk) {
      if(talk == null){
        return false;
      }
      return _($scope.userVotes.results).detect(function(vote){
        return vote.talk.id === talk.id;
      });
    };

    $scope.toggleVote = function(talk, category) {
      $scope.hasVoted(talk) ? $scope.unvote(talk, category) : $scope.vote(talk, category);
    };

    $scope.unvote = function(talk, category) {
      new Vote({id: $scope.hasVoted(talk).id}).$delete(function(){
       $scope.loadVotedTalks(category);
      });
    };

    $scope.vote = function(talk, category) {
      var vote = new Vote();
      vote.talk = talk.id;
      vote.$save(function(){
        //alert("Thank you for voting");
        $scope.loadVotedTalks(category);
      }, function(response) {
        alert(response.data.voter);
      });
    };
}];
