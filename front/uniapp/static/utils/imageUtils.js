/**
 * 图片压缩
 */
export const imageCompress = (url) => {
	return new Promise((resolve, reject) => {
		// #ifdef H5
		const img = new Image()
		img.src = url
		let files = {};
		img.onload = async () => {
			const canvas = document.createElement('canvas') // 创建Canvas对象(画布)
			const context = canvas.getContext('2d')
			// 默认按比例压缩
			let cw = img.width
			let ch = img.height
			let w = img.width
			let h = img.height
			canvas.width = w
			canvas.height = h
			if (cw > 600 && cw > ch) {
				w = 600
				h = (600 * ch) / cw
				canvas.width = w
				canvas.height = h
			}
			if (ch > 600 && ch > cw) {
				h = 600
				w = (600 * cw) / ch
				canvas.width = w
				canvas.height = h
			}
			// 生成canvas
			let base64 // 创建属性节点
			context.clearRect(0, 0, 0, w, h)
			context.drawImage(img, 0, 0, w, h)
			base64 = canvas.toDataURL()
			resolve(base64)
		}
		// #endif
	});
}
