
function init() {
  
  //// Initialize Firebase.
  var config = {
    apiKey: "AIzaSyC_JdByNm-E1CAJUkePsr-YJZl7W77oL3g",
    authDomain: "firepad-tests.firebaseapp.com",
    databaseURL: "https://firepad-tests.firebaseio.com"
  };

  firebase.initializeApp(config);
  
  //// Get Firebase Database reference.
  var firepadRef = getExampleRef();
  var firepadRef1 = getExampleRef1();

  console.log(firepadRef);
  console.log(firepadRef1);
  
  //// Create CodeMirror (with lineWrapping on).
  var codeMirror = CodeMirror(document.getElementById('firepad-container'), { lineWrapping: true });
  var codeMirror1 = CodeMirror(document.getElementById('firepad-container1'), { lineWrapping: true, lineNumbers: true,
    gutter: true});
  
  //// Create Firepad (with rich text toolbar and shortcuts enabled).
  var firepad = Firepad.fromCodeMirror(firepadRef, codeMirror, { richTextToolbar: true, richTextShortcuts: true });
  var firepad1 = Firepad.fromCodeMirror(firepadRef1, codeMirror1, { richTextToolbar: true, richTextShortcuts: true });

  //// Initialize contents.
  firepad.on('ready', function() {
    if (firepad.isHistoryEmpty()) {
      firepad.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Write your article here...</span>');
    }
  });
  firepad1.on('ready', function() {
    if (firepad1.isHistoryEmpty()) {
      firepad1.setHtml('<span style="font-size: 20px; font-family: sans-serif; color: #808080;">Write your article here...</span>');
    }
  });

}

// Helper to get hash from end of URL or generate a random one.
function getExampleRef() {
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

function getExampleRef1() {
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
