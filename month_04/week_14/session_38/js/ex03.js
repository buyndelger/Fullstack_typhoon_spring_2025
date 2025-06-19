let colorOne = document.getElementById('color-one');
let colorTwo = document.getElementById('color-two');
let colorThree = document.getElementById('color-three');

let color1 = prompt('Ehnii ongo');
let color2 = prompt('Xoer dah ongo');
let color3 = prompt('Gurav dah ongo');

colorOne.setAttribute('style', `background-color: ${color1};`);
colorTwo.setAttribute('style', `background-color: ${color2};`);
colorThree.setAttribute('style', `background-color: ${color3};`);