let body =document.getElementsByTagName('body');
let parent = document.createElement('div')

for (var i =0; i<49; i++){
    let div = document.createElement('div');
    if (i%2 ===0){
        div.setAttribute('style' , 'width:60px', 'height:60px' ,'backgroundColor:black');
    } else {
        div.setAttribute('style' , 'width:60px', 'height:60px' ,'backgroundColor:red');
    
    }
    parent.appendChild(div)
}

parent.setAttribute('style', 'display:grid , grid-template-columns:repeat(7, 1fr); grid-template-rows:(7, 1fr); flex-wrap: wrap; width:420px; height:420px',);
body[0].appendChild(parent)

