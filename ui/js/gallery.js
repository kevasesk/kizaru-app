var openGallery = async function(targetId){
    $('#galleryModal').modal('show');
    $('#galleryModal').data('target', targetId);
    $('#galleryModal .gallery-items').empty();
    let images = await eel.load_gallery()()
    if(Array.isArray(images) && images.length > 0){
        for(var i=0; i < images.length; i++){
            var galleryImageTemplate = $('#galleryImageTemplate').html();
            galleryImageTemplate = galleryImageTemplate.replaceAll('${src}', images[i].src);
            galleryImageTemplate = galleryImageTemplate.replaceAll('${dataId}', images[i].dataId);
            $('#galleryModal .gallery-items').append(galleryImageTemplate);
        }
    }else{
        $.toast('Что-то пошло не так при загрузке галереи.', 'error')
        $('#galleryModal .gallery-items').append('Что-то не так.');
    }
};

var closeGallery = function(){
    $('#galleryModal').modal('hide');
};

var saveImage = function(){
    if($('#galleryModal').data('target')){
        var tagertId = $('#galleryModal').data('target');
        var selectedImage = $('#galleryModal img.active');
        if(selectedImage.length){
            var id = selectedImage.data('id');
            var src = selectedImage.attr('src');
            $('#'+tagertId).find('[data-role="gallery-image-data-id"]').val(id);
            $('#'+tagertId).find('[data-role="gallery-image-src"]').attr('src', src);
            $.toast('Вы выбрали новую картинку для текущего сообщения', 'success')
        }else{
            $.toast('Выбере картинку', 'warning')
        }
        closeGallery();
    }else{
        $.toast('Что-то пошло не так при сохранении картинки', 'error')
    }
};

$(document).on('click','#galleryModal img', function(){
    var gallery = $('#galleryModal');
  
    gallery.find('.gallery-items .gallery-item-wrapper img').removeClass('active');
    $(this).addClass('active');
});