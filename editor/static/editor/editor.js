var questionPad;
var codeMirror;
var codePad;
var inPad;
var outPad;
var lang = document.getElementById("language").value;

function init() {

  //// Initialize Firebase.
  var config = {
    apiKey: "AIzaSyC_JdByNm-E1CAJUkePsr-YJZl7W77oL3g",
    authDomain: "firepad-tests.firebaseapp.com",
    databaseURL: "https://firepad-tests.firebaseio.com"
  };

  firebase.initializeApp(config);

  //// Get Firebase Database reference.
  var questionfirepasRef = getQuestionRef();
  var codefirepadRef = getCodeRef();
  var inputref = getInputRef();
  var outputref = getOutputRef();

  //// Create CodeMirror (with lineWrapping on).
  var questionMirror = CodeMirror(document.getElementById('firepad-container'), { lineWrapping: true });
  var codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineWrapping: true, lineNumbers: true,
    gutter: true, theme: "dracula",
        indentUnit: 4,
        matchBrackets: true,
        indentAuto: true});
  var inMirror = CodeMirror(document.getElementById('input'), { lineWrapping: true });
  var outMirror = CodeMirror(document.getElementById('output'), { lineWrapping: true });
  //// Create Firepad (with rich text toolbar and shortcuts enabled).
  questionPad = Firepad.fromCodeMirror(questionfirepasRef, questionMirror, { richTextToolbar: true, richTextShortcuts: true});
  codePad = Firepad.fromCodeMirror(codefirepadRef, codeMirror, { });
  inPad = Firepad.fromCodeMirror(inputref, inMirror, { richTextShortcuts: true});
  outPad = Firepad.fromCodeMirror(outputref, outMirror, { richTextShortcuts: true});
  //// Initialize contents.
  questionPad.on('ready', function() {
    if (questionPad.isHistoryEmpty()) {
      questionPad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Write your article here...</span>');
    }
  });
  codePad.on('ready', function() {
    if (codePad.isHistoryEmpty()) {
      codePad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Write your article here...</span>');
    }
  });
  inPad.on('ready', function() {
    if (inPad.isHistoryEmpty()) {
      inPad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Write your article here...</span>');
    }
  });
  outPad.on('ready', function() {
    if (outPad.isHistoryEmpty()) {
      outPad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Write your article here...</span>');
    }
  });

}

// Helper to get hash from end of URL or generate a random one.
function getQuestionRef() {
  var ref = firebase.database().ref();
  var hash = "question"+window.location.hash.replace(/#/g, '');
  if (hash) {
    ref = ref.child(hash);
  } else {
    ref = ref.push(); // generate unique location.
    window.location = window.location + '#' + ref.key; // add it as a hash to the URL.
  }
  if (typeof console !== 'undefined') {
    console.log('Firebase data: ', ref.toString());
  }
  return ref;
}

function getCodeRef() {
  var ref = firebase.database().ref();
  var hash = "code" + window.location.hash.replace(/#/g, '');
  if (hash) {
    ref = ref.child(hash);
  } else {
    ref = ref.push(); // generate unique location.
    window.location = window.location + '#' + ref.key; // add it as a hash to the URL.
  }
  if (typeof console !== 'undefined') {
    console.log('Firebase data: ', ref.toString());
  }
  return ref;
}



function getInputRef() {
  var ref = firebase.database().ref();
  var hash = "input"+window.location.hash.replace(/#/g, '');
  if (hash) {
    ref = ref.child(hash);
  } else {
    ref = ref.push(); // generate unique location.
    window.location = window.location + '#' + ref.key; // add it as a hash to the URL.
  }
  if (typeof console !== 'undefined') {
    console.log('Firebase data: ', ref.toString());
  }
  return ref;
}

function getOutputRef() {
  var ref = firebase.database().ref();
  var hash = "output"+window.location.hash.replace(/#/g, '');
  if (hash) {
    ref = ref.child(hash);
  } else {
    ref = ref.push(); // generate unique location.
    window.location = window.location + '#' + ref.key; // add it as a hash to the URL.
  }
  if (typeof console !== 'undefined') {
    console.log('Firebase data: ', ref.toString());
  }
  return ref;
}

function compileandrun(){

  var url = 'http://127.0.0.1:8000/editor/run';
  var source = codePad.getText();
  var lang = document.getElementById("language").value;
  var input = document.getElementById("in").value;

  var data = {
    source: source,
    lang: lang,
    input: input
  };

  $.ajax({
    type: "POST",
    url: url,
    dataType: "json",
    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, 'params': JSON.stringify(data)},
    success: function(result) {
        console.log(result);
        document.getElementById("out").value = result['output'];
        alert("done");
    }
  });

}

function freezeall(){
  questionPad.setOptions('readOnly',true);
  questionPad.refresh();
  codePad.setOptions('readOnly',true);
  codePad.refresh();
  inPad.setOptions('readOnly',true);
  inPad.refresh();
  outPad.setOptions('readOnly',true);
  outPad.refresh();

}
var modeInput = document.getElementById("select");
function select(x){
  var optionText = modeInput.selectedIndex;
  var modes = {'PYTHON2':'text/python','Javascript':'text/javascript','C':'text/x-csrc', 'CPP':'text/x-c++src'};

  codeMirror.setOptions('mode', modes[optionText]);
  CodeMirror.autoLoadMode(codeMirror, modes[optionText]);
}