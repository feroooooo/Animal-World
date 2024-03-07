<template>
	<view class="img_container">
		<image class="splashimg" src="/static/images/splash_screen.png" mode="widthFix"></image>
	</view>
</template>

<script>
	export default{
		data() {
			return {
				countdownTime: 3
			};
		},
		mounted() {
			let timer = setInterval(() => {
				if (this.countdownTime > 0) {
					this.countdownTime--;
				} 
				else{
					clearInterval(timer)
					uni.switchTab({
						url: '/pages/index/index'
					});
				}
			}, 1000);
		}
	};
</script>

<style>
	.img_container{
		width: 100vw;
		height: 175vw;
		flex: auto;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		position: relative;
	}
	.splashimg{
		position: absolute;
		width: 80%;
		height: 100%;
	}

page{
	background-color:#e4ffd8;
}
</style>