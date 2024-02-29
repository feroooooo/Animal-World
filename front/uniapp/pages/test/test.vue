<template>
	<view class="content">
		<uni-uploader action="http://your_springboot_server.com/upload" :files="files" @change="onChange" @success="onSuccess"></uni-uploader>
		<image class="logo" src="/static/logo.png" @click="chooseImage"></image>
		<view class="text-area">
			<text class="title">{{prediction}}</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				prediction: 'Hello'
			}
		},
		onLoad() {

		},
		methods: {
			// 用户点击按钮选择图片
			chooseImage() {
			  uni.chooseImage({
				count: 1, // 默认为9，设置为1表示只选择一张图片
				sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
				sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
				success: (res) => {
				  // 获取文件的临时路径
				  const tempFilePaths = res.tempFilePaths;
				  // 上传图片
				  this.uploadFile(tempFilePaths[0]);
				  console.log(tempFilePaths)
				}
			  });
			},
		
			// 上传图片到服务器
			uploadFile(filePath) {
			  uni.uploadFile({
				url: 'http://localhost:5000/predict', // 你的SpringBoot服务器上传API
				filePath: filePath,
				name: 'file', // 必须与SpringBoot服务器端接收文件的参数名一致
				formData: {
				  'user': 'test' // 如果需要，可以附加更多的字段
				},
				success: (uploadFileRes) => {
				  console.log(JSON.parse(uploadFileRes.data));
				  // 处理服务器响应的数据
				  console.log(JSON.parse(uploadFileRes.data).prediction)
				  this.prediction = JSON.parse(uploadFileRes.data).prediction
				},
				fail: (uploadFileErr) => {
				  console.log(uploadFileErr);
				  // 处理上传失败的情况
				}
			  });
			}
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
</style>
