let numberOfVisits= localStorage.getItem('visits');

if (numberOfVisits == null){
    numberOfVisits =0;
}else {
    numberOfVisits=parseInt(numberOfVisits, 10);
}


let visits = document.getElementById('visits');
visits.innerHTML = numberOfVisits;




console.log(numberOfVisits);
numberOfVisits++;

localStorage.setItem('visits', numberOfVisits);

//student

let student = localStorage.getItem('student');
if(student == null){
    student = 'Khangai'
} else{
    student =student;
}
localStorage.setItem('student', student);

//show student name to the Dom on the HTML
let studentE =document.getElementById('student')
studentE.innerHTML = student;


//animal -dog

let animal = localStorage.getItem('animal');
if(animal == null){
    animal = 'Dog'
} else{
    animal=animal;
}
localStorage.setItem('animal', animal);
let animalE =document.getElementById('animal')
animalE.innerHTML = animal;


//hobbies - football, basketball
let hobbies = localStorage.getItem('hobbies');
if(hobbies == null){
    hobbies = 'Game'
} else{
    hobbies=hobbies;
}
localStorage.setItem('hobbies', hobbies);
let hobbiesE =document.getElementById('hobbies')
hobbiesE.innerHTML = hobbies;

// activities -swmming laudry
let activities = localStorage.getItem('activities');
if(activities == null){
    activities = 'riding'
} else{
    activities= activities;
}
localStorage.setItem(' activities',  activities);
let  activitiesE =document.getElementById(' activities')
activities.innerHTML =  activities;

