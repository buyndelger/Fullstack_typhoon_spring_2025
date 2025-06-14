function welcome() {
    let yourname =prompt('What is your name?');
document.getElementById('welcome').textContent = 'welcome' + yourName + 'to the Javascript'
}
function changeColor() {
    let givenColor = prompt('Give me website background color');
    console.log('givenColor');
    givenColor=
    givenColor === 'black'
    ? prompt ('black is not allowed. Give me different color')
    : givenColor;
    document.getElementById("main-content").style.backgroundColor=givenColor;
    
}

function findTeenage() {
    const age = prompt("Насаа оруулна уу:");
    const ageNum = parseInt(age);

    const message = (ageNum <= 13) ? "You are baby" :
                    (ageNum >= 14 && ageNum <= 19) ? "You are teenager" :
                    (ageNum >= 20 && ageNum <= 65) ? "You are an adult" :
                    (ageNum > 65 && ageNum <= 99) ? "You are a senior" :
                    (ageNum >= 100) ? "You are a dinosaur" :
                    "Буруу утга оруулсан байна.";

    document.getElementById("is-teenager").innerText = message;
  }

  function calculateNaadam(horsePlaces, bukhColor, HowManyWins) {
    let point = 0;
    switch(horsePlaces){
        case 1:
            point +=50;
            break;
        case 2:
            point +=40;
            break;
        case 3:
            point +=30;
            break; 
            
        case 4:
        case 5:
            point +=20;
            break; 
        default:
            console.log('Буруу');
            
    }
  }