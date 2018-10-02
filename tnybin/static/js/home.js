(function() {
  var d = document;
  var selectEl = d.getElementById('lang-select');
  var textArea = document.getElementById('code');

 // editor setup
  var editor = CodeMirror.fromTextArea(textArea,
    {
      lineNumbers: true,
      lineWrapping: true,
      indentUnit: 4,
      matchBrackets:true,
      theme: 'base16-light'
    });

  CodeMirror.modeURL = '/static/js/vendors/codemirror/mode/%N/%N.js';

  // set mode on load
  var langOnLoad = selectEl.value;
  CodeMirror.autoLoadMode(editor, langOnLoad);
  editor.setOption('mode', langOnLoad);

  // check if language is saved on localStorage
  var langOpt = localStorage.getItem('tnybin-lang') || 'html';
  selectEl.value = langOpt;

  // add listener to language select tag
  selectEl.addEventListener('change', function(event) {
    var lang = event.target.value;

    if (lang) {
      CodeMirror.autoLoadMode(editor, lang);
      editor.setOption('mode', lang);

      // save selected option on localStorage
      localStorage.setItem('tnybin-lang', lang);
    }
  });
})();

