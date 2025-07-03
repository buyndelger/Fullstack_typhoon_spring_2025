console.log('Promise JS');

const firstPromise = new Promise((resolved, rejected)=>{
    const isTrue = true;
    if (isTrue) {
        return   resolved('Success');
    } else{
        rejected('Error');
    }
});
console.log(firstPromise);

console.log(new Promise((rej, rec) => {
    
}));

firstPromise
.then((result)=>{
    console.log(result);
    return 'B';
    
}).then((result)=>{
    console.log(result);
    return 'C';
}).then((result)=>{
    console.log(result);
    return 'D';

}).catch((error)=>{
    console.log(error);
    
});

