$(function(){
    $('#subnav-wrapper').height($('#subnav').height());
    $('#subnav').affix({
        offset: {top: function() {
            var element = $('#subnav');
            if(!element.data('top')){
                element.data('top', element.position().top);
            }
            return element.data('top');
        }}
    });
    Vote.init();
});

var Vote = {
    init: function() {
        $.getJSON('/talks/api/talks/', function(talks) {
        })
    }
}

var talk = function(title, category, votes) {
        var self=this;
        self.title = title;
        self.category = category;
        self.votes = ko.observable(votes);
    };

var user = function() {
    var self = this;
    self.selectedTopics = ko.observableArray();
    self.canVote = ko.computed(function() {
        return self.selectedTopics().length < 3 ;}, self);
};


var votableViewModel = function() {
    var self = this;
    self.talks = ko.observableArray();
    self.user = ko.observable(new user());
};

var xconf = new votableViewModel();
ko.applyBindings(xconf);