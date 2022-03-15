<template>
    <div class="gallery-item-wrapper">
        <img :class="{ active: isActive() }" :src="this.src" :data-id="this.dataId" width="160" height="200" @click="makeActive()"/>
    </div>
</template>

<script>
export default {
    props:['src', 'dataId', 'worksheet'],
    methods:{
        makeActive(){
            this.$store.state.galleryActiveImageId[
                this.$store.state.currentGalleryWorksheetId
            ] = this.dataId;
            this.$store.state.galleryActiveImageSrc[
                this.$store.state.currentGalleryWorksheetId
            ] = this.src;
        },
        isActive(){
            return this.dataId == this.$store.state.galleryActiveImageId[
                this.$store.state.currentGalleryWorksheetId
            ];
        }
    }
}
</script>