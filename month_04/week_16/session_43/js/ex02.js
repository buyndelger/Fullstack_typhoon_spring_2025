let changeButton =document.getElementById('user-info');
changeButton.addEventListener('click', function () {
    let existingUserName= prompt('Give me your name');
    let  name = prompt('What is your name');
    let height = prompt('What is your height ');
    let animal = prompt('What is your favorite animal');
    let userData =localStorage.getItem('welcome');
    if ( userData){
        let user =JSON.parse(userData);
        alert(`Name: {existingUserName}\nHeight: ${user.height}\nanimal${user.favorite}`);

    } else{
        let newUser = {
            name : name,
            height : height,
            animal : animal,
           
        };
        localStorage.setItem(existingUserName, JSON.stringify(newUser));
        alert(`User information saved!`)
    }
 
    if(localStorage.getItem(existingUserName)){
        let user = JSON.parse(localStorage.getItem(existingUserName));
        const welcome= document.getElementById('welcome')
        welcome.innerHTML+="h2>welcome back" +user.name+ "</h2>";
        welcome.innerHTML+="<p2> Your Height is :" +user.height+"</p>"
        welcome.innerHTML+="<p> Your favorite Animal is :" +user ['favorite-animal']+ "</p>" 
        }else{
            let nameOfUser = prompt('what is your name?')
            let heightOfuser = prompt('What is your height')
            let userFavoriteAnimal = prompt('What is your favourite animal?');
    
            let person={
                name : nameOfUser,
                height: heightOfuser,
                'favorite-animal': userFavoriteAnimal
            }
    
            localStorage.setItem(existingUserName, JSON.stringify(person))
        }
});

