document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;

    const menuToggle = document.querySelector(".menu-toggle");
    const nav = document.querySelector(".site-nav");

    const lightbox = document.querySelector(".lightbox");
    const lightboxImage = document.querySelector(".lightbox-image");
    const lightboxClose = document.querySelector(".lightbox-close");
    const galleryButtons = document.querySelectorAll("[data-lightbox]");

    const syncBodyLock = () => {
        const menuOpen = nav && nav.classList.contains("open");
        const lightboxOpen = lightbox && lightbox.classList.contains("open");
        body.classList.toggle("is-locked", Boolean(menuOpen || lightboxOpen));
    };

    const closeMenu = () => {
        if (!nav || !menuToggle) return;
        nav.classList.remove("open");
        menuToggle.setAttribute("aria-expanded", "false");
        syncBodyLock();
    };

    const openMenu = () => {
        if (!nav || !menuToggle) return;
        nav.classList.add("open");
        menuToggle.setAttribute("aria-expanded", "true");
        syncBodyLock();
    };

    if (menuToggle && nav) {
        menuToggle.addEventListener("click", (event) => {
            event.stopPropagation();
            const isOpen = nav.classList.contains("open");

            if (isOpen) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        nav.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                closeMenu();
            });
        });

        document.addEventListener("click", (event) => {
            if (!nav.classList.contains("open")) return;
            if (!nav.contains(event.target) && !menuToggle.contains(event.target)) {
                closeMenu();
            }
        });

        window.addEventListener("resize", () => {
            if (window.innerWidth > 860) {
                closeMenu();
            }
        });
    }

    const countdown = document.querySelector("[data-countdown]");
    if (countdown) {
        const targetDate = new Date(countdown.dataset.countdown).getTime();
        const daysEl = countdown.querySelector('[data-unit="days"]');
        const hoursEl = countdown.querySelector('[data-unit="hours"]');
        const minutesEl = countdown.querySelector('[data-unit="minutes"]');
        const secondsEl = countdown.querySelector('[data-unit="seconds"]');

        const updateCountdown = () => {
            const now = new Date().getTime();
            const distance = targetDate - now;

            if (distance <= 0) {
                if (daysEl) daysEl.textContent = "0";
                if (hoursEl) hoursEl.textContent = "00";
                if (minutesEl) minutesEl.textContent = "00";
                if (secondsEl) secondsEl.textContent = "00";
                return false;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance / (1000 * 60 * 60)) % 24);
            const minutes = Math.floor((distance / (1000 * 60)) % 60);
            const seconds = Math.floor((distance / 1000) % 60);

            if (daysEl) daysEl.textContent = String(days);
            if (hoursEl) hoursEl.textContent = String(hours).padStart(2, "0");
            if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, "0");
            if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, "0");

            return true;
        };

        updateCountdown();

        const countdownInterval = setInterval(() => {
            const shouldContinue = updateCountdown();
            if (!shouldContinue) {
                clearInterval(countdownInterval);
            }
        }, 1000);
    }

    const backToTop = document.querySelector(".back-to-top");
    const sections = document.querySelectorAll("section[id]");
    const navLinks = document.querySelectorAll(".site-nav a");

    const updateScrollUI = () => {
        const scrollY = window.scrollY;

        if (backToTop) {
            backToTop.classList.toggle("visible", scrollY > 500);
        }

        sections.forEach((section) => {
            const sectionTop = section.offsetTop - 150;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute("id");

            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                navLinks.forEach((link) => {
                    const isActive = link.getAttribute("href") === `#${sectionId}`;
                    link.classList.toggle("active", isActive);
                });
            }
        });
    };

    window.addEventListener("scroll", updateScrollUI, { passive: true });
    updateScrollUI();

    if (backToTop) {
        backToTop.addEventListener("click", () => {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    const revealItems = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window && revealItems.length) {
        const observer = new IntersectionObserver(
            (entries, obs) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("is-visible");
                        obs.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.15 }
        );

        revealItems.forEach((item) => observer.observe(item));
    } else {
        revealItems.forEach((item) => item.classList.add("is-visible"));
    }

    const faqItems = document.querySelectorAll(".faq-item");
    faqItems.forEach((item) => {
        const button = item.querySelector(".faq-question");
        const answer = item.querySelector(".faq-answer");

        if (!button || !answer) return;

        button.addEventListener("click", () => {
            const isOpen = item.classList.contains("open");

            faqItems.forEach((faq) => {
                faq.classList.remove("open");

                const faqButton = faq.querySelector(".faq-question");
                const faqAnswer = faq.querySelector(".faq-answer");

                if (faqButton) faqButton.setAttribute("aria-expanded", "false");
                if (faqAnswer) faqAnswer.style.maxHeight = null;
            });

            if (!isOpen) {
                item.classList.add("open");
                button.setAttribute("aria-expanded", "true");
                answer.style.maxHeight = `${answer.scrollHeight}px`;
            }
        });
    });

    const closeLightbox = () => {
        if (!lightbox || !lightboxImage) return;
        lightbox.classList.remove("open");
        lightbox.setAttribute("aria-hidden", "true");
        lightboxImage.src = "";
        lightboxImage.alt = "";
        syncBodyLock();
    };

    if (lightbox && lightboxImage && galleryButtons.length) {
        galleryButtons.forEach((button) => {
            button.addEventListener("click", () => {
                lightboxImage.src = button.dataset.lightbox;
                lightboxImage.alt = button.dataset.alt || "Immagine gallery";
                lightbox.classList.add("open");
                lightbox.setAttribute("aria-hidden", "false");
                syncBodyLock();
            });
        });

        lightbox.addEventListener("click", (event) => {
            if (event.target === lightbox) {
                closeLightbox();
            }
        });

        if (lightboxClose) {
            lightboxClose.addEventListener("click", closeLightbox);
        }
    }

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeMenu();
            closeLightbox();
        }
    });
});