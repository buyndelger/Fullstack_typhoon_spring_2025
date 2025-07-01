let changeButton =document.getElementById('user-info');
let welcome = document.getElementById('welcome')
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
 
});

for (let i =0; i<localStorage.length; i++){
        welcome.innerHTML +=welcome[i];
     
    }
