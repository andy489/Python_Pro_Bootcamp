'use strict';

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('=== PORTFOLIO SCRIPT INITIALIZATION ===');

    // Initialize all functionality
    initializeSidebar();
    initializeTestimonials();
    initializePortfolio();
    initializeZoomModal();
    initializeFormValidation();
    initializeCertModal();

    console.log('=== ALL COMPONENTS INITIALIZED ===');
});

// Sidebar toggle
function initializeSidebar() {
    const sidebar = document.querySelector("[data-sidebar]");
    const sidebarBtn = document.querySelector("[data-sidebar-btn]");

    if (sidebarBtn && sidebar) {
        sidebarBtn.addEventListener("click", function() {
            sidebar.classList.toggle("active");

            const iconElement = this.querySelector("i.fas");
            if (iconElement) {
                if (iconElement.classList.contains("fa-chevron-down")) {
                    iconElement.classList.replace("fa-chevron-down", "fa-chevron-up");
                } else {
                    iconElement.classList.replace("fa-chevron-up", "fa-chevron-down");
                }
            }
        });
    }
}

// Testimonials modal (keep your existing function)
function initializeTestimonials() {
    const testimonialsItem = document.querySelectorAll('[data-testimonials-item]');
    const modalContainer = document.querySelector('[data-modal-container]');
    const modalCloseBtn = document.querySelector('[data-modal-close-btn]');
    const overlay = document.querySelector('[data-overlay]');
    const modalImg = document.querySelector('[data-modal-img]');
    const modalTitle = document.querySelector('[data-modal-title]');
    const modalText = document.querySelector('[data-modal-text]');
    const modalDate = document.querySelector('[data-modal-date]');

    if (!testimonialsItem.length || !modalContainer) return;

    for (let i = 0; i < testimonialsItem.length; i++) {
        testimonialsItem[i].addEventListener('click', function () {
            if (modalImg && modalTitle && modalText) {
                modalImg.src = this.querySelector('[data-testimonials-avatar]').src;
                modalImg.alt = this.querySelector('[data-testimonials-avatar]').alt;
                modalTitle.innerHTML = this.querySelector('[data-testimonials-title]').innerHTML;
                modalText.innerHTML = this.querySelector('[data-testimonials-text]').innerHTML;
            }

            const testimonialDate = this.closest('.testimonials-item').getAttribute('data-testimonial-date');
            if (testimonialDate && modalDate) {
                const date = new Date(testimonialDate);
                const options = { year: 'numeric', month: 'long', day: 'numeric' };
                modalDate.innerHTML = date.toLocaleDateString('en-US', options);
                modalDate.setAttribute('datetime', testimonialDate);
            }

            testimonialsModalFunc();
        });
    }

    const testimonialsModalFunc = function () {
        modalContainer.classList.toggle('active');
        overlay.classList.toggle('active');
    };

    if (modalCloseBtn) {
        modalCloseBtn.addEventListener('click', testimonialsModalFunc);
    }

    if (overlay) {
        overlay.addEventListener('click', testimonialsModalFunc);
    }
}

// Portfolio filtering (keep your existing function)
function initializePortfolio() {
    const select = document.querySelector('[data-select]');
    const selectItems = document.querySelectorAll('[data-select-item]');
    const selectValue = document.querySelector('[data-select-value]');
    const filterBtn = document.querySelectorAll('[data-filter-btn]');

    if (!select) return;

    select.addEventListener('click', function () {
        this.classList.toggle("active");
    });

    for(let i = 0; i < selectItems.length; i++) {
        selectItems[i].addEventListener('click', function() {
            let selectedValue = this.innerText.toLowerCase();
            selectValue.innerText = this.innerText;
            select.classList.remove("active");
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

    let lastClickedBtn = filterBtn[0];

    for (let i = 0; i < filterBtn.length; i++) {
        filterBtn[i].addEventListener('click', function() {
            let selectedValue = this.innerText.toLowerCase();
            selectValue.innerText = this.innerText;
            filterFunc(selectedValue);

            lastClickedBtn.classList.remove('active');
            this.classList.add('active');
            lastClickedBtn = this;
        });
    }
}

// Image zoom functionality (keep your existing function)
function initializeZoomModal() {
    const zoomModal = document.getElementById('zoomModal');
    const zoomedImage = document.getElementById('zoomedImage');
    const closeZoomModal = document.querySelector('.close-zoom-modal');
    const zoomButtons = document.querySelectorAll('[data-zoom-btn]');
    const projectImages = document.querySelectorAll('[data-project-img]');

    if (!zoomModal) return;

    const openZoomModal = function (imageSrc, imageAlt) {
        zoomedImage.src = imageSrc;
        zoomedImage.alt = imageAlt;
        zoomModal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    };

    const closeZoomModalFunc = function () {
        zoomModal.style.display = 'none';
        document.body.style.overflow = 'auto';
    };

    if (zoomButtons.length > 0) {
        zoomButtons.forEach((zoomBtn, index) => {
            zoomBtn.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();

                const projectImg = projectImages[index];
                const imgSrc = projectImg.src;
                const imgAlt = projectImg.alt;

                openZoomModal(imgSrc, imgAlt);
            });
        });
    }

    if (projectImages.length > 0) {
        projectImages.forEach((projectImg, index) => {
            projectImg.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();

                const imgSrc = this.src;
                const imgAlt = this.alt;

                openZoomModal(imgSrc, imgAlt);
            });
        });
    }

    if (closeZoomModal) {
        closeZoomModal.addEventListener('click', closeZoomModalFunc);
    }

    if (zoomModal) {
        zoomModal.addEventListener('click', function (e) {
            if (e.target === zoomModal) {
                closeZoomModalFunc();
            }
        });
    }

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && zoomModal && zoomModal.style.display === 'block') {
            closeZoomModalFunc();
        }
    });
}

// Form validation - KEEP THIS FUNCTION
function initializeFormValidation() {
    const form = document.querySelector('[data-form]');
    const formBtn = document.querySelector('[data-form-btn]');

    if (form && formBtn) {
        const formInputs = form.querySelectorAll('input, textarea');

        formInputs.forEach(input => {
            input.addEventListener('input', function () {
                if (form.checkValidity()) {
                    formBtn.removeAttribute('disabled');
                } else {
                    formBtn.setAttribute('disabled', '');
                }
            });
        });

        // Check initial state
        if (form.checkValidity()) {
            formBtn.removeAttribute('disabled');
        } else {
            formBtn.setAttribute('disabled', '');
        }
    }
}

function initializeCertModal() {
    if (document.querySelector('.cert-modal')) {
        console.log('Cert modal already exists');
        return;
    }

    const certModal = document.createElement('div');
    certModal.className = 'cert-modal';
    certModal.style.display = 'none';
    certModal.innerHTML = `
        <span class="close-cert-modal">&times;</span>
        <div class="cert-modal-content">
            <div class="cert-pdf-container">
                <iframe id="certPdfFrame" width="100%" height="100%" frameborder="0"></iframe>
            </div>
        </div>
    `;

    document.body.appendChild(certModal);

    const closeCertModal = document.querySelector('.close-cert-modal');
    const certPdfFrame = document.getElementById('certPdfFrame');

    const openCertPdf = function (pdfUrl) {
        if (certPdfFrame) {
            certPdfFrame.src = pdfUrl;
        }
        certModal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    };

    const closeCertModalFunc = function () {
        certModal.style.display = 'none';
        if (certPdfFrame) {
            certPdfFrame.src = '';
        }
        document.body.style.overflow = 'auto';
    };

    if (closeCertModal) {
        closeCertModal.addEventListener('click', closeCertModalFunc);
    }

    certModal.addEventListener('click', function (e) {
        if (e.target === certModal) {
            closeCertModalFunc();
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && certModal.style.display === 'block') {
            closeCertModalFunc();
        }
    });

    const certLinks = document.querySelectorAll('.cert-link');
    certLinks.forEach(certLink => {
        certLink.addEventListener('click', function (e) {
            e.preventDefault();

            const pdfUrl = this.getAttribute('href');
            console.log('Cert link clicked, PDF URL:', pdfUrl);

            if (pdfUrl && pdfUrl.toLowerCase().endsWith('.pdf')) {
                openCertPdf(pdfUrl);
            } else {
                window.open(pdfUrl, '_blank');
            }
        });
    });
}