let firstName = 'buyndelger';
let lastName = 'boldbaatar';
let age =21;

//soliton js object


let khangai={
    firstName : "Khangaikhuu",
    lastName : "UvgunKhuu",
    age: 43,
    'favoirte-animal': 'dog'
}


let buynaa={
    firstName : "buynaa",
    lastName : 'boldbaatar',
    age: 22
}

console.log(khangai);
console.log(buynaa);

//object with arrays
let dog={
    name: 'banhar',
    age: 3,
    activities : ['Bell', 'Eat', 'Sleep', 'Play a Ball'],
    race:{
        orgin: "Tibet",
        name: "Bibetain Dog"
    }
}

console.log(dog);


//accessing object property
//dot notation
console.log(buynaa.age);
console.log(buynaa.firstName);
console.log(buynaa.lastName);


//bracket notation
console.log(khangai['firstName']);
console.log(khangai['age']);
console.log(khangai['lastName']);
console.log(khangai["favoirte-animal"]);


//change object property
khangai.age =44;
buynaa.age= 23;
dog['age']= 4;
console.log(khangai);
console.log(buynaa);
console.log(dog);

//adding property

buynaa['favorite-animal']='Cat';
console.log(buynaa);



console.log(dog.race.orgin);

console.log(dog.activities[1]);

for (let i = 0; i< dog.activities.length; i++) {
    console.log(dog.activities[i]);
    // console.log(dog[0.3]);
    
}
