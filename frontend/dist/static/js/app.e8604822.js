(function(t){function e(e){for(var o,i,s=e[0],u=e[1],c=e[2],l=0,d=[];l<s.length;l++)i=s[l],r[i]&&d.push(r[i][0]),r[i]=0;for(o in u)Object.prototype.hasOwnProperty.call(u,o)&&(t[o]=u[o]);f&&f(e);while(d.length)d.shift()();return a.push.apply(a,c||[]),n()}function n(){for(var t,e=0;e<a.length;e++){for(var n=a[e],o=!0,i=1;i<n.length;i++){var u=n[i];0!==r[u]&&(o=!1)}o&&(a.splice(e--,1),t=s(s.s=n[0]))}return t}var o={},r={app:0},a=[];function i(t){return s.p+"static/js/"+({about:"about"}[t]||t)+"."+{about:"831e74d3"}[t]+".js"}function s(e){if(o[e])return o[e].exports;var n=o[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.e=function(t){var e=[],n=r[t];if(0!==n)if(n)e.push(n[2]);else{var o=new Promise(function(e,o){n=r[t]=[e,o]});e.push(n[2]=o);var a,u=document.createElement("script");u.charset="utf-8",u.timeout=120,s.nc&&u.setAttribute("nonce",s.nc),u.src=i(t),a=function(e){u.onerror=u.onload=null,clearTimeout(c);var n=r[t];if(0!==n){if(n){var o=e&&("load"===e.type?"missing":e.type),a=e&&e.target&&e.target.src,i=new Error("Loading chunk "+t+" failed.\n("+o+": "+a+")");i.type=o,i.request=a,n[1](i)}r[t]=void 0}};var c=setTimeout(function(){a({type:"timeout",target:u})},12e4);u.onerror=u.onload=a,document.head.appendChild(u)}return Promise.all(e)},s.m=t,s.c=o,s.d=function(t,e,n){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)s.d(n,o,function(e){return t[e]}.bind(null,o));return n},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="/",s.oe=function(t){throw console.error(t),t};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],c=u.push.bind(u);u.push=e,u=u.slice();for(var l=0;l<u.length;l++)e(u[l]);var f=c;a.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"56d7":function(t,e,n){"use strict";n.r(e);n("cadf"),n("551c"),n("f751"),n("097d");var o=n("2b0e"),r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("h1",[t._v(t._s(t.title))]),n("h2",[t._v(t._s(t.office))]),n("router-view"),n("div",[t._v("\n    Version "+t._s(t.version)+"\n  ")])],1)},a=[],i=(n("7f7f"),{name:"App",data:function(){return{defaultTitle:"Reunión de Comunicación Interna",defaultOffice:"Oficina de Asuntos Importantes",defaultVersion:"?.?.?"}},computed:{title:function(){if(this.$store.getters.event)return this.$store.getters.event.name||this.defaultTitle},office:function(){if(this.$store.getters.event)return this.$store.getters.event.office_name||this.defaultOffice},version:function(){return this.$store.getters.appInfo?this.$store.getters.appInfo.version:this.defaultVersion}},created:function(){this.$store.dispatch("GET_CURRENT_EVENT",1),this.$store.dispatch("GET_APP_INFO")}}),s=i,u=(n("5c0b"),n("2877")),c=Object(u["a"])(s,r,a,!1,null,null,null),l=c.exports,f=n("8c4f"),d=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"home"},[n("ask-question")],1)},p=[],v=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-container",{attrs:{fluid:"","grid-list-md":"","text-xs-center":"","fill-height":""}},[n("v-layout",{attrs:{row:"",wrap:"","align-center":""}},[n("v-flex",{attrs:{xs12:"",md6:"","offset-md3":""}},[n("v-card",[n("v-toolbar",{attrs:{dark:"",color:"teal"}},[n("v-toolbar-title",[t._v("Question")])],1),n("v-card-text",[n("v-layout",{attrs:{row:"",wrap:""}},[n("v-container",{attrs:{fluid:"","grid-list-md":""}},[n("v-textarea",{attrs:{name:"input-7-1",box:"",label:"","auto-grow":""},model:{value:t.question,callback:function(e){t.question=e},expression:"question"}})],1)],1)],1),n("v-card-actions",[n("v-layout",{attrs:{row:""}},[n("v-flex",{attrs:{xs12:""}},[n("v-layout",{attrs:{"align-center":"","justify-end":"",row:"","fill-height":""}},[n("v-btn",{attrs:{right:"",dark:"",color:"indigo",disabled:t.readyToSend},on:{click:function(e){return e.preventDefault(),t.sendQuestion(e)}}},[t._v("Send Question")])],1)],1)],1)],1)],1)],1)],1)],1)},h=[],m=n("2f62"),g={data:function(){return{event:null,question:"",readyToSend:!0}},watch:{question:function(t){console.log("Question",t),t.length>3?this.readyToSend=!1:this.readyToSend=!0}},methods:{sendQuestion:function(){this.$router,this.$route;this.$store.dispatch("SEND_QUESTION",this.question),this.$router.push("/thanks")},ready:function(){return!1}},name:"AskQuestion"},b=g,_=Object(u["a"])(b,v,h,!1,null,"10397c74",null),E=_.exports,y={name:"home",components:{AskQuestion:E}},k=y,O=Object(u["a"])(k,d,p,!1,null,null,null),w=O.exports,T=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"home"},[n("h1",[t._v("Thanks")]),n("v-btn",{attrs:{dark:"",color:"indigo"},on:{click:t.askQuestion}},[t._v("Ask another question")])],1)},x=[],P={name:"ThankYou",components:{AskQuestion:E},methods:{askQuestion:function(){this.$router.push({name:"home"})}}},A=P,$=Object(u["a"])(A,T,x,!1,null,null,null),I=$.exports;o["default"].use(f["a"]);var S=new f["a"]({mode:"history",base:"/",routes:[{path:"/",name:"home",component:w},{path:"/thanks",name:"thanks",component:I},{path:"/about",name:"about",component:function(){return n.e("about").then(n.bind(null,"f820"))}}]}),j=n("bc3a"),Q=n.n(j),q=Q.a.create({baseURL:Object({NODE_ENV:"production",BASE_URL:"/"}).VUE_APP_API_URL}),N=q;o["default"].use(m["a"]);var R=new m["a"].Store({state:{event:null,question:null,appInfo:null},mutations:{setEvent:function(t,e){t.event=e},setQuestion:function(t,e){t.question=e},setAppInfo:function(t,e){t.appInfo=e}},actions:{GET_CURRENT_EVENT:function(t,e){var n=t.commit;console.log("API URL",Object({NODE_ENV:"production",BASE_URL:"/"}).VUE_APP_API_URL),console.log("NODE Env","production");var o="/events/api/v1/event/".concat(e,"/");N.get(o).then(function(t){console.log("Event data",t.data),n("setEvent",t.data)}).catch(function(t){console.log(t)})},SEND_QUESTION:function(t,e){var n=t.commit,o=t.getters,r=$cookies.get("csrftoken"),a={headers:{"X-CSRFToken":r}},i=o.event,s={question:e,event:i.id,moderator_num:1};console.log("Question data",s,a);var u="/questions/api/v1/question/create/";N.post(u,s).then(function(t){console.log("Question data",t.data),n("setQuestion",t.data)}).catch(function(t){console.log("Post Question Error",t)})},GET_APP_INFO:function(t){var e=t.commit,n="/core/api/v1/app-info/";N.get(n).then(function(t){console.log("App Info",t.data),e("setAppInfo",t.data)}).catch(function(t){console.log(t)})}},getters:{event:function(t){return t.event},question:function(t){return t.question},appInfo:function(t){return t.appInfo}}}),U=n("ce5b"),V=n.n(U),C=(n("bf40"),n("2b27")),L=n.n(C);o["default"].use(L.a),o["default"].use(V.a),o["default"].config.productionTip=!1,new o["default"]({router:S,store:R,render:function(t){return t(l)}}).$mount("#app")},"5c0b":function(t,e,n){"use strict";var o=n("5e27"),r=n.n(o);r.a},"5e27":function(t,e,n){}});
//# sourceMappingURL=app.e8604822.js.map