let message: string ='Hello , Typescript '
console.log(message);

//basic types 
// JS: string , number , boolean

let frameWork: string = "Typescript"
let version:  number =5.0;
let isAwesome: boolean = true;

//arrays 
// array ofe numbers
let list: number[] = [1,2,3];

let listBoolen: boolean[]= [true, false ,true];
//alternative generic symtax
let anotherList: Array<number> = [1,2,3]


//string typed listOfString

let listOfString: Array<string> =['HI', "hello"]


enum color{
    red, //0
    green, //1
    blue, //2
}

let c: color =color.green
console.log(c);

//Special types
//ANY type
let notSure: any =4
notSure = "Maybe a String instead";
notSure= false;
console.log(notSure);


//Unknown Type 
let value: unknown= "Hello"
if (typeof value === "string"){
    console.log(value.toUpperCase());
    
}

//union types

let id: string |number;
id = 101;
id ="101-A"
console.log(id);

//type aliases

type StringOrNumber = string | number;
let customerId: StringOrNumber ="C123";
customerId=123;
console.log(customerId);

function mergeArray(one: number[] , two: number[]):Array<number>{
    return one.concat(two)
}


interface User{
    name: string,
    id: number,
    isAdmin?: boolean,
    readonly email: string
}

function createUser(user: User):void{
    console.log(`Creating user${user.name} with eamil ${user.email}`);
    
}

const newUser ={
    name: "Jane Doe",
    id: 1,
    email: "jane@example.com"
}
createUser(newUser);
interface Shape{
    getArea(): number;

}
class Circle implements Shape{
    constructor(public radius: number){}
    getArea(): number {
        return Math.PI *this.radius **2
    }
}
class Animal{
    private name: string ;
    constructor(theName: string){
        this.name=theName;
    }
    public move(distanceInMerets:number):void{
        console.log(`${this.name} moved ${distanceInMeretsm.}`);
        
    }
}

let cat =new Animal("cat")
cat.move(10);
console.log(cat);


function identity<T>(arg: T):T{
    return arg
}

let output1 =identity<String>("myString")
let output2 =identity<number>(100)

