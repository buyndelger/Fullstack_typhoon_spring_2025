let paragraphs = document.getElementById('paragraphs');

console.log(`the first element of paraphs is: ${paragraphs.firstElementChild.innerHTML}`);

console.log(`the last element of paragraphs: ${paragraphs.lastElementChild.innerHTML}`);

console.log(`the last element of paragraphs: ${paragraphs.parentElement.id}`);

let childParagraphs = paragraphs.children;
console.log(childParagraphs);


for (let i = 0; i < childParagraphs.length; i++){
    console.log(`${i+1}: ${childParagraphs[i].innerHTML}`);
    
}
