jQuery('document').ready(function() {
  var count = 0;
  $('.buy').on('click', function() {
    count = count + 1;
    $('.count').html('Товаров в корзине: ' + count);
  });



});
