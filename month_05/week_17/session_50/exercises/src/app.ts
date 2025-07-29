

const input= document.getElementById("passwordInput") as HTMLInputElement;
const button = document.getElementById("toggleButton") as HTMLButtonElement;


button.addEventListener('click',() =>{
    if (input.type === 'password'){
        input.type = 'text'
    }
    else{
        input.type= 'password'
    }
   if(button.innerHTML == 'Харуулах'){
    button.innerHTML ='nuuh'
}
    else{
        button.innerHTML = 'Харуулах'
    }
})