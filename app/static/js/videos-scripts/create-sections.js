//Esse script faz cria uma nova seção para guardar os vídeos, caso eles ultrapassem a tela, cria-se uma nova div para armazenar eles. Enfim, não precisa entender esse código e eu só fiz porque eu já tinha ele pronto, então foi bem deboa para implementá-lo aqui.


var sectionInicial = document.getElementById("row-0")
    //Essa é section inicial, onde será renderizada por padrão.   
var videosContainer = document.querySelector(".container")
var videosIniciais = document.querySelectorAll(".video-link-0");

//-> Fabrica de sections:
var indicator = 0
    //indicator é uma variável apenas para nomear uma id variável à section, para que cada section criada tenha um id diferente.
function section_factory(section, users) {
    //Função para criar sections, se o número de filhos dela for maior que 6
    //a cada chamada de função, users será a user_box, mas cada section com seus próprios user_box.
    indicator = indicator + 1;

    if (section.childElementCount > 9) {
       //childElementCoount retorna quantos filhos um elemento tem
       //Se section tiver mais de 6 filhos, executa-se a criação de uma nova section?:
       var new_sec = document.createElement("div");
       new_sec.setAttribute("id", "row-"+indicator.toString());
       new_sec.setAttribute("class", "row");
       new_sec.style.display="none";
       videosContainer.append(new_sec)
          //pode padrão essa section deverá estar com display: none.

       for (let i=0; i < users.length; i++) {
           if (i > 8) {
               users[i].setAttribute("class", "video-link-"+indicator.toString())
               users[i].classList.add("video-link")
               new_sec.append(users[i])
           }
           //para cada user_box que saia da section inicial, ou seja, seu pai já "excedeu" o limite de filhos, essa user_box será colocada na nova section. Lembrando que é 5, por que o indice começa no 0.
       }
    } else {
        return 
          //Se a section não tiver mais de 6 elementos filhos, para execução do código.
    }

    var new_boxUsers = document.querySelectorAll(".video-link-"+indicator.toString())
    section_factory(new_sec, new_boxUsers)
       //Executa-se a função novamente, com a new_section como parâmetro. Se essa nova section tiver mais de 6 elementos, mais uma vez essa função será executado. Caso contrário, isto é, se cair no else, não se executa mais a função.
}

//-> Navegação entre as sections:
var sectionAtualID = sectionInicial.id;
    //Com a sectionAtualID, temos a página que o usuário está. Por padrão, ela é o id da página inicial.
function change_userSection (btn) {
    let sections = document.querySelectorAll(".row");
    var num_sectionAtualID = parseInt(sectionAtualID.split("-")[1]);
       //num_section recebe apenas o número do id da section.

    if (btn == 'next') {
        if(num_sectionAtualID < (sections.length-1)) {
           //condição para que o usuário não consiga fazer o next, quando não se tem mais sections para ir (sections.length-1 porque fiz com que a section começasse a partir do 0)
           num_sectionAtualID += 1;
            //passa para próxima section
        }
    } else if (btn == "prev") {
        if (num_sectionAtualID > 0) {
           //aqui basta verificar se o usuário está numa section com ID maior que 0, já que as sections começam no zero, não tem nenhum anterior.
           num_sectionAtualID -= 1; 
            //volta para a section anterior.
        }
    }

    sectionAtualID = "row-"+num_sectionAtualID.toString()
       //sectionAtualID será uma nova ID, contendo para qual página o usuário está indo (a próxima ou a anterior)
    display_section(sectionAtualID)
}

function display_section(sectionAtualID) {
    //essa função faz com que a section para qual o usuário está indo aparecer, enquanto a anterior é setada com display="none"
    let sections = document.querySelectorAll(".row");
    for (let i=0; i < sections.length; i++) {
        if (sections[i].id == sectionAtualID) {
            sections[i].style.display = "flex"
        }
        else {
            sections[i].style.display = "none"
        }
    }
}

document.addEventListener("load", section_factory(sectionInicial, videosIniciais)) 
   //section_factory recebe a section inicial por padrão.