var Gallery = $('#galleryModal');

var openGallery = function(){
    console.log(Gallery);
    $('#galleryModal').modal('show');
};

var closeGallery = function(){
    Gallery.modal('hide');
};

var saveImage = function(){
    console.log('save proccess');
    closeGallery();
};

$(document).on('click','#galleryModal img', function(){
  
    $('.gallery-items .gallery-item-wrapper').addClass('active');
    $(this).parent('.gallery-item-wrapper').addClass('active');
});