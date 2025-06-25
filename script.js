function takePhoto() {
  const shutterSound = document.getElementById('shutterSound');
  shutterSound.currentTime = 0; // 最初から再生できるようにリセット
  shutterSound.play();

  const canvas = document.createElement('canvas');
  canvas.width = videoElement.videoWidth;
  canvas.height = videoElement.videoHeight;

  const context = canvas.getContext('2d');
  context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

  const dataURL = canvas.toDataURL('image/png');
  console.log("写真撮影成功:", dataURL);
}
