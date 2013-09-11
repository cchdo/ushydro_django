var nav_top = 0;
$(function(){
  $(window).load(function() {
    nav_top = $('.navbar').offset().top;
    console.log(nav_top);

    $('.sticker').css({'visibility':'hidden'});

    $(this).bind("touchmove", scrollDeligate);
    $(this).scroll(scrollDeligate);
  });
});
function scrollDeligate(e){
  if ($(window).scrollTop() > nav_top) {
    $('.navbar').css('position', 'fixed');
  } else{
    $('.navbar').css('position', 'static');
  }
  if( $('.navbar').css('position') == 'fixed' ) {
    $('body').css({'padding-top':'70px'})
      s = $('.sticker')
      if ( s.css('visibility') == 'hidden'){
        s.css({'visibility':'visible'});
        s.css({'display':'none'});
      };
    s.fadeIn('fast');
    $("#spynav").css('position', 'fixed');
    $("#spynav").css('top', '70px');

  } else {
    $('.sticker').css({'visibility':'hidden'});
    $('body').css({'padding-top':'0px'})
    $("#spynav").css('position', 'absolute');
    $("#spynav").css('top', '0');
  }
}
