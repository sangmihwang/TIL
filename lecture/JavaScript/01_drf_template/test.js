const getEventAdd = function() {
    const getBtn = document.querySelector('#get-btn')
    getBtn.addEventListener('click', (event) => {
        const backendURL = 'http://127.0.0.1:8000/api/v1/articles/'
        axios({
            method: 'GET',
            // method: 'POST',
            url: backendURL,
            params: {content: 'test'}
            // data: {
            //     title: 'test',
            //     content: 'test',
            // }
        }).then((response) => {
            console.log('response =', response.data)
            const articles=  response.data
            const ulElement = document.querySelector('#article-list')
            articles.forEach((article) => {
                // create 하기 전에 있는거면 pass, 없는거면 생성
                if (!document.querySelector(`#article-${article.id}`)) {

                    const liElement = document.createElement('li')
                    liElement.textContent = `${article.id} - ${article.content}`
                    // liElement 하나하나에 id 지정
                    liElement.id = `article-${article.id}`

                    ulElement.appendChild(liElement)

                    const deleteBtn = document.createElement('button')
                    deleteBtn.textContent = '삭제'
                    deleteBtn.addEventListener('click', (event) => {
                        liElement.remove()
                    })
                    liElement.appendChild(deleteBtn)
                }   
            }).catch((error) => {
                console.log('error =', error)
            })
        })
    })
}