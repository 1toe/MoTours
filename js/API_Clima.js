document.addEventListener("DOMContentLoaded", function () {
    const apiKey = "c69107fa1a2b99771c6bc5511da98a97";
    const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";
    const container = document.querySelector(".container-Api");
    const weatherBox = document.querySelector(".weather-box");
    const weatherDetails = document.querySelector(".weather-details");
    const error404 = document.querySelector(".not-found");
    const cityhide = document.querySelector(".city-hide");
    let weatherData = null; // Variable para almacenar los datos del clima
    let timer;

    async function checkWeather(city) {
        const response = await fetch(apiUrl + city + `&appid=${apiKey}`);
        const data = await response.json();

        if (data.cod === '404') {
            cityhide.textContent = city;
            container.style.height = '400px';
            weatherBox.classList.remove('active');
            weatherDetails.classList.remove('active');
            error404.classList.add('active');
            return;
        }

        // Almacena los datos del clima
        weatherData = {
            temperature: Math.round(data.main.temp) + "<span>°C</span>",
            description: data.weather[0].description,
            humidity: data.main.humidity + "%",
            windSpeed: data.wind.speed + " Km/h",
            weatherMain: data.weather[0].main
        };

        // Actualiza la información del clima
        updateWeatherInfo();

        cityhide.textContent = city;
        container.style.height = '555px';
        container.classList.add('active');
        weatherBox.classList.add('active');
        weatherDetails.classList.add('active');
        error404.classList.remove('active');

        // Reiniciamos el temporizador para ocultar la información
        clearTimeout(timer);
    }

    function updateWeatherInfo() {
        document.querySelector(".temp").innerHTML = weatherData.temperature;
        document.querySelector(".description").innerHTML = weatherData.description;
        document.querySelector(".humidity span").innerHTML = weatherData.humidity;
        document.querySelector(".wind span").innerHTML = weatherData.windSpeed;

        const weatherIcon = document.querySelector(".weather-icon");

        // Actualiza el icono del clima
        switch (weatherData.weatherMain) {
            case "Clouds":
                weatherIcon.src = "../image/cloud.png";
                break;
            case "Clear":
                weatherIcon.src = "../image/clear.png";
                break;
            case "Rain":
                weatherIcon.src = "../image/rain.png";
                break;
            case "Mist":
                weatherIcon.src = "../image/mist.png";
                break;
            case "Snow":
                weatherIcon.src = "../image/snow.png";
                break;
            default:
                weatherIcon.src = "";
                break;
        }
    }

    const searchBox = document.querySelector(".search-box input");
    const searchBtn = document.querySelector(".search-box button");

    searchBtn.addEventListener("click", function () {
        const city = searchBox.value.trim();
        if (city === "") {
            container.style.height = '400px';
            weatherBox.classList.remove('active');
            weatherDetails.classList.remove('active');
            error404.classList.add('active');
            return;
        }

        // Oculta la información existente antes de mostrar la nueva
        container.classList.remove('active');
        weatherBox.classList.remove('active');
        weatherDetails.classList.remove('active');
        error404.classList.remove('active');

        // Espera un breve momento antes de realizar la nueva consulta
        setTimeout(() => {
            checkWeather(city);
        }, 0);
    });
});
