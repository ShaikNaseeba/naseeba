
// MOBILE NAVIGATION

function toggleMenu() {
    const nav = document.getElementById("navLinks");

    nav.classList.toggle("active");
}


// SEARCH FUNCTIONALITY

function searchStay() {

    const destination = document.getElementById("destination").value.trim();

    const checkin = document.getElementById("checkin").value;

    const checkout = document.getElementById("checkout").value;

    const guests = document.getElementById("guests").value;

    if (!destination || !checkin || !checkout) {
        alert("Please enter destination and travel dates.");
        return;
    }

    if (new Date(checkout) <= new Date(checkin)) {
        alert("Check-out date must be after check-in date.");
        return;
    }

    alert(
        "Your search details:\n" +
        "Destination: " + destination +
        "\nCheck-in: " + checkin +
        "\nCheck-out: " + checkout +
        "\nGuests: " + guests
    );

    document.getElementById("properties").scrollIntoView({
        behavior: "smooth"
    });
}


// BOOKING INQUIRY FORM

document.getElementById("bookingForm").addEventListener("submit", function(event) {

    event.preventDefault();

    alert("Thank you for contacting ESCAPE! We will get back to you soon.");

    this.reset();

});


// CLOSE MOBILE MENU AFTER CLICKING LINK

document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", function() {

        document.getElementById("navLinks").classList.remove("active");

    });

});
