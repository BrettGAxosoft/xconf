$(function(){

    bespoke.horizontal.from('article', {
        loop: true
    });

    var controller = new Leap.Controller();
    var controllerOptions = {enableGestures: true};

    var swipeStarted = false;
    
    var controlSlides = function(elem,index) {

        if(elem.type === 'swipe' && elem.state === 'start') {
            swipeStarted = true;
        }

        if(swipeStarted === true && elem.type === 'swipe' && elem.state === 'stop'){
            var xStartPos = elem.startPosition[0];
            var xPos = elem.position[0];
            if(xStartPos > xPos) {
                bespoke.next();
            }
            swipeStarted = false;
            setTimeout(function() {
            }, 1000);
        }
    };

    Leap.loop({enableGestures: true}, function(frame){
        if(frame.gestures && frame.gestures.length > 0){
            var userGestures = frame.gestures;
            userGestures.forEach(controlSlides);
        }
    });
});