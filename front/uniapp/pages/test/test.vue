<template>
	<view>
		<image 
			:class="lock?'animal-img-lock':'animal-img-unlock'" 
			src="/static/logo.png"
		/>
	</view>
</template>

<script setup>
	import {ref} from"vue";

	let lock = ref(false);

	setInterval(() => {
	    lock.value = !lock.value;
		console.log("Interval:"+lock.value);
	}, 1000);
</script>

<style>
.animal-img-lock{
	width: 100px;
	height: 100px;
	filter: contrast(50%);
	filter: brightness(50%);
}
.animal-img-unlock{
	width: 100px;
	height: 100px;
}
</style>
