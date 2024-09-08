Webcam.set({
  width: 490,
  height: 390,
  image_format: "jpeg",
  jpeg_quality: 90,
});

Webcam.attach("#camera");

function takeSnapshot() {
  Webcam.snap(function (data_uri) {
    document.querySelector(".image-tag").value = data_uri;
    // alert(data_uri);
    document.getElementById("imageForm").submit();
  });
}

Webcam.on("load", function () {
  takeSnapshot();
});
