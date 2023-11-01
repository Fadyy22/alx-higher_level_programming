const $ = window.$;
window.onload = () => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();

    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + code + '', (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
};
