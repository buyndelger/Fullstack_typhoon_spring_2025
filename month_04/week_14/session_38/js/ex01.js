let h4Element = document.createElement('h4');
h4Element.innerHTML = 'Typhooon Class';
const classlist = document.getElementById('class-list')


const myName = document.createElement('li');
myName.innerHTML = "Buyndelger"; 

classlist.lastElementChild.appendChild(myName);

const classWindow = document.getElementById('class-window');

classWindow.insertBefore(h4Element, classlist);