const POST_API = 'https://jsonplaceholder.typicode.com/posts';
const postPromise = fetch(POST_API);
const mainElements = document.getElementsByTagName('main')
const searchElement = document.getElementById('search')

postPromise
    .then((response) => {
        const data = response.json();
        console.log(data)
        return data
    })
    .then((data) => {
        for (let i = 0; i < data.length; i++) {
            let div = document.createElement('div')
            div.classList.add('post')
            let idElement = document.createElement('h2')
            idElement.innerHTML = data[i].id
            let titleElement = document.createElement('h1')
            titleElement.innerHTML = data[i].title
            let bodyElement = document.createElement('p')
            bodyElement.innerHTML = data[i].body
            div.appendChild(idElement)
            div.appendChild(titleElement)
            div.appendChild(bodyElement)
            mainElements[0].appendChild(div)
        }
    })

// searchElement.addEventListener('')