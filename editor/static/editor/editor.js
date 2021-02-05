var questionPad;
var codePad;
var inPad;
var outPad;

function init(question, freeze, lang) {

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
  var questionMirror;
  var codeMirror;
  var inMirror = CodeMirror(document.getElementById('input'), { lineWrapping: true });
  var outMirror = CodeMirror(document.getElementById('output'), { lineWrapping: true });
  questionMirror = CodeMirror(document.getElementById('firepad-container'), { lineWrapping: true, readOnly: true });
  switch(lang){
    case 'CPP':
      console.log(lang);
      console.log("refresh");
      if(freeze == "True") {
        codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineNumbers: true, readOnly: true, mode: 'text/x-c++src',matchBrackets: true,});
      } else {
        codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineNumbers: true, mode: 'text/x-c++src',matchBrackets: true,});
      }
      break;
    case 'C':
      console.log(lang);
      console.log("refresh");
      if(freeze == "True") {
        codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineNumbers: true, readOnly: true, mode: 'text/x-csrc',matchBrackets: true,});
      } else {
        codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineNumbers: true, mode: 'text/x-csrc',matchBrackets: true,});
      }
      break;
    case 'JAVA':
      console.log(lang);
      console.log("refresh");
      if(freeze == "True") {
        codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineNumbers: true, readOnly: true, mode: 'text/x-java',matchBrackets: true,});
      } else {
        codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineNumbers: true, mode: 'text/x-java',matchBrackets: true,});
      }
      break;
    case 'PYTHON2':
      console.log(lang);
      console.log("refresh");
      if(freeze == "True") {
        codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineNumbers: true, readOnly: true, mode:{name: "python",
               version: 2, singleLineStringErrors: false}, indentUnit: 4, matchBrackets: true});
      } else {
        codeMirror = CodeMirror(document.getElementById('firepad-container1'), { lineNumbers: true, mode: {name: "python",
               version: 2, singleLineStringErrors: false}, indentUnit: 4, matchBrackets: true});
      }
      break;
  }


  //// Create Firepad (with rich text toolbar and shortcuts enabled).
  questionPad = Firepad.fromCodeMirror(questionfirepasRef, questionMirror, { richTextToolbar: true, richTextShortcuts: true});
  codePad = Firepad.fromCodeMirror(codefirepadRef, codeMirror);
  inPad = Firepad.fromCodeMirror(inputref, inMirror, { richTextShortcuts: true});
  outPad = Firepad.fromCodeMirror(outputref, outMirror, { richTextShortcuts: true});
  //// Initialize contents.
  questionPad.on('ready', function() {
    if (questionPad.isHistoryEmpty()) {
      questionPad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">'+question+'</span>');
    }
  });
  codePad.on('ready', function() {
    if (codePad.isHistoryEmpty()) {
      codePad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Write your Code here...</span>');
    }
  });
  inPad.on('ready', function() {
    if (inPad.isHistoryEmpty()) {
      inPad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Input Area</span>');
    }
  });
  outPad.on('ready', function() {
    if (outPad.isHistoryEmpty()) {
      outPad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Output Area</span>');
    }
  });

  document.getElementById("language").value = lang;

}

// Helper to get hash from end of URL or generate a random one.
function getQuestionRef() {

  var ref = firebase.database().ref();
  var hash = "question"+"-"+window.location.pathname.replace('/editor/', '');
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
  var hash = "code" +"-"+window.location.pathname.replace('/editor/', '');
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
  var hash = "input"+"-"+window.location.pathname.replace('/editor/', '');
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
  var hash = "output"+"-" + window.location.pathname.replace('/editor/', '');
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

  var path =  'http://127.0.0.1:8000'+window.location.pathname+'/freeze';
  window.location = path;

}

function checkState(state){
  
  var url = 'http://127.0.0.1:8000' + window.location.pathname + "/check";
  
  $.ajax({
    type: "POST",
    url: url, 
    dataType: "json",
    data: {csrfmiddlewaretoken: window.CSRF_TOKEN},
    success: function(result) {
        console.log(result);
        if (result.state == false && state == "True")
          window.location.reload();
        else if (result.state == true && state == "False")
          window.location.reload();
        else
          console.log("nvm");
    }
  });
}

function select(){

  var url = 'http://127.0.0.1:8000'+window.location.pathname+'/changelang';
  var lang = document.getElementById("language").value;

  $.ajax({
    type: "POST",
    url: url,
    dataType: "json",
    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, 'params': JSON.stringify(lang)},
    success: function(result) {
        console.log(result);
    }
  });
}

function checklanguage(lang){

  var url = 'http://127.0.0.1:8000' + window.location.pathname + "/checklang";

  $.ajax({
    type: "POST",
    url: url,
    dataType: "json",
    data: {csrfmiddlewaretoken: window.CSRF_TOKEN},
    success: function(result) {
        if (result.language != lang) {
          var langset = document.getElementById('language');
          langset.value = result.language;
          window.location.reload();
        }
    }
  });
}
