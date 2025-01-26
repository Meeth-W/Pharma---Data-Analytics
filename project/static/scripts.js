document.addEventListener("DOMContentLoaded", () => {
    console.log("Website is ready!");

    const refreshButton = document.getElementById("refresh-stats");

    refreshButton.addEventListener("click", async () => {
        refreshButton.innerText = "Refreshing...";
        refreshButton.disabled = true;

        try {
            const response = await fetch("http://127.0.0.1:8000/api/v1/refresh_stats");
            if (!response.ok) {
                throw new Error("Failed to refresh stats");
            }

            const data = await response.json();
            alert(data.message);

            // Refresh the carousel images
            refreshCarouselImages();
        } catch (error) {
            console.error("Error refreshing stats:", error);
            alert("An error occurred while refreshing stats.");
        } finally {
            refreshButton.innerText = "Refresh Stats";
            refreshButton.disabled = false;
        }
    });

    // Handle Carousel
    const imagesBasePath = "./static/images/carousel/";
    const images = Array.from({ length: 10 }, (_, i) => `image${i + 1}.jpg`);
    const carouselImages = document.querySelector(".carousel-images");
    const carouselSelectors = document.querySelector(".carousel-selectors");
    let currentIndex = 0;

    // Populate carousel images and selectors
    function populateCarousel() {
        carouselImages.innerHTML = ""; // Clear existing images
        carouselSelectors.innerHTML = ""; // Clear existing selectors

        images.forEach((imageName, index) => {
            const img = document.createElement("img");
            img.src = `${imagesBasePath}${imageName}?t=${Date.now()}`; // Add timestamp to invalidate cache
            carouselImages.appendChild(img);

            const button = document.createElement("button");
            button.classList.add("selector-btn");
            if (index === 0) button.classList.add("active");
            button.addEventListener("click", () => goToImage(index));
            carouselSelectors.appendChild(button);
        });

        goToImage(0); // Reset to the first image
    }

    const prevButton = document.querySelector(".carousel-btn.prev");
    const nextButton = document.querySelector(".carousel-btn.next");

    prevButton.addEventListener("click", () => goToImage(currentIndex - 1));
    nextButton.addEventListener("click", () => goToImage(currentIndex + 1));

    function goToImage(index) {
        if (index < 0) index = images.length - 1;
        if (index >= images.length) index = 0;
        carouselImages.style.transform = `translateX(-${index * 100}%)`;
        document.querySelector(".selector-btn.active").classList.remove("active");
        carouselSelectors.children[index].classList.add("active");
        currentIndex = index;
    }

    function refreshCarouselImages() {
        populateCarousel(); // Rebuild the carousel with updated image URLs
    }

    // Initialize carousel
    populateCarousel();
});
