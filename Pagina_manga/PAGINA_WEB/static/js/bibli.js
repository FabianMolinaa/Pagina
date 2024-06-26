const product = [
    {
        id: 0,
        image: "{% static 'img/sousou-no-frieren-banner.png' %}",
        title: 'Sousou no Frieren',
        link: "{% url 'sousou' %}",
    },
    {
        id: 1,
        image: "{% static 'img/black-clover-banner.jpg' %}",
        title: 'Black Clover',
        link: "{% url 'black_clover' %}",
    },
    {
        id: 2,
        image: "{% static 'img/Jujutsu-Kaisen-banner.jpg' %}",
        title: 'Jujutsu Kaisen',
        link: "{% url 'jujutsu_kaisen' %}",
    },
    {
        id: 3,
        image: "{% static 'img/Akuyaku-Reijou-level-99-banner.jpg' %}",
        title: 'Akuyaku Reijō Level 99',
        link: "{% url 'akuyaku' %}",
    },
    {
        id: 4,
        image: "{% static 'img/Yofukashi-no-Uta-banner.jpg' %}",
        title: 'Yofukashi no Uta',
        link: "{% url 'yofukashi' %}",
    },
    {
        id: 5,
        image: "{% static 'img/spyxfamily-banner.jpg' %}",
        title: 'Spy × Family',
        link: "{% url 'spy' %}",
    },
    {
        id: 6,
        image: "{% static 'img/blue-lock-banner.png' %}",
        title: 'Blue Lock',
        link: "{% url 'blue_lock' %}",
    },
    {
        id: 7,
        image: "{%static'img/Chainsaw-Man-banner.jpg'%}",
        title: 'Chainsaw Man',
        link: "{%url'chainsaw_man'%}",
    },
];
document.addEventListener("DOMContentLoaded", function() {
    if (typeof product === 'undefined') {
        console.error('Variable product is not defined');
        return;
    }

    const categories = [...new Set(product.map(item => item))];

    document.getElementById('searchBar').addEventListener('keyup', (e) => {
        const searchData = e.target.value.toLowerCase();
        const filteredData = categories.filter(item => item.title.toLowerCase().includes(searchData));
        displayItem(filteredData);
    });

    const displayItem = (items) => {
        document.getElementById('root').innerHTML = items.map(item => {
            const { image, link, title } = item;
            return `
                <section>   
                    <div class="card">
                        <a href="${link}">
                            <img src="${image}" alt="${title}">
                        </a>
                        <br>
                        <div class="title">
                            <h5>${title}</h5>
                        </div>
                    </div>
                </section>`;
        }).join('');
    };

    displayItem(categories);
});
