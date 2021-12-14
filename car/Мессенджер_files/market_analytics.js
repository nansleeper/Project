﻿(()=>{"use strict";var e,t,r,n={135645:(e,t,r)=>{r.d(t,{PLATFORM_MVK:()=>n});var n="mvk"},290968:(e,t,r)=>{r.d(t,{trackMarketEvent:()=>v,trackMarketArea:()=>p});var n=r(521795),i=r(630790),o=r(559326),a=r(135645),s=r(539931),c=r(165207),d=[],_=!1;function m(e,t){void 0===t&&(t=0);var r=u(t);return!!r&&e.includes(r.event)}function u(e){return void 0===e&&(e=0),d.length>e?d[d.length-(1+e)]:null}function l(e){_||(window.addEventListener("beforeunload",(function(){(0,o.observersStop)(),(0,n.flushMarketEvents)(e)})),_=!0)}function v(e){if(function(e){var t=u();if(t){if(e===c.ECommGoodsEvent.CLOSE_ITEM&&t.event===c.ECommGoodsEvent.CLOSE_ITEM)return!1;if(e===c.ECommGoodsEvent.TRANSITION_TO_ITEM){if(m([c.ECommGoodsEvent.TRANSITION_TO_ITEM_LEFT,c.ECommGoodsEvent.TRANSITION_TO_ITEM_RIGHT]))return!1;if(m([c.ECommGoodsEvent.SWITCH_ITEM_VARIANT_1,c.ECommGoodsEvent.SWITCH_ITEM_VARIANT_2]))return!1}}return!0}(e.event))if(e.event||e.table){e.table||(Object.values(c.ECommGoodsEvent).includes(e.event)?e.table=c.AnalyticsEventTable.GOODS:Object.values(c.ECommOrdersEvent).includes(e.event)?e.table=c.AnalyticsEventTable.ORDERS:(0,s.marketDebug)("error","table not specified")),e.screen=e.screen?e.screen:window.MarketAnalyticsManager&&window.MarketAnalyticsManager.getScreen(),e.platform=e.platform?e.platform:"web",e.itemType=e.itemType?e.itemType:"",l(e.platform);var t=String(e.event),r=e.table+":"+t;e.instant?(0,n.logMarketEventNow)(e.platform,r,e.ownerId,e.itemId,e.screen,e.albumId,e.time,e.duration,e.itemType):(0,n.logMarketEvent)(e.platform,r,e.ownerId,e.itemId,e.screen,e.albumId,e.time,e.duration,e.itemType),d.push(e),d.length>3&&d.shift()}else(0,s.marketDebug)("error","event and table not specified",e)}function p(e,t){var r;switch(void 0===t&&(t=""),l(t),(0,n.flushMarketEvents)(t),(0,o.observersStop)(),(0,s.marketDebug)("warn","analytics: start tracking area",e),e){case c.AnalyticsArea.MARKET:r=function(e){var t=0;void 0!==window.cur.aid&&(t=window.cur.aid),v({event:"market_item"===e.type?c.ECommGoodsEvent.VIEW_ITEM:c.ECommGoodsEvent.VIEW_ALBUM,ownerId:e.ownerId,itemId:"market_item"===e.type?e.itemId:0,albumId:"market_item"===e.type?t:e.itemId,duration:e.duration,time:e.viewStart,platform:e.platform})};var d=i.MarketAnalyticsObserver.create({observerId:"market_products",itemSelector:{types:"market_item"},isUnifyNodes:!0,isDynamicContent:!0,platform:t});d.itemReachedCallback=r;var _=i.MarketAnalyticsObserver.create({observerId:"market_albums",itemSelector:{types:"market_album"},isUnifyNodes:!0,isDynamicContent:!1,platform:t});_.itemReachedCallback=r,t!==a.PLATFORM_MVK&&(_.preCheckReachedCallback=function(e){var t,r=e.offsetTop,n=null===(t=e.parentNode)||void 0===t?void 0:t.parentNode;return n&&r<n.offsetHeight}),d.watch(),_.watch();break;case c.AnalyticsArea.GROUP:r=function(e){v({event:"market_item"===e.type?c.ECommGoodsEvent.VIEW_ITEM:c.ECommGoodsEvent.VIEW_ALBUM,ownerId:e.ownerId,itemId:"market_item"===e.type?e.itemId:0,albumId:"market_item"===e.type?0:e.itemId,duration:e.duration,time:e.viewStart,platform:e.platform})};var m=i.MarketAnalyticsObserver.create({observerId:"market_module",itemSelector:{types:"market_item"},isUnifyNodes:!0,platform:t});m.itemReachedCallback=r;var u=i.MarketAnalyticsObserver.create({observerId:"group_wall",itemSelector:{types:"market_item,market_album"},isUnifyNodes:!0,isDynamicContent:!0,platform:t});u.itemReachedCallback=r,m.watch(),u.watch();break;case c.AnalyticsArea.USER_PROFILE:var p=i.MarketAnalyticsObserver.create({observerId:"user_wall",itemSelector:{types:"market_item,market_album"},isUnifyNodes:!0,isDynamicContent:!0,platform:t});p.itemReachedCallback=function(e){v({event:"market_item"===e.type?c.ECommGoodsEvent.VIEW_ITEM:c.ECommGoodsEvent.VIEW_ALBUM,ownerId:e.ownerId,itemId:"market_item"===e.type?e.itemId:0,duration:e.duration,time:e.viewStart,albumId:"market_item"===e.type?0:e.itemId,platform:e.platform})},p.watch();break;case c.AnalyticsArea.BOOKMARKS:var f=i.MarketAnalyticsObserver.create({observerId:"bookmarks",itemSelector:{types:"market_item"},isUnifyNodes:!0,isDynamicContent:!0,platform:t});f.itemReachedCallback=function(e){v({table:c.AnalyticsEventTable.GOODS,event:c.ECommGoodsEvent.VIEW_ITEM,ownerId:e.ownerId,itemId:e.itemId,duration:e.duration,time:e.viewStart,albumId:0,platform:e.platform})},f.watch();break;case c.AnalyticsArea.FEED:var h=i.MarketAnalyticsObserver.create({observerId:"feed",itemSelector:{types:"market_item"},isUnifyNodes:!0,isDynamicContent:!0,container:".feed_wrap",platform:t});h.itemReachedCallback=function(e){v({event:"market_item"===e.type?c.ECommGoodsEvent.VIEW_ITEM:c.ECommGoodsEvent.VIEW_ALBUM,ownerId:e.ownerId,itemId:"market_item"===e.type?e.itemId:0,duration:e.duration,time:e.viewStart,albumId:"market_item"===e.type?0:e.itemId,platform:e.platform})},h.watch()}}},630790:(e,t,r)=>{r.d(t,{MarketAnalyticsObserver:()=>d});var n=r(570655),i=r(539931),o=r(933614),a=r(951583),s=r(712459),c=r(135645),d=function(e){function t(r,n,i,a,s,c,d){void 0===i&&(i=""),void 0===a&&(a=!1),void 0===s&&(s=!1),void 0===c&&(c="");var _=e.call(this,r,n,i,a,c,d)||this;return _.observerId=r,_.itemSelector=n,_.container=i,_.isUnifyNodes=a,_.isDynamicNodes=s,_.gap=null,s&&_.addMutators([new o.NodeMutationObserver]),_.gap=t.getViewportGap(_.getPlatform()),_}return(0,n.__extends)(t,e),t.prototype.isReached=function(e){if(!(0,i.isElementVisible)(e))return!1;var t,r=this.gap,n=e.closest("[data-stat-viewport]");if(n){var o=n.getBoundingClientRect();r={top:o.top,left:o.left},t={width:o.left+o.width,height:o.top+o.height}}return(0,i.isElementInViewport)(e,45,r,t)},t.create=function(e){return new t(e.observerId,e.itemSelector,null==e?void 0:e.container,null==e?void 0:e.isUnifyNodes,null==e?void 0:e.isDynamicContent,null==e?void 0:e.platform,null==e?void 0:e.getExtraItemParams)},t.getViewportGap=function(e){void 0===e&&(e="");var t={left:0,top:0},r="";return r=e===c.PLATFORM_MVK?"#vk_head":"#page_header_wrap,#market_search_input",document.querySelectorAll(r).forEach((function(e){var r=(0,s.getElementSize)(e);t.top=t.top+r.height})),t},t}(a.NodeViewObserver)},165207:(e,t,r)=>{var n,i,o,a;r.d(t,{AnalyticsArea:()=>n,AnalyticsEventTable:()=>i,ECommGoodsEvent:()=>o,ECommOrdersEvent:()=>a}),function(e){e.MARKET="market",e.GROUP="group",e.USER_PROFILE="user_profile",e.BOOKMARKS="bookmarks",e.FEED="feed"}(n||(n={})),function(e){e.GOODS="ecomm_goods",e.ORDERS="ecomm_orders"}(i||(i={})),function(e){e.TRANSITION_TO_ITEM="transition_to_item",e.TRANSITION_TO_ALBUM="transition_to_album",e.SWITCH_ITEM_VARIANT_1="switch_item_variant_1",e.SWITCH_ITEM_VARIANT_2="switch_item_variant_2",e.TRANSITION_TO_ITEM_LEFT="transition_to_item_left",e.TRANSITION_TO_ITEM_RIGHT="transition_to_item_right",e.VIEW_ITEM="view_item",e.VIEW_ALBUM="view_album",e.CLOSE_ITEM="close_item",e.TRANSITION_TO_OWNER="transition_to_owner",e.VIEW_ITEM_MEDIA="view_item_media",e.ADD_ITEM_TO_CART="add_item_to_cart",e.EXPAND_ITEM_DESCRIPTION="expand_item_description",e.ADD_ITEM_TO_BOOKMARKS="add_item_to_bookmarks",e.REMOVE_ITEM_FROM_BOOKMARKS="remove_item_from_bookmarks",e.EXPAND_COMMENTS="expand_comments",e.COMMENT="comment",e.ADD_TO_CART_HS="add_to_cart_hs",e.OPEN_WIKI="open_wiki",e.SEND_MESSAGE_TO_OWNER="send_message_to_owner",e.SEND_MESSAGE_TO_OWNER_2="send_message_to_owner_2",e.OPEN_CHAT_WITH_OWNER="open_chat_with_owner",e.OPEN_CHAT_WITH_OWNER_2="open_chat_with_owner_2",e.LIKE_ITEM="like_item",e.UNLIKE_ITEM="unlike_item",e.SHARE_ITEM="share_item",e.CTA_LINK="cta_link",e.CTA_LINK_2="cta_link_2",e.CALL="call",e.CALL_2="call_2",e.CREATE_ITEM="create_item",e.CREATE_ALBUM="create_album",e.EDIT_ITEM="edit_item",e.EDIT_ALBUM="edit_album",e.DELETE_ITEM="delete_item",e.DELETE_ALBUM="delete_album",e.GROUP_ITEMS="group_items",e.ADD_PROPERTY="add_property",e.ADD_PROPERTY_VALUE="add_property_value",e.DELETE_PROPERTY="delete_property",e.DELETE_PROPERTY_VALUE="delete_property_value",e.TRANSITION_TO_EDIT_PROPERTIES="transition_to_edit_properties",e.TRANSITION_TO_EDIT_ALBUMS="transition_to_edit_albums",e.TRANSITION_TO_ADD_ALBUM="transition_to_add_album",e.TRANSITION_TO_ADD_ITEM="transition_to_add_item",e.TRANSITION_TO_EDIT_ITEM="transition_to_edit_item",e.TRANSITION_TO_DELETE_ALBUM="transition_to_delete_album",e.TRANSITION_TO_GROUP_ITEMS="transition_to_group_items",e.VIEW_FEEDBACK="view_feedback",e.OPEN_FEEDBACK_PHOTO="open_feedback_photo"}(o||(o={})),function(e){e.EVENT_MAKE_ORDER="make_order",e.CANCEL_ORDER="cancel_order",e.EXPAND_ORDER_INFO="expand_order_info",e.TRANSITION_TO_ORDERS="transition_to_orders",e.OPEN_MARKET_GROUP_ORDERS="open_market_group_orders",e.OPEN_MARKET_GROUP_ITEMS="open_market_group_items",e.OPEN_MARKET_GROUP_SETTINGS="open_market_group_settings",e.OPEN_MARKET_GROUP_DELIVERY="open_market_group_delivery",e.TRANSITION_TO_MARKET_SUPPORT="transition_to_market_support",e.OPEN_ORDER_INFO="open_order_info",e.ADD_TRACK_CODE="add_track_code",e.ADD_INTERNAL_COMMENT="add_internal_comment",e.CHANGE_ORDER_STATUS="change_order_status",e.OPEN_CHAT_WITH_CUSTOMER="open_chat_with_customer",e.SEND_MESSAGE_TO_CUSTOMER="send_message_to_customer",e.OPEN_ORDER_HISTORY="open_order_history",e.FILTER_ORDERS_BY_STATUS="filter_orders_by_status",e.EXPORT_ORDERS_DATA="export_orders_data"}(a||(a={}))},521795:(e,t,r)=>{r.d(t,{logMarketEventNow:()=>_,logMarketEvent:()=>m,flushMarketEvents:()=>u});var n=r(570655),i=r(539931),o=r(135645),a=r(190302),s="market_event_count",c="market_event_item_";function d(e,t,r,o){var c=window.MarketAnalyticsManager&&window.MarketAnalyticsManager.getHash();if(c){var d=r.slice(0,10),_=0,m=a.vkLocalStorage.getItem(s);m&&(_=parseInt(m)),_>=20&&(u(e),_=0);var l=Date.now(),v="market_event_item_"+Math.floor(1e5*Math.random())+"_"+l+"_"+t;d.unshift(l),d.unshift(t),d.push(c),a.vkLocalStorage.setItem(v,JSON.stringify(d)),a.vkLocalStorage.setItem(s,String(++_)),o&&u(e),i.marketDebug.apply(void 0,(0,n.__spreadArray)(["debug","event",t],(0,n.__read)(r)))}else(0,i.marketDebug)("warn","events","Hash error")}function _(e,t){for(var r=[],n=2;n<arguments.length;n++)r[n-2]=arguments[n];d(e,t,r,!0)}function m(e,t){for(var r=[],n=2;n<arguments.length;n++)r[n-2]=arguments[n];d(e,t,r,!1)}function u(e){for(var t=[],r=0;r<a.vkLocalStorage.length();++r){var n=a.vkLocalStorage.key(r);n&&0===n.lastIndexOf(c)&&t.push(n)}if(!(t.length<=0)){a.vkLocalStorage.setItem(s,String(0));var d=[],_="";t.forEach((function(e){var t=a.vkLocalStorage.getItem(e);if(a.vkLocalStorage.removeItem(e),t)try{var r=JSON.parse(t);_?r.pop():_=r.pop(),d.push(Object.values(r))}catch(e){(0,i.marketDebug)("error","event error","Unable to assemble events pack",e)}})),!_||d.length<1||(!window.MarketAnalyticsManager||window.MarketAnalyticsManager.isEnabled()?window.ajax.post(e===o.PLATFORM_MVK?"market.php":"al_market.php",{act:"log_events",hash:_,events:d},{onDone:function(){(0,i.marketDebug)("warn","events sent",d.length+" events sent")}}):(0,i.marketDebug)("error","event error","analytics disabled"))}}},539931:(e,t,r)=>{r.d(t,{marketDebug:()=>c,isElementVisible:()=>d,isElementInViewport:()=>_});var n=r(712459),i=r(486353),o=r(190302),a="extended_client_logging",s="market_extended_client_logging";function c(e,t){for(var r=[],n=2;n<arguments.length;n++)r[n-2]=arguments[n];((0,i.partConfigEnabled)(a)||o.vkLocalStorage.getItem(s))&&("error"===e?console.error("[market "+t+"]: ",r):"warn"===e?console.warn("[market "+t+"]: ",r):"info"===e?console.info("[market "+t+"]: ",r):console.debug("[market "+t+"]: ",r))}function d(e){var t;return"none"!==(null===(t=e.style)||void 0===t?void 0:t.display)}function _(e,t,r,i){void 0===t&&(t=50),void 0===r&&(r=null);var o=r?r.left:0,a=r?r.top:0,s=(0,n.getViewportSize)(),c=(0,n.getElementOffset)(e),d=(0,n.getElementSize)(e),_=d.width*t/100,m=d.height*t/100;if(i){if(i.width>s.width)return!1;if(i.height>s.height)return!1;s=i}return!(c.left+d.width<o+_)&&(!(c.left+_>s.width)&&(!(c.top+d.height<a+m)&&!(c.top+m>s.height)))}},933614:(e,t,r)=>{r.d(t,{NodeMutationObserver:()=>n});var n=function(){function e(){}return e.prototype.connectMutator=function(t){if(this.mutationObserver)throw new Error("{Observer #"+t.getObserverId()+"} MutationObserver already connected to observer");var r=document.querySelector(t.getContainerQuery());r instanceof HTMLElement&&(this.mutationObserver=new MutationObserver((function(r){r.forEach((function(r){if(r.addedNodes)for(var n=0;n<r.addedNodes.length;n++){var i=r.addedNodes[n];if(i instanceof HTMLElement){var o=e.resolveNodes(i,t).filter((function(e){return!!e}));o&&(o.forEach((function(e){t.add(e)})),t.scan())}}}))})),this.mutationObserver.observe(r,{childList:!0,subtree:!0,attributes:!1,characterData:!1}))},e.prototype.disconnectMutator=function(e){e.isRunning()&&this.mutationObserver&&this.mutationObserver.disconnect()},e.resolveNodes=function(e,t){var r=[];if(t.getSelectorQuery(!1).split(",").forEach((function(t){if(e.matches(t))return r.push(e),!1})),r.length<1){var n=e.querySelectorAll(t.getSelectorQuery(!1));r=Array.from(n)}return r},e}()},316013:(e,t,r)=>{r.d(t,{NodeObserver:()=>d,getStatIdx:()=>_});var n=r(570655),i=r(503369),o=r(559326),a=r(408830),s="data-stat-item",c="data-stat-id",d=function(){function e(e,t,r,n,i,a){if(void 0===r&&(r=""),void 0===n&&(n=!1),void 0===i&&(i=""),this.observerId=e,this.itemSelector=t,this.container=r,this.isUnifyNodes=n,this.platform=i,this.getExtraItemParams=a,this.trackingItems={},this._debounceTimeout=20,this.uniqueNodeCounter=0,this.nodes=[],this.isWatching=!1,this.mutatorList=[],(0,o.observersRegister)(this),!this.itemSelector.types&&!this.itemSelector.selectors)throw new Error("Empty itemSelector definition");this.container||(this.container=this.observerId)}return Object.defineProperty(e.prototype,"debounceTimeout",{set:function(e){this._debounceTimeout=e},enumerable:!1,configurable:!0}),Object.defineProperty(e.prototype,"itemReachedCallback",{set:function(e){this._itemReachedCallback=e},enumerable:!1,configurable:!0}),Object.defineProperty(e.prototype,"preCheckReachedCallback",{set:function(e){this._preCheckReachedCallback=e},enumerable:!1,configurable:!0}),e.prototype.getObserverId=function(){return this.observerId},e.prototype.getItemSelector=function(){return this.itemSelector},e.prototype.getPlatform=function(){return this.platform},e.prototype.add=function(e){this.nodes.push(e)},e.prototype.getTrackingItems=function(){return this.trackingItems},e.prototype.addMutators=function(e){this.mutatorList=this.mutatorList.concat(e)},e.prototype.isRunning=function(){return this.isWatching},e.prototype.watch=function(){this.isWatching||(this.update(),this.startObserving(),this.connectMutators(),this.isWatching=!0)},e.prototype.stop=function(){this.isWatching&&(this.trackUntracked(),this.stopObserving(),this.disconnectMutators(),this.isWatching=!1)},e.prototype.scan=function(){this.viewportScanner()},e.prototype.trackUntracked=function(){var e=this.getTrackingItems();for(var t in e)if(e[t]){var r=e[t];!r.isTracked&&r.isReached&&(this.track(r),this.persist(r))}},e.prototype.connectMutators=function(){var e=this;this.mutatorList.forEach((function(t){t.connectMutator(e)}))},e.prototype.disconnectMutators=function(){var e=this;this.mutatorList.forEach((function(t){t.disconnectMutator(e)}))},e.prototype.getContainerQuery=function(){var e=this.container.substr(0,1);return"#"===e||"."===e?this.container:'[data-stat-container="'+(this.container?this.container:this.observerId)+'"]'},e.prototype.getSelectorQuery=function(e){void 0===e&&(e=!0);var t=this.getContainerQuery(),r=[];return this.itemSelector.selectors?r=this.itemSelector.selectors.split(",").map((function(r){return e?t+" "+r:r})):this.itemSelector.types&&(r=this.itemSelector.types.split(",").map((function(r){return e?t+" ["+'data-stat-item^="'+r+'|"]':'[data-stat-item^="'+r+'|"]'}))),r.join(",")},e.prototype.update=function(){var e=document.querySelectorAll(this.getSelectorQuery());this.nodes=Array.from(e)},e.parseStatAttribute=function(e){var t=e.getAttribute(s),r=null==t?void 0:t.split("|");return r?{type:r[0],ownerId:parseInt(r[1]),itemId:r[2]}:{type:"",ownerId:0,itemId:0}},e.prototype.getNodeKey=function(e,t){var r=String(t.itemId);this.isUnifyNodes&&(this.unifyNode(e),r=r+"_"+e.getAttribute(c));return this.observerId+"_"+r},e.prototype.isItemReached=function(e){return!(void 0!==this._preCheckReachedCallback&&!this._preCheckReachedCallback(e))&&this.isReached(e)},e.prototype.filterItem=function(e){return!e.isTracked&&!e.isReached&&(this.isItemReached(e.node)?(this.track(e),this.persist(e),!1):(this.persist(e),!0))},e.prototype.track=function(e){e.isTracked||(e.viewEnd=Date.now(),e.duration=e.viewEnd-e.viewStart,this._itemReachedCallback(e),e.isReached=!1,e.isTracked=!0)},e.prototype.persist=function(e){this.trackingItems[e.key]=e},e.prototype.getTrackingItem=function(t){var r=e.parseStatAttribute(t);if(!r.type||!r.itemId)return null;var n=this.getNodeKey(t,r);return n?n in this.trackingItems?this.trackingItems[n]:this.createTrackingItem(t,r):null},e.prototype.createTrackingItem=function(e,t){var r=this.getNodeKey(e,t),i=this.getExtraItemParams&&this.getExtraItemParams()||{};return this.trackingItems[r]=(0,n.__assign)((0,n.__assign)({},i),{key:r,type:t.type,observerId:this.observerId,ownerId:t.ownerId,itemId:t.itemId,isTracked:!1,isReached:!1,viewStart:0,viewEnd:0,duration:0,node:e,viewTimer:0,data:{},platform:this.getPlatform(),city:(0,a.getStatCity)(),screen:(0,a.getStatScreen)()}),this.trackingItems[r]},e.prototype.getNextUnifyId=function(){return++this.uniqueNodeCounter},e.prototype.unifyNode=function(e){e.getAttribute(c)||e.setAttribute(c,String(this.getNextUnifyId()))},e.prototype.startObserving=function(){var e=this;this.update(),this.viewportScanner=(0,i.debounce)((function(){e.nodes=e.nodes.filter((function(t){var r=e.getTrackingItem(t);return!!r&&e.filterItem(r)}))}),this._debounceTimeout),this.scrollEventListener=function(){return e.scan()},document.addEventListener("scroll",this.scrollEventListener,{passive:!0}),this.scan()},e.prototype.stopObserving=function(){document.removeEventListener("scroll",this.scrollEventListener),this.nodes=[],this.viewportScanner=function(){},this.scrollEventListener=function(){}},e}();function _(e){if(e.dataset.statIdx)return parseInt(e.dataset.statIdx||"")}},951583:(e,t,r)=>{r.d(t,{NodeViewObserver:()=>o});var n=r(570655),i=r(316013);var o=function(e){function t(){return null!==e&&e.apply(this,arguments)||this}return(0,n.__extends)(t,e),t.prototype.filterItem=function(e){return!e.isTracked&&(e.isReached&&!this.isItemReached(e.node)?(this.track(e),this.persist(e),!1):(this.isItemReached(e.node)&&this.view(e),this.persist(e),!0))},t.prototype.view=function(e){var t=this;e.isTracked||(e.isReached=!0,e.viewStart||(e.viewStart=Date.now()),e.viewTimer&&(clearTimeout(e.viewTimer),e.viewTimer=0),e.viewTimer=window.setTimeout((function(){var r=e.node;!t.isItemReached(r)||function(e){var t=e.viewStart;return Date.now()-t>3e4}(e)?t.track(e):t.view(e)}),3e3))},t.prototype.track=function(t){t.viewTimer&&(clearTimeout(t.viewTimer),t.viewTimer=0),e.prototype.track.call(this,t)},t}(i.NodeObserver)},559326:(e,t,r)=>{r.d(t,{observersRegister:()=>i,observersStop:()=>o,observersRescan:()=>a});var n={};function i(e){e.getObserverId()in n&&(n[e.getObserverId()].stop(),delete n[e.getObserverId()]),n[e.getObserverId()]=e}function o(){for(var e in n){if(n[e])n[e].stop()}}function a(){for(var e in n){if(n[e])n[e].scan()}}},408830:(e,t,r)=>{r.d(t,{getStatData:()=>a,setStatData:()=>s,getUtmMarks:()=>c,getStatCategoryId:()=>d,getStatScreen:()=>_,getStatOwnerId:()=>m,getStatCity:()=>u});var n=r(570655),i=r(190302),o="market_stat_data";function a(){var e=i.vkSessionStorage.getItem(o);return e?JSON.parse(e):{}}function s(e){var t=i.vkSessionStorage.getItem(o),r=t&&JSON.parse(t);i.vkSessionStorage.setItem(o,JSON.stringify((0,n.__assign)((0,n.__assign)({},r),e)))}var c=function(){var e=a();return{utm_source:e.utm_source,utm_medium:e.utm_medium,utm_campaign:e.utm_campaign,utm_campaign_id:e.utm_campaign_id,utm_content:e.utm_content}},d=function(){return a().category_id};function _(){return a().screen||window.cur.module}function m(){return a().ownerId||0}function u(){return a().city}},618873:(e,t,r)=>{var n=r(290968),i=r(165207),o={trackArea:n.trackMarketArea,onMarketAlbumEdit:function(e,t,r){(0,n.trackMarketEvent)({table:i.AnalyticsEventTable.GOODS,event:r?i.ECommGoodsEvent.CREATE_ALBUM:i.ECommGoodsEvent.EDIT_ALBUM,ownerId:e,albumId:t,instant:!0})}};window.MarketAnalytics=o;try{window.stManager.done(window.jsc("web/market_analytics.js"))}catch(e){}}},i={};function o(e){var t=i[e];if(void 0!==t)return t.exports;var r=i[e]={id:e,loaded:!1,exports:{}};return n[e].call(r.exports,r,r.exports,o),r.loaded=!0,r.exports}o.m=n,e=[],o.O=(t,r,n,i)=>{if(!r){var a=1/0;for(_=0;_<e.length;_++){for(var[r,n,i]=e[_],s=!0,c=0;c<r.length;c++)(!1&i||a>=i)&&Object.keys(o.O).every((e=>o.O[e](r[c])))?r.splice(c--,1):(s=!1,i<a&&(a=i));if(s){e.splice(_--,1);var d=n();void 0!==d&&(t=d)}}return t}i=i||0;for(var _=e.length;_>0&&e[_-1][2]>i;_--)e[_]=e[_-1];e[_]=[r,n,i]},o.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return o.d(t,{a:t}),t},r=Object.getPrototypeOf?e=>Object.getPrototypeOf(e):e=>e.__proto__,o.t=function(e,n){if(1&n&&(e=this(e)),8&n)return e;if("object"==typeof e&&e){if(4&n&&e.__esModule)return e;if(16&n&&"function"==typeof e.then)return e}var i=Object.create(null);o.r(i);var a={};t=t||[null,r({}),r([]),r(r)];for(var s=2&n&&e;"object"==typeof s&&!~t.indexOf(s);s=r(s))Object.getOwnPropertyNames(s).forEach((t=>a[t]=()=>e[t]));return a.default=()=>e,o.d(i,a),i},o.d=(e,t)=>{for(var r in t)o.o(t,r)&&!o.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},o.e=()=>Promise.resolve(),o.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),o.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),o.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),o.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{var e={37317:0};o.O.j=t=>0===e[t];var t=(t,r)=>{var n,i,[a,s,c]=r,d=0;for(n in s)o.o(s,n)&&(o.m[n]=s[n]);if(c)var _=c(o);for(t&&t(r);d<a.length;d++)i=a[d],o.o(e,i)&&e[i]&&e[i][0](),e[a[d]]=0;return o.O(_)},r=self.webpackChunkvk=self.webpackChunkvk||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})();var a=o.O(void 0,[68592],(()=>o(618873)));a=o.O(a)})();