$.ajax({
  type: "POST",
  url: "http://ec2-35-160-139-230.us-west-2.compute.amazonaws.com/simplex",
  data: formData,
  success: function(){},
  dataType: "json",
  contentType : "application/json"
});
function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "ajax_info.txt", true);
  xhttp.send();
}










function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "http://ec2-35-160-139-230.us-west-2.compute.amazonaws.com/", true);
  xhttp.send();
}
