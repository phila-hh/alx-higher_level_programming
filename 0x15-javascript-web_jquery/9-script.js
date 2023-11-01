const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(this).ready(function () {
  $.getJSON(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
