document.addEventListener("DOMContentLoaded", async function () {
    try {
        const response = await fetch("https://your-api.com/services"); // Replace with your API URL
        const services = await response.json();

        const servicesContainer = document.getElementById("services-container"); // Ensure you have a div with this ID
        servicesContainer.innerHTML = "";

        services.forEach(service => {
            const serviceElement = `
                <div class="service-item">
                    <img src="${service.image}" alt="${service.title}">
                    <h3>${service.title}</h3>
                    <p>${service.description}</p>
                </div>
            `;
            servicesContainer.innerHTML += serviceElement;
        });
    } catch (error) {
        console.error("Error fetching services:", error);
    }
});
