console.log('Pokemon api');


const POKEMON_URL = 'https://pokeapi.co/api/v2/pokemon';
fetch(POKEMON_URL)
.then((response)=> response.json())
.then((data)=>{
    const pokemons =data.results;
    console.log(pokemons);
    const mainElement = mainElement[0];
    const ulElement =document.createElement('ul');
    for (let i = 0; i< pokemons.length; i++) {
        const pokemonDeatilContainer =document.createElement("div")
        pokemonDeatilContainer.classList.add('pokemon-detail-container')
      console.log(pokemons);
      const liElement =document.createElement('li')
      liElement.textContent= pokemons[i].name
      ulElement.appendChild(liElement) 
      const Pokemon_Detail_Url =pokemons[i].url
      fetch(Pokemon_Detail_Url)
      .then((response)=>response.json())
      .then((data)=>{
        console.log(data);
        const pokemonImageUrl =data.spites.other['official-artwork'].front_default;
        const imgElement = document.createElement('img')
        imgElement.src+pokemonImageUrl;
        pokemonDeatilContainer.appendChild(imgElement)
        
      })  
    }
    mainElement.appendChild(ulElement)
}).catch((error)=>{
    console.log(error);
    
})
