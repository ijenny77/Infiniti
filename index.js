let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n){
    showSlides(slideIndex += n);
}

//Thumbnail image controls

function currentSlide(n){
    showSlides(slideIndex = n);
}

function showSlides(n){
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementByClassName("dot");
    if (n > slides.length){slideIndex =1 }
    if(n < 1 ){ slideIndex = slide.length}
    for(i = 0; i < slides.length; i++){
        slides[i].style.display = 'none';
    }
    for (i = 0; i < dots.length; i++){
        dots[i].className = dots[i].className.replace("active", "");
    }
    dots[slideIndex - 1].className += "active";
}