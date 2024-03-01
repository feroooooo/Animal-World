<template>
	<swiper indicator-dots circular autoplay>
		<swiper-item><image class="swiperImg" src="/static/images/swiper1.png" mode="aspectFill"></image></swiper-item>
		<swiper-item><image class="swiperImg" src="/static/images/swiper2.png" mode="aspectFill"></image></swiper-item>
		<swiper-item><image class="swiperImg" src="/static/images/swiper3.png" mode="aspectFill"></image></swiper-item>
		<swiper-item><image class="swiperImg" src="/static/images/swiper4.png" mode="aspectFill"></image></swiper-item>
		<swiper-item><image class="swiperImg" src="/static/images/swiper5.png" mode="aspectFill"></image></swiper-item>
	</swiper>
	<view class="mainFunction">
		<view class="upld-container">
			<image class="upld-img" :src="imageUrl" mode="aspectFit"></image>
			<text class="upld-text">
					上传图片<br>
					立即识别多种动物
			</text>
		</view>
		<button class="predict-btn" @click="predict">
			<image src="/static/icons/camera.png" class="btn-img" mode="aspectFit"></image>
			拍照识别
		</button>
		<view>{{prediction}}</view>
	</view>
</template>

<script setup>
	import {ref} from "vue";

	const backUrl="http://10.10.25.13:8080/predict";
	let imageUrl=ref("");
	let prediction=ref("");
	
    function predict(){
		uni.chooseImage({
			count: 1,
			sizeType: ['compressed'],
			sourceType: ['album', 'camera'],
			success: res => {				
				imageUrl.value = res.tempFilePaths[0];
				console.log("FilePath:"+imageUrl.value);
				
				uni.uploadFile({
					url:backUrl,
					filePath: imageUrl.value,
					name:"file",
					success: (uploadFileRes) => {
						console.log(JSON.parse(uploadFileRes.data));
						prediction.value = JSON.parse(uploadFileRes.data).prediction;
						
					},
					fail: (uploadFileErr) => {
					console.log(uploadFileErr);
						uni.showToast({
							title: '上传失败',
							icon: 'none'
						});
					}
				});
			},
			fail: res=>{
				uni.showToast({
					title: '请先选择图片',
					icon: 'none'
				});
				console.log(res);
				return;
			}
		});
	}
</script>

<style>
swiper{
	width:100vw;
	height:200px;
}
swiper-item{
	width:100%;
	height:100%;
	background: black;
}
.swiperImg{
	width:100%;
}
.mainFunction {
	display: flex;
	flex-direction: column;
	align-items: center;
}
.upld-container {
	margin:5vh;
	width: 80vw;
	height: 30vh;
	border: 3px dashed #ccc;
	display: flex;
	justify-content: center;
	align-items: center;
	position: relative;
}

.upld-img {
	width: 100%;
	height: 100%;
	position: absolute;
	top: 0;
	left: 0;
}

.upld-text {
	font-size: 16px;
	color: #878787;
	text-align: center;
}

.predict-btn{
	width:150px;
	height:40px;
	color:white;
	display:flex;
	align-items: center;
	text-align:center;
	justify-content: center;
	background-color:#93D2F3;
	line-height:40px;
	font-size:15px;
}
.btn-img{
	width:35px;
	height:25px;
	margin-right:5px;
}
</style>
