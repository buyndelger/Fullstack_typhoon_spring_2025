console.log(window);
window.addEventListener(`DOMContentLoaded`, function(){
    let savedColor = localStorage.getItem('background-color');
    if (savedColor){
        this.document.body.style.backgroundColor =savedColor;
    }

    const changeColorButton = this.document.getElementById('change-background');
    changeColorButton.addEventListener('click',function(){
        let newColor = prompt("Enter a color name or hex code ( e.g., blue, #ff0000");
        if(newColor){
            this.localStorage.setItem('background-color', newColor)
        }
    
    
    
    
    
    });
})
