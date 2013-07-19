
$(function(){
    $(window).load(function() {
        $('.navbar').affix({offset: $('.navbar').offset().top});

        $('.sticker').css({'visibility':'hidden'});
        $(this).scroll(function(){
            if( $('.affix').css('position') == 'fixed' ) {
                s = $('.sticker')
                if ( s.css('visibility') == 'hidden'){
                  s.css({'visibility':'visible'});
                  s.css({'display':'none'});
                };
                s.fadeIn('fast');

            } else {
                $('.sticker').css({'visibility':'hidden'});
			}
        });
    });
});
