const $ = window.$;
window.onload = () => {
  $('INPUT#btn_translate').click(() => {
    translateHello();
  });
  $('INPUT#language_code').keypress((event) => {
    if (event.key === 'Enter') {
      translateHello();
    }
  });
};

function translateHello () {
  const code = $('INPUT#language_code').val();

  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + code + '', (data) => {
    $('DIV#hello').text(data.hello);
  });
}
