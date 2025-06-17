let PI =3.14;
console.log(PI);


PI =3.45;
console.log(PI);

const SPEED_OF_LIGHT = 299_792_458;
console.log(SPEED_OF_LIGHT);

const COLORS = [ 'yellow', 'red', 'green', 'purple', 'black'];

for (let i = 0; i<5; i++){
    console.log(`Color t index: ${i}= ${COLORS[i]}`);
    
}
for(let i=0; i<COLORS.length; i++){
    document.writeln(`<div style="background: ${COLORS[i]});
        height: 20px;  widht:30px;
        "></div>`);
}

