"use strict";
let message = 'Hello , Typescript ';
console.log(message);
//basic types 
// JS: string , number , boolean
let frameWork = "Typescript";
let version = 5.0;
let isAwesome = true;
//arrays 
// array ofe numbers
let list = [1, 2, 3];
let listBoolen = [true, false, true];
//alternative generic symtax
let anotherList = [1, 2, 3];
//string typed listOfString
let listOfString = ['HI', "hello"];
var color;
(function (color) {
    color[color["red"] = 0] = "red";
    color[color["green"] = 1] = "green";
    color[color["blue"] = 2] = "blue";
})(color || (color = {}));
let c = color.green;
console.log(c);
//Special types
//ANY type
let notSure = 4;
notSure = "Maybe a String instead";
notSure = false;
console.log(notSure);
//Unknown Type 
let value = "Hello";
if (typeof value === "string") {
    console.log(value.toUpperCase());
}
//union types
let id;
id = 101;
id = "101-A";
console.log(id);
let customerId = "C123";
customerId = 123;
console.log(customerId);
function mergeArray(one, two) {
    return one.concat(two);
}
function createUser(user) {
    console.log(`Creating user${user.name} with eamil ${user.email}`);
}
const newUser = {
    name: "Jane Doe",
    id: 1,
    email: "jane@example.com"
};
createUser(newUser);
class Circle {
    constructor(radius) {
        this.radius = radius;
    }
    getArea() {
        return Math.PI * this.radius ** 2;
    }
}


//classes

