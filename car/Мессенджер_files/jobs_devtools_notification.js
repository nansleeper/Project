﻿/*! For license information please see jobs_devtools_notification.1d6cb652e1e3404fb9a7.js.LICENSE.txt */
(()=>{"use strict";var e,n,t,o={638425:(e,n,t)=>{function o(){var e={isOpen:!1,orientation:void 0},n=(e,n)=>{window.dispatchEvent(new CustomEvent("devtoolschange",{detail:{isOpen:e,orientation:n}}))},t=setInterval((()=>{try{var o=window.outerWidth-window.innerWidth>160,r=window.outerHeight-window.innerHeight>160,i=o?"vertical":"horizontal";r&&o||!(window.Firebug&&window.Firebug.chrome&&window.Firebug.chrome.isInitialized||o||r)?(e.isOpen&&n(!1,void 0),e.isOpen=!1,e.orientation=void 0):(e.isOpen&&e.orientation===i||n(!0,i),e.isOpen=!0,e.orientation=i)}catch(e){clearInterval(t)}}),500);return e}t.d(n,{start:()=>o})},976406:(e,n,t)=>{(0,t(966912).init)();try{window.stManager.done(window.jsc("web/jobs_devtools_notification.js"))}catch(e){}},966912:(e,n,t)=>{t.d(n,{init:()=>i});var o=t(349970),r=function(){(0,o.fetchVacancies)().then(o.logMessage,(function(){}))},i=function(){void 0!==window.Promise&&(0,o.onDevtoolsOpen)().then(r,(function(){}))}},394238:(e,n,t)=>{t.d(n,{requestJson:()=>a});var o=t(570655),r=t(883011),i=t(368045),a=function(e,n){return(0,r.request)(e,(0,o.__assign)((0,o.__assign)({},n),{al:1}),{}).then((function(e){var n=function(e){var n;try{n=(new i.AjaxProtoJson).parseResponse(e)}catch(e){return}return n}(e.data);return void 0!==n?n:Promise.reject(new Error("Unable to parse response payload"))}))}},349970:(e,n,t)=>{t.d(n,{logMessage:()=>i,fetchVacancies:()=>a,onDevtoolsOpen:()=>s});var o=t(638425),r=t(394238),i=function(e){console.log(e)},a=function(){var e=window.location.pathname.replace(/^\//,"");return(0,r.requestJson)("/al_jobs.php",{act:"get_by_section",section:e}).then((function(e){var n=e.code,t=e.payload,o=null==t?void 0:t[0];return 0===n&&"string"==typeof o?o:Promise.reject(new Error("Invalid response"))}))},s=function(){var e,n=(0,o.start)().isOpen,t=n?Promise.resolve():new Promise((function(n){e=n}));return n||window.addEventListener("devtoolschange",(function(n){var t;(null===(t=null==n?void 0:n.detail)||void 0===t?void 0:t.isOpen)&&e()})),t}}},r={};function i(e){var n=r[e];if(void 0!==n)return n.exports;var t=r[e]={id:e,loaded:!1,exports:{}};return o[e].call(t.exports,t,t.exports,i),t.loaded=!0,t.exports}i.m=o,e=[],i.O=(n,t,o,r)=>{if(!t){var a=1/0;for(l=0;l<e.length;l++){for(var[t,o,r]=e[l],s=!0,d=0;d<t.length;d++)(!1&r||a>=r)&&Object.keys(i.O).every((e=>i.O[e](t[d])))?t.splice(d--,1):(s=!1,r<a&&(a=r));if(s){e.splice(l--,1);var c=o();void 0!==c&&(n=c)}}return n}r=r||0;for(var l=e.length;l>0&&e[l-1][2]>r;l--)e[l]=e[l-1];e[l]=[t,o,r]},i.n=e=>{var n=e&&e.__esModule?()=>e.default:()=>e;return i.d(n,{a:n}),n},t=Object.getPrototypeOf?e=>Object.getPrototypeOf(e):e=>e.__proto__,i.t=function(e,o){if(1&o&&(e=this(e)),8&o)return e;if("object"==typeof e&&e){if(4&o&&e.__esModule)return e;if(16&o&&"function"==typeof e.then)return e}var r=Object.create(null);i.r(r);var a={};n=n||[null,t({}),t([]),t(t)];for(var s=2&o&&e;"object"==typeof s&&!~n.indexOf(s);s=t(s))Object.getOwnPropertyNames(s).forEach((n=>a[n]=()=>e[n]));return a.default=()=>e,i.d(r,a),r},i.d=(e,n)=>{for(var t in n)i.o(n,t)&&!i.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:n[t]})},i.e=()=>Promise.resolve(),i.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),i.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),i.o=(e,n)=>Object.prototype.hasOwnProperty.call(e,n),i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{var e={72269:0};i.O.j=n=>0===e[n];var n=(n,t)=>{var o,r,[a,s,d]=t,c=0;for(o in s)i.o(s,o)&&(i.m[o]=s[o]);if(d)var l=d(i);for(n&&n(t);c<a.length;c++)r=a[c],i.o(e,r)&&e[r]&&e[r][0](),e[a[c]]=0;return i.O(l)},t=self.webpackChunkvk=self.webpackChunkvk||[];t.forEach(n.bind(null,0)),t.push=n.bind(null,t.push.bind(t))})();var a=i.O(void 0,[68592],(()=>i(976406)));a=i.O(a)})();