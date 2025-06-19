console.log('we are building a new button');
let text = prompt('Ehst woul you like to say the button')

let button = document.createElement('button');
button.innerHTML =text;

document.getElementById('button-box').appendChild(button);

const textArea = document.createElement('textarea');
textArea.placeholder= 'This is text area text';
buttonBox.appendChild(textArea);

const inputElement = document.createElement('input');
textArea.placeholder= 'This is text area text';
buttonBox.appendChild(inputElement);