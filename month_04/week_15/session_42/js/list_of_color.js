document.getElementById('change-background').addEventListener('click', function () {
    let color = prompt(
      `What color would you like to change your background color the next time you visit the site?"):`
    );

    if (localStorage.backgroundList) {
        let colorList = JSON.parse(localStorage.backgroundList);
        colorList.push(color);
        console.log(colorList);
        
        localStorage.getItem('backgroundList',JSON.stringify(colorList))
    } else {
      let list = [color];
      localStorage.getItem('backgroundList', JSON.stringify(list) );
    }
});
let lastThree = document.getElementById('last-three')
let colorList = JSON.parse(localStorage.backgroundList);
let body =document.getElementsByTagName('body')
body[0].style.backgroundColor=colorList[colorList.length -1]
if(colorList.length >=3){
    for (let i =colorList.length -1; i>colorList.length-4; i--){
    lastThree.innerHTML+= colorList[i]
    } 
}
