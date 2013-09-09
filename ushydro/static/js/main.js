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
  console.log("called")
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

  } else {
    $('.sticker').css({'visibility':'hidden'});
    $('body').css({'padding-top':'0px'})
  }
}
