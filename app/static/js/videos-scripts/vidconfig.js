//seta as configurações do vídeo
/*
outro método a ser explorado, mas o tamanho constante fica mais fácil de encaixar na tela
a = video.src({type: 'video/mp4', src: 'video/MY_VIDEO.mp4'});
vheight = a.height
vwidth =a.width
*/
var video = videojs('video', {
    preload : "auto",
    width : "640",
    height : "264",
    poster : "thumbnail/MY_VIDEO_POSTER.jpg"
    });

// função para fazer o vídeo começar com 50% do volume
video.ready(function() {
      var howLoudIsIt = video.volume();
      video.volume(0.5);
    });

