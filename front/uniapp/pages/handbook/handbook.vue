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
				:class="lock[0]?'animal-img-lock':'animal-img-unlock'" 
				src="/static/images/book1.png"
				mode="aspectFill"
				@click="baike('狮子')"
			/>
			<text class="animal-name">狮子</text>
		</view>
		<view class="item">
			<image
				:class="lock[1]?'animal-img-lock':'animal-img-unlock'" 
				src="/static/images/book2.png"
				@click="baike('兔子')"
			/>
			<text class="animal-name">兔子</text>
		</view>		
		<view class="item">
			<image
				:class="lock[2]?'animal-img-lock':'animal-img-unlock'" 
				src="/static/images/book3.png"
				@click="baike('鹤')"
			/>
			<text class="animal-name">鹤</text>
		</view>		
		<view class="item">
			<image
				:class="lock[3]?'animal-img-lock':'animal-img-unlock'" 
				src="/static/images/book4.png"
				@click="baike('猎豹')"
			/>
			<text class="animal-name">猎豹</text>
		</view>
		<view class="item">
			<image
				:class="lock[4]?'animal-img-lock':'animal-img-unlock'" 
				src="/static/images/book5.png"
				@click="baike('北极熊')"
			/>
			<text class="animal-name">北极熊</text>
		</view>
		<view class="item">
			<image
				:class="lock[5]?'animal-img-lock':'animal-img-unlock'" 
				src="/static/images/book6.png"
				@click="baike('雪豹')"
			/>
			<text class="animal-name">雪豹</text>
		</view>
	</view>
</template>

<script setup>
import {ref} from "vue";
let userCnt = ref(0);
let lock = ref([true,true,true,true,true,true]);

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
		let totalCnt = 10;
        let res = {
            series: [
              {
                data: [{"name":"一班","value":userCnt,"labelShow":false},{"name":"二班","value":totalCnt-userCnt,"labelShow":false}]
              }
            ]
          };
		this.opts.subtitle.name = `${(userCnt / totalCnt) * 100}%`;
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