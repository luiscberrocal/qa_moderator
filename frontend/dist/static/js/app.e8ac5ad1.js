(function(t){function e(e){for(var n,u,s=e[0],i=e[1],l=e[2],c=0,d=[];c<s.length;c++)u=s[c],o[u]&&d.push(o[u][0]),o[u]=0;for(n in i)Object.prototype.hasOwnProperty.call(i,n)&&(t[n]=i[n]);f&&f(e);while(d.length)d.shift()();return a.push.apply(a,l||[]),r()}function r(){for(var t,e=0;e<a.length;e++){for(var r=a[e],n=!0,u=1;u<r.length;u++){var i=r[u];0!==o[i]&&(n=!1)}n&&(a.splice(e--,1),t=s(s.s=r[0]))}return t}var n={},o={app:0},a=[];function u(t){return s.p+"static/js/"+({about:"about"}[t]||t)+"."+{about:"c7a718cd"}[t]+".js"}function s(e){if(n[e])return n[e].exports;var r=n[e]={i:e,l:!1,exports:{}};return t[e].call(r.exports,r,r.exports,s),r.l=!0,r.exports}s.e=function(t){var e=[],r=o[t];if(0!==r)if(r)e.push(r[2]);else{var n=new Promise(function(e,n){r=o[t]=[e,n]});e.push(r[2]=n);var a,i=document.createElement("script");i.charset="utf-8",i.timeout=120,s.nc&&i.setAttribute("nonce",s.nc),i.src=u(t),a=function(e){i.onerror=i.onload=null,clearTimeout(l);var r=o[t];if(0!==r){if(r){var n=e&&("load"===e.type?"missing":e.type),a=e&&e.target&&e.target.src,u=new Error("Loading chunk "+t+" failed.\n("+n+": "+a+")");u.type=n,u.request=a,r[1](u)}o[t]=void 0}};var l=setTimeout(function(){a({type:"timeout",target:i})},12e4);i.onerror=i.onload=a,document.head.appendChild(i)}return Promise.all(e)},s.m=t,s.c=n,s.d=function(t,e,r){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:r})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var r=Object.create(null);if(s.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)s.d(r,n,function(e){return t[e]}.bind(null,n));return r},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="/",s.oe=function(t){throw console.error(t),t};var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=e,i=i.slice();for(var c=0;c<i.length;c++)e(i[c]);var f=l;a.push([0,"chunk-vendors"]),r()})({0:function(t,e,r){t.exports=r("56d7")},"56d7":function(t,e,r){"use strict";r.r(e);r("cadf"),r("551c"),r("f751"),r("097d");var n=r("2b0e"),o=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{attrs:{id:"app"}},[r("div",{attrs:{id:"nav"}},[r("router-link",{attrs:{to:"/"}},[t._v("Home")]),t._v(" |\n    "),r("router-link",{attrs:{to:"/about"}},[t._v("About")])],1),r("router-view")],1)},a=[],u=(r("5c0b"),r("2877")),s={},i=Object(u["a"])(s,o,a,!1,null,null,null),l=i.exports,c=r("8c4f"),f=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"home"},[r("ask-question")],1)},d=[],p=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-container",{attrs:{fluid:"","grid-list-md":"","text-xs-center":"","fill-height":""}},[r("v-layout",{attrs:{row:"",wrap:"","align-center":""}},[r("v-flex",{attrs:{xs12:"",md6:"","offset-md3":""}},[r("v-card",[r("v-toolbar",{attrs:{dark:"",color:"teal"}},[r("v-toolbar-title",[t._v("QA ")])],1),r("v-card-text",[r("v-layout",{attrs:{row:"",wrap:""}},[r("v-flex",{attrs:{xs12:""}},[r("v-text-field",{attrs:{label:"User name","prepend-icon":"person"},model:{value:t.username,callback:function(e){t.username=e},expression:"username"}})],1),r("v-flex",{attrs:{xs12:""}},[r("v-text-field",{attrs:{label:"Password","prepend-icon":"lock",type:"password"},model:{value:t.password,callback:function(e){t.password=e},expression:"password"}})],1)],1)],1),r("v-card-actions",[r("v-layout",{attrs:{row:""}},[r("v-flex",{attrs:{xs12:""}},[r("v-layout",{attrs:{"align-center":"","justify-end":"",row:"","fill-height":""}},[r("v-btn",{attrs:{right:"",dark:"",color:"indigo"},on:{click:function(e){return e.preventDefault(),t.login(e)}}},[t._v("Login\n                ")])],1)],1)],1)],1)],1)],1)],1)],1)},v=[],m=r("2f62"),b={data:function(){return{username:"",password:""}},methods:{login:function(){this.$router,this.$route;this.$store.dispatch("login",{username:this.username,password:this.password})}},name:"AskQuestion"},h=b,w=Object(u["a"])(h,p,v,!1,null,"2a21bfd2",null),g=w.exports,y={name:"home",components:{AskQuestion:g}},x=y,_=Object(u["a"])(x,f,d,!1,null,null,null),k=_.exports;n["default"].use(c["a"]);var j=new c["a"]({mode:"history",base:"/",routes:[{path:"/",name:"home",component:k},{path:"/about",name:"about",component:function(){return r.e("about").then(r.bind(null,"f820"))}}]});n["default"].use(m["a"]);var O=new m["a"].Store({state:{},mutations:{},actions:{}}),P=r("ce5b"),$=r.n(P);r("bf40");n["default"].use($.a),n["default"].config.productionTip=!1,new n["default"]({router:j,store:O,render:function(t){return t(l)}}).$mount("#app")},"5c0b":function(t,e,r){"use strict";var n=r("5e27"),o=r.n(n);o.a},"5e27":function(t,e,r){}});
//# sourceMappingURL=app.e8ac5ad1.js.map