const books = ['Tunalag Tamir', 'Dulguum Don', 'Harry Potter'];

const mainElement = document.getElementsByTagName('main');
console.log(mainElement);

for (let i =0; i <books.length; i++ ){
    const pElement = document.createElement(`p`)
    pElement.textContent= books[i];
    mainElement[0].appendChild(pElement);
}
