(function() {
  var d = document;
  var selectEl = d.getElementById('lang-select');
  var textArea = document.getElementById('code');

 // editor setup
  var editor = CodeMirror.fromTextArea(textArea,
    {
      lineNumbers: true,
      lineWrapping: true,
      matchBrackets:true,
      theme: 'base16-light'
    });

  CodeMirror.modeURL = '/static/js/vendors/codemirror/mode/%N/%N.js';

  // set mode on load
  var langOnLoad = selectEl.value;
  CodeMirror.autoLoadMode(editor, langOnLoad);
  editor.setOption('mode', langOnLoad);

  selectEl.addEventListener('change', function(event) {
    var lang = event.target.value;

    if (lang) {
      CodeMirror.autoLoadMode(editor, lang);
      editor.setOption('mode', lang);
    }
  });
})();

