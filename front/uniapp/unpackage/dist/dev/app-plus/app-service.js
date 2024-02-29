if (typeof Promise !== "undefined" && !Promise.prototype.finally) {
  Promise.prototype.finally = function(callback) {
    const promise = this.constructor;
    return this.then(
      (value) => promise.resolve(callback()).then(() => value),
      (reason) => promise.resolve(callback()).then(() => {
        throw reason;
      })
    );
  };
}
;
if (typeof uni !== "undefined" && uni && uni.requireGlobal) {
  const global = uni.requireGlobal();
  ArrayBuffer = global.ArrayBuffer;
  Int8Array = global.Int8Array;
  Uint8Array = global.Uint8Array;
  Uint8ClampedArray = global.Uint8ClampedArray;
  Int16Array = global.Int16Array;
  Uint16Array = global.Uint16Array;
  Int32Array = global.Int32Array;
  Uint32Array = global.Uint32Array;
  Float32Array = global.Float32Array;
  Float64Array = global.Float64Array;
  BigInt64Array = global.BigInt64Array;
  BigUint64Array = global.BigUint64Array;
}
;
if (uni.restoreGlobal) {
  uni.restoreGlobal(Vue, weex, plus, setTimeout, clearTimeout, setInterval, clearInterval);
}
(function(vue, shared) {
  "use strict";
  function formatAppLog(type, filename, ...args) {
    if (uni.__log__) {
      uni.__log__(type, filename, ...args);
    } else {
      console[type].apply(console, [...args, filename]);
    }
  }
  function resolveEasycom(component, easycom) {
    return shared.isString(component) ? easycom : component;
  }
  const _export_sfc = (sfc, props) => {
    const target = sfc.__vccOpts || sfc;
    for (const [key, val] of props) {
      target[key] = val;
    }
    return target;
  };
  const _sfc_main$4 = {
    name: "bottomBar",
    data() {
      return {};
    }
  };
  function _sfc_render$2(_ctx, _cache, $props, $setup, $data, $options) {
    return vue.openBlock(), vue.createElementBlock("view");
  }
  const __easycom_0 = /* @__PURE__ */ _export_sfc(_sfc_main$4, [["render", _sfc_render$2], ["__file", "D:/program/java/GitHub/Animal-World/front/uniapp/components/bottomBar/bottomBar.vue"]]);
  const _sfc_main$3 = {
    __name: "index",
    setup(__props) {
      let imageUrl = vue.ref("");
      let prediction = vue.ref("");
      function chooseImage() {
        uni.chooseImage({
          count: 1,
          sizeType: ["compressed"],
          sourceType: ["album", "camera"],
          success: (res) => {
            imageUrl.value = res.tempFilePaths[0];
            formatAppLog("log", "at pages/index/index.vue:64", "FilePath:" + imageUrl.value);
          }
        });
      }
      return (_ctx, _cache) => {
        const _component_bottomBar = resolveEasycom(vue.resolveDynamicComponent("bottomBar"), __easycom_0);
        return vue.openBlock(), vue.createElementBlock(
          vue.Fragment,
          null,
          [
            vue.createElementVNode("swiper", {
              "indicator-dots": "",
              circular: "",
              autoplay: ""
            }, [
              vue.createElementVNode("swiper-item", null, [
                vue.createElementVNode("image", {
                  src: "/static/swiper1.png",
                  mode: "aspectFill"
                })
              ]),
              vue.createElementVNode("swiper-item", null, [
                vue.createElementVNode("image", {
                  src: "/static/swiper2.png",
                  mode: "aspectFill"
                })
              ]),
              vue.createElementVNode("swiper-item", null, [
                vue.createElementVNode("image", {
                  src: "/static/swiper3.png",
                  mode: "aspectFill"
                })
              ]),
              vue.createElementVNode("swiper-item", null, [
                vue.createElementVNode("image", {
                  src: "/static/swiper4.png",
                  mode: "aspectFill"
                })
              ]),
              vue.createElementVNode("swiper-item", null, [
                vue.createElementVNode("image", {
                  src: "/static/swiper5.png",
                  mode: "aspectFill"
                })
              ])
            ]),
            vue.createElementVNode("view", { class: "mainFunction" }, [
              vue.createElementVNode("view", { class: "upld-container" }, [
                vue.createElementVNode("view", { class: "uplld-content" }, [
                  vue.createElementVNode("image", {
                    class: "upld-img",
                    src: vue.unref(imageUrl),
                    mode: "aspectFill"
                  }, null, 8, ["src"]),
                  vue.createElementVNode("text", { class: "upld-text" }, [
                    vue.createTextVNode("       上传图片"),
                    vue.createElementVNode("br"),
                    vue.createTextVNode(" 立即识别多种动物 ")
                  ])
                ])
              ]),
              vue.createElementVNode(
                "view",
                null,
                vue.toDisplayString(vue.unref(prediction)),
                1
                /* TEXT */
              ),
              vue.createElementVNode("button", { onClick: chooseImage }, "拍照识别")
            ]),
            vue.createVNode(_component_bottomBar)
          ],
          64
          /* STABLE_FRAGMENT */
        );
      };
    }
  };
  const PagesIndexIndex = /* @__PURE__ */ _export_sfc(_sfc_main$3, [["__file", "D:/program/java/GitHub/Animal-World/front/uniapp/pages/index/index.vue"]]);
  const _sfc_main$2 = {
    data() {
      return {};
    },
    methods: {}
  };
  function _sfc_render$1(_ctx, _cache, $props, $setup, $data, $options) {
    return vue.openBlock(), vue.createElementBlock("view");
  }
  const PagesHandbookHandbook = /* @__PURE__ */ _export_sfc(_sfc_main$2, [["render", _sfc_render$1], ["__file", "D:/program/java/GitHub/Animal-World/front/uniapp/pages/handbook/handbook.vue"]]);
  const _sfc_main$1 = {
    data() {
      return {};
    },
    methods: {}
  };
  function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
    return vue.openBlock(), vue.createElementBlock("view");
  }
  const PagesHistoryHistory = /* @__PURE__ */ _export_sfc(_sfc_main$1, [["render", _sfc_render], ["__file", "D:/program/java/GitHub/Animal-World/front/uniapp/pages/history/history.vue"]]);
  __definePage("pages/index/index", PagesIndexIndex);
  __definePage("pages/handbook/handbook", PagesHandbookHandbook);
  __definePage("pages/history/history", PagesHistoryHistory);
  const _sfc_main = {
    onLaunch: function() {
      formatAppLog("log", "at App.vue:4", "App Launch");
    },
    onShow: function() {
      formatAppLog("log", "at App.vue:7", "App Show");
    },
    onHide: function() {
      formatAppLog("log", "at App.vue:10", "App Hide");
    }
  };
  const App = /* @__PURE__ */ _export_sfc(_sfc_main, [["__file", "D:/program/java/GitHub/Animal-World/front/uniapp/App.vue"]]);
  function createApp() {
    const app = vue.createVueApp(App);
    return {
      app
    };
  }
  const { app: __app__, Vuex: __Vuex__, Pinia: __Pinia__ } = createApp();
  uni.Vuex = __Vuex__;
  uni.Pinia = __Pinia__;
  __app__.provide("__globalStyles", __uniConfig.styles);
  __app__._component.mpType = "app";
  __app__._component.render = () => {
  };
  __app__.mount("#app");
})(Vue, uni.VueShared);
