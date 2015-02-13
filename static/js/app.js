$(function() {

    //Set up instafeed
    var feed = new Instafeed({
        //clientId: 'dd20ca0e6dd74ed8a12e13b5d4841637',
        target: 'instafeed',
        get: 'user',
        userId: 1660779127, 
        accessToken: '1660779127.682f757.ae522e0680a84182885d03115f5b23cf',
        links: true,
        limit: 8,
        sortBy: 'most-recent',
        resolution: 'standard_resolution',
        template: '<div class="col-xs-12 col-sm-6 col-md-4 col-lg-3"><div class="photo-box"><div class="image-wrap"><a href="{{link}}"><img src="{{image}}"></a><div class="likes">{{likes}} Likes</div></div><div class="description">{{caption}}<div class="date">{{model.date}}</div></div></div></div>'
    });
    feed.run();
    $('#i_scroll_down').on('click', function(){
        $('html, body').animate({
            scrollTop: $(".site-description").offset().top-20
        }, 600);
    });
});