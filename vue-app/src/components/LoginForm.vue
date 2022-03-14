<template>
  <div id="login-wrapper">
	<div class="container" v-if="!showDashboard()">
		<div class="row">
			<div class="col align-self-center login">
				<h1 class="gtxt">Добро пожаловать!</h1>
				<h6>Для продолжения войдите в свой аккаунт</h6>
				<form>
					<div class="form-group">
						<input type="text" class="custom-input form-control" id="login-username" placeholder="Имя пользователя" v-model="username">
					</div>
					<div class="form-group">
						<input type="password" class="custom-input form-control" id="login-password" placeholder="Пароль" v-model="password">
					</div>
					<div class="login-form-footer">
						<div class="custom-control custom-switch">
							<input type="checkbox" class="custom-control-input" id="login-save-details" checked v-model="remember">
							<label class="custom-control-label" for="login-save-details">Запомнить меня</label>
						</div>
						<button type="button" class="btn btn-dark" @click="login()">Войти</button>
					</div>
				</form>
			</div>
		</div>
	</div>
	<DashboardForm v-if="showDashboard()" :username="username"/>
  </div>
</template>

<script>
import DashboardForm from './DashboardForm.vue'

export default {
    name: "LoginForm",
	components: {
		DashboardForm
	},
	props:['loginData'],
	data() {
		return {
			username: this.loginData.username,
			password: this.loginData.password,
			remember: this.loginData.remember ?? true
		}
	},
    methods:{
        async login(){
			if (this.username != '' && this.password != '') {
				let result = await window.eel.login(0, this.username, this.password, this.remember)()
				if (result) {
					this.$store.state.isLoggedIn = true;
				}
				else {
					this.toast('Не удалось войти', 'error')
				}
			}
			else {
				this.toast('Пожалуйста, введите логин и пароль', 'warning')
			}
			return true;
        },
		showDashboard(){
			return this.$store.state.isLoggedIn;
		}
    }
}
</script>