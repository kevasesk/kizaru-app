<template>
  <div class="modal fade" id="galleryModal" tabindex="-1" role="dialog"  aria-hidden="true">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header">
				<h5 class="modal-title">Галерея анкеты</h5>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="closeGallery()">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
				<div class="gallery-items">
					<template v-for="image in getImages()" :key="image.dataId" >
						<GalleryImage :src="image.src" :dataId="image.dataId" :worksheet="worksheet" />
					</template>
				</div>
			</div>
			<!-- <div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-dismiss="modal" @click="closeGallery()">Отмена</button>
				<button type="button" class="btn btn-success" @click="saveImage()">Выбрать картинку</button>
			</div> -->
		</div>
	</div>
</div>
</template>

<script>
import GalleryImage from "./GalleryImage.vue";

export default {
	props:['worksheet'],
	components:{
		GalleryImage
	},
	methods:{
		closeGallery(){
			window.jQuery('#galleryModal').modal('hide');
		},
		// saveImage(){
		// 	//var dataId = this.$store.state.galleryActiveImageId;
		// 	window.jQuery('#galleryModal').modal('hide');
		// },
		getImages(){
			return this.$store.state.galleryImages;
		}
	}
}
</script>