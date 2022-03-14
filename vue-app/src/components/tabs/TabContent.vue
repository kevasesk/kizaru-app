<template>
   <div class="tab-pane fade" :id="worksheet.id">
        <div class="row align-items-center">
            <div class="col-2">
                <img data-role="profile-pic" :src="worksheet.image">
            </div>
            <div class="col-4">
                <input type="text" class="custom-input form-control form-control-sm" data-role="profile-username" placeholder="Логин" :value="worksheet.username">
            </div>
            <div class="col-4">
                <input type="password" class="custom-input form-control form-control-sm" data-role="profile-password" placeholder="Пароль" :value="worksheet.password">
            </div>
            <div class="col-2">
                <button data-role="profile-login-btn" type="button" class="btn btn-dark float-right" @click="loginOnSite()">Вход</button>
            </div>
        </div>
        <div class="row">
            <div class="col-10">
                <div class="input-group input-group-sm" id="ua-block">
                    <input type="text" class="custom-input form-control" placeholder="User-Agent" data-role="ua" aria-describedby="basic-addon1" :value="worksheet.ua">
                </div>
            </div>
            <div class="col-2">
                <button class="btn btn-dark float-right" type="button" @click="setUserAgent()">Сохранить</button>
            </div>
        </div>
        <div class="row">
            <div class="col-2">
                <span class="block-head">Список ссылок</span>
            </div>
            <div class="col-10">
                <button class="btn btn-dark float-right" type="button" @click="saveLinks()">Сохранить ссылки</button>
                <button class="btn btn-dark float-right" type="button" @click="loadLinks()" style="margin-right:5px;">Загрузить ссылки</button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <textarea class="block" data-role="mail-links"></textarea>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <h6 class="block-head">Текст рассылки</h6>
                <textarea class="block" data-role="mail-text"></textarea>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <input type="hidden" data-role="gallery-image-data-id"/>
                <img :src="worksheet.image" data-role="gallery-image-src" width="70" height="100"/>
                <button type="button" class="btn btn-dark" @click="openGallery()">Выбрать картинку</button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <button data-role="start-btn" type="button" class="btn btn-block btn-dark start-btn" @click="start()">Начать работу</button>
            </div>
        </div>
    <!-- Modal -->

    </div>
</template>

<script>
export default {
  name: "TabContent",
  props: ["worksheet"],
  methods:{
      loginOnSite(){
          console.log('login on site');
      },
      setUserAgent(){
          console.log('setUserAgent');
      },
      saveLinks(){

      },
      loadLinks(){

      },
      openGallery(){

      },
      start(){
          
      }
  }
};
</script>

<style>
</style>