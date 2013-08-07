
$(function(){
    $(window).load(function() {
        $('.navbar').affix({offset: $('.navbar').offset().top});

        $('.sticker').css({'visibility':'hidden'});
        $(this).scroll(function(){
            if( $('.affix').css('position') == 'fixed' ) {
              $('body').css({'padding-top':'70px'})
                s = $('.sticker')
                if ( s.css('visibility') == 'hidden'){
                  s.css({'visibility':'visible'});
                  s.css({'display':'none'});
                };
                s.fadeIn('fast');

            } else {
                $('.sticker').css({'visibility':'hidden'});
              $('body').css({'padding-top':'0px'})
			}
        });
    });
});
