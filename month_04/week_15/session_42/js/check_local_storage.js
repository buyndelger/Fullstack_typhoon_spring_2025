document.getElementById('progress-button').addEventListener('click',function () {
    let progressElement = document.getElementById('progress');
    setTimeout(function(){
        progressElement.style.width='300px';
        checkLocal();
    }, 2000);
});







function checkLocal() {
    if(typeof(Storage) !==undefined){
        document.getElementById('local-storage').textContent ='Your browser supports local storage!'
    } else{
        document.getElementById('local-storage').textContent=
        'Your browser does not suppert local storage! try using a new browser for this unit:(';
    }
}