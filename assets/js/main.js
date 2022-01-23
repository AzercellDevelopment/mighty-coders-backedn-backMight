//  this is for loading effect (start)
$(window).on("load", function () {
    setTimeout(() => {
        $("#myLoader").fadeOut("slow");
        $("body").css("overflow-y", "scroll")
    }, 2000);

});
 //  this is for loading effect (end)

// this is for scrollBtn (start)
window.onscroll = function () {
    scrollFunction();
  
  };
  
  function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        $(".scrollBtn").css(
            "bottom", "3%"
        )
  
    } else {
        $(".scrollBtn").css(
            "bottom", "-150px"
        )
    }
  }
  
  
  
  $(".scrollBtn").click(function () {
    toTop();
    var self = $(this);
    $(this).addClass("activeBtn")
    setTimeout(function () {
        $(self).removeClass("activeBtn")
    }, 2000)
    
  
  })
  
  function toTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
// this is for scrollBtn (end)

var headerDrop = $("#header .mobile-drop");

$("#header .header-mobile").click(function(){

    headerDrop.addClass("active-menu")

})

$("#header .mobile-drop .drop-close").click(function(){
    headerDrop.removeClass("active-menu")
    
})

$("#header .header-search .search-top").click(function () {

    var searchIcon = $(".search-icon");
    var xIcon = $(".x-icon");
    var drop = $(".search-dropdown");

    if (searchIcon.hasClass("active-icon")) {
        searchIcon.removeClass("active-icon");
        xIcon.addClass("active-icon")
    } else {
        searchIcon.addClass("active-icon");
        xIcon.removeClass("active-icon")
    }

    if (drop.hasClass("active-dropdown")) {
        drop.removeClass("active-dropdown")
    } else {
        drop.addClass("active-dropdown")

    }
})


// this is the part where we change the playback speed of the video
//----------------------------------------------------------//
var myVideo = document.querySelector("#video video")
myVideo.playbackRate = 2.0
//----------------------------------------------------------//


//Tab menu
const tabTop=[...document.querySelectorAll(".Tab-top button")]
const tabdown=[...document.querySelectorAll(".Tab-down .content")]


for(let i=0;i<tabTop.length;i++){

    tabTop[i].onclick=function(){

        for(let j=0;j<tabdown.length;j++){
            tabdown[j].classList.remove("active")
            tabTop[j].classList.remove("active")

        }
        let indexBtn=tabTop.indexOf(this)
        setTimeout(() => {
            tabdown[indexBtn].classList.add("active")
        }, 100);
       tabTop[indexBtn].classList.add("active")


    }
    console.log(tabdown)

}


//Slick
$('.Loc-Slider').slick({
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows:false,
    autoplay:true,
    responsive: [
      {
        breakpoint: 1350,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
          dots: true
        }
      },
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            dots: true

          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            dots: true
          }
        }
      ]
  });


  //Slick
$('.Content').slick({
  infinite: true,
  slidesToShow: 4,
  slidesToScroll: 1,
  arrows:false,
  autoplay:true,
  responsive: [
        {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 750,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
});



