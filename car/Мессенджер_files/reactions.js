﻿(()=>{"use strict";var e,t,n,i={429697:(e,t,n)=>{n.d(t,{default:()=>p});var i=n(654337),o=n(773949),r=n(486186),a=(n(45697),n(292859)),s=n(316787),l=n(667294),u=n(696630),c=function(e,t){return e&&t&&t.split(" ").forEach((function(t){return(0,s.default)(e,t)}))},d=function(e){function t(){for(var t,n=arguments.length,i=new Array(n),o=0;o<n;o++)i[o]=arguments[o];return(t=e.call.apply(e,[this].concat(i))||this).appliedClasses={appear:{},enter:{},exit:{}},t.onEnter=function(e,n){t.removeClasses(e,"exit"),t.addClass(e,n?"appear":"enter","base"),t.props.onEnter&&t.props.onEnter(e,n)},t.onEntering=function(e,n){var i=n?"appear":"enter";t.addClass(e,i,"active"),t.props.onEntering&&t.props.onEntering(e,n)},t.onEntered=function(e,n){var i=n?"appear":"enter";t.removeClasses(e,i),t.addClass(e,i,"done"),t.props.onEntered&&t.props.onEntered(e,n)},t.onExit=function(e){t.removeClasses(e,"appear"),t.removeClasses(e,"enter"),t.addClass(e,"exit","base"),t.props.onExit&&t.props.onExit(e)},t.onExiting=function(e){t.addClass(e,"exit","active"),t.props.onExiting&&t.props.onExiting(e)},t.onExited=function(e){t.removeClasses(e,"exit"),t.addClass(e,"exit","done"),t.props.onExited&&t.props.onExited(e)},t.getClassNames=function(e){var n=t.props.classNames,i="string"==typeof n,o=i?""+(i&&n?n+"-":"")+e:n[e];return{baseClassName:o,activeClassName:i?o+"-active":n[e+"Active"],doneClassName:i?o+"-done":n[e+"Done"]}},t}(0,r.default)(t,e);var n=t.prototype;return n.addClass=function(e,t,n){var i=this.getClassNames(t)[n+"ClassName"];"appear"===t&&"done"===n&&(i+=" "+this.getClassNames("enter").doneClassName),"active"===n&&e&&e.scrollTop,this.appliedClasses[t][n]=i,function(e,t){e&&t&&t.split(" ").forEach((function(t){return(0,a.default)(e,t)}))}(e,i)},n.removeClasses=function(e,t){var n=this.appliedClasses[t],i=n.base,o=n.active,r=n.done;this.appliedClasses[t]={},i&&c(e,i),o&&c(e,o),r&&c(e,r)},n.render=function(){var e=this.props,t=(e.classNames,(0,o.default)(e,["classNames"]));return l.createElement(u.default,(0,i.default)({},t,{onEnter:this.onEnter,onEntered:this.onEntered,onEntering:this.onEntering,onExit:this.onExit,onExiting:this.onExiting,onExited:this.onExited}))},t}(l.Component);d.defaultProps={classNames:""},d.propTypes={};const p=d},696630:(e,t,n)=>{n.d(t,{default:()=>h});var i=n(773949),o=n(486186),r=(n(45697),n(667294)),a=n(973935),s=n(806035),l=n(500220),u="unmounted",c="exited",d="entering",p="entered",f="exiting",v=function(e){function t(t,n){var i;i=e.call(this,t,n)||this;var o,r=n&&!n.isMounting?t.enter:t.appear;return i.appearStatus=null,t.in?r?(o=c,i.appearStatus=d):o=p:o=t.unmountOnExit||t.mountOnEnter?u:c,i.state={status:o},i.nextCallback=null,i}(0,o.default)(t,e),t.getDerivedStateFromProps=function(e,t){return e.in&&t.status===u?{status:c}:null};var n=t.prototype;return n.componentDidMount=function(){this.updateStatus(!0,this.appearStatus)},n.componentDidUpdate=function(e){var t=null;if(e!==this.props){var n=this.state.status;this.props.in?n!==d&&n!==p&&(t=d):n!==d&&n!==p||(t=f)}this.updateStatus(!1,t)},n.componentWillUnmount=function(){this.cancelNextCallback()},n.getTimeouts=function(){var e,t,n,i=this.props.timeout;return e=t=n=i,null!=i&&"number"!=typeof i&&(e=i.exit,t=i.enter,n=void 0!==i.appear?i.appear:t),{exit:e,enter:t,appear:n}},n.updateStatus=function(e,t){if(void 0===e&&(e=!1),null!==t){this.cancelNextCallback();var n=a.findDOMNode(this);t===d?this.performEnter(n,e):this.performExit(n)}else this.props.unmountOnExit&&this.state.status===c&&this.setState({status:u})},n.performEnter=function(e,t){var n=this,i=this.props.enter,o=this.context?this.context.isMounting:t,r=this.getTimeouts(),a=o?r.appear:r.enter;!t&&!i||s.default.disabled?this.safeSetState({status:p},(function(){n.props.onEntered(e)})):(this.props.onEnter(e,o),this.safeSetState({status:d},(function(){n.props.onEntering(e,o),n.onTransitionEnd(e,a,(function(){n.safeSetState({status:p},(function(){n.props.onEntered(e,o)}))}))})))},n.performExit=function(e){var t=this,n=this.props.exit,i=this.getTimeouts();n&&!s.default.disabled?(this.props.onExit(e),this.safeSetState({status:f},(function(){t.props.onExiting(e),t.onTransitionEnd(e,i.exit,(function(){t.safeSetState({status:c},(function(){t.props.onExited(e)}))}))}))):this.safeSetState({status:c},(function(){t.props.onExited(e)}))},n.cancelNextCallback=function(){null!==this.nextCallback&&(this.nextCallback.cancel(),this.nextCallback=null)},n.safeSetState=function(e,t){t=this.setNextCallback(t),this.setState(e,t)},n.setNextCallback=function(e){var t=this,n=!0;return this.nextCallback=function(i){n&&(n=!1,t.nextCallback=null,e(i))},this.nextCallback.cancel=function(){n=!1},this.nextCallback},n.onTransitionEnd=function(e,t,n){this.setNextCallback(n);var i=null==t&&!this.props.addEndListener;e&&!i?(this.props.addEndListener&&this.props.addEndListener(e,this.nextCallback),null!=t&&setTimeout(this.nextCallback,t)):setTimeout(this.nextCallback,0)},n.render=function(){var e=this.state.status;if(e===u)return null;var t=this.props,n=t.children,o=(0,i.default)(t,["children"]);if(delete o.in,delete o.mountOnEnter,delete o.unmountOnExit,delete o.appear,delete o.enter,delete o.exit,delete o.timeout,delete o.addEndListener,delete o.onEnter,delete o.onEntering,delete o.onEntered,delete o.onExit,delete o.onExiting,delete o.onExited,"function"==typeof n)return r.createElement(l.default.Provider,{value:null},n(e,o));var a=r.Children.only(n);return r.createElement(l.default.Provider,{value:null},r.cloneElement(a,o))},t}(r.Component);function m(){}v.contextType=l.default,v.propTypes={},v.defaultProps={in:!1,mountOnEnter:!1,unmountOnExit:!1,appear:!1,enter:!0,exit:!0,onEnter:m,onEntering:m,onEntered:m,onExit:m,onExiting:m,onExited:m},v.UNMOUNTED=0,v.EXITED=1,v.ENTERING=2,v.ENTERED=3,v.EXITING=4;const h=v},500220:(e,t,n)=>{n.d(t,{default:()=>i});const i=n(667294).createContext(null)},806035:(e,t,n)=>{n.d(t,{default:()=>i});const i={disabled:!1}},654337:(e,t,n)=>{function i(){return(i=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var i in n)Object.prototype.hasOwnProperty.call(n,i)&&(e[i]=n[i])}return e}).apply(this,arguments)}n.d(t,{default:()=>i})},486186:(e,t,n)=>{function i(e,t){e.prototype=Object.create(t.prototype),e.prototype.constructor=e,e.__proto__=t}n.d(t,{default:()=>i})},773949:(e,t,n)=>{function i(e,t){if(null==e)return{};var n,i,o={},r=Object.keys(e);for(i=0;i<r.length;i++)n=r[i],t.indexOf(n)>=0||(o[n]=e[n]);return o}n.d(t,{default:()=>i})},292859:(e,t,n)=>{n.d(t,{default:()=>o});var i=n(305261);function o(e,t){e.classList?e.classList.add(t):(0,i.default)(e,t)||("string"==typeof e.className?e.className=e.className+" "+t:e.setAttribute("class",(e.className&&e.className.baseVal||"")+" "+t))}},305261:(e,t,n)=>{function i(e,t){return e.classList?!!t&&e.classList.contains(t):-1!==(" "+(e.className.baseVal||e.className)+" ").indexOf(" "+t+" ")}n.d(t,{default:()=>i})},316787:(e,t,n)=>{function i(e,t){return e.replace(new RegExp("(^|\\s)"+t+"(?:\\s|$)","g"),"$1").replace(/\s+/g," ").replace(/^\s*|\s*$/g,"")}function o(e,t){e.classList?e.classList.remove(t):"string"==typeof e.className?e.className=i(e.className,t):e.setAttribute("class",i(e.className&&e.className.baseVal||"",t))}n.d(t,{default:()=>o})},994356:(e,t,n)=>{n.d(t,{makePendingRequestState:()=>i});var i=function(e){void 0===e&&(e={});var t=Object.create(null);return{cancel:function(e){var n=t[e];null==n||n.abort(),delete t[e]},register:function(n,i){var o,r=t[n],a=function(e){var n;return void 0!==(null===(n=t[e])||void 0===n?void 0:n.throttleTimerId)}(n);if(r){if(a)return!1;console.warn("Reactions pending request for key '"+n+"' wasn't unregistered, but has to be overwritten.\nPending request should be cancelled through .cancel() explicitly before .register()"),r.abort()}t[n]={abort:i},void 0!==(null==e?void 0:e.throttleMs)&&(o=function(e,n){var i=t[e];if(i){i.throttleTimerId&&window.clearTimeout(i.throttleTimerId);var o=window.setTimeout((function(){var n=t[e];n&&(n.throttleTimerId=void 0)}),n);return i.throttleTimerId=o,o}}(n,e.throttleMs));return function(){var e;(null===(e=t[n])||void 0===e?void 0:e.abort)===i&&delete t[n],window.clearTimeout(o)}}}}},66081:(e,t,n)=>{var i=n(228385);window.Reactions=i.ReactionsEntryGlobal,(0,i.init)();try{window.stManager.done(window.jsc("web/reactions.js"))}catch(e){}},728542:(e,t,n)=>{n.d(t,{useOnClickOutside:()=>o});var i=n(667294),o=function(e,t){(0,i.useEffect)((function(){var n=function(n){!e.current||n.target instanceof Node&&e.current.contains(n.target)||t(n)};return document.addEventListener("mousedown",n,{passive:!0}),document.addEventListener("touchstart",n,{passive:!0}),function(){document.removeEventListener("mousedown",n),document.removeEventListener("touchstart",n)}}),[e,t])}},283767:(e,t,n)=>{n.d(t,{parseLikeObjectId:()=>o,likePostObjectId:()=>r,likeReplyObjectId:()=>a,getElementLikeButtonCount:()=>s,getElementLikeButtonIcon:()=>l,getElementLikeButtonLabel:()=>u});var i=n(570655);function o(e){var t=e.match(/^([a-z_]+)([0-9\-_]+)$/);if(!t)return null;var n=(0,i.__read)(t,3);return{objectType:n[1],objectId:n[2]}}var r=function(e){return"wall"+e},a=function(e){return"wall_reply"+e},s=function(e){var t;return null!==(t=null==e?void 0:e.querySelector(".like_button_count, ._like_button_count"))&&void 0!==t?t:void 0},l=function(e){var t;return null!==(t=null==e?void 0:e.querySelector(".like_button_icon, ._like_button_icon"))&&void 0!==t?t:void 0},u=function(e){var t;return null!==(t=e.querySelector(".like_button_label, ._like_button_label"))&&void 0!==t?t:void 0}},383794:(e,t,n)=>{n.d(t,{PreloadImages:()=>r});var i=n(10246),o=n(667294),r=o.memo((function(e){var t=e.imageURLs;return o.useEffect((function(){Promise.all(t.map((function(e){return(0,i.preloadImage)(e)}))).catch((function(){}))}),[t]),null}))},314258:(e,t,n)=>{n.d(t,{Reaction:()=>u});var i=n(570655),o=n(667294),r=n(917685),a=n(659397),s=n(892039),l=n(757216),u=function(e){var t=e.animationURL,n=e.image,u=e.onReactionClick,c=e.reactionId,d=e.reactionTitle,p=!0,f=o.useRef(null),v=(0,i.__read)(o.useState(p),2),m=v[0],h=v[1],E=(0,l.useReactionAnimation)({animationElem:f,animationURL:t,play:m}).isAnimationReady&&m,g=function(){null==u||u(c)},y=(0,i.__read)((0,s.useDebouncedCallback)((function(){t&&h(!0)}),80,[t]),2),_=(y[0],y[1]);o.useCallback((function(){_(),h(!1)}),[]);return o.useEffect((function(){return function(){_()}}),[]),o.createElement("div",{className:(0,a.classNames)("Reaction"),onClick:function(e){g(),e.stopPropagation()},onKeyDown:function(e){[r.KEY.RETURN,r.KEY.SPACE].includes(e.keyCode)&&(g(),e.stopPropagation())},onMouseEnter:void 0,onMouseLeave:void 0,tabIndex:0,role:"button","aria-label":d||void 0},o.createElement("div",{className:"Reaction__hoverArea"}),d?o.createElement("div",{className:"Reaction__title"},d):null,o.createElement("div",{className:"Reaction__image",style:{backgroundImage:!E&&n?"url("+n+")":void 0}},o.createElement("div",{className:(0,a.classNames)("Reaction__animationContainer",{"Reaction__animationContainer--hidden":!E}),ref:f})))}},533354:(e,t,n)=>{n.d(t,{ReactionsMenu:()=>u});var i=n(570655),o=n(667294),r=n(659397),a=n(917685),s=n(314258),l=n(483156),u=o.forwardRef((function(e,t){var n=e.close,u=e.currentReactionId,c=e.onReactionChoose,d=e.position,p=void 0===d?l.PopperVerticalPosition.TOP:d,f=e.reactionsOptions,v=(0,i.__rest)(e,["close","currentReactionId","onReactionChoose","position","reactionsOptions"]),m=o.useCallback((function(e){e.keyCode===a.KEY.ESC&&(null==n||n())}),[]);return o.createElement("div",(0,i.__assign)({},v,{className:(0,r.classNames)("ReactionsMenu ReactionsMenu--extraHoverArea",{"ReactionsMenu--extraHoverAreaToTop":p===l.PopperVerticalPosition.TOP,"ReactionsMenu--extraHoverAreaToBottom":p===l.PopperVerticalPosition.BOTTOM}),onKeyDown:m,ref:t}),o.createElement("div",{className:"ReactionsMenu__inner"},f.items.map((function(e){return o.createElement(s.Reaction,{key:e.id,animationURL:e.animationURL,image:e.imageMenuURL,isSelected:e.id===u,onReactionClick:c,reactionId:e.id,reactionTitle:e.title})}))))}))},892039:(e,t,n)=>{n.d(t,{useDebouncedCallback:()=>r});var i=n(570655),o=n(667294),r=function(e,t,n){void 0===t&&(t=0),void 0===n&&(n=[]);var r=(0,o.useCallback)(function(e,t,n){void 0===t&&(t=0);var o,r=(void 0===n?{}:n).immediate;function a(){clearTimeout(o)}var s=function(){for(var n=[],s=0;s<arguments.length;s++)n[s]=arguments[s];var l=function(){o=void 0,r||e.apply(void 0,(0,i.__spreadArray)([],(0,i.__read)(n)))},u=r&&!o;a(),o=window.setTimeout(l,t),u&&e.apply(void 0,(0,i.__spreadArray)([],(0,i.__read)(n)))};return s.cancel=a,s}(e,t),(0,i.__spreadArray)([t],(0,i.__read)(n)));return[r,r.cancel]}},757216:(e,t,n)=>{n.d(t,{useReactionAnimation:()=>s});var i=n(570655),o=n(667294),r=n(723361),a=n(880001),s=function(e){var t=e.animationElem,n=e.animationURL,s=e.play,l=void 0===s||s,u=o.useRef(null),c=(0,i.__read)(o.useState((function(){return n&&(0,r.animationItemHasData)(n)})),2),d=c[0],p=c[1];return o.useEffect((function(){if(n){if(t.current){u.current=(0,r.getAnimation)(n,t.current);var e=function(){p(!0)};return(0,a.onAnimationReady)(u.current,e),function(){var t,n;!u.current||!u.current._cbs||(null===(t=u.current)||void 0===t||t.removeEventListener("DOMLoaded",e),null===(n=u.current)||void 0===n||n.destroy()),p(!1),u.current=null}}console.error(new Error("Missing animation container"))}else u.current=null}),[n,t]),o.useEffect((function(){var e,t;d&&(l?null===(e=u.current)||void 0===e||e.play():null===(t=u.current)||void 0===t||t.stop())}),[l,d]),{isAnimationReady:d}}},863233:(e,t,n)=>{n.d(t,{useReactionMenuSet:()=>r});var i=n(667294),o=n(353417),r=function(e){return i.useMemo((function(){return(0,o.getReactionSet)(e)}),[e])}},696540:(e,t,n)=>{n.d(t,{ReactionsMenuButton:()=>v});var i=n(570655),o=n(667294),r=n(138201),a=n(315963),s=n(572635),l=n(383794),u=n(236538),c=n(533354),d=n(863233),p=n(105620),f=n(423777),v=function(e){var t=e.objectId,n=e.onReactionChoose,v=e.reactionButtonContainerElem,m=e.reactionIdInitial,h=e.reactionSetId,E=e.styleVariant,g=e.triggerMouseenterOnInitial,y=(0,s.useTooltipVisibility)(),_=y.isAllowedReenter,b=y.tooltipVisibility,w=y.triggerClose,R=(0,i.__read)(o.useState(m),2),C=R[0],T=R[1];o.useEffect((function(){var e=[(0,u.addReactionChooseListener)(t,(function(){w()})),(0,u.addDataUpdateListener)(t,(function(e){T(e.currentReactionId)}))];return function(){e.forEach((function(e){e()}))}}),[]);var P=(0,d.useReactionMenuSet)(h),O=(0,a.useReactionMenuConfig)(),S=o.useMemo((function(){var e;return null!==(e=null==P?void 0:P.items.map((function(e){return e.imageMenuURL})))&&void 0!==e?e:[]}),[null==P?void 0:P.id]);o.useEffect((function(){var e;P&&void 0!==C&&!(null===(e=P.items)||void 0===e?void 0:e.find((function(e){return e.id===C})))&&console.warn("Current reaction ID "+C+" is not found in set '"+h+"'")}),[P]);if(!P)return console.warn("ReactionsMenuButton init error, unavailable reaction set: "+h),null;var k={close:w,currentReactionId:C,onReactionChoose:function(e){(w(),e!==C)&&n(e)},reactionsOptions:P};return o.createElement(o.Fragment,null,o.createElement(p.ReactionsMenuTooltip,{delayShow:null==O?void 0:O.menuShowDelay,getAttachElem:function(e){if(e){var t=(0,f.getClosestLikeBtnContainerElem)(e);return t||(0,r.isDebugEnabled)()&&console.warn("ReactionsMenuButton missing attach target:",e),t}},isAllowedReenter:_,popup:c.ReactionsMenu,popupProps:k,reactionButtonContainer:v,styleVariant:E,triggerMouseenterOnInitial:g,visibility:b}),o.createElement(l.PreloadImages,{imageURLs:S}))}},105620:(e,t,n)=>{n.d(t,{ReactionsMenuTooltip:()=>f});var i=n(570655),o=n(667294),r=n(692128),a=n(10246),s=n(356984),l=n(432793),u=n(572635),c=n(218643),d=["--post-padding-lr"],p=function(){var e=document.createElement("div");return e.setAttribute("aria-hidden","true"),e},f=function(e){var t=e.getAttachElem,n=e.initialIsOpen,f=void 0!==n&&n,v=e.isAllowedReenter,m=e.reactionButtonContainer,h=e.popup,E=e.popupProps,g=e.delayHide,y=void 0===g?r.HIDE_TOOLTIP_TIMEOUT:g,_=e.delayShow,b=void 0===_?r.SHOW_TOOLTIP_TIMEOUT:_,w=e.onOpenStateChange,R=e.onPopperVisibilityChange,C=e.styleVariant,T=e.triggerMouseenterOnInitial,P=void 0===T||T,O=e.visibility,S=void 0===O?u.TooltipVisibility.uncontrolled:O,k=void 0!==t,I=(0,i.__read)(o.useState(f),2),x=I[0],M=I[1],L=S!==u.TooltipVisibility.uncontrolled,H=(0,a.usePrevious)(S),N=o.useRef(null),V=o.useRef(null),A=o.useRef(null),j=(0,c.useCSSVarsPropagation)({elementWithPropsRef:V,properties:d}).style,B=o.useMemo((function(){var e;if(t)return t(null!==(e=A.current)&&void 0!==e?e:void 0)}),[t,A.current]),U=o.useCallback((function(e,t){!t&&L||M(e)}),[L]);o.useEffect((function(){null==w||w(x)}),[x]),o.useEffect((function(){x&&v&&(v.current=!0)}),[x]);var D=(0,l.useTooltipTrigger)({afterHide:U,afterShow:U,cancelCloseOnContentHover:v,delayHide:y,delayShow:b,ignoreMouseTriggers:L,popperPopupRef:N,reactionButtonContainer:m,triggerMouseenterOnInitial:P});return o.useEffect((function(){if(L){var e=S===u.TooltipVisibility.opened;return e||D.cancelDelayedOpening(),void M(e)}x&&H===u.TooltipVisibility.opened&&M(!1)}),[S,L]),o.createElement(s.TransitionPopper,{attachTarget:B,isOpen:x,content:h,contentProps:(0,i.__assign)((0,i.__assign)({},E),D.contentProps),mode:"side",onPopperVisibilityChange:R,position:"t",popperContentStyle:j,popperPopupRef:N,ref:k?A:V,renderNodeFactory:p,styleVariant:C},o.createElement("div",{className:"ReactionsMenuButtonPopperReference"}))}},356984:(e,t,n)=>{n.d(t,{TransitionPopper:()=>d});var i=n(570655),o=n(667294),r=n(121265),a=n(429697),s=n(617841),l=n(483156),u=n(56751),c={appear:150,enter:150,exit:150},d=o.forwardRef((function(e,t){var n,d,p=e.attachTarget,f=e.isOpen,v=void 0!==f&&f,m=e.content,h=e.contentProps,E=e.onPopperVisibilityChange,g=e.popperContentStyle,y=e.popperPopupRef,_=e.styleVariant,b=(0,i.__rest)(e,["attachTarget","isOpen","content","contentProps","onPopperVisibilityChange","popperContentStyle","popperPopupRef","styleVariant"]),w=function(e){var t=(0,i.__read)(o.useState(!!e),2),n=t[0],r=t[1];return{isVisible:!!e||n,onEnter:o.useCallback((function(){r(!0)}),[]),onHidden:o.useCallback((function(){r(!1)}),[])}}(v),R=w.isVisible,C=w.onEnter,T=w.onHidden,P=o.useRef(null),O=(0,u.useCombinedRefs)(t,P),S=(0,l.usePopperTopAutoPosition)(null!==(n=P.current)&&void 0!==n?n:void 0,120,R),k=(d=o.useRef(!0),o.useEffect((function(){d.current=!1}),[]),d.current);o.useEffect((function(){k||null==E||E(R)}),[R]);var I=(0,r.classNames)("ReactionsMenuPopper _ReactionsMenuPopperRoot",{"ReactionsMenuPopper--alignType-post":"post"===_,"ReactionsMenuPopper--popperBottom":S===l.PopperVerticalPosition.BOTTOM,"ReactionsMenuPopper--popperTop":S===l.PopperVerticalPosition.TOP}),x=o.createElement(m,(0,i.__assign)({},h,{position:S})),M=o.createElement(a.default,{appear:!0,in:v,classNames:"ReactionsMenuPopperTransition",onEnter:C,onExited:T,timeout:c},o.createElement("div",{className:I,ref:y,style:g},x));return o.createElement(s.Popper,(0,i.__assign)({},b,{align:"left",attachTarget:p,content:M,open:R,position:S,ref:O}))}))},218643:(e,t,n)=>{n.d(t,{useCSSVarsPropagation:()=>o});var i=n(667294),o=function(e){var t=e.elementWithPropsRef,n=e.properties;return(0,i.useMemo)((function(){var e=t.current;if(!e)return{style:{}};var i=window.getComputedStyle(e),o={};return n.forEach((function(e){var t=i.getPropertyValue(e);t&&(o[e]=t)})),{style:o}}),[t.current,n])}},483156:(e,t,n)=>{n.d(t,{PopperVerticalPosition:()=>i,usePopperTopAutoPosition:()=>a});var i,o=n(667294),r=n(163131);!function(e){e.BOTTOM="b",e.TOP="t"}(i||(i={}));var a=function(e,t,n){return void 0===t&&(t=120),o.useMemo((function(){return function(e,t){void 0===t&&(t=120);var n=i.TOP;if(!e)return n;var o=(0,r.default)(e),a=window.pageYOffset||document.documentElement.scrollTop;return o.top-a<t?i.BOTTOM:n}(e,t)}),[e,t,n])}},315963:(e,t,n)=>{n.d(t,{useReactionMenuConfig:()=>r});var i=n(667294),o=n(353417),r=function(){return(0,i.useMemo)((function(){return(0,o.getReactionConfig)()}),[])}},432793:(e,t,n)=>{n.d(t,{useTooltipTrigger:()=>r});var i=n(728542),o=n(667294),r=function(e){var t=e.afterHide,n=e.afterShow,r=e.cancelCloseOnContentHover,a=e.delayHide,s=void 0===a?0:a,l=e.delayShow,u=void 0===l?0:l,c=e.ignoreMouseTriggers,d=void 0!==c&&c,p=e.reactionButtonContainer,f=e.popperPopupRef,v=e.triggerMouseenterOnInitial,m=o.useRef(null),h=o.useRef(void 0),E=o.useRef(void 0),g=o.useCallback((function(){var e;window.clearTimeout(null!==(e=h.current)&&void 0!==e?e:void 0)}),[]),y=o.useCallback((function(){g(),null==n||n(!1)}),[n]),_=o.useCallback((function(){g(),null==n||n(!0)}),[n]);(0,i.useOnClickOutside)(f,y),o.useEffect((function(){return function(){window.clearTimeout(h.current),window.clearTimeout(E.current)}}),[]);var b=function(e){return window.setTimeout((function(){null==t||t(!1)}),null!=e?e:0)},w=function(){var e,t;(window.clearTimeout(null!==(e=E.current)&&void 0!==e?e:void 0),d)||(h.current=(t=u,window.setTimeout((function(){_()}),null!=t?t:0)))},R=function(e){var t,n;if(window.clearTimeout(null!==(t=h.current)&&void 0!==t?t:void 0),!d){e.relatedTarget instanceof HTMLElement&&(null===(n=null==m?void 0:m.current)||void 0===n?void 0:n.contains(e.relatedTarget))||(E.current=b(s))}};return o.useEffect((function(){v&&w()}),[]),o.useEffect((function(){return null==p||p.addEventListener("mouseenter",w,{passive:!0}),null==p||p.addEventListener("mouseleave",R,{passive:!0}),function(){null==p||p.removeEventListener("mouseenter",w),null==p||p.removeEventListener("mouseleave",R)}}),[p]),{cancelDelayedOpening:g,contentProps:{ref:m,onMouseEnter:function(){var e;window.clearTimeout(null!==(e=E.current)&&void 0!==e?e:void 0),(null==r?void 0:r.current)&&_()},onMouseLeave:function(e){d||p&&e.target instanceof HTMLElement&&p.contains(e.target)||(E.current=b(s))}}}}},572635:(e,t,n)=>{n.d(t,{TooltipVisibility:()=>i,useTooltipVisibility:()=>a});var i,o=n(570655),r=n(667294);!function(e){e.closed="closed",e.opened="opened",e.uncontrolled="uncontrolled"}(i||(i={}));var a=function(){var e=(0,o.__read)(r.useState(i.uncontrolled),2),t=e[0],n=e[1],a=r.useRef(!0),s=r.useCallback((function(e){void 0===e&&(e=!1),t!==i.closed&&(void 0!==e&&(a.current=e),n(i.closed),window.setTimeout((function(){n(i.uncontrolled)})))}),[]);return{isAllowedReenter:a,tooltipVisibility:t,setTooltipVisibility:n,triggerClose:s}}},431700:(e,t,n)=>{n.d(t,{SUPPORTED_OBJECT_TYPES:()=>i,SIZE_MENU:()=>o,SIZE_PREVIEW:()=>r,REACTIONS_COUNTS_RESPONSE_FIELD:()=>a});var i={wall:"wall",wall_reply:"wall_reply"},o={width:96,height:96},r={width:40,height:40},a="reactions_counts"},859878:(e,t,n)=>{n.d(t,{reactionsButtonMount:()=>f});var i=n(667294),o=n(973935),r=n(832626),a=n(138201),s=n(162481),l=n(696540),u=n(236538),c=n(522494),d=n(423777),p=c.ButtonStyleVariant.Post,f=function(e,t){var n;if(void 0===t&&(t={}),!("__isMounted"in e)){var c=(0,d.getMenuMount)(e),f=(0,s.reactionsElemPayload)(e);if(c&&(null==f?void 0:f.objectRaw)){var v=f.csrfHash,m=f.objectRaw,h=f.reactionSetId,E=f.styleVariant,g=void 0===E?p:E,y=f.userReactionId;v||console.warn("Missing reactions csrf hash"),(0,a.isDebugEnabled)()&&console.log("Init reactions button",m,h);o.render(i.createElement(l.ReactionsMenuButton,{objectId:m,onReactionChoose:function(t){var n=(0,s.reactionsElemPayload)(e);v&&n&&((0,u.emitReactionChoose)(m),(0,r.reactionButtonSetReaction)(t,n.userReactionId,m,v,e))},reactionButtonContainerElem:e,reactionIdInitial:y,reactionSetId:h,styleVariant:g,triggerMouseenterOnInitial:!!t.isMouseenterEvent}),c),null===(n=window.cur.destroy)||void 0===n||n.push((function(){c&&(o.unmountComponentAtNode(c),delete e.__isMounted)})),e.__isMounted=!0}else(0,a.isDebugEnabled)()&&console.error("Init reactions button failed",c,f)}}},832626:(e,t,n)=>{n.d(t,{reactionButtonSetReaction:()=>f});var i=n(570655),o=n(457700),r=n(878012),a=n(683393),s=n(68482),l=n(598258),u=n(138201),c=n(162481),d=n(10246),p=function(e,t){var n=t.counts,i=t.isFromWkLayer,o=t.isPrimaryLikeButtonClick,r=t.isUserAction,s=void 0!==r&&r,l=t.objectRaw,u=t.previewVisibility,c=t.reactionId;(0,a.triggerReactionsUpdate)(l,n,{id:c},{isFromWkLayer:i,isPrimaryLikeButtonClick:o,isUserAction:s,previewVisibility:u})},f=function(e,t,n,a,f,v){if((0,u.isDebugEnabled)()&&console.log("Change reaction for object "+n+": "+e),(0,d.isValidEnvironment)()){var m=(0,c.reactionsElemPayload)(f),h=null==m?void 0:m.counts,E=function(e,t,n){var o=(0,i.__assign)({},e);return void 0!==t&&(o[t]=(o[t]||0)+1),void 0!==n&&(o[n]=Math.max(0,(o[n]||0)-1)),o}((null==m?void 0:m.counts)||(0,o.reactionCountsBrandWrap)({}),e,t),g=null==v?void 0:v.isPrimaryLikeButtonClick,y=(0,s.isWkLayerWallPostOpen)(),_=(0,r.previewVisibilityIntentForVariant)(null==m?void 0:m.previewVariant);p(0,{counts:E,isFromWkLayer:y,isPrimaryLikeButtonClick:g,isUserAction:!0,objectRaw:n,previewVisibility:_,reactionId:e}),(0,l.requestPostReactionSet)(e,n,a).promise.then((function(e){var t=(0,l.validateLikesChangeResponse)(e),i=null==t?void 0:t.userReaction;t&&void 0!==i&&p(0,{counts:t.counts,isFromWkLayer:y,isPrimaryLikeButtonClick:!1,isUserAction:!1,objectRaw:n,previewVisibility:_,reactionId:i.id})}),(function(e){(null==e?void 0:e.isAborted)||p(0,{counts:h,isFromWkLayer:y,isPrimaryLikeButtonClick:!1,isUserAction:!1,objectRaw:n,previewVisibility:_,reactionId:t})}))}}},598258:(e,t,n)=>{n.d(t,{requestPostReactionSet:()=>c,validateLikesChangeResponse:()=>d});var i=n(994356),o=n(754),r=n(64385),a=n(883011),s=n(431700),l=n(523845),u=(0,i.makePendingRequestState)(),c=function(e,t,n,i){var o,s;(null===(o=null==i?void 0:i.abortPendingRequests)||void 0===o||o)&&u.cancel(t);var c={act:"a_set_reaction",object:t,reaction_id:e,hash:n,wall:2,from:null===(s=window.Likes)||void 0===s?void 0:s._getReference(t)},d=new a.AjaxCancellationToken,p=new Promise((function(e,t){var n=r.ajax.post("like.php",c,{cancellationToken:d,onDone:function(n){if(null==n?void 0:n.unauth_action_box)return l.UnauthActionBox.show(n.unauth_action_box),void t();e(n)},onFail:function(e){var i=function(e){return"object"==typeof(t=e)&&null!==t&&"readyState"in t&&0===e.readyState;var t}(n);return t({err:e,isAborted:i}),!!i}})})),f=function(){d.cancel()},v=u.register(t,f);return p.catch((function(){})).finally((function(){v&&v()})),{abort:f,promise:p}},d=function(e){var t;if(void 0!==(null==e?void 0:e.reactions_my)){var n=null!==(t=null==e?void 0:e[s.REACTIONS_COUNTS_RESPONSE_FIELD])&&void 0!==t?t:void 0,i=e.reactions_my,r=void 0;return null===i?r={id:void 0}:(0,o.isValidReactionId)(i)&&(r={id:i}),{counts:n,userReaction:r}}console.warn("Invalid reaction change response format",e)}},228385:(e,t,n)=>{n.d(t,{init:()=>d,ReactionsEntryGlobal:()=>p});var i=n(917685),o=n(859878),r=n(476598),a=n(107553),s=n(133031),l=n(966693),u=n(353417),c=n(529821),d=function(){(0,c.postRenderReactionsInit)(),(0,l.initResponseHandlers)(),(0,s.initOnboardingTooltipHandlers)()},p={onReactionKeyDown:function(e,t){(0,r.isEventFromMenu)(t)||[i.KEY.RETURN,i.KEY.SPACE].includes(t.keyCode)&&(t.stopPropagation(),(0,r.toggleReactionOnClick)(e))},onReactionMouseEnter:function(e,t){t.target===e&&(0,a.reactionsButtonInit)(e,{isMouseenterEvent:!0})},onReactionClick:function(e,t){(0,i.checkEvent)(t)||(0,r.isEventFromMenu)(t)||((0,r.toggleReactionOnClick)(e),(0,a.reactionsButtonInit)(e))},reactionsButtonMount:o.reactionsButtonMount,storageAddSets:u.storageAddSets,storageSetConfig:u.storageSetConfig}},476598:(e,t,n)=>{n.d(t,{isEventFromMenu:()=>s,toggleReactionOnClick:()=>l});var i=n(692128),o=n(832626),r=n(236538),a=n(162481),s=function(e){var t,n;return e.target instanceof HTMLElement&&(null===(n=(t=e.target).closest)||void 0===n?void 0:n.call(t,"._ReactionsMenuPopperRoot"))},l=function(e){var t=(0,a.reactionsElemPayload)(e);if(null==t?void 0:t.objectRaw){var n=t.csrfHash,s=t.objectRaw,l=t.userReactionId;if((0,r.emitReactionChoose)(s),n){var u=void 0===l?i.REACTION_ID_DEFAULT:void 0;(0,o.reactionButtonSetReaction)(u,l,s,n,e,{isPrimaryLikeButtonClick:!0})}else console.warn("Missing reactions csrf hash",e)}else console.warn("Missing reactions object raw",e)}},633819:(e,t,n)=>{n.d(t,{helpHintTooltipReactions:()=>a,propagateCloseToOtherTabs:()=>s});var i=n(570655),o=n(64385),r=n(45150),a=function(e,t,n){var a,s,l,u;void 0===n&&(n={});var c=!1,d=!1,p=function(e){var n,i=(void 0===e?{}:e).hideHintOnServer;c||(c=!0,void 0!==i&&i&&(d||(d=!0,o.ajax.post("al_index.php",{act:"help_hints_hide",hash:t.helpHintHash,hint_id:t.helpHintId})),null===(n=t.onHideRequestSent)||void 0===n||n.call(t)))},f=function(){d=!0,null==u||u.hide()},v={autoShow:!1,cls:"feature_intro_tt feature_intro_blue_tt feature_intro_blue_tt--heightSmall feature_info_tooltip",content:t.content,noAutoHideOnWindowClick:!0,onDestroy:function(){p({hideHintOnServer:!0})},onFirstTimeShow:function(e){var t;e instanceof HTMLElement&&(null===(t=e.querySelector(".feature_tooltip__close"))||void 0===t||t.addEventListener("click",(function(){null==u||u.hide()})))},onHide:function(){null==u||u.destroy()},width:230},m=(0,i.__assign)((0,i.__assign)({},v),n);return u=new r.default(e,m),null===(l=null===(s=null===(a=window.cur)||void 0===a?void 0:a.destroy)||void 0===s?void 0:s.push)||void 0===l||l.call(s,(function(){f()})),{hideClientOnly:f,tooltip:u}},s=function(e){var t,n,i,o=e.helpHintId,r=e.onHideFromOtherTab,a="help_hint:"+o,s=function(e){if("visible"!==document.visibilityState&&e.storageArea===window.localStorage&&e.key===a&&"1"===e.newValue){r(),l();try{localStorage.removeItem(a)}catch(e){console.error(e)}}};function l(){window.removeEventListener("storage",s)}window.addEventListener("storage",s);return null===(i=null===(n=null===(t=window.cur)||void 0===t?void 0:t.destroy)||void 0===n?void 0:n.push)||void 0===i||i.call(n,(function(){l()})),{sendEventHintHidden:function(){!function(e,t){try{localStorage.setItem(e,t)}catch(e){console.error(e)}setTimeout((function(){try{localStorage.removeItem(e)}catch(e){console.error(e)}}),100)}(a,"1"),l()}}}},107553:(e,t,n)=>{n.d(t,{reactionsButtonInit:()=>o});var i=n(570655),o=function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t];var n=window.Reactions;n?n.reactionsButtonMount.apply(n,(0,i.__spreadArray)([],(0,i.__read)(e))):window.stManager.add([window.jsc("web/reactions.js"),"reactions.css"]).then((function(){window.Reactions?o.apply(void 0,(0,i.__spreadArray)([],(0,i.__read)(e))):console.error("Reactions module is unavailable")}))}},133031:(e,t,n)=>{n.d(t,{initOnboardingTooltipHandlers:()=>h});var i=n(128533),o=n(633819),r=n(45150),a=n(423777),s=n(95402),l=n(283767),u=n(509723),c=n(754),d=n(509698),p=n(993093),f=function(e){return"string"==typeof e&&!!e},v=function(e){var t=e.payload;(0,u.isDebugEnabled)()&&console.log("Reactions post button onboarding tooltip init",t);var n,i=t.target,a=t.data,s=a||{},l=s.content,c=s.helpHintHash,p=s.helpHintId;if(!(i&&f(l)&&f(c)&&f(p))){var v=new Error("Invalid reactions tooltip onboarding data");return(0,d.reactionLogError)({error:v}),void console.error(v,i,a)}var m=(0,o.helpHintTooltipReactions)(i,{content:l,helpHintHash:c,helpHintId:p,onHideRequestSent:function(){null==n||n()}},{align:r.default.ALIGN_CENTER,appendToParent:!0,autoAdjustToViewport:!1,forceSide:"right",offset:[5,0],type:r.default.TYPE_HORIZONTAL,withCloseButton:!1}),h=m.tooltip,E=m.hideClientOnly;i.addEventListener("mouseenter",(function(){h.hide()}),{once:!0}),window.requestAnimationFrame((function(){h.show()}));var g=(0,o.propagateCloseToOtherTabs)({helpHintId:p,onHideFromOtherTab:E}).sendEventHintHidden;n=g},m=function(e){var t=e.payload;(0,u.isDebugEnabled)()&&console.log("Reactions post preview onboarding tooltip init",t);var n=t.target,i=t.data,v=i||{},m=v.autoShowOnStart,h=void 0!==m&&m,E=v.content,g=v.helpHintHash,y=v.helpHintId;if(!(n&&f(E)&&f(g)&&f(y))){var _=new Error("Invalid reactions preview tooltip onboarding data");return(0,d.reactionLogError)({error:_}),void console.error(_,n,i)}var b=[],w=function(){b.forEach((function(e){e()}))},R=function(e){var t=e.targetElem,n=function(e){var t=e.getBoundingClientRect();return t.left+t.width/2>window.innerWidth/2?"left":"right"}(t),i=(0,o.helpHintTooltipReactions)(t,{content:E,helpHintHash:g,helpHintId:y,onHideRequestSent:w},{align:r.default.ALIGN_CENTER,autoAdjustToViewport:!1,forceSide:n,offset:[8,0],type:r.default.TYPE_HORIZONTAL,withCloseButton:!1}),a=i.tooltip,s=i.hideClientOnly;t.addEventListener("mouseenter",(function(){a.hide()}),{once:!0}),a.show();var l=(0,o.propagateCloseToOtherTabs)({helpHintId:y,onHideFromOtherTab:s}).sendEventHintHidden;b.push(l)};if(h)window.requestAnimationFrame((function(){R({targetElem:n})}));else{var C=void 0;C=(0,s.registerUniqueListener)("reactions-preview-onboarding-tooltip",s.WallDataEvents.post_reactions_counts_update,(function(e){if(e.isUserAction&&(0,p.isReactionsFullUpdatePayload)(e)&&!(0,c.isReactionIdUnset)(e.reactionIdState.reactionId)){var t=(0,l.likePostObjectId)(e.postFullId),n=(0,a.getPreviewElem)(t);if(n)R({targetElem:n}),null==C||C();else{var i=new Error("Reactions preview tooltip onboarding: preview elem is unavailable");console.error(i,e)}}}))}};var h=function(){(0,i.tq)().setStartupHandler("Wall/reactions_onboarding_tooltip",v,!0),(0,i.tq)().setStartupHandler("Wall/reactions_preview_onboarding_tooltip",m,!0)}},878012:(e,t,n)=>{n.d(t,{isVariantInActionBar:()=>o,isVariantInActionStatusBar:()=>r,isVariantHidden:()=>a,previewVisibilityUseCurrent:()=>s,isIntentPreviewInActionBar:()=>l,isIntentPreviewInActionStatusBar:()=>u,isIntentPreviewHidden:()=>c,isIntentPreviewUseCurrent:()=>d,previewVisibilityIntentForVariant:()=>p,parsePreviewVariant:()=>f});var i=n(927792),o=function(e){return e===i.PreviewVariantActionBar},r=function(e){return e===i.PreviewVariantActionStatusBar},a=function(e){return e===i.PreviewVariantHidden},s={kind:"useCurrent"},l=function(e){return e.kind===i.PreviewVariantActionBar},u=function(e){return e.kind===i.PreviewVariantActionStatusBar},c=function(e){return e.kind===i.PreviewVariantHidden},d=function(e){return"useCurrent"===e.kind},p=function(e){return e?{kind:e}:s},f=function(e){return i.PreviewVariants.includes(e)?e:void 0}},927792:(e,t,n)=>{n.d(t,{PreviewVariantActionBar:()=>i,PreviewVariantActionStatusBar:()=>o,PreviewVariantHidden:()=>r,PreviewVariants:()=>a});var i="action_bar",o="action_status_bar",r="hidden",a=[i,o,r]},966693:(e,t,n)=>{n.d(t,{initResponseHandlers:()=>l});var i=n(541575),o=n(353417),r=function(e){var t=null==e?void 0:e.reaction_sets;t&&(0,o.storageAddSets)(t)},a=function(e){e&&(0,o.storageSetConfig)(e)},s=!1,l=function(){s||((0,i.replaceExtraHandler)("reactionsConfig",a),(0,i.replaceExtraHandler)("reactions",r),s=!0)}},993093:(e,t,n)=>{n.d(t,{reactionsCountsUpdatePayload:()=>r,isReactionsFullUpdatePayload:()=>a,reactionsCountsOnlyUpdatePayload:()=>s});var i=n(570655),o=n(677796),r=function(e,t){return(0,i.__assign)((0,i.__assign)({kind:o.PayloadKindFull},e),{reactionIdState:{reactionId:t.id}})},a=function(e){return e.kind===o.PayloadKindFull},s=function(e){return(0,i.__assign)({kind:o.PayloadKindCountsOnly},e)}},677796:(e,t,n)=>{n.d(t,{PayloadKindCountsOnly:()=>i,PayloadKindFull:()=>o});var i="counts_only",o="counts_with_current_reaction"},683393:(e,t,n)=>{n.d(t,{triggerReactionsUpdate:()=>s});var i=n(283767),o=n(431700),r=n(406108),a=n(993093),s=function(e,t,n,s){var l=(0,i.parseLikeObjectId)(e);l&&l.objectType===o.SUPPORTED_OBJECT_TYPES.wall&&l.objectId?(0,r.emitEvent)(r.WallDataEvents.post_reactions_counts_update,function(e,t,n,i){var o={counts:e,isFromWkLayer:null==t?void 0:t.isFromWkLayer,isPrimaryLikeButtonClick:null==t?void 0:t.isPrimaryLikeButtonClick,isQueueUpdate:null==t?void 0:t.isQueueUpdate,isUserAction:t.isUserAction,postFullId:n.objectId,previewVisibility:t.previewVisibility,reactionIdState:i?{reactionId:i.id}:void 0};return i?(0,a.reactionsCountsUpdatePayload)(o,i):(0,a.reactionsCountsOnlyUpdatePayload)(o)}(t,s,l,n)):l&&l.objectType===o.SUPPORTED_OBJECT_TYPES.wall_reply&&l.objectId?(0,r.emitEvent)(r.WallDataEvents.reply_reactions_counts_update,{counts:t,replyFullId:l.objectId,reactionIdState:n?{reactionId:n.id}:void 0}):console.warn("Unsupported reactions object update",e)}},406108:(e,t,n)=>{n.d(t,{WallDataEvents:()=>a,registerUniqueListener:()=>u,emitEvent:()=>c});var i=n(570655),o=n(970793),r=n(257451),a={post_reactions_counts_update:"wall/post_reactions_counts_update",reply_reactions_counts_update:"wall/reply_reactions_counts_update"},s=(0,r.makeSharedState)("wall-data",(function(){return{emitter:new o.default,keyedListeners:Object.create(null)}})),l=function(e,t,n){var o,r,a=s(),l=null===(r=null===(o=a.keyedListeners)||void 0===o?void 0:o[e])||void 0===r?void 0:r[t];return l&&a.emitter.removeListener(e,l),function(e,t,n){var o,r=s();return r.emitter.addListener(e,n),r.keyedListeners[e]=(0,i.__assign)((0,i.__assign)({},r.keyedListeners[e]),((o={})[t]=n,o)),function(){var i,o;r.emitter.removeListener(e,n),(null===(i=r.keyedListeners[e])||void 0===i?void 0:i[t])===n&&(null===(o=r.keyedListeners[e])||void 0===o||delete o[t])}}(e,t,n)},u=function(e,t,n){return l(t,e,n)},c=function(e,t){s().emitter.emit(e,t)}}},o={};function r(e){var t=o[e];if(void 0!==t)return t.exports;var n=o[e]={id:e,loaded:!1,exports:{}};return i[e].call(n.exports,n,n.exports,r),n.loaded=!0,n.exports}r.m=i,e=[],r.O=(t,n,i,o)=>{if(!n){var a=1/0;for(c=0;c<e.length;c++){for(var[n,i,o]=e[c],s=!0,l=0;l<n.length;l++)(!1&o||a>=o)&&Object.keys(r.O).every((e=>r.O[e](n[l])))?n.splice(l--,1):(s=!1,o<a&&(a=o));if(s){e.splice(c--,1);var u=i();void 0!==u&&(t=u)}}return t}o=o||0;for(var c=e.length;c>0&&e[c-1][2]>o;c--)e[c]=e[c-1];e[c]=[n,i,o]},r.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return r.d(t,{a:t}),t},n=Object.getPrototypeOf?e=>Object.getPrototypeOf(e):e=>e.__proto__,r.t=function(e,i){if(1&i&&(e=this(e)),8&i)return e;if("object"==typeof e&&e){if(4&i&&e.__esModule)return e;if(16&i&&"function"==typeof e.then)return e}var o=Object.create(null);r.r(o);var a={};t=t||[null,n({}),n([]),n(n)];for(var s=2&i&&e;"object"==typeof s&&!~t.indexOf(s);s=n(s))Object.getOwnPropertyNames(s).forEach((t=>a[t]=()=>e[t]));return a.default=()=>e,r.d(o,a),o},r.d=(e,t)=>{for(var n in t)r.o(t,n)&&!r.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},r.e=()=>Promise.resolve(),r.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),r.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),r.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),r.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{var e={70724:0};r.O.j=t=>0===e[t];var t=(t,n)=>{var i,o,[a,s,l]=n,u=0;for(i in s)r.o(s,i)&&(r.m[i]=s[i]);if(l)var c=l(r);for(t&&t(n);u<a.length;u++)o=a[u],r.o(e,o)&&e[o]&&e[o][0](),e[a[u]]=0;return r.O(c)},n=self.webpackChunkvk=self.webpackChunkvk||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))})();var a=r.O(void 0,[38288,68592,24509,90613],(()=>r(66081)));a=r.O(a)})();