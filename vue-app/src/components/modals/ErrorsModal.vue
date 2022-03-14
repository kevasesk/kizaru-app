<template>
  <div class="modal fade" id="errorsModal" tabindex="-1" role="dialog"  aria-hidden="true">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header">
				<h5 class="modal-title">Не обработанные ссылки!</h5>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close" onclick="closeErrorsModal();">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
				<textarea id="errorLinks"></textarea>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-dismiss="modal" onclick="closeErrorsModal();">Закрыть</button>
			</div>
		</div>
	</div>
</div>
</template>

<script>
export default {

}
</script>

<style>

</style>