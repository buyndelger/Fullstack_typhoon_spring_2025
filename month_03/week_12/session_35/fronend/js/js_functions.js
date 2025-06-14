console.log("Session 35");

// function declaration
function printMyName() {
  console.log("Buyndelger");
}

// function call
printMyName();

// function with parameters

function printAnyName(firstName) {
  console.log("My name is : " + firstName);
}

printAnyName("Buyanaa");

function printFullName(firstName, lastName) {
  console.log("My name is: " + firstName + " " + lastName);
}

printFullName("Boldbaatar", "Buyndelger");

/// function with default parameters

function calculateSquareArea(width, height = 16) {
  console.log("Square Area is : " + width * height);
}

calculateSquareArea(8, 20); // 160
calculateSquareArea(8); // 128;

// function return
function myFunction(a, b) {
  return a * b;
}

console.log(myFunction(10, 10)); // 100

function addTwoNumbers(a, b) {
  return a + b;
}

console.log(addTwoNumbers(10, 15)); // 25

// function expression - anonymous function
let calculateCircleArea = function (radius) {
  return 2 * 3.14 * radius;
};
console.log(calculateCircleArea(10.5));

// exercises
// a, b, c гэдэг параметр авдаг anonymous function бичээд нэг хувьсагчид хадгалаарай.
// Тэгээд энэ 3-ийн дунджийг нь олоод буцаадаг болгоорой. Функцээ дуудаж утгууд өгч тестлээрэй.

let average = function (a, b, c) {
  return (a + b + c) / 3;
};

console.log(average(4, 5, 6)); // 5

// this does not work
// fahrenheitToCelcius(100); this rule is against hoisting of javascript
// function expression = arrow function
let fahrenheitToCelcius = (fahrenheit) => {
  return ((32 - fahrenheit) * 5) / 9;
};

console.log(fahrenheitToCelcius(212)); //

// function declaration VS function expression
console.log(funcExpression());
// function declaration
function funcExpression() {
  return 1;
}
console.log(funcExpression());

/// function expression

/// hoisting javascript
let a = 1;
console.log(a);

(function callMe() {
  console.log("called my self");
})();

// global scoped variable
let global = "Global Variable";

function readGlobal() {
  console.log(global);
}
readGlobal(); // Global Variable
console.log(global); // Global Variable

// local scoped variable
function readLocal() {
  let local = "Local Variable";
  console.log(local);
}

readLocal();
// Local Variable

// console.log(local); // it will throw an error
// example 01
(function () {
  let str = "42";
  let num = parseInt(str);
  console.log(num + 8); 
  console.log(parseInt("42nd Street")); 
})();
// example 02
(function () {
  let str = "42.5656";
  let num = parseInt(str);
  console.log(num + 8); 
})();

// example 03
(function () {
  let num = 42;
  let str = num.toString();
  console.log(str); 
})();

// js operations comparison operations
(function () {
  console.log("2" == 2); 
  console.log("2" === 2); 
})();

// js logical operators
(function () {
  // AND
  let resultAND = true && true; 
  console.log(resultAND);
  let resultAND2 = true && false; 
  console.log(resultAND2);

  // OR
  let resultOR = true || false; 
  console.log(resultOR);
  let resultOR2 = false || false; 
  console.log(resultOR2);
  // NOT
  let resultNOT = !true; 
  console.log(resultNOT);
})();

(function () {
  let a = 5;
  let result = ~a; 
  console.log(~5); 
})();


