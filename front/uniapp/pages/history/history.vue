<template>
	<button class="delete-btn" @click="deleteall">
		<image src="/static/icons/delete.png" class="btn-img" mode="aspectFit"></image>
		一键清空
	</button>

	<view class="container1">
		<view class="container2" v-for="(info,index) in history" :key="info.timestamp">
			<image :src="info.image_url" class="picture" mode="aspectFit">
				
			</image>
			<view class="container3">
				
				<text class="result">识别结果：{{info.name}}
				</text>
				
				<button class="intro" @click="baike(info.baike_url)">查看详情</button>
				
				<text class="time">时间：{{formatDate(info.timestamp)}}
				</text>
				
			</view>
		</view>
	</view>
</template>

<script setup>
	import {ref} from "vue";
	import {onShow} from "@dcloudio/uni-app";
	
	let history = ref([]);
	
	onShow(()=>{
		let tmp = uni.getStorageSync("history");
		if(!tmp){
			tmp = [];
		}
		else{
			history.value = JSON.parse(tmp);
		}
	});
	
	function deleteall(){
		try {
			uni.removeStorageSync("history");
			uni.removeStorageSync("genus");
		} catch (e) {
			console.log("删除失败");
		}
		
		//#ifdef H5
		window.location.reload();
		//#endif
	}
	
	function baike(url){
		// #ifdef H5
		window.location.href=url;
		// #endif
	}
	
function formatDate(timestamp) {
	let date = new Date(timestamp * 1000);
	let y = date.getFullYear();
	let MM = date.getMonth() + 1;
	MM = MM < 10 ? "0" + MM : MM;
	let d = date.getDate();
	d = d < 10 ? "0" + d : d;
	let h = date.getHours();
	h = h < 10 ? "0" + h : h;
	let m = date.getMinutes();
	m = m < 10 ? "0" + m : m;
	let s = date.getSeconds();
	s = s < 10 ? "0" + s : s;
	return y + "-" + MM + "-" + d + " " + h + ":" + m + ":" + s;
}
</script>

<style>
button::after{ border: none;} 

.delete-btn{
	background-color: transparent;
	width:120px;
	height:40px;
	display:flex;
	margin-left: auto;
	align-items: center;
	text-align:center;
	justify-content: flex-end;	
	margin-right: 10rpx;
	line-height:40px;
	font-size:15px;
}
.btn-img{
	width:25px;
	height:40px;
	margin-right:7px;
}
	
.container1{
	display: flex;
	flex-direction: column;
	justify-content: center;
}	
	
.container2{
	width: 100%;
	height: auto;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	border-radius: 5px;
	box-shadow: 1px 1px 2px 0.5px rgba(0, 0, 0, 0.1);
}

.picture{
	width: 38%;
	height: 200rpx;
	justify-content:center;

}
		
.container3{
	width: 60%;
	display:flex;
	flex-direction: column;
	justify-content:space-around;
	
}			
			
.result{
	display:flex;
	justify-content: left;
}
			
.intro{
	display:flex;
	justify-content: flex-start;	
	width:90px;
	height:30px;
	margin-left: 0rpx;
	line-height:30px;
	font-size:15px;
}
			
.time{
	display:flex;
	justify-content: left;
}
			


</style>


