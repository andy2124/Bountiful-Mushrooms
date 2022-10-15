const mushroomData = document.getElementById('mushroom-data')// targeting id with the name of mushroom-data on index.html

function getData(){
    
    console.log('testing')
    axios({
        method: 'get',
        url: `https://mushroomobserver.org/api2/observations?detail=high`
    }).then((response) => { // then a promise to get it back after waiting
        console.log(response.data, 'response data')
        renderMushroomData(response)
    
      })  //  add CDN to be able to use this <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

}
function renderMushroomData(response){
    console.log(response, 'total response object')
    console.log(response.data.results, 'response data results')
    const ul = document.createElement('ul') // creates ul in js to index.html. creating ul element 
    mushroomData.appendChild(ul) // the indent of musroomdata div
    for(let x of response.data.results){
        const li = document.createElement('li')
        const image = document.createElement('img')
        image.src =  x.primary_image.original_url
        console.log(li) 
        console.log(image.src)
        li.innerHTML = `
            <h1>${x.date}</h1> <img src='${image.src}' height=100px/> <h1>${x.location.name}</h1>
            <h1>${x.location.latitude_north}</h1>
            <h1>${x.location.latitude_south}</h1>
            <h1>${x.location.longitude_east}</h1>
            <h1>${x.location.longitude_west}</h1>
            <h1>${x.namings[0].name.name}</h1>
            `
        // li.textContent = x.date   // textContent is the info between the closing and opening brackets which will be the date
        // li.textContent = x.consensus.name   // textContent is the info between the closing and opening brackets which will be the date
      console.log(x)
        
        ul.appendChild(li) // li is the grandchild of the div
    }
    
}
getData()