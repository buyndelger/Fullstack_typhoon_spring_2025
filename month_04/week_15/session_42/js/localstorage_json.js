let listOfScores = [10,30,455,80];

console.log('List Without JSON');


localStorage.setItem('scores', listOfScores);
console.log('Values sstored in scores:' +localStorage.scores);
console.log('Data types of local storage listOfScores:' +typeof(localStorage.scores));
console.log('Second index if localStorage listOfScores:' +localStorage.scores[2]);


localStorage.setItem('scores', JSON.stringify(listOfScores));
console.log('With JSON');
console.log('Values stored in scores: ' +localStorage.scores);
console.log('Date type of stringified local storage list of scores:' +typeof(JSON.parse(localStorage.scores)));
console.log('Second index if localStorage listOfScores:' +JSON.parse(localStorage.scores[2]));





