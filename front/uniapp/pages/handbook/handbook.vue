<template>
	<view class="charts-box">
		<qiun-data-charts 
			type="ring"
			:opts="opts"
			:chartData="chartData"
			:tooltipShow=false
		/>
	</view>
	<view class="intro">恭喜你已成功发现{{userCnt}}种动物！</view>
	<view class="container">
		<view class="item">
			<image
				:class="unlock['狗']?'animal-img-unlock':'animal-img-lock'" 
				src="/static/images/book1.jpg"
				mode="aspectFill"
				@click="baike('狗')"
			/>
			<text class="animal-name">狗</text>
		</view>
		<view class="item">
			<image
				:class="unlock['兔']?'animal-img-unlock':'animal-img-lock'" 
				src="/static/images/book2.png"
				@click="baike('兔')"
			/>
			<text class="animal-name">兔</text>
		</view>		
		<view class="item">
			<image
				:class="unlock['鹤']?'animal-img-unlock':'animal-img-lock'" 
				src="/static/images/book3.png"
				@click="baike('鹤')"
			/>
			<text class="animal-name">鹤</text>
		</view>		
		<view class="item">
			<image
				:class="unlock['豹']?'animal-img-unlock':'animal-img-lock'" 
				src="/static/images/book4.png"
				@click="baike('豹')"
			/>
			<text class="animal-name">豹</text>
		</view>
		<view class="item">
			<image
				:class="unlock['熊']?'animal-img-unlock':'animal-img-lock'" 
				src="/static/images/book5.png"
				@click="baike('熊')"
			/>
			<text class="animal-name">熊</text>
		</view>
		<view class="item">
			<image
				:class="unlock['猫']?'animal-img-unlock':'animal-img-lock'" 
				src="/static/images/book6.jpg"
				@click="baike('猫')"
			/>
			<text class="animal-name">猫</text>
		</view>
	</view>
</template>

<script setup>
import {onMounted, ref} from "vue";
let userCnt = ref(0);
let unlock = ref({"猫":false,"狗":false,"兔":false,"鹤":false,"熊":false,"豹":false});

onMounted(()=>{
	let genus = JSON.parse(uni.getStorageSync("genus"));
	Object.entries(genus).forEach(([key,value])=>{
		if(value){unlock.value[key]=true;}
	});
	console.log(unlock.value);
})

function baike(name){
		// #ifdef H5
		window.location.href="https://baike.baidu.com/item/" + name;
		// #endif
}
</script>
<!-- ucharts -->
<script>
export default {
  data() {
    return {		
      chartData: {},
      //您可以通过修改 config-ucharts.js 文件中下标为 ['ring'] 的节点来配置全局默认参数，如都是默认参数，此处可以不传 opts 。实际应用过程中 opts 只需传入与全局默认参数中不一致的【某一个属性】即可实现同类型的图表显示不同的样式，达到页面简洁的需求。
      opts: {
        color: ["#1890FF","#909090"],
        padding: [5,5,5,5],
        dataLabel: false,
        legend: {show: false},
        title: {
          name: "图鉴",
          fontSize: 15,
          color: "#666666"
        },
        subtitle: {
          name: "",
          fontSize: 25,
          color: "#7cb5ec"
        },
        extra: {
          ring: {
            ringWidth: 20,
            border: true,
            borderWidth: 3,
			offsetAngle:-90,
            borderColor: "#FFFFFF"
          }
        }
      }
    };
  },
  onReady() {
    this.getServerData();
  },
  methods: {
    getServerData() {
      //模拟从服务器获取数据时的延时
      setTimeout(() => {
        //模拟服务器返回数据，如果数据格式和标准格式不同，需自行按下面的格式拼接
		let userCnt = 0;
		let totalCnt = 0;
		let genus = JSON.parse(uni.getStorageSync("genus"));
		console.log(genus)
		Object.entries(genus).forEach(([key,value])=>{
			totalCnt++;
			if(value){userCnt++;}
		});

        let res = {
            series: [
              {
                data: [{"name":"一","value":userCnt,"labelShow":false},{"name":"二","value":totalCnt-userCnt,"labelShow":false}]
              }
            ]
          };
		this.opts.subtitle.name = `${Math.floor((userCnt / totalCnt) * 100)}%`;
        this.chartData = JSON.parse(JSON.stringify(res));
      }, 500);
    },
  }
};
</script>

<style lang="scss">
	.charts-box {
	  width: 100%;
	  height: 150px;
	}
	
	.intro{
		font-size:22px;
		text-align: center;
	}
	
	.container{
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		margin:40px;
	}
	.item {
	        width: 48%;
	        margin-bottom: 10px;
	        display: flex;
	        flex-direction: column;
	        align-items: center;
	}
	.animal-img-lock{
		width: 100px;
		height: 100px;
		filter: brightness(50%);
		filter: grayscale(100%);
	}
	.animal-img-unlock{
		width: 100px;
		height: 100px;
	}
	.animal-name{
		font-size: 20px;
	}
</style>