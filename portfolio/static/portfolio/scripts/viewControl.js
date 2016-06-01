(function(module) {
  var pageView = {};

  pageView.initPage = function(){
    Project.all.forEach(function(a){
      $('#portfolio').append(a.postProj());
    });
  };

  $(document).ready(function(){
    $('a[href^="#"]').on('click',function (event) {
      event.preventDefault();
      var target = this.hash;
      var $target = $(target);
      $('html, body').stop().animate({
        'scrollTop': $target.offset().top
      }, 900, 'swing', function () {
        window.location.hash = target;
      });
    });
  });

  module.pageView = pageView;
})(window);
