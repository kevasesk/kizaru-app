<template>
  <div class="modal fade" id="galleryModal" tabindex="-1" role="dialog"  aria-hidden="true">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header">
				<h5 class="modal-title">Галерея анкеты</h5>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close" onclick="closeGallery();">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
				<div class="gallery-items"></div>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-dismiss="modal" onclick="closeGallery();">Отмена</button>
				<button type="button" class="btn btn-success" onclick="saveImage();">Выбрать картинку</button>
			</div>
		</div>
	</div>
	<template id="galleryImageTemplate">
		<div class="gallery-item-wrapper">
			<img src="${src}" data-id="${dataId}" width="160" height="200"/>
		</div>
	</template>
</div>
</template>

<script>
export default {

}
</script>