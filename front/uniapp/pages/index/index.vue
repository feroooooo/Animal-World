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
		<view class="predict-result">
			<view v-show="prediction!=='' && isAnimal">
				<text class="result">识别结果: {{prediction}}</text>
				<button class="result-btn" @click="baike">查看详情</button>
			</view>
			<view v-show="prediction!=='' && !isAnimal">
				<text class="result">该图片中没有动物,请重新上传!</text>
			</view>
		</view>

		<button class="predict-btn" @click="predict">
			<image src="../../static/icons/photo.png" class="btn-img" mode="aspectFit"></image>
			拍照识别
		</button>
	</view>
</template>

<script setup>
	import {ref} from "vue";

	const backUrl="http://154.8.193.179:5000/predict";
	let imageUrl=ref("");
	let baikeUrl=ref("");
	let prediction=ref("");
	let isAnimal=ref(false);
	
    function predict(){
		uni.chooseImage({
			count: 1,
			sizeType: ['compressed'],
			sourceType: ['album', 'camera'],
			success: res => {
				imageUrl.value = res.tempFilePaths[0];
				console.log("FilePath:"+imageUrl.value);
				
				uni.showLoading({
				        title: '加载中...'
				});
				
				uni.uploadFile({
					url:backUrl,
					filePath: imageUrl.value,
					name:"file",
					success: (uploadFileRes) => {
						const response = JSON.parse(uploadFileRes.data);
						console.log(response);
						prediction.value = response.prediction;
						isAnimal.value = response.is_animal;
						baikeUrl.value = response.baike_url;
						
						console.log(prediction.value);
						uni.hideLoading();
						let nowTime = Date.parse(new Date()) / 1000;
						let info = {
							"name":response.prediction,
							"genus":response.genus,
							"image_url":response.image_url,
							"baike_url":response.baike_url,
							"timestamp": nowTime
						};
						
						try{
							//历史记录存储
							let history = uni.getStorageSync("history");
							let tmp = history ? JSON.parse(history) : [];
							tmp.push(info);
							uni.setStorageSync("history",JSON.stringify(tmp));
							//动物图鉴存储
							let genus = uni.getStorageSync("genus");
							let tmp2 = genus ? JSON.parse(genus) : {"大猩猩":false,"狗":false,"兔":false,"鹤":false,"熊":false,"豹":false};
							
							if(!tmp2[response.genus]){
								uni.showToast({
									title: '图鉴解锁: '+info.genus,
									icon: 'success',
									duration: 2000
								})  
							}
							
							tmp2[response.genus] = true;
							uni.setStorageSync("genus",JSON.stringify(tmp2));
						}catch(e){
							console.log("存储失败");
							console.log(e);
						}
					},
					fail: (uploadFileErr) => {
					console.log(uploadFileErr);
						uni.showModal({
							content: '上传失败',
							showCancel:false,
							confirmColor:"#000000"
						});
						uni.hideLoading();
					}
				});
			},
			fail: res=>{
				uni.showModal({
					title: '请先选择图片',
					icon: 'none'
				});
				console.log(res);
				return;
			}
		});
	}
	
	function baike(){
		// #ifdef H5
		window.location.href=baikeUrl.value;
		// #endif
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

.predict-result{
	display:flex;
	align-items: center;
	justify-content: center;
	margin-bottom: 5vh;
}

.result{
	font-size:16px;
}
.result-btn{
	width:76px;
	height:22px;
	font-size:8px;
	line-height:22px;
	left: 50px;
	background-color: #009183;
	border-color:#BBBBBB;
	color:white;
	
	display: inline-block;
	vertical-align: middle;
}

.predict-btn{
	width:150px;
	height:40px;
	color:white;
	display:flex;
	align-items: center;
	text-align:center;
	justify-content: center;
	background-color:#80bb5d;
	line-height:40px;
	font-size:15px;
}
.btn-img{
	width:35px;
	height:25px;
	margin-right:5px;
}
</style>
