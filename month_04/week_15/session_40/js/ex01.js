const divElement = document.getElementsByTagName('div');
console.log(divElement);


for (let i = 0; i< divElement.length; i++){
    divElement[i].addEventListener('click', function (element) {
        console.log(element.target);
        element.target.style.background = 'red'
        
        
    })
}