/*Caso a descrição do vídeo seja muito grande, a ponto de sair do card, oculta-se ela, substuindo-a por "..." */

var video_descricao = document.querySelectorAll(".video-descricao_resumo") 
    //Seleciona todas descrições de vídeo da página.

video_descricao.forEach((e, index) => { 
    if (video_descricao[index].innerHTML.length >= 150) {
        video_descricao[index].innerHTML = video_descricao[index].innerHTML.substring(0, 150) + "..."
    }
    //para cada video_descricao, verifica-se se o seu conteúdo tem um length (número de caracteres) maior ou igual a 50. Se sim, o inner html desse elemento será um substring dos 50 primeiros caractere concatenado com "..."
})