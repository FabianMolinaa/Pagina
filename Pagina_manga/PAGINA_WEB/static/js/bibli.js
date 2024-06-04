const product = [
    {
        id: 0,
        image: '../static/img/sousou-no-frieren-banner.png',
        title: 'Sousou no Frieren',
        link: 'vista/sousou-no-frieren.html',
    },
    {
        id: 1,
        image: '../static/img/black-clover-banner.jpg',
        title: 'Black Clover',
        link: 'vista/black-clover.html',
    },
    {
        id: 2,
        image: '../static/img/Jujutsu-Kaisen-banner.jpg',
        title: 'Jujutsu Kaisen',
        link: 'vista/jujutsu-kaisen.html',
    },
    {
        id: 3,
        image: '../static/img/Akuyaku-Reijou-level-99-banner.jpg',
        title: 'Akuyaku Reijō Level 99',
        link: 'vista/Akuyaku-Reijou.html',
    },
    {
        id: 4,
        image: '../static/img/Yofukashi-no-Uta-banner.jpg',
        title: 'Yofukashi no Uta',
        link: 'vista/yofukashi.html',
    },
    {
        id: 5,
        image: '../static/img/spyxfamily-banner.jpg',
        title: 'Spy × Family',
        link: 'vista/spyxfamily.html',
    },
    {
        id: 6,
        image: '../static/img/blue-lock-banner.png',
        title: 'Blue Lock',
        link: 'vista/blue_lock.html',
    },
    {
        id: 7,
        image: '../static/img/tokyo-revengers-banner.png',
        title: 'Tokyo Revengers',
        link: 'vista/tokyo-revengers.html',
    },
    {
        id: 8,
        image: '../static/img/Chainsaw-Man-banner.jpg',
        title: 'Chainsaw Man',
        link: 'vista/chainsaw-man.html',
    },
    ];
    const categories = [...new Set(product.map((item) => { return item }))]
    
    
    document.getElementById('searchBar').addEventListener('keyup', (e) => {
        const searchData = e.target.value.toLowerCase();
        const filteredData = categories.filter((item) => {
            return (
                item.title.toLowerCase().includes(searchData)
            )
        })
        displayItem(filteredData)
    });
    
    const displayItem = (items) => {
        document.getElementById('root').innerHTML = items.map((item) => {
            var { image,link ,title, } = item;
            return (
               
                `<section>   
                    <div class="card">
                        <a href=${link}>
                            <img src=${image} 
                            alt="...">
                        </a>
                        <br>
                        <div class="title">
                            <h5>${title} </h5>
                            
                        </div>
                    </div>
                </section>`
            )
        }).join('')
    };
    displayItem(categories);
