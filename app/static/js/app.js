var instafeed = (function(){
    return {
        init : function(paramUserId, paramAccessToken){
            try {
                new Instafeed({
                    target: 'instafeed',
                    get: 'user',
                    userId: paramUserId, //1660779127, 
                    accessToken: paramAccessToken, //'1660779127.682f757.ae522e0680a84182885d03115f5b23cf',
                    links: true,
                    limit: 8,
                    sortBy: 'most-recent',
                    resolution: 'standard_resolution',
                    template: '<div class="col-xs-12 col-sm-6 col-md-4 col-lg-3"><div class="photo-box"><div class="image-wrap"><a href="{{link}}"><img src="{{image}}"></a><div class="likes">{{likes}} Likes</div></div><div class="description">{{caption}}<div class="date">{{model.date}}</div></div></div></div>'
                }).run();
            } catch (e){
                console.log('Instafeed init exception: '+e.message);
            }
        }
    }
}());

var subscribe_form = (function(){
    return {
        init : function(){
            try {
                $('#form_contact').on('submit', function(e){
                    e.preventDefault();
                    $('.contact-form .messages .alert').remove();
                    $.ajax({
                        url: $(this).attr('action'),
                        type : 'POST',
                        data : $(this).serialize(),
                        cache:false,
                        timeout:5000
                    }).done(function(rpo){
                        switch(rpo.CODE){
                            case "0":
                                $('.contact-form .messages').append($('<div>', { 'class' : 'alert alert-success', text : rpo.TEXT}));
                                $('#form_contact').addClass('hidden');
                                break;
                            default:
                                $('.contact-form .messages').append($('<div>', { 'class' : 'alert alert-warning', text : rpo.TEXT}));
                                break;
                        }
                    }).fail(function(){
                        $('.contact-form .messages').append($('<div>', { 'class' : 'alert alert-warning', text : 'Произошла ошибка. Попробуйте еще раз'}));
                    }).always(function(){
                        $('#btn_wannago').removeAttr('disabled');
                    });
                });
            } catch (e){
                console.log('Subscribe form init exception: '+e.message);
            }
        }
    }
}());

var app = (function(){
    return {
        init : function(){
            try {
                subscribe_form.init();
                instafeed.init(1660779127, '1660779127.682f757.ae522e0680a84182885d03115f5b23cf');
                $('#bg_video').tubular({videoId: 'ajPPMBtqY1k'});

                $('#i_scroll_down').on('click', function(){
                    $('html, body').animate({
                        scrollTop: $(".site-description").offset().top-20
                    }, 600);
                });
                $('#btn_wannago').removeAttr('disabled');
            } catch (e){
                console.log('App init form exception: '+e.message);
            }
        }
    }
}());

$(function() {
    app.init();
});