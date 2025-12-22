'use strict';

//Opening or closing side bar

const elementToggleFunc = function (elem) { elem.classList.toggle("active"); }

const sidebar = document.querySelector("[data-sidebar]");
const sidebarBtn = document.querySelector("[data-sidebar-btn]");

sidebarBtn.addEventListener("click", function() {
    elementToggleFunc(sidebar);

    const iconElement = this.querySelector("i.fas");

    if (iconElement) {
        const isDown = iconElement.classList.contains("fa-chevron-down");

        if (isDown) {
            iconElement.classList.replace("fa-chevron-down", "fa-chevron-up");
        } else {
            iconElement.classList.replace("fa-chevron-up", "fa-chevron-down");
        }
    }
})

//Activating Modal-testimonial

const testimonialsItem = document.querySelectorAll('[data-testimonials-item]');
const modalContainer = document.querySelector('[data-modal-container]');
const modalCloseBtn = document.querySelector('[data-modal-close-btn]');
const overlay = document.querySelector('[data-overlay]');

const modalImg = document.querySelector('[data-modal-img]');
const modalTitle = document.querySelector('[data-modal-title]');
const modalText = document.querySelector('[data-modal-text]');
const modalDate = document.querySelector('[data-modal-date]');

// Create PDF button - ONLY ONCE
const pdfButton = document.createElement('button');
pdfButton.className = 'pdf-button';
pdfButton.innerHTML = '<i class="fas fa-file-pdf"></i> View PDF Version';

// Add button to modal container
const pdfButtonContainer = document.querySelector('.pdf-button-container');
if (pdfButtonContainer) {
    pdfButtonContainer.appendChild(pdfButton);
    pdfButton.style.display = 'none'; // Hide by default
}

const testimonialsModalFunc = function () {
    modalContainer.classList.toggle('active');
    overlay.classList.toggle('active');

    // Hide PDF button when closing modal
    if (!modalContainer.classList.contains('active')) {
        pdfButton.style.display = 'none';
    }
}

for (let i = 0; i < testimonialsItem.length; i++) {
    testimonialsItem[i].addEventListener('click', function () {
        modalImg.src = this.querySelector('[data-testimonials-avatar]').src;
        modalImg.alt = this.querySelector('[data-testimonials-avatar]').alt;
        modalTitle.innerHTML = this.querySelector('[data-testimonials-title]').innerHTML;
        modalText.innerHTML = this.querySelector('[data-testimonials-text]').innerHTML;

        // Get the date from the parent testimonial item's data attribute
        const testimonialDate = this.closest('.testimonials-item').getAttribute('data-testimonial-date');

        if (testimonialDate && modalDate) {
            const date = new Date(testimonialDate);
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            modalDate.innerHTML = date.toLocaleDateString('en-US', options);
            modalDate.setAttribute('datetime', testimonialDate);
        }

        // Check if this testimonial has a PDF
        const pdfUrl = this.closest('.testimonials-item').getAttribute('data-pdf-url');

        if (pdfUrl) {
            // Show and configure PDF button
            pdfButton.style.display = 'flex';

            // Update the onclick handler for the current testimonial
            pdfButton.onclick = function(e) {
                e.preventDefault();
                window.open(pdfUrl, '_blank');
            };
        } else {
            pdfButton.style.display = 'none';
        }

        testimonialsModalFunc();
    });
}

//Activating close button in modal-testimonial

modalCloseBtn.addEventListener('click', testimonialsModalFunc);
overlay.addEventListener('click', testimonialsModalFunc);

//Activating Filter Select and filtering options

const select = document.querySelector('[data-select]');
const selectItems = document.querySelectorAll('[data-select-item]');
const selectValue = document.querySelector('[data-select-value]');
const filterBtn = document.querySelectorAll('[data-filter-btn]');

select.addEventListener('click', function () {elementToggleFunc(this); });

for(let i = 0; i < selectItems.length; i++) {
    selectItems[i].addEventListener('click', function() {

        let selectedValue = this.innerText.toLowerCase();
        selectValue.innerText = this.innerText;
        elementToggleFunc(select);
        filterFunc(selectedValue);

    });
}

const filterItems = document.querySelectorAll('[data-filter-item]');

const filterFunc = function (selectedValue) {
    for(let i = 0; i < filterItems.length; i++) {
        if(selectedValue == "all") {
            filterItems[i].classList.add('active');
        } else if (selectedValue == filterItems[i].dataset.category) {
            filterItems[i].classList.add('active');
        } else {
            filterItems[i].classList.remove('active');
        }
    }
}

//Enabling filter button for larger screens 

let lastClickedBtn = filterBtn[0];

for (let i = 0; i < filterBtn.length; i++) {
    
    filterBtn[i].addEventListener('click', function() {

        let selectedValue = this.innerText.toLowerCase();
        selectValue.innerText = this.innerText;
        filterFunc(selectedValue);

        lastClickedBtn.classList.remove('active');
        this.classList.add('active');
        lastClickedBtn = this;

    })
}

// Zoom functionality for portfolio images
const zoomModal = document.getElementById('zoomModal');
const zoomedImage = document.getElementById('zoomedImage');
const closeZoomModal = document.querySelector('.close-zoom-modal');
const zoomButtons = document.querySelectorAll('[data-zoom-btn]');
const projectImages = document.querySelectorAll('[data-project-img]');

// Function to open zoom modal
const openZoomModal = function (imageSrc, imageAlt) {
    zoomedImage.src = imageSrc;
    zoomedImage.alt = imageAlt;
    zoomModal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent scrolling
};

// Function to close zoom modal
const closeZoomModalFunc = function () {
    zoomModal.style.display = 'none';
    document.body.style.overflow = 'auto'; // Restore scrolling
};

// Add click event to each zoom button
zoomButtons.forEach((zoomBtn, index) => {
    zoomBtn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation(); // Prevent triggering the parent link

        const projectImg = projectImages[index];
        const imgSrc = projectImg.src;
        const imgAlt = projectImg.alt;

        openZoomModal(imgSrc, imgAlt);
    });
});

// Also allow clicking on the image itself to zoom (optional)
projectImages.forEach((projectImg, index) => {
    projectImg.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation(); // Prevent triggering the parent link

        const imgSrc = this.src;
        const imgAlt = this.alt;

        openZoomModal(imgSrc, imgAlt);
    });
});

// Close modal when clicking the X
closeZoomModal.addEventListener('click', closeZoomModalFunc);

// Close modal when clicking outside the image
zoomModal.addEventListener('click', function (e) {
    if (e.target === zoomModal) {
        closeZoomModalFunc();
    }
});

// Close modal with ESC key
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && zoomModal.style.display === 'block') {
        closeZoomModalFunc();
    }
});

// Enabling Contact Form

const form = document.querySelector('[data-form]');
const formInputs = document.querySelectorAll('[data-form-input]');
const formBtn = document.querySelector('[data-form-btn]');

for(let i = 0; i < formInputs.length; i++) {
    formInputs[i].addEventListener('input', function () {
        if(form.checkValidity()) {
            formBtn.removeAttribute('disabled');
        } else { 
            formBtn.setAttribute('disabled', '');
        }
    })
}

// Enabling Page Navigation 

const navigationLinks = document.querySelectorAll('[data-nav-link]');
const pages = document.querySelectorAll('[data-page]');

for(let i = 0; i < navigationLinks.length; i++) {
    navigationLinks[i].addEventListener('click', function() {
        
        for(let i = 0; i < pages.length; i++) {
            if(this.innerHTML.toLowerCase() == pages[i].dataset.page) {
                pages[i].classList.add('active');
                navigationLinks[i].classList.add('active');
                window.scrollTo(0, 0);
            } else {
                pages[i].classList.remove('active');
                navigationLinks[i]. classList.remove('active');
            }
        }
    });
}