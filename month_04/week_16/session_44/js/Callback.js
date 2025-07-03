// console.log('callback functions');
function funcA() {
    setTimeout(()=>{
        console.log('A');
        
    },1000);
}

function funcB() {
    setTimeout(()=>{
        console.log('B');
        
    },2000);
}
function funcC() {
    setTimeout(()=>{
        console.log('C');
        
    },3000);
}
funcB();
funcA();
funcC();
//fuunction dependent on function
function funcA1() {
    setTimeout(() => {
        console.log('A1');
        
    }, 1000);
}

//callback function fuction-d parametraar ogson teriig argiig xeldeg
function funcA2(funcA1) {
    setTimeout(() => {
        funcA1();
        console.log('A2');
        
    }, 2000);
}

function funcA3(funcA2) {
    setTimeout(() => {
        funcA2(funcA1);
        console.log('A3');
        
    }, 3000);
}

funcA3(funcA2);

const button = document.getElementById('click-me')
button.addEventListener('click', buttonClicked);

function buttonClicked() {
    console.log('button is clicked');
    
}
