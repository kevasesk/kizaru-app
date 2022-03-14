<template>
    <div class="modal fade" data-role="progressModal" tabindex="-1" role="dialog" aria-labelledby="exampleModal3Label" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModal3Label">Работаем...</h5><br/>
                    <button type="button" class="close" @click="closeProgressModal()" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="progress">
                        <p class="progress-text">10 из 20</p>
                        <div data-role="progress" class="progress-bar progress-bar-striped bg-dark progress-bar-animated" role="progressbar" style="width: 0"></div>
                    </div>
                    <br/>
                    <p>Что бы перейди к другой анкете, нажмите вне окна что бы свернуть окно процесса.</p>
                </div>
                <div class="modal-footer">
                    <button data-role="stop-btn" type="button" class="btn btn-dark" @click="stop()">Остановить</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
 name: "TabProgress",
}
</script>

<style>

</style>