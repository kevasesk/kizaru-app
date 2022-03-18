<template>
  <div class="modal fade" data-role="errorsModal" tabindex="-1" role="dialog"  aria-hidden="true">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header">
				<h5 class="modal-title">Не обработанные ссылки!</h5>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="closeErrorsModal()">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
				<textarea data-role="errorLinks" rows="15"></textarea>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-dismiss="modal" @click="closeErrorsModal()">Закрыть</button>
			</div>
		</div>
	</div>
</div>
</template>

<script>
export default {
	props: ['worksheet'],
	methods:{
		closeErrorsModal(){
			window.jQuery('#'+this.worksheet.id).find('[data-role="errorsModal"]').modal('hide');
		}
	},
	mounted(){
		window.jQuery('#'+this.worksheet.id).find('[data-role="errorsModal"]').modal({backdrop: false});
		window.jQuery('#'+this.worksheet.id).find('[data-role="errorsModal"]').draggable({handle: ".modal-header"});
	}
}
</script>

<style>

</style>