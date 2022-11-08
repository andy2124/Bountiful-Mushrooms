function getData(){

    axios({
        method: 'get',
        url: `/api/mushrooms/`
    }).then((response) => { // then a promise to get it back after waiting
        console.log(response.data, 'response data')
    
      }) 
}
getData()