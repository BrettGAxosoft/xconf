// var Vote = {
//     init: function(categoryId) {
//         $.getJSON('/talks/api/categories/' + categoryId, function(talks) {    
//         })
//     }
// }

var user = function() {
    var self = this;
    self.selectedTopics = ko.observableArray();
    self.canVote = ko.computed(function() {
        return self.selectedTopics().length < 3 ;}, self);
};


var votableViewModel = function() {
    var self = this;
    self.categories = ko.observable();
    self.activeCategory = ko.observable(null);
    self.user = ko.observable(new user());
    self.getTalks = function(category)
    {
        $.getJSON('/talks/api/categories/' + category.id(), function(cat) {    
            var xconf = ko.mapping.fromJS(cat);
            console.log(xconf);
            self.activeCategory(xconf);
        }) ;
    };

};

var votableViewModel = new votableViewModel();
ko.applyBindings(votableViewModel);

(function()
{
    $.getJSON('/talks/api/categories/', function(data) {
        var categories = ko.mapping.fromJS(data);
        votableViewModel.categories(categories.results());
    });
})();



